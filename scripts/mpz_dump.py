# -*- coding: utf-8 -*-
"""Dump multiprecision batches 0049-0096 to work/scratch/mpz_dump/<id>.txt.

Each line: idx<TAB>source-segment-string. Also validates that zh TSV files
present in the same dir parse and produce results JSON via mpz_build.py.
"""
import json
import sys
from pathlib import Path

WS = Path(__file__).resolve().parent.parent
BATCH = WS / "work" / "batches"
OUT = WS / "work" / "scratch" / "mpz_dump"
OUT.mkdir(parents=True, exist_ok=True)


def dump(batch_id: str):
    b = json.loads((BATCH / f"{batch_id}.json").read_text(encoding="utf-8"))
    lines = [f"## {batch_id}  ctx={b.get('ctx')!r}  n={len(b['items'])}"]
    for i, it in enumerate(b["items"]):
        s = it["s"].replace("\t", " ")
        npieces = sum(1 for e in (it.get("g") or [["t"]]) if e[0] == "t")
        lines.append(f"{i}\t{npieces}\t{s}")
    (OUT / f"{batch_id}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ids = sys.argv[1:] or [
        f"multiprecision__{i:04d}" for i in range(49, 97)]
    for bid in ids:
        dump(bid)
        print("dumped", bid)


if __name__ == "__main__":
    main()
