# -*- coding: utf-8 -*-
"""test_common.py — 扫描器与段串回填映射的自检（运行: python -I pipeline/test_common.py）"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent))
from common import (HTMLBlockScanner, scan_html, parse_segment_string,
                    Segment, Item, escape_min)

CASES = []


def case(name, html_text, expect_segs=None):
    CASES.append((name, html_text, expect_segs or []))


case("plain paragraph",
     "<html><head><title>T1</title></head><body><p>Hello boost world.</p></body></html>",
     [("p", "Hello boost world.")])

case("inline tags merged",
     "<p>See <b>foo</b> and <i>bar</i> now.</p>",
     [("p", "See \u27e6b\u27e7foo\u27e6/b\u27e7 and \u27e6i\u27e7bar\u27e6/i\u27e7 now.")])

case("code inline marker",
     "<p>Call <code>boost::foo()</code> twice.</p>",
     [("p", "Call \u29830\u2984 twice.")])

case("unclosed p implied close",
     "<p>first para<p>second para</p>",
     [("p", "first para"), ("p", "second para")])

case("unclosed p inside div",
     "<div><p>inner text</div><p>after</p>",
     [("p", "inner text"), ("p", "after")])

case("pre skipped with gap",
     "<p>before</p><pre>raw code here</pre><p>after</p>",
     [("p", "before"), ("p", "after")])

case("pre inside div gap",
     "<div>text1<pre>x=1</pre>text2</div>",
     [("div", "text1\u29830\u2984text2")])

case("void br marker",
     "<p>line1<br/>line2</p>",
     [("p", "line1\u29830\u2984line2")])

case("skip script/style",
     "<style>.x{color:red}</style><p>ok text</p><script>var a=1;</script>",
     [("p", "ok text")])

case("nested blocks div>p",
     "<div class=\"s\">stray <p>in p</p> tail</div>",
     [("p", "in p"), ("div", "stray \u29830\u2984 tail")])

case("entities decoded",
     "<p>A &amp; B &lt;tag&gt; &quot;q&quot;</p>",
     [("p", "A & B <tag> \"q\"")])

case("li auto close",
     "<ul><li>one<li>two</li></ul>",
     [("li", "one"), ("li", "two")])

case("table td th",
     "<table><tr><td>c1</td><td>c2</td></tr></table>",
     [("td", "c1"), ("td", "c2")])

case("comment gap",
     "<p>text1<!-- hidden -->text2</p>",
     [("p", "text1\u29830\u2984text2")])

case("nested inline",
     "<p><b>bold <i>both</i></b> end</p>",
     [("p", "\u27e6b\u27e7bold \u27e6i\u27e7both\u27e6/i\u27e7\u27e6/b\u27e7 end")])

case("title captured",
     "<html><head><title>The Boost C++ &amp; More</title></head><body></body></html>",
     [])


def run():
    fails = 0
    for name, html_text, expect in CASES:
        segs, attrs = scan_html(html_text.encode("utf-8"))
        # title 段单独经 title_text 断言，对比时排除
        got = [(s.tag, s.segment_string()) for s in segs if s.tag != "title"]
        ok = True
        if name == "title captured":
            sc = HTMLBlockScanner()
            sc.view = html_text
            from common import line_start_table
            sc.line_starts = line_start_table(sc.view)
            sc.feed(sc.view)
            sc.close()
            ok = sc.title_text == "The Boost C++ & More"
            print(("PASS" if ok else "FAIL"), name, "->", repr(sc.title_text))
            if not ok:
                fails += 1
            continue
        expect_filtered = expect
        ok = got == expect_filtered
        print(("PASS" if ok else "FAIL"), name)
        if not ok:
            fails += 1
            print("  expect:", expect_filtered)
            print("  got   :", got)

    # ---- 回填映射自检 ----
    seg = Segment("p", [
        Item("text", (0, 4), "See "),
        Item("iopen", tag="b"),
        Item("text", (8, 11), "foo"),
        Item("iclose", tag="b"),
        Item("text", (12, 17), " and "),
        Item("code", (23, 37), "boost::foo()"),
        Item("text", (38, 44), " twice"),
        Item("gap"),
        Item("text", (46, 47), "."),
    ])
    seg_str = seg.segment_string()
    # 模拟译文
    tr = seg_str.replace("See ", "参见 ").replace("foo", "富").replace(
        " and ", " 和 ").replace(" twice", " 两次").replace(".", "。")
    pieces, err = parse_segment_string(seg, tr)
    ok = err is None and len(pieces) == 5
    print(("PASS" if ok else "FAIL"), "reemit mapping", "->", pieces, err)
    if not ok:
        fails += 1

    # 坏译文：token 丢失
    bad = seg_str.replace("\u29830\u2984", "").replace("See ", "参见 ")
    pieces, err = parse_segment_string(seg, bad)
    ok = err is not None
    print(("PASS" if ok else "FAIL"), "reemit rejects broken tokens")
    if not ok:
        fails += 1

    # 属性段定位自检
    html_doc = b"<img src=\"a.png\" alt=\"Arrow diagram\" title=\"tip\">\n<meta name=\"description\" content=\"Boost page desc\">"
    segs, asegs = scan_html(html_doc, with_attr_spans=True)
    names = [(a[0], a[2], a[3]) for a in asegs]
    ok = names == [("alt", "Arrow diagram", "img"), ("title", "tip", "img"),
                   ("content", "Boost page desc", "meta")]
    print(("PASS" if ok else "FAIL"), "attr segments", names)
    if not ok:
        fails += 1
    # 字节区间验证
    doc = html_doc.decode("latin-1")
    for a in asegs:
        s, e = a[1]
        ok2 = doc[s:e] == a[2]
        if not ok2:
            print("  span mismatch:", repr(doc[s:e]), repr(a[2]))
            fails += 1

    print("====", "ALL PASS" if fails == 0 else f"{fails} FAILURES")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(run())
