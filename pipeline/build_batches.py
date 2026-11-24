# -*- coding: utf-8 -*-
"""build_batches.py - pack untranslated segments into LLM translation batches.

Usage: python -I pipeline/build_batches.py --lib asio [--lib math] [--size 50]

Inputs:  work/segments/<lib>.jsonl, tm/segments.jsonl, pipeline/common_segments.json
Outputs: work/batches/<lib>__<seq>.json + work/ledger/batch_ledger.csv (append)
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import safe_join  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent


def safe_name(lib: str) -> str:
    return "".join(ch if (ch.isalnum() or ch in "_-") else "_"
                   for ch in lib)


def load_done_keys() -> dict:
    """h -> zh from TM + common segments."""
    done = {}
    tm = safe_join(WORKSPACE, "tm", "segments.jsonl")
    if tm.exists():
        with open(tm, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                d = json.loads(line)
                if d.get("zh"):
                    done[d["h"]] = d["zh"]
    cs = safe_join(WORKSPACE, "pipeline", "common_segments.json")
    if cs.exists():
        data = json.loads(cs.read_text(encoding="utf-8"))
        for h, zh in data.get("map", {}).items():
            done[int(h)] = zh
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", action="append", default=[])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--size", type=int, default=50)
    args = ap.parse_args()

    segdir = safe_join(WORKSPACE, "work", "segments")
    batchdir = safe_join(WORKSPACE, "work", "batches")
    batchdir.mkdir(parents=True, exist_ok=True)
    ledgerdir = safe_join(WORKSPACE, "work", "ledger")
    ledgerdir.mkdir(parents=True, exist_ok=True)

    done = load_done_keys()
    print(f"[batches] done keys (TM+common): {len(done)}")

    if args.all:
        segfiles = sorted(segdir.glob("*.jsonl"))
    else:
        segfiles = [safe_join(segdir, f"{safe_name(l)}.jsonl")
                    for l in args.lib]
        segfiles = [p for p in segfiles if p.exists()]
    ledger_path = safe_join(ledgerdir, "batch_ledger.csv")
    existing_ids = set()
    live_rows = []
    if ledger_path.exists():
        with open(ledger_path, newline="", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                existing_ids.add(r["batch_id"])
                bfile = safe_join(batchdir, f"{r['batch_id']}.json")
                if r["status"] == "merged" or bfile.exists():
                    live_rows.append(r)
                # queued 且文件已不存在的陈旧行：清除
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(["batch_id", "lib", "n_items", "words_est", "status",
                    "created_at"])
        for r in live_rows:
            w.writerow([r["batch_id"], r["lib"], r["n_items"],
                        r["words_est"], r["status"], r["created_at"]])
        ledger_path.write_text(buf.getvalue(), encoding="utf-8-sig")
        existing_ids = {r["batch_id"] for r in live_rows}

    # 已被现有 queued 批次文件覆盖的段：跳过，防重复入批
    pending_h = set()
    for r in live_rows:
        if r["status"] == "queued":
            bfile = safe_join(batchdir, f"{r['batch_id']}.json")
            if bfile.exists():
                try:
                    d = json.loads(bfile.read_text(encoding="utf-8"))
                    for it in d.get("items", []):
                        pending_h.add(it["h"])
                except (json.JSONDecodeError, OSError):
                    pass

    rows = []
    total_new = 0
    # per-lib next sequence: continue after the max seq already in ledger
    next_seq = {}
    for bid in existing_ids:
        if "__" in bid:
            lib, seq = bid.rsplit("__", 1)
            try:
                s = int(seq)
                next_seq[lib] = max(next_seq.get(lib, 1), s + 1)
            except ValueError:
                pass
    # (stale queued rows are harmless: merge_results ignores ids whose
    #  batch file is missing, and TM skips their segments on rebuild)
    for sf in segfiles:
        lib = sf.stem
        recs = []
        with open(sf, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                d = json.loads(line)
                if d["h"] in done or d["h"] in pending_h:
                    continue
                recs.append(d)
        if not recs:
            continue
        total_new += len(recs)
        seq = next_seq.get(lib, 1)
        i = 0
        # group by page title to keep context, preserving file order
        recs.sort(key=lambda d: (d["f"], d.get("t") or ""))
        while i < len(recs):
            j = i
            budget = 0
            while j < len(recs) and (j - i) < args.size:
                w = len(recs[j]["s"].split())
                if j > i and budget + w > 900:
                    break
                budget += w
                j += 1
            chunk = recs[i:j]
            i = j
            bid = f"{lib}__{seq:04d}"
            seq += 1
            next_seq[lib] = seq
            titles = []
            for d in chunk:
                t = d.get("t") or ""
                if t and t not in titles:
                    titles.append(t)
            batch = {"id": bid, "lib": lib, "n": len(chunk),
                     "ctx": titles[:6], "items": chunk}
            bpath = safe_join(batchdir, f"{bid}.json")
            bpath.write_text(json.dumps(batch, ensure_ascii=False,
                                        indent=1), encoding="utf-8")
            words_est = sum(len(d["s"].split()) for d in chunk)
            rows.append([bid, lib, len(chunk), words_est, "queued",
                         time.strftime("%Y-%m-%d %H:%M:%S")])
    if rows:
        new_file = not ledger_path.exists()
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerows(rows)
        if new_file:
            header = "batch_id,lib,n_items,words_est,status,created_at\n"
            ledger_path.write_text(header + buf.getvalue(), encoding="utf-8")
        else:
            with open(ledger_path, "a", encoding="utf-8") as f:
                f.write(buf.getvalue())
    print(f"[batches] {total_new} segments -> {len(rows)} batches")


if __name__ == "__main__":
    sys.exit(main())
