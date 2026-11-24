# -*- coding: utf-8 -*-
"""build_common_segments.py - compile work/common_zh.tsv into
pipeline/common_segments.json keyed by segment hash.

Sample matching: exact key match, or 240-char prefix match (segments.jsonl
stores keys truncated to 240 chars).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import safe_join  # noqa: E402
from inventory import hash_key  # noqa: E402
from common import punct_halfwidth  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent


def main():
    tsv = safe_join(WORKSPACE, "work", "common_zh.tsv")
    segs = safe_join(WORKSPACE, "inventory", "segments.jsonl")
    key2h = {}
    with open(segs, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                h, s, pages, words = json.loads(line)
                key2h[s] = h
    pairs = []
    misses = []
    for line in tsv.read_text(encoding="utf-8").splitlines():
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        sample, zh = line.split("\t", 1)
        zh = punct_halfwidth(zh)
        h = key2h.get(sample)
        derived = zh
        if h is None and len(sample) >= 240:
            for s, hh in key2h.items():
                if s.startswith(sample):
                    h = hh
                    break
        if h is None:
            # wrapper-marker derivation: key = MARKERS + sample + MARKERS
            import re as _re
            tok = r"(?:\u27e6[^\u27e7]*\u27e7|\u2983\d+\u2984)"
            pat = _re.compile(
                r"^((?:" + tok + r")+)" + _re.escape(sample) +
                r"((?:" + tok + r")*)$")
            for s, hh in key2h.items():
                m = pat.match(s)
                if m:
                    h = hh
                    derived = m.group(1) + zh + m.group(2)
                    break
        if h is None:
            misses.append(sample[:60])
        else:
            pairs.append((h, sample, derived))
    meta = {
        "description": "common segments: human-refined once, applied mechanically",
        "generated": "2026-11-14",
        "baseline": "Boost 1.92.0",
        "source_tsv": "work/common_zh.tsv",
        "count": len(pairs),
    }
    m = {str(h): zh for h, _s, zh in pairs}
    out = safe_join(WORKSPACE, "pipeline", "common_segments.json")
    out.write_text(json.dumps({"meta": meta, "map": m}, ensure_ascii=False,
                              indent=1), encoding="utf-8")
    print(f"[common] entries={len(pairs)} misses={len(misses)}")
    for s in misses[:20]:
        print(f"[common] MISS: {s}")


if __name__ == "__main__":
    sys.exit(main())
