# -*- coding: utf-8 -*-
"""emit_from_txt.py - main-session translation emitter.

Usage: python -I pipeline/emit_from_txt.py <batch_id>
Input:  work/zh_txt/<batch_id>.json  (a JSON array of zh strings, positional)
Output: work/results/<batch_id>.json (h values paired from the batch file)
Prints per-item validation failures; nonzero exit if any.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from common import punct_halfwidth, parse_segment_string, Segment  # noqa: E402
from extract_segments import rebuild_items  # noqa: E402
from inventory import safe_join  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) != 2:
        print("usage: emit_from_txt.py <batch_id>")
        return 2
    bid = sys.argv[1]
    bpath = safe_join(WORKSPACE, "work", "batches", f"{bid}.json")
    tpath = safe_join(WORKSPACE, "work", "zh_txt", f"{bid}.json")
    batch = json.loads(bpath.read_text(encoding="utf-8"))
    zh_list = json.loads(tpath.read_text(encoding="utf-8"))
    items = batch["items"]
    if len(zh_list) != len(items):
        print(f"[emit] FATAL: {len(zh_list)} zh strings != {len(items)} items")
        return 2
    fails = 0
    out = []
    for i, (it, zh) in enumerate(zip(items, zh_list)):
        zh = punct_halfwidth(zh)
        pieces, err = parse_segment_string(
            Segment("p", rebuild_items(it.get("g"))), zh)
        if err:
            print(f"[emit] FAIL item {i}: {err}")
            print(f"   en: {it['s'][:110]}")
            print(f"   zh: {zh[:110]}")
            fails += 1
        out.append({"h": it["h"], "zh": zh})
    rpath = safe_join(WORKSPACE, "work", "results", f"{bid}.json")
    if fails == 0:
        rpath.write_text(json.dumps({"id": bid, "items": out},
                                    ensure_ascii=False, indent=1),
                         encoding="utf-8")
        print(f"[emit] {bid}: {len(out)} items OK -> results/")
        return 0
    print(f"[emit] {bid}: {fails} failures, NOT written")
    return 1


if __name__ == "__main__":
    sys.exit(main())
