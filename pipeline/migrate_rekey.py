# -*- coding: utf-8 -*-
"""migrate_rekey.py - re-key TM entries after the norm_key change.

Old TM rows were keyed by marker-stripped text; the canonical key is now the
normalized segment string (markers preserved). The `en` field stores exactly
that string, so re-keying is: new_h = hash_key(normalize(en)).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import safe_join, hash_key  # noqa: E402
from common import normalize_text, punct_halfwidth  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent


def main():
    tm = safe_join(WORKSPACE, "tm", "segments.jsonl")
    rows = {}
    if tm.exists():
        with open(tm, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    d = json.loads(line)
                    en = normalize_text(d["en"])
                    h = hash_key(en)
                    rows.setdefault(h, {"h": h, "en": en,
                                        "zh": punct_halfwidth(d["zh"])})
    lines = "".join(json.dumps(d, ensure_ascii=False) + "\n"
                    for d in rows.values())
    tm.write_text(lines, encoding="utf-8")
    print(f"[rekey] TM rows now: {len(rows)}")


if __name__ == "__main__":
    sys.exit(main())
