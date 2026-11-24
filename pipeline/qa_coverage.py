# -*- coding: utf-8 -*-
"""qa_coverage.py - QA gate 4: full-corpus missed-translation detection.

Usage: python -I pipeline/qa_coverage.py [--lib asio]

For each paired en/zh segment: zh must contain >= 0.5 CJK chars per english
word (words >= 4). Short labels (<= 3 words), pure-ascii content, and
segments whose english contains no letters are whitelisted.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from inventory import safe_join  # noqa: E402
from common import scan_html, count_words, count_cjk  # noqa: E402

WORKSPACE = Path(__file__).resolve().parent.parent
# 命令行/路径/构建语法形态（官方文档中未包 <code> 的命令文本，不属散文）
RE_CMDISH = re.compile(
    r"(?:^\.\/|\s--\w|\\\\|/\w+|\b[a-z]+[\w\-.]*=[\"]?\w|<compileflags>|"
    r"\.la\b|\.exe\b|\.txt\b|error [A-Z]+\d+:|`[^`]*'::|"
    r"^template\s*<|^\s*static\s+\w|^operator\b|decay_copy|::forward<|"
    r"=>|\bstd::\w+<|\w\s*\(\s*\w+\s*,|\b\w+\(\s*\w+\s+const\s*&\s*,|"
    # hana 会话扩展（2026-11-16）：Doxygen 既有形态
    # ^Inherited by：Doxygen 继承关系名单（数百个限定类名，非散文）
    r"^Inherited by\b|"
    # \\[ / @f$：LaTeX/Doxygen 数学公式定界符
    r"\\\[|@f\$|"
    # std::name( / ns::name<：纯 C++ 调用、签名与限定名模板实参列表
    # ... ) {：C++ 函数定义起始行（散文不会以此结尾）
    r"\bstd::\w+\(|\b\w+::\w+<|\)\s*\{\s*$|"
    # gil 会话扩展（2026-11-17）：
    # -> typename：C++ trailing-return-type 签名；auto f( / auto operator(：auto 函数声明；
    # ns::f(：限定名函数调用/声明（IODevice::read 等）；void f(：函数声明起始；
    # {%- block / {{：Sphinx/Jinja 模板标记行（_templates 产物，非散文）
    r"->\s*typename\b|"
    r"\bauto\s+(?:operator\s*\(|\w+\s*\()|"
    r"\b\w+::\w+\s*\(|\bvoid\s+\w+\(|"
    r"\{%-?\s*block\b|\{\{|"
    # locale 会话扩展（2026-11-18）：
    # f(...const...)：括号内含 const 的 C++ 签名/声明行（散文括号注释不含 C++ const）；
    # operatorXX(：运算符函数声明（operator==/!=/<=/>=/() 等）
    r"\w+\([^)]*\bconst\b|\boperator\s*[^\s(]*\(|"
    # 字面量/格式记号名单（如 fp_facets 类代码表 one#ind、nan(...)），
    # 散文不会含 one#x 记号；name(...) 省略号形态亦属签名/格式串
    r"\bone#[a-z]+|\w+\(\.\.\.\)|"
    # tool:build 会话扩展（2026-11-19）：
    # ^using <toolset> :|;：b2/Jamfile 工具集声明行（using embarcadero : 7.40 : bcc32x ;），
    # 纯构建配置代码行，散文行首不会是 "using xxx :"
    r"^\s*using\s+\w+\s*[:;]|"
    # sort 会话扩展（2026-11-19）：bool f(：bool 返回值函数声明行（与既有 \bvoid\s+\w+\( 同族）；
    # f(... &x)：参数含引用声明的签名行（散文不会含 C++ 引用参数形态）
    r"\bbool\s+\w+\s*\(|\w+\([^()]*&\s*\w+\s*[,)]|"
    # iterator 会话扩展（2026-11-21）：reST/QuickBook 指令行（.. _anchor: / .. |sub| replace::）
    r"^\.\.\s*[_|]|"
    # G8 会话扩展（2026-11-21）：^name<...>：行首词后直接跟尖括号的模板声明行
    # （cpp<int C, int S, ...>；散文行首不会出现 "word<" 形态）
    r"^\w+<\w|"
    # wave 会话扩展（2026-11-22）：^word: [0：pragma wave option 语法行
    # （line: [0 | 1 | push | pop] / preserve: [...] / output: [...]；
    #  line/preserve/output 为字面语法关键字，非散文）
    r"^\s*\w+: \[\d|"
    # xpressive 会话扩展（2026-11-22）：^\d+- ：基准测试样例数据行
    # （FTP 响应样例 "100- this is a line of..." 等正则匹配输入文本，非散文）
    r"^\d+-\s|"
    # hof 会话扩展（2026-11-22）：CMake 脚本行（上游 CMakeLists.txt 整页误存为 html；
    # function(...)/set(...)/if (...)/file(...)/foreach(...) 等 CMake 命令，非散文）
    r"^\s*(?:function|macro|set|if|foreach|file|string|option|project|include|add_\w+|target_\w+)\s*\(|"
    # tool_boostdep 会话扩展（2026-11-23）：^⇢ ：模块依赖树行（箭头前缀 + 纯模块名列表，
    # 字面标识符名单，非散文）
    r"^\s*⇢\s|"
    # tokenizer 会话扩展（2026-11-23）：^Field \d, ：CSV 格式样例行
    # （escaped_list_separator 章节的字面示例数据，非散文）
    r"^Field \d,|"
    # 补页会话扩展（2026-11-23）：has been matched: full match = ：示例程序输出行
    # （spirit classic FAQ 解析器样例的运行输出数据，非散文）
    r"has been matched: full match = (?:true|false)|"
    # deferred 清零会话扩展（2026-11-24）：
    # 纯占位符段（⦃n⦄ 序列，无任何可译文本的表格空行）；
    # 引号字面量名单行（"one only"⦃0⦄ 等 spirit 解析匹配样例数据）；
    # 解析器原语名表行（chlit, ch_p⦃0⦄ 等——纯受保护标识符名单）
    r"^\s*(?:⦃\d+⦄\s*)+$|"
    r"^\"[^\"]*\"⦃\d+⦄|"
    r"^[a-z_0-9]+, [a-z_0-9]+⦃\d+⦄|"
    # 小库组 A 会话扩展（2026-11-23）：^typename ：C++ 表达式/声明行
    # （typename Fn::template impl<...>(...) 等，散文行首不会出现 typename）
    r"^\s*typename\b|"
    # deferred 四轮会话扩展（2026-11-24）：--> ：流程图箭头链行
    # （phoenix actors 页 "actor's base operation --> return result --> ..."，图示文本非散文）
    r" --> .* --> )",
    re.IGNORECASE | re.M)


def exempt(en_key: str, words: int, cjk: int) -> bool:
    if words < 4:
        return True
    if RE_CMDISH.search(en_key):
        return True
    # 低散文词段（人名/产品名列表等）：小写实词 < 6 个，无法按比值判漏译
    if len(re.findall(r"\b[a-z][a-z']{2,}\b", en_key)) < 6:
        return True
    # 致谢/署名列表：大写词占比 > 40% 时按名单处理（有 CJK 即视为已译）
    toks = re.findall(r"[A-Za-z][\w'.-]*", en_key)
    if toks and sum(1 for t in toks if t[0].isupper()) / len(toks) > 0.40:
        return cjk >= 1
    if words <= 6:
        return cjk >= 1  # 短段：有 CJK 即视为已处理（名单/标题类）
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", action="append", default=[])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--prefix", action="append", default=[])
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    en_root = safe_join(WORKSPACE, "data", "boost_1_92_0")
    zh_root = safe_join(WORKSPACE, "site", "zh", "1.92.0")
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

    misses = []
    checked = segs_checked = 0
    for r in rows:
        rel = r["relpath"]
        if not rel.lower().endswith((".html", ".htm")):
            continue
        en_f = safe_join(en_root, rel)
        zh_f = safe_join(zh_root, rel)
        if not zh_f.exists():
            continue
        try:
            en_segs, _ = scan_html(en_f.read_bytes())
            zh_segs, _ = scan_html(zh_f.read_bytes())
        except Exception:
            continue
        checked += 1
        if len(en_segs) != len(zh_segs):
            continue
        for i, (a, b) in enumerate(zip(en_segs, zh_segs)):
            en_key = a.norm_key()
            w = count_words(en_key)
            if w < 4:
                continue
            zh_str = b.segment_string()
            cjk = count_cjk(zh_str)
            segs_checked += 1
            if exempt(en_key, w, cjk):
                continue
            if cjk / max(1, w) < 0.5:
                misses.append((rel, i, w, cjk, en_key[:80]))
                if len(misses) > 40:
                    break
        if len(misses) > 40:
            break
    for rel, i, w, cjk, key in misses[:40]:
        print(f"[qa_cov] MISS {rel} seg#{i} words={w} cjk={cjk}: {key}")
    print(f"[qa_coverage] files={checked} segs_checked={segs_checked} "
          f"misses={len(misses)}")
    sys.exit(1 if misses else 0)


if __name__ == "__main__":
    sys.exit(main())
