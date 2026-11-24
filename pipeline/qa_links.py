# -*- coding: utf-8 -*-
"""qa_links.py - QA gate 3: link integrity of the mirror.

Usage: python -I pipeline/qa_links.py [--lib asio] [--prefix P] ...

Buckets:
  ok        - target exists in the zh mirror
  deferred  - exists in EN, not yet mirrored (expected during phased rollout;
              must be 0 at S6 full acceptance)
  upstream  - missing in the EN tree as well (upstream defect or template
              placeholder; mirrored faithfully, non-fatal)
  hard      - exists in EN but missing in zh AND is an asset (css/js/img/
              font/manifest): a real mirror defect. Exit code is driven by
              this bucket only.
"""
from __future__ import annotations

import argparse
import csv
import posixpath
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import safe_join  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent
RE_LINK = re.compile(rb'(?:href|src)\s*=\s*["\']([^"\']+)["\']',
                     re.IGNORECASE)
ASSET_EXTS = {".css", ".js", ".png", ".gif", ".jpg", ".jpeg", ".svg", ".ico",
              ".pdf", ".woff", ".woff2", ".ttf", ".webmanifest", ".json",
              ".xml", ".mp3", ".wav"}


def is_relative_link(u: str) -> bool:
    if not u or u.startswith(("#", "http:", "https:", "mailto:",
                              "data:", "javascript:")):
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", action="append", default=[])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--prefix", action="append", default=[])
    args = ap.parse_args()

    zh_root = safe_join(WORKSPACE, "site", "zh", "1.92.0")
    en_root = safe_join(WORKSPACE, "data", "boost_1_92_0")
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

    hard = []
    n_defer = n_upstream = n_ok = 0
    checked = 0
    for r in rows:
        rel = r["relpath"]
        if not rel.lower().endswith((".html", ".htm")):
            continue
        f = safe_join(zh_root, rel)
        if not f.exists():
            continue
        checked += 1
        raw = f.read_bytes()
        base = posixpath.dirname(rel)
        seen = set()
        for m in RE_LINK.finditer(raw):
            u = m.group(1).decode("utf-8", "replace")
            if not is_relative_link(u):
                continue
            path = u.split("#", 1)[0].split("?", 1)[0]
            if not path or path in seen:
                continue
            seen.add(path)
            target = posixpath.normpath(posixpath.join(base, path))
            if target.startswith("../") or target == "..":
                n_upstream += 1
                continue
            if "/example/" in "/" + target:
                n_upstream += 1  # 策略排除：example/ 不在镜像范围（总纲 §4.2）
                continue
            if (en_root / target).is_dir():
                n_upstream += 1  # 策略排除：目录链接（源码树目录索引，静态镜像无目录列表）
                continue
            try:
                en_ok = safe_join(en_root, target).exists()
                zh_ok = safe_join(zh_root, target).exists()
            except ValueError:
                # 上游 HTML 内嵌的畸形链接（如 file:/E:/... 绝对路径遗留），
                # safe_join 拒绝解析 → 如实镜像的上游缺陷，归 upstream
                n_upstream += 1
                continue
            if zh_ok:
                n_ok += 1
            elif en_ok:
                ext = posixpath.splitext(target)[1].lower()
                if ext in ASSET_EXTS:
                    hard.append((rel, u))
                else:
                    n_defer += 1
                    if n_defer <= 40:
                        print(f"[qa_links] DEFER {rel}: {u}")
            else:
                n_upstream += 1
        if len(hard) > 40:
            break
    for rel, u in hard[:40]:
        print(f"[qa_links] HARD {rel}: {u}")
    print(f"[qa_links] checked={checked} hard={len(hard)} "
          f"deferred={n_defer} upstream={n_upstream} ok={n_ok}")
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    sys.exit(main())
