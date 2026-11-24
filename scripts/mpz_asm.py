# -*- coding: utf-8 -*-
"""Assemble + validate multiprecision results from per-piece TSVs.

Piece dump (work/scratch/mpz_dump/<id>.pieces.txt): `idx<TAB>k<TAB>source_piece`
where k is the translatable text-node index within the item (0-based).

Translation TSV (work/scratch/mpz_dump/<id>.zh.pieces.tsv):
`idx<TAB>k<TAB>zh_piece`. The script re-inserts pieces at their claimed gaps
(tokens/marks copied verbatim from the source string), validates each item
with pipeline.merge_results.validate_item, and writes
work/results/<id>.json. Items with no translation rows fall back to the
source string (only safe for pure-numeric segments).

Usage: python -I scripts/mpz_asm.py <batch_id> [more...]
"""
import json
import re
import sys
from pathlib import Path

WS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WS / "pipeline"))
from merge_results import validate_item  # noqa: E402

BATCH = WS / "work" / "batches"
TSVDIR = WS / "work" / "scratch" / "mpz_dump"
RES = WS / "work" / "results"

TOKEN_RE = re.compile(r"⦃\d+⦄|⟦/?[-a-zA-Z0-9_,]+⟧")


def claimed_gaps(g):
    """Gap indices claimed by text items, in text-item order (validator walk)."""
    claimed = []
    tokens_seen = 0
    next_gap = 0
    for kind, *_ in (g or [["t"]]):
        if kind == "t":
            gi = max(tokens_seen, next_gap)
            claimed.append(gi)
            next_gap = gi + 1
        elif kind in ("o", "c", "m"):
            tokens_seen += 1
        else:
            raise ValueError(f"unknown g kind {kind!r}")
    return claimed


def source_pieces(s, g):
    """Source text of each text node, in order."""
    claimed = claimed_gaps(g)
    toks = list(TOKEN_RE.finditer(s))
    n = len(toks)
    out = []
    for gi in range(n + 1):
        start = toks[gi - 1].end() if gi > 0 else 0
        end = toks[gi].start() if gi < n else len(s)
        if gi in claimed:
            out.append(s[start:end])
    return out


def rebuild(s, g, pieces):
    claimed = claimed_gaps(g)
    if len(pieces) != len(claimed):
        raise ValueError(f"piece count {len(pieces)} != text nodes {len(claimed)}")
    toks = list(TOKEN_RE.finditer(s))
    n = len(toks)
    gtok = [(k, *e) for k, *e in (g or [["t"]]) if k != "t"]
    if len(gtok) != n:
        raise ValueError(f"token count {n} != g non-text count {len(gtok)}")
    mi = 0
    for m, (kind, *extra) in zip(toks, gtok):
        tok = m.group(0)
        if kind == "m":
            want = f"⦃{mi}⦄"
            if tok != want:
                raise ValueError(f"mark mismatch: {tok!r} vs {want!r}")
            mi += 1
        elif kind == "o":
            if tok != f"⟦{extra[0]}⟧":
                raise ValueError(f"open mismatch: {tok!r}")
        elif kind == "c":
            if tok != f"⟦/{extra[0]}⟧":
                raise ValueError(f"close mismatch: {tok!r}")
        else:
            raise ValueError(f"unexpected kind {kind!r}")
    gap2piece = dict(zip(claimed, pieces))
    out = []
    for gi in range(n + 1):
        if gi in gap2piece:
            out.append(gap2piece[gi])
        if gi < n:
            out.append(toks[gi].group(0))
    return "".join(out)


def load_tsv(path):
    rows = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            parts = line.split("\t", 2)
            if len(parts) == 2:
                idx, k = parts
                text = ""
            else:
                idx, k, text = parts
            rows.setdefault(int(idx), {})[int(k)] = text
    return rows


def dump_pieces(batch_id: str):
    b = json.loads((BATCH / f"{batch_id}.json").read_text(encoding="utf-8"))
    lines = []
    for i, it in enumerate(b["items"]):
        for k, p in enumerate(source_pieces(it["s"], it.get("g"))):
            lines.append(f"{i}\t{k}\t{p}".replace("\n", " "))
    (TSVDIR / f"{batch_id}.pieces.txt").write_text(
        "\n".join(lines) + "\n", encoding="utf-8")


def build(batch_id: str):
    b = json.loads((BATCH / f"{batch_id}.json").read_text(encoding="utf-8"))
    rows = load_tsv(TSVDIR / f"{batch_id}.zh.pieces.tsv")
    items = []
    n_err = 0
    for i, it in enumerate(b["items"]):
        if i in rows:
            g = it.get("g")
            npieces = len(claimed_gaps(g))
            d = rows[i]
            if sorted(d) != list(range(npieces)):
                print(f"{batch_id} item {i}: piece keys {sorted(d)} != "
                      f"0..{npieces - 1}")
                n_err += 1
                continue
            try:
                zh = rebuild(it["s"], g, [d[k] for k in range(npieces)])
            except ValueError as e:
                print(f"{batch_id} item {i}: ASSEMBLE ERROR: {e}")
                n_err += 1
                continue
        else:
            zh = it["s"]
        _pieces, err = validate_item(it.get("g"), zh)
        if err:
            print(f"{batch_id} item {i}: VALIDATE ERROR: {err}")
            print(f"  zh={zh!r}")
            n_err += 1
        items.append({"h": it["h"], "zh": zh})
    if n_err:
        print(f"{batch_id}: {n_err} errors, NOT written")
        return False
    res = {"id": batch_id, "items": items}
    RES.mkdir(parents=True, exist_ok=True)
    (RES / f"{batch_id}.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"built {batch_id}: {len(items)} items, 0 errors "
          f"({sum(1 for r in rows)} translated items)")
    return True


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    if sys.argv[1] == "--dump":
        for bid in sys.argv[2:]:
            dump_pieces(bid)
        print("dumped pieces:", len(sys.argv) - 2)
        return
    ok = True
    for bid in sys.argv[1:]:
        ok = build(bid) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
