# -*- coding: utf-8 -*-
"""merge_results.py - validate translation results and merge into TM.

Usage: python -I pipeline/merge_results.py [--results work/results]

Validation (plan R5): result item count == batch item count; each zh string
parses back through the batch's stored token layout (segment count and
marker/tag parity). Invalid batches are marked failed for retry.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import safe_join  # noqa: E402
from common import (parse_segment_string, punct_halfwidth, Segment,
                    TOKEN_RE)  # noqa: E402
from extract_segments import rebuild_items  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent


def validate_item(g, zh: str):
    seg = Segment("p", rebuild_items(g))
    pieces, err = parse_segment_string(seg, zh)
    return pieces, err


def load_ledger(ledger_path: Path) -> dict:
    rows = {}
    if ledger_path.exists():
        with open(ledger_path, newline="", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                rows[r["batch_id"]] = r
    return rows


def save_ledger(ledger_path: Path, rows: dict):
    buf = csv.writer(_sink := __import__("io").StringIO())
    buf.writerow(["batch_id", "lib", "n_items", "words_est", "status",
                  "created_at"])
    for r in rows.values():
        buf.writerow([r["batch_id"], r["lib"], r["n_items"], r["words_est"],
                      r["status"], r["created_at"]])
    ledger_path.write_text(_sink.getvalue(), encoding="utf-8-sig")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="work/results")
    args = ap.parse_args()

    batchdir = safe_join(WORKSPACE, "work", "batches")
    resultsdir = safe_join(WORKSPACE, "work", "results")
    ledger_path = safe_join(WORKSPACE, "work", "ledger", "batch_ledger.csv")
    tm_path = safe_join(WORKSPACE, "tm", "segments.jsonl")
    tm_path.parent.mkdir(parents=True, exist_ok=True)

    ledger = load_ledger(ledger_path)
    done_h = set()
    if tm_path.exists():
        with open(tm_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    done_h.add(json.loads(line)["h"])

    n_merged = n_failed = n_skip = 0
    tm_lines = []
    for rpath in sorted(resultsdir.glob("*.json")):
        bid = rpath.stem
        lr = ledger.get(bid)
        if lr is None:
            print(f"[merge] {bid}: not in ledger, skip")
            n_skip += 1
            continue
        if lr["status"] == "merged":
            n_skip += 1
            continue
        bpath = safe_join(batchdir, f"{bid}.json")
        if not bpath.exists():
            print(f"[merge] {bid}: batch file missing")
            continue
        batch = json.loads(bpath.read_text(encoding="utf-8"))
        try:
            result = json.loads(rpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            lr["status"] = "failed:bad_json"
            n_failed += 1
            print(f"[merge] {bid}: bad json ({e})")
            continue
        items = result.get("items", [])
        bitems = batch["items"]
        if len(items) != len(bitems):
            lr["status"] = "failed:count_mismatch"
            n_failed += 1
            print(f"[merge] {bid}: item count {len(items)} != {len(bitems)}")
            continue
        ok = True
        new_items = []
        for bi, ri in zip(bitems, items):
            if ri.get("h") != bi["h"]:
                ok = False
                lr["status"] = "failed:h_mismatch"
                break
            zh = ri.get("zh", "")
            if not isinstance(zh, str) or not zh.strip():
                ok = False
                lr["status"] = "failed:empty_zh"
                break
            zh = punct_halfwidth(zh)
            pieces, err = validate_item(bi.get("g"), zh)
            if err:
                ok = False
                lr["status"] = f"failed:layout:{err[:60]}"
                break
            # 空文本硬校验：原文有标记外文本而译文只有标记 → 拒收
            en_text = TOKEN_RE.sub("", bi.get("s", "")).strip()
            zh_text = TOKEN_RE.sub("", zh).strip()
            if en_text and not zh_text:
                ok = False
                lr["status"] = "failed:empty_text"
                break
            if bi["h"] in done_h:
                continue
            new_items.append({"h": bi["h"], "en": bi["s"], "zh": zh})
        if not ok:
            n_failed += 1
            print(f"[merge] {bid}: {lr['status']}")
            continue
        for it in new_items:
            tm_lines.append(json.dumps(it, ensure_ascii=False) + "\n")
        lr["status"] = "merged"
        n_merged += 1
        rpath.unlink()
    if tm_lines:
        with open(tm_path, "a", encoding="utf-8") as f:
            f.write("".join(tm_lines))
    save_ledger(ledger_path, ledger)
    print(f"[merge] merged={n_merged} failed={n_failed} skipped={n_skip} "
          f"tm_lines={len(tm_lines)}")


if __name__ == "__main__":
    sys.exit(main())
