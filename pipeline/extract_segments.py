# -*- coding: utf-8 -*-
"""extract_segments.py - extract translatable segments per library.

Usage: python -I pipeline/extract_segments.py --lib asio [--limit N]
       python -I pipeline/extract_segments.py --all

Output: work/segments/<lib>.jsonl, one line per unique segment key:
    {"h": hash, "s": segment string, "g": token layout or null, "t": page title, "f": first file}
Layout g is a list of [kind, extra] where kind in t(text)/m(mark)/o(open)/c(close);
omitted (null) means a single plain text item.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import attribute_lib, build_libname_sets, safe_join  # noqa: E402
from common import (filter_attrs_inside_code, scan_html, count_words,
                    normalize_text)  # noqa: E402
from inventory import hash_key  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent


def load_manifest():
    man = safe_join(WORKSPACE, "inventory", "manifest.csv")
    rows = []
    with open(man, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def seg_layout(seg):
    """Compact token layout: None for plain single-text segments."""
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


def rebuild_items(g):
    """Pseudo-items for validation (kinds only, no spans/text)."""
    from common import Item
    if not g:
        return [Item("text")]
    out = []
    for kind, *extra in g:
        if kind == "t":
            out.append(Item("text"))
        elif kind == "m":
            out.append(Item("gap"))
        elif kind == "o":
            out.append(Item("iopen", tag=extra[0]))
        elif kind == "c":
            out.append(Item("iclose", tag=extra[0]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", action="append", default=[])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    root = safe_join(WORKSPACE, "data", "boost_1_92_0")
    segdir = safe_join(WORKSPACE, "work", "segments")
    segdir.mkdir(parents=True, exist_ok=True)

    rows = load_manifest()
    libs, tools = build_libname_sets(root)
    if args.all:
        targets = sorted({r["lib"] for r in rows})
    else:
        targets = args.lib
        known = set(libs) | set(tools) | {"(root)"}
        for lib in targets:
            known.add(lib)
    sel = [r for r in rows if r["lib"] in targets or args.all]
    if args.limit:
        sel = sel[:args.limit]
    print(f"[extract] {len(sel)} files, libs={len(targets)}")

    n_seg = 0
    per_lib = {}
    for r in sel:
        rel = r["relpath"]
        lib = r["lib"]
        full = safe_join(root, rel)
        try:
            raw = full.read_bytes()
        except OSError:
            continue
        try:
            segments, attr_segs = scan_html(raw, with_attr_spans=True)
        except Exception:
            continue
        seen_page = set()
        title = ""
        recs = []
        for s in segments:
            if s.tag == "title" and not title:
                t = normalize_text(s.segment_string())
                title = t
            if s.word_count() == 0:
                continue
            key = s.norm_key()
            if not key:
                continue
            h = hash_key(key)
            if h in seen_page:
                continue
            seen_page.add(h)
            recs.append({"h": h, "s": s.segment_string(),
                         "g": seg_layout(s), "t": title[:160],
                         "f": rel})
        for _n, _span, v, _tag in filter_attrs_inside_code(
                attr_segs, segments):
            key = normalize_text(v)
            if not key:
                continue
            h = hash_key("attr:" + key)
            if h in seen_page:
                continue
            seen_page.add(h)
            recs.append({"h": h, "s": key, "g": None,
                         "t": title[:160], "f": rel, "a": _n})
        bucket = per_lib.setdefault(lib, {})
        for rec in recs:
            if rec["h"] not in bucket:
                bucket[rec["h"]] = rec
                n_seg += 1
    for lib, bucket in per_lib.items():
        out_path = safe_join(segdir, f"{safe_name(lib)}.jsonl")
        lines = "".join(json.dumps(x, ensure_ascii=False) + "\n"
                        for x in bucket.values())
        out_path.write_text(lines, encoding="utf-8")
    print(f"[extract] wrote {n_seg} unique segment records "
          f"for {len(per_lib)} libs")


def safe_name(lib: str) -> str:
    keep = []
    for ch in lib:
        if ch.isalnum() or ch in "_-":
            keep.append(ch)
        else:
            keep.append("_")
    return "".join(keep)


if __name__ == "__main__":
    sys.exit(main())
