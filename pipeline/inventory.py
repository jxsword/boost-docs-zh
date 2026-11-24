# -*- coding: utf-8 -*-
"""inventory.py — S1 语料盘点（总纲 §4.2/§4.4/R6）。

用法（工作区根目录执行）:
    python -I pipeline/inventory.py [--root data/boost_1_92_0]

产出:
    inventory/manifest.csv            路径/库归属/形态/编码/词数/状态
    inventory/盘点报告.md             每库统计与估算校准
    inventory/common_segments_top.csv 高频公共段 Top
    inventory/segments.sqlite         段频表（seg / seglib）

安全设计（不可信语料约束）：
- 语料只读解析，不执行其中任何文件；脚本位于 pipeline/，与语料隔离。
- 全部路径统一经 safe_join()：拒绝 '..' 组件 + resolve 后 is_relative_to 校验。
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import sqlite3
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from common import count_words, detect_encoding, normalize_text, scan_html  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent


def safe_join(base: Path, *parts) -> Path:
    """安全拼接：拒绝 '..' 组件；resolve 后必须仍在 base 内。"""
    for p in parts:
        s = str(p)
        if s == "" or s == ".":
            continue
        if s == ".." or s.startswith("../") or "/../" in s or s.endswith("/.."):
            raise ValueError(f"path traversal rejected: {p!r}")
    joined = (base / Path(*parts)).resolve()
    if not joined.is_relative_to(base.resolve()):
        raise ValueError(f"path escapes base: {base} <- {parts}")
    return joined


EXCLUDE_COMPONENTS = {"example", "examples", "test", "tests", "status",
                      "boost", "node_modules"}
# 总纲 §4.2 修正（2026-11-16）：上述排除仅适用于仓库根层级的 example/test/
# status/boost 源码树；libs/*/doc 与 tools/*/doc 树内不得按组件名剪枝——
# 库 doc 树中名为 test/boost/examples 的目录是正常渲染文档
# （如 Boost.Test 手册 libs/test/doc/html、mysql examples 章节页）。
# 库名白名单同理：Boost.Test 是真实库（libs/test），不得因名跳过。
DOC_TREE_PRUNE = set()  # doc 树游走不剪枝
HTML_EXTS = {".html", ".htm"}

RE_DOXYGEN = re.compile(rb'name="generator" content="Doxygen|>Doxygen<')
RE_ASCIIDOCTOR = re.compile(rb'name="generator" content="Asciidoctor|class="docca')
RE_BOOSTBOOK = re.compile(
    rb'name="generator" content="DocBook XSL|class="boostbook|'
    rb'copyright-footer|class="nav_header|BoostBook')
RE_ANTORA = re.compile(rb'class="body"|antora|class="navbar')


def enumerate_forest(root: Path):
    """按总纲 §4.2 枚举文档森林。产出 [(relpath, rule)]。"""
    rules = []

    def add_dir(base: Path, rule: str):
        if not base.is_dir():
            return
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames
                           if d not in DOC_TREE_PRUNE]
            for fn in filenames:
                if Path(fn).suffix.lower() in HTML_EXTS:
                    rel = (Path(dirpath) / fn).relative_to(root)
                    rules.append((rel.as_posix(), rule))

    for fn in ("index.html", "index.htm"):
        if (root / fn).is_file():
            rules.append((fn, "root_index"))
    add_dir(root / "more", "more")
    add_dir(root / "doc" / "html", "doc_html")
    add_dir(root / "doc" / "antora", "doc_antora")
    libs_dir = root / "libs"
    if libs_dir.is_dir():
        for entry in sorted(p for p in libs_dir.iterdir() if p.is_dir()):
            if entry.name in EXCLUDE_COMPONENTS - {"test", "tests"}:
                continue
            for fn in ("index.html", "index.htm"):
                if (entry / fn).is_file():
                    rules.append((f"libs/{entry.name}/{fn}", "libs_index"))
            add_dir(entry / "doc", "libs_doc")
    tools_dir = root / "tools"
    if tools_dir.is_dir():
        for entry in sorted(p for p in tools_dir.iterdir() if p.is_dir()):
            if entry.name in EXCLUDE_COMPONENTS - {"test", "tests"}:
                continue
            add_dir(entry / "doc", "tools_doc")

    seen = {}
    order = {"root_index": 0, "more": 1, "doc_html": 2, "doc_antora": 3,
             "libs_index": 4, "libs_doc": 5, "tools_doc": 6}
    for rel, rule in sorted(rules, key=lambda x: (order[x[1]], x[0])):
        if rel not in seen:
            seen[rel] = rule
    return [(rel, rule) for rel, rule in seen.items()]


def build_libname_sets(root: Path):
    libs = {p.name for p in (root / "libs").iterdir() if p.is_dir()}
    tools = {p.name for p in (root / "tools").iterdir() if p.is_dir()}
    return libs, tools


def attribute_lib(rel: str, rule: str, libs: set, tools: set) -> str:
    if rule in ("root_index", "more"):
        return "(root)"
    parts = rel.split("/")
    if rule == "doc_html":
        name = parts[2] if len(parts) > 2 else ""
        if name in libs or name in tools:
            return name
        if name.startswith("boost_"):
            stripped = name[len("boost_"):]
            if stripped in libs:
                return stripped
            return name
        return f"(book:{name})" if name else "(root)"
    if rule == "doc_antora":
        return parts[2] if len(parts) > 2 else "(antora)"
    if rule in ("libs_index", "libs_doc"):
        return parts[1]
    if rule == "tools_doc":
        return f"tool:{parts[1]}"
    return "(unknown)"


def classify_form(rel: str, rule: str, head: bytes) -> str:
    if rule == "doc_antora":
        return "antora"
    if RE_DOXYGEN.search(head):
        return "doxygen"
    if RE_ASCIIDOCTOR.search(head):
        return "docca_asciidoctor"
    if RE_BOOSTBOOK.search(head):
        return "quickbook_boostbook"
    if RE_ANTORA.search(head):
        return "antora_like"
    return "handwritten_html"


def hash_key(s: str) -> int:
    """段键哈希（去重用途，非安全用途；按门禁要求用 SHA-256 截断 8 字节）。"""
    return int.from_bytes(
        hashlib.sha256(s.encode("utf-8", "replace")).digest()[:8], "big")
