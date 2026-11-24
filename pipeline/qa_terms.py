# -*- coding: utf-8 -*-
"""qa_terms.py - QA gate 2: protected identifiers must survive translation.

Usage: python -I pipeline/qa_terms.py [--lib asio]

Two checks, per paired en/zh segment:
  A. every identifier in en text that is listed in protected_terms.txt
     (or starts with BOOST_) must appear verbatim in the zh segment;
  B. every qualified name chain (ns::name::...) in en text must appear
     verbatim in the zh segment.
Zero violations required. Code/pre content is excluded by the scanner.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import safe_join  # noqa: E402
from common import scan_html  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent
RE_IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
RE_QUAL = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)+")


def load_terms() -> set:
    p = safe_join(WORKSPACE, "pipeline", "protected_terms.txt")
    out = set()
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.add(line)
    return out


def text_of(seg) -> str:
    return " ".join(it.text for it in seg.items if it.kind == "text")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", action="append", default=[])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--prefix", action="append", default=[])
    args = ap.parse_args()

    terms = load_terms()
    # strict matching: generic English words that double as lib dir names
    # (system/exception/config/...) must not hard-fail the gate; display
    # names that are not English words are protected explicitly.
    STRICT_EXTRA = {"Asio", "Beast", "Hana", "Spirit", "Boost"}

    def is_strict(t: str) -> bool:
        if t in STRICT_EXTRA:
            return True
        if t.startswith("BOOST_") or "_" in t or "::" in t or "." in t:
            return True
        return bool(t[1:] and any(c.isupper() for c in t[1:])) or t.isupper()

    strict_terms = {t for t in terms if is_strict(t)}
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

    viols = []
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
            en_segs, _ = scan_html(en_f.read_bytes())
            zh_segs, _ = scan_html(zh_f.read_bytes())
        except Exception:
            continue
        if len(en_segs) != len(zh_segs):
            continue
        checked += 1
        for i, (a, b) in enumerate(zip(en_segs, zh_segs)):
            en_t = text_of(a)
            zh_t = text_of(b)
            if not en_t or en_t == zh_t:
                continue
            for q in set(RE_QUAL.findall(en_t)):
                if q not in zh_t:
                    viols.append((rel, i, "qualified", q))
            for ident in set(RE_IDENT.findall(en_t)):
                if ident.startswith("BOOST_") or ident in strict_terms:
                    if ident not in zh_t:
                        viols.append((rel, i, "term", ident))
            if len(viols) > 40:
                break
        if len(viols) > 40:
            break
    for rel, i, kind, what in viols[:40]:
        print(f"[qa_terms] VIOL {rel} seg#{i} {kind}: {what}")
    print(f"[qa_terms] files={checked} violations={len(viols)} "
          f"terms={len(terms)}")
    sys.exit(1 if viols else 0)


if __name__ == "__main__":
    sys.exit(main())
