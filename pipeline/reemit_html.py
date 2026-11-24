# -*- coding: utf-8 -*-
"""reemit_html.py - byte-slice re-emission of translated HTML (plan C2).

Usage: python -I pipeline/reemit_html.py --lib asio [--lib ...] [--all]

For each manifest file: scan the (transcoded-to-utf8) source, look up each
segment h in TM/common_segments, parse the translated segment string back to
text pieces, and replace ONLY the text-node byte spans. Everything else -
tags, attributes (except whitelisted attr segments), code, pre, script -
stays byte-identical. Non-HTML assets are copied as-is.

Output: site/zh/1.92.0/<relpath>
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import safe_join, hash_key  # noqa: E402
from common import (escape_min, filter_attrs_inside_code, normalize_text,
                    parse_segment_string, scan_html, Segment)  # noqa: E402
from extract_segments import rebuild_items  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent
OUT_ROOT = "site/zh/1.92.0"
ASSET_EXTS = {".css", ".js", ".png", ".gif", ".jpg", ".jpeg", ".svg", ".ico",
              ".pdf", ".woff", ".woff2", ".ttf", ".txt", ".xml", ".json",
              ".manifest", ".webmanifest", ".mp3", ".wav"}

RE_CHARSET = re.compile(r'(charset\s*=\s*["\']?\s*)([a-zA-Z0-9_\-]+)',
                        re.IGNORECASE)


def load_translations() -> dict:
    zh_map = {}
    tm = safe_join(WORKSPACE, "tm", "segments.jsonl")
    if tm.exists():
        with open(tm, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    d = json.loads(line)
                    if d.get("zh"):
                        zh_map[d["h"]] = d["zh"]
    cs = safe_join(WORKSPACE, "pipeline", "common_segments.json")
    if cs.exists():
        data = json.loads(cs.read_text(encoding="utf-8"))
        for h, zh in data.get("map", {}).items():
            zh_map[int(h)] = zh
    return zh_map


def transcode_to_utf8(raw: bytes, declared: str) -> bytes:
    if not declared or declared in ("utf-8", "utf8", "ascii", "unknown"):
        declared = "cp1252"
    try:
        text = raw.decode(declared)
    except (UnicodeDecodeError, LookupError):
        text = raw.decode("latin-1")
    text = RE_CHARSET.sub(lambda m: m.group(1) + "utf-8", text, count=1)
    return text.encode("utf-8")


def apply_replacements(raw: bytes, repls: list) -> bytes:
    repls.sort(key=lambda r: r[0])
    out = bytearray()
    pos = 0
    for start, end, new in repls:
        if start < pos:
            continue  # overlap guard: keep first
        out += raw[pos:start]
        out += new
        pos = end
    out += raw[pos:]
    return bytes(out)


def copy_assets(root: Path, outroot: Path, lib_scope: list) -> int:
    """Mirror non-HTML asset files under the doc forest (same include/exclude
    rules as inventory, minus the .html filter)."""
    from inventory import EXCLUDE_COMPONENTS
    import os
    n = 0
    roots = []
    if lib_scope:
        for lib in lib_scope:
            if lib.startswith("tool:"):
                roots.append(root / "tools" / lib[5:])
            elif lib in ("(root)",) or lib.startswith("(book:"):
                roots.append(root / "more")
                roots.append(root / "doc")
            else:
                roots.append(root / "libs" / lib)
        roots.append(root / "doc" / "html")
        roots.append(root / "doc" / "antora")
        roots.append(root / "doc" / "src")
        roots.append(root / "more")
        # 根级资产（boost.png / boost.css 等被 ../../../ 引用）
        for g in root.glob("*"):
            if g.is_file() and g.suffix.lower() in (
                    ".png", ".css", ".ico", ".svg", ".js", ".gif",
                    ".webmanifest"):
                roots.append(g)
    else:
        roots = [root / "doc", root / "more",
                 root / "libs", root / "tools"]
    seen = set()
    for base in roots:
        if base.is_file():
            rel = base.relative_to(root)
            if rel in seen:
                continue
            seen.add(rel)
            dst = safe_join(outroot, rel)
            if not dst.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(base, dst)
                n += 1
            continue
        if not base.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames
                           if d not in EXCLUDE_COMPONENTS]
            for fn in filenames:
                p = Path(dirpath) / fn
                if p.suffix.lower() in (".html", ".htm", ".qbk", ".adoc",
                                        ".jam", ".v2", ".py", ".cpp", ".hpp",
                                        ".h", ".pl", ".rb", ".dox", ".txt"):
                    continue
                rel = p.relative_to(root)
                if rel in seen:
                    continue
                seen.add(rel)
                dst = safe_join(outroot, rel)
                if not dst.exists():
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(p, dst)
                    n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", action="append", default=[])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--assets-only", action="store_true",
                    help="only mirror non-HTML assets, then exit")
    args = ap.parse_args()

    root = safe_join(WORKSPACE, "data", "boost_1_92_0")
    outroot = safe_join(WORKSPACE, OUT_ROOT)
    zh_map = load_translations()
    print(f"[reemit] translations loaded: {len(zh_map)}")

    if args.assets_only:
        n = copy_assets(root, outroot, args.lib)
        print(f"[reemit] assets copied: {n}")
        return 0

    man = safe_join(WORKSPACE, "inventory", "manifest.csv")
    rows = []
    with open(man, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    if not args.all:
        targets = set(args.lib)
        rows = [r for r in rows if r["lib"] in targets]

    n_html = n_assets = n_seg_replaced = 0
    for idx, r in enumerate(rows):
        if args.limit and idx >= args.limit:
            break
        rel = r["relpath"]
        src = safe_join(root, rel)
        dst = safe_join(outroot, rel)
        if not r["relpath"].lower().endswith((".html", ".htm")):
            if src.exists() and not dst.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
                n_assets += 1
            continue
        if not src.exists():
            continue
        raw = src.read_bytes()
        if r["encoding"].startswith("nonutf8"):
            raw = transcode_to_utf8(raw, r["declared_charset"])
        try:
            segments, attr_segs = scan_html(raw, with_attr_spans=True)
        except Exception as e:
            print(f"[reemit] scan failed {rel}: {e}")
            continue
        repls = []
        for seg in segments:
            if seg.word_count() == 0:
                continue
            zh = zh_map.get(hash_key(seg.norm_key()))
            if not zh or zh == seg.norm_key():
                continue
            pieces, err = parse_segment_string(
                Segment(seg.tag, rebuild_items(
                    layout_of(seg))), zh)
            if err:
                print(f"[reemit] layout err {rel}: {err[:50]}")
                continue
            spans = seg.text_spans()
            if len(pieces) != len(spans):
                continue
            for (s0, e0), piece in zip(spans, pieces):
                orig = raw[s0:e0].decode("utf-8", "replace")
                if piece == orig:
                    continue
                if piece.strip() == "":
                    if orig.strip() == "":
                        continue          # 空白→空白：保留原空白字节
                    piece = " "           # 空译文→单空格：保留节点防边界移位
                repls.append((s0, e0, escape_min(piece).encode("utf-8")))
                n_seg_replaced += 1
        for name, (v0, v1), text, tag in filter_attrs_inside_code(
                attr_segs, segments):
            zh = zh_map.get(hash_key("attr:" + normalize_text(text)))
            if not zh or zh == normalize_text(text):
                continue
            repls.append((v0, v1,
                          escape_attr(zh).encode("utf-8")))
            n_seg_replaced += 1
        if repls or r["encoding"].startswith("nonutf8"):
            new_raw = apply_replacements(raw, repls)
        else:
            new_raw = raw
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(new_raw)
        n_html += 1
        if (idx + 1) % 500 == 0:
            print(f"[reemit] {idx+1}/{len(rows)}", flush=True)
    print(f"[reemit] html={n_html} assets={n_assets} "
          f"segments_replaced={n_seg_replaced}")


def layout_of(seg):
    kinds = [it.kind for it in seg.items]
    if all(k == "text" for k in kinds):
        return None
    g = []
    marker = 0
    for it in seg.items:
        if it.kind == "text":
            g.append(["t"])
        elif it.kind in ("code", "void", "gap"):
            g.append(["m", marker])
            marker += 1
        elif it.kind == "iopen":
            g.append(["o", it.tag])
        elif it.kind == "iclose":
            g.append(["c", it.tag])
    return g


def escape_attr(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


if __name__ == "__main__":
    sys.exit(main())
