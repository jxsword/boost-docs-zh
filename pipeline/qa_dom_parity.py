# -*- coding: utf-8 -*-
"""qa_dom_parity.py - QA gate 1: DOM parity between en and zh trees.

Usage: python -I pipeline/qa_dom_parity.py [--lib asio]

Checks per file: segment count, token signature per segment, code-span bytes.
Exit 0 only if zero failures.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import safe_join  # noqa: E402
from common import scan_html  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent


def sig(seg):
    return seg.token_signature()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", action="append", default=[])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--prefix", action="append", default=[])
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    en_root = safe_join(WORKSPACE, "data", "boost_1_92_0")
    zh_root = safe_join(WORKSPACE, "site", "zh", "1.92.0")
    man = safe_join(WORKSPACE, "inventory", "manifest.csv")
    rows = []
    with open(man, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    if args.lib:
        rows = [r for r in rows if r["lib"] in set(args.lib)]
    if args.prefix:
        rows = [r for r in rows
                if any(r["relpath"].startswith(p) for p in args.prefix)]
    if args.limit:
        rows = rows[:args.limit]

    fails = []
    checked = 0
    for r in rows:
        rel = r["relpath"]
        if not rel.lower().endswith((".html", ".htm")):
            continue
        en_f = safe_join(en_root, rel)
        zh_f = safe_join(zh_root, rel)
        if not zh_f.exists():
            continue
        try:
            en_segs, en_attrs = scan_html(en_f.read_bytes())
            zh_segs, zh_attrs = scan_html(zh_f.read_bytes())
        except Exception as e:
            fails.append((rel, f"scan error: {e}"))
            continue
        checked += 1
        en_s = [s for s in en_segs]
        zh_s = [s for s in zh_segs]
        if len(en_s) != len(zh_s):
            fails.append((rel, f"segment count {len(en_s)} != {len(zh_s)}"))
            continue
        for i, (a, b) in enumerate(zip(en_s, zh_s)):
            if sig(a) != sig(b):
                fails.append((rel, f"seg#{i} token sig mismatch"))
                break
            en_codes = [it.text for it in a.items if it.kind == "code"]
            zh_codes = [it.text for it in b.items if it.kind == "code"]
            if en_codes != zh_codes:
                fails.append((rel, f"seg#{i} code bytes differ"))
                break
        if len(en_attrs) != len(zh_attrs):
            fails.append((rel, f"attr count {len(en_attrs)} != "
                               f"{len(zh_attrs)}"))
        if len(fails) > 40:
            fails.append(("...", "too many failures, truncated"))
            break
    for rel, msg in fails[:40]:
        print(f"[qa_dom] FAIL {rel}: {msg}")
    print(f"[qa_dom] checked={checked} fails={len(fails)}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    sys.exit(main())
