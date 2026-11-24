# -*- coding: utf-8 -*-
"""Build work/results/<id>.json from a TSV of translations.

TSV format (work/scratch/mpz_dump/<id>.zh.tsv): each non-empty line is
`idx<TAB>zh`. Lines are optional; missing indices fall back to the source
string unchanged (safe for pure-mark segments). Usage:

  python -I scripts/mpz_build.py multiprecision__0049 [more ids...]
"""
import json
import sys
from pathlib import Path

WS = Path(__file__).resolve().parent.parent
BATCH = WS / "work" / "batches"
TSVDIR = WS / "work" / "scratch" / "mpz_dump"
RES = WS / "work" / "results"


def build(batch_id: str, force_all: bool = False):
    b = json.loads((BATCH / f"{batch_id}.json").read_text(encoding="utf-8"))
    tsv = TSVDIR / f"{batch_id}.zh.tsv"
    zh = {}
    if tsv.exists():
        for ln, line in enumerate(tsv.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            idx, _, text = line.partition("\t")
            zh[int(idx)] = text
    items = []
    for i, it in enumerate(b["items"]):
        if i in zh:
            text = zh[i]
        elif force_all:
            raise SystemExit(f"{batch_id}: item {i} missing in tsv")
        else:
            text = it["s"]
        items.append({"h": it["h"], "zh": text})
    res = {"id": batch_id, "items": items}
    RES.mkdir(parents=True, exist_ok=True)
    (RES / f"{batch_id}.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"built {batch_id}: {len(items)} items ({len(zh)} from tsv)")


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for bid in sys.argv[1:]:
        build(bid)


if __name__ == "__main__":
    main()
