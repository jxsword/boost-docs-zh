# -*- coding: utf-8 -*-
"""inventory_run.py - S1 corpus inventory (no SQL, fixed file names only).

Usage: python -I pipeline/inventory_run.py [--root data/boost_1_92_0]
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import (attribute_lib, build_libname_sets, classify_form,
                       enumerate_forest, hash_key, safe_join)
from common import count_words, detect_encoding, normalize_text, scan_html

WORKSPACE = Path(__file__).resolve().parent.parent
COMMON_PAGES = 3
P_BITS = 21
P_MASK = (1 << P_BITS) - 1


def pack(pages: int, words: int) -> int:
    if words >= (1 << 40):
        words = (1 << 40) - 1
    return (words << P_BITS) | pages


def unpack(packed: int):
    return (packed & P_MASK, packed >> P_BITS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="data/boost_1_92_0")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    root = safe_join(WORKSPACE, args.root)
    if not root.is_dir():
        print("[FATAL] corpus root missing")
        return 2
    outdir = safe_join(WORKSPACE, "inventory")
    outdir.mkdir(exist_ok=True)
    files = enumerate_forest(root)
    libs, tools = build_libname_sets(root)
    print(f"[inventory] enumerated {len(files)} html files")
    return run_scan(files, root, outdir, libs, tools, args.limit)


def run_scan(files, root: Path, outdir: Path, libs: set, tools: set, limit: int):
    manifest_rows = []
    excl = Counter()
    t0 = time.time()
    agg = {}          # h -> packed(pages | words<<21)
    pair_set = set()  # (h<<8 | lib_id) unique (h, lib) membership
    lib_ids = {}      # lib name -> id
    samples = {}      # h -> sample text for keys that reached >=2 pages
    total = len(files)
    for idx, (rel, rule) in enumerate(files):
        if limit and idx >= limit:
            break
        try:
            full = safe_join(root, rel)
        except ValueError:
            excl["path_escape"] += 1
            continue
        try:
            raw = full.read_bytes()
        except OSError as e:
            manifest_rows.append([rel, attribute_lib(rel, rule, libs, tools),
                                  "read_error", "", "", 0, "", 0, 0, "error"])
            excl["read_error"] += 1
            continue
        enc_state, declared = detect_encoding(raw)
        lib = attribute_lib(rel, rule, libs, tools)
        form = classify_form(rel, rule, raw[:16384])
        try:
            segments, attr_segs = scan_html(raw)
            scan_ok = True
        except Exception:
            segments, attr_segs = [], []
            scan_ok = False
            excl["parse_error"] += 1
        words = sum(s.word_count() for s in segments)
        words += sum(count_words(v) for _n, v, _t in attr_segs)
        title = ""
        for s in segments:
            if s.tag == "title":
                t = normalize_text(s.segment_string())
                title = re.sub(r"[\u2983\u2984\u27e6\u27e7]", "", t)
                break
        page_counter = {}
        for s in segments:
            key = s.norm_key()
            if not key:
                continue
            w = s.word_count()
            if w == 0:
                continue
            if key in page_counter:
                page_counter[key][2] += 1
            else:
                page_counter[key] = [key, w, 1]
        lid = lib_ids.get(lib)
        if lid is None:
            lid = len(lib_ids)
            lib_ids[lib] = lid
        for key, (_k, w, inst) in page_counter.items():
            h = hash_key(key)
            p = agg.get(h, 0)
            pages = p & P_MASK
            if pages == 0:
                agg[h] = pack(1, w)
            else:
                if pages == 1:
                    samples.setdefault(h, key[:200])
                agg[h] = pack(pages + 1, p >> P_BITS)
            pair_set.add((h << 16) | lid)
        manifest_rows.append([
            rel, lib, form, enc_state, declared, len(raw), title[:200],
            words, len(segments) + len(attr_segs),
            "ok" if scan_ok else "parse_error",
        ])
        if (idx + 1) % 500 == 0:
            print(f"[inventory] {idx+1}/{total} ({time.time()-t0:.0f}s)",
                  flush=True)
    print(f"[inventory] scan done ({time.time()-t0:.0f}s)")
    return finish(manifest_rows, agg, pair_set, lib_ids, samples, excl,
                  outdir, t0)


def finish(manifest_rows, agg, pair_set, lib_ids, samples, excl, outdir, t0):
    # per-lib stats from unique (h, lib) pairs
    id2lib = {v: k for k, v in lib_ids.items()}
    per_lib = {}
    for pair in pair_set:
        h = pair >> 16
        lid = pair & 0xFFFF
        lib = id2lib[lid]
        pages, words = unpack(agg.get(h, 0))
        st = per_lib.setdefault(lib, {"llm_cnt": 0, "llm_words": 0,
                                      "common_words": 0})
        if pages >= COMMON_PAGES:
            st["common_words"] += words
        else:
            st["llm_cnt"] += 1
            st["llm_words"] += words
    pair_set.clear()

    # segments.jsonl (sorted by h)
    seg_out = safe_join(outdir, "segments.jsonl")
    common_cnt = common_words = uniq_words = 0
    with open(seg_out, "w", encoding="utf-8") as f:
        for h in sorted(agg.keys()):
            pages, words = unpack(agg[h])
            uniq_words += words
            if pages >= COMMON_PAGES:
                common_cnt += 1
                common_words += words
            f.write(json.dumps([h, samples.get(h, ""), pages, words],
                               ensure_ascii=False) + "\n")
    print("[inventory] segments.jsonl written")

    # manifest.csv
    man_path = safe_join(outdir, "manifest.csv")
    with open(man_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["relpath", "lib", "form", "encoding", "declared_charset",
                    "bytes", "title", "words", "segments", "status"])
        w.writerows(manifest_rows)
    print("[inventory] manifest.csv written")

    write_report(manifest_rows, per_lib, common_cnt, common_words, uniq_words,
                 samples, excl, outdir, t0)
    return 0


def write_report(manifest_rows, per_lib, common_cnt, common_words,
                 uniq_words, samples, excl, outdir, t0):
    form_cnt, form_words = Counter(), Counter()
    enc_cnt = Counter()
    lib_files, lib_words = Counter(), Counter()
    nonutf8 = []
    total_words = total_bytes = 0
    for r in manifest_rows:
        rel, lib, form, enc, declared, nbytes, title, words, nseg, status = r
        form_cnt[form] += 1
        form_words[form] += words
        enc_cnt[enc.split(":")[0]] += 1
        lib_files[lib] += 1
        lib_words[lib] += words
        total_words += words
        total_bytes += nbytes
        if enc.startswith("nonutf8"):
            nonutf8.append((rel, enc))

    llm_cnt = sum(s["llm_cnt"] for s in per_lib.values())
    llm_words = sum(s["llm_words"] for s in per_lib.values())
    batches = (llm_cnt + 49) // 50
    hit = (common_words / uniq_words * 100.0) if uniq_words else 0.0

    L = []
    a = L.append
    a("# Boost 1.92.0 corpus inventory report (S1)")
    a("")
    a("> meta: generated 2026-11-14; baseline Boost 1.92.0 (frozen 2026-11-14)")
    a("> corpus: boost_1_92_0.7z from archives.boost.io (144,300,348 bytes,")
    a("> downloaded 2026-11-14 via proxy with resume; extracted read-only at")
    a("> data/boost_1_92_0; tools pipeline/inventory.py + inventory_run.py)")
    a("")
    a("## 1. totals")
    a("")
    a("| metric | value |")
    a("|---|---|")
    a(f"| html files | {len(manifest_rows):,} |")
    a(f"| html bytes | {total_bytes:,} ({total_bytes/1048576:.1f} MiB) |")
    a(f"| translatable english words | {total_words:,} |")
    a(f"| unique segment keys | {common_cnt + llm_cnt:,} |")
    a(f"| unique segment words | {uniq_words:,} |")
    a(f"| common keys (pages>=3) | {common_cnt:,} (words {common_words:,}) |")
    a(f"| common hit rate (unique-word basis) | {hit:.1f}% |")
    a(f"| LLM segments (pages<3) | {llm_cnt:,} (words {llm_words:,}) |")
    a(f"| LLM batches (50 seg/batch) | {batches:,} |")
    a("")
    a("## 2. form distribution")
    a("")
    a("| form | files | words |")
    a("|---|---|---|")
    for form, c in form_cnt.most_common():
        a(f"| {form} | {c:,} | {form_words[form]:,} |")
    a("")
    a("## 3. encoding distribution")
    a("")
    a("| encoding | files |")
    a("|---|---|")
    for enc, c in enc_cnt.most_common():
        a(f"| {enc} | {c:,} |")
    a("")
    a(f"non-utf8 files: {len(nonutf8)} (details in manifest encoding column)")
    for rel, enc in nonutf8[:40]:
        a(f"- {rel} ({enc})")
    if len(nonutf8) > 40:
        a(f"- ... {len(nonutf8) - 40} more in manifest")
    a("")
    a("## 4. per-library detail (top 80 by words)")
    a("")
    a("| lib | files | words | llm segs | common words | batches |")
    a("|---|---|---|---|---|---|")
    for lib in sorted(lib_words, key=lambda k: -lib_words[k])[:80]:
        st = per_lib.get(lib, {"llm_cnt": 0, "llm_words": 0,
                               "common_words": 0})
        b = (st["llm_cnt"] + 49) // 50
        a(f"| {lib} | {lib_files[lib]:,} | {lib_words[lib]:,} | "
          f"{st['llm_cnt']:,} | {st['common_words']:,} | {b:,} |")
    rest = sorted(lib_words, key=lambda k: -lib_words[k])[80:]
    if rest:
        a(f"| (others: {len(rest)} libs) | "
          f"{sum(lib_files[k] for k in rest):,} | "
          f"{sum(lib_words[k] for k in rest):,} | | | |")
    a("")
    a("## 5. calibration vs plan section 4.4")
    a("")
    a("| item | plan estimate | measured |")
    a("|---|---|---|")
    a(f"| html pages | 25k-40k | {len(manifest_rows):,} |")
    a(f"| english words | 10M-20M | {total_words:,} "
      f"({total_words/1e6:.1f}M) |")
    a(f"| common-segment reduction | 20-40% | {hit:.1f}% |")
    a(f"| LLM batches | thousands | {batches:,} ({llm_cnt:,} segs) |")
    a(f"| chinese output | 15M-30M chars | ~{int(total_words*1.6):,} chars "
      f"(1 word ~ 1.6 chars) |")
    a("")
    a("## 6. exclusions and anomalies")
    a("")
    for k, v in sorted(excl.items()):
        a(f"- {k}: {v}")
    if not excl:
        a("- none")
    a("")
    a("basis: translatable text nodes + whitelist attrs (alt/title/meta")
    a("description); pre/code/script/style excluded; unique key = normalized")
    a("text sha256 truncated; common = key on >=3 pages; batches=ceil(n/50).")
    text = "\n".join(L)
    rep = safe_join(outdir, "inventory_report.md")
    rep.write_text(text, encoding="utf-8")

    # per-lib stats csv (progress ledger base)
    import io
    sio = io.StringIO()
    cw = csv.writer(sio)
    cw.writerow(["lib", "files", "words", "llm_cnt", "llm_words",
                 "common_words"])
    for lib in sorted(lib_words, key=lambda k: -lib_words[k]):
        st = per_lib.get(lib, {"llm_cnt": 0, "llm_words": 0,
                               "common_words": 0})
        cw.writerow([lib, lib_files[lib], lib_words[lib], st["llm_cnt"],
                     st["llm_words"], st["common_words"]])
    stpath = safe_join(outdir, "lib_stats.csv")
    stpath.write_text(sio.getvalue(), encoding="utf-8-sig")
    print("[inventory] lib_stats.csv written")


if __name__ == "__main__":
    sys.exit(main())
