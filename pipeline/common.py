# -*- coding: utf-8 -*-
"""common.py — 流水线共用核心（纯 stdlib）。

设计要点（总纲 §5 / C2/R2/R3）：
- 解析基于字节串 latin-1 视图（1 字符 == 1 字节），html.parser 的 getpos 行列
  因此可直接换算为**原始字节偏移**，供 reemit_html.py 做字节切片替换。
- 文本节点以"原始字节区间 [start,end)"记录：区间内含实体原文（如 &amp;），
  替换时整体换为译文（最小转义 & < > 后按 UTF-8 编码），其余字节不动。
- 一个"段"（Segment）= 一个块级元素的**直接文本**（叶子块）；
  段内穿插的不可译结构（code/samp/kbd 内容、br/hr/img、注释、pre 块）
  以 ⦃n⦄ 标记占位，可译内联标签（b/i/a/span…）以 ⟦tag⟧ / ⟦/tag⟧ 标记占位
  ——这些字节均不动，仅文本节点字节区间被译文替换。
- 未闭合块级标签（老手写 HTML 常见）经"隐式闭合"规则处理，保证段完整产出。
- 段串回填（reemission）映射不变式：
  段串按 token（⦃n⦄ 与 ⟦⟧）切分后的 gap 数 == 文本节点数 + 1，
  逐项走查（text 认领 gap，token 消耗 token），未被认领的 gap 译文必须为空白。
"""
from __future__ import annotations

import html
import re
from html.parser import HTMLParser

# ---------------------------------------------------------------- 常量表

# 内容完全跳过（不译、字节不动）的元素（含其子孙）
SKIP_TAGS = {"script", "style", "template", "svg", "math"}
# 内联不可译元素：内容在段串中以 ⦃n⦄ 占位、字节原样保留
CODE_INLINE_TAGS = {"code", "samp", "kbd"}
# 整块跳过的块级元素（如 <pre>）：内容不译，在父段占一个 ⦃n⦄ 位
PRE_BLOCK_TAGS = {"pre", "listing", "xmp", "plaintext"}
# 空内联元素：段串中以 ⦃n⦄ 占位、无内文字节
VOID_INLINE_TAGS = {"br", "hr", "img", "input", "wbr", "area", "embed"}
# 块级元素（作为段边界/段本体）
BLOCK_TAGS = {
    "p", "div", "td", "th", "li", "dt", "dd", "caption", "figcaption",
    "blockquote", "title", "h1", "h2", "h3", "h4", "h5", "h6",
    "body", "section", "article", "aside", "header", "footer", "nav",
    "table", "tr", "ul", "ol", "dl", "form", "fieldset", "figure", "main",
    "center", "address", "summary", "details",
}
# 隐式闭合：开始标签 T 出现时，若栈顶开块的标签 O 满足 T ∈ CLOSERS[O]，O 先闭合
_HEADINGS = {f"h{i}" for i in range(1, 7)}
CLOSERS: dict[str, set] = {
    "p": BLOCK_TAGS,                       # 任何块级开始都终结未闭合的 p
    "li": {"li"},
    "dt": {"dt", "dd"}, "dd": {"dt", "dd"},
    "td": {"td", "th", "tr"}, "th": {"td", "th", "tr"},
    "tr": {"tr"},
    "thead": {"thead", "tbody", "tfoot", "tr"},
    "tbody": {"thead", "tbody", "tfoot", "tr"},
    "tfoot": {"thead", "tbody", "tfoot", "tr"},
    "option": {"option", "optgroup"},
}
for _h in _HEADINGS:
    CLOSERS[_h] = _HEADINGS

# 须原样保留原文位置的可翻译属性（总纲 §4.3 白名单）
TRANSLATABLE_ATTRS = {"alt", "title"}

# 段串标记
MARK_OPEN, MARK_CLOSE = "\u2983", "\u2984"   # ⦃ ⦄（不可译/结构占位）
ITAG_OPEN, ITAG_CLOSE = "\u27e6", "\u27e7"   # ⟦ ⟧（可译内联标签）
TOKEN_RE = re.compile(
    f"{MARK_OPEN}\\d+{MARK_CLOSE}|{ITAG_OPEN}/?[-a-zA-Z0-9_,]+{ITAG_CLOSE}")

_WS_RE = re.compile(r"\s+")
_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'+._\-]*")


def normalize_text(s: str) -> str:
    """TM 键规范化：空白折叠、去首尾空白（实体已在抽取时统一 unescape）。"""
    return _WS_RE.sub(" ", s).strip()


def count_words(s: str) -> int:
    """英文词数：含至少一个 ASCII 字母的空白分隔 token。"""
    n = 0
    for tok in s.split():
        if _WORD_RE.search(tok):
            n += 1
    return n


def count_cjk(s: str) -> int:
    return sum(1 for ch in s
               if "\u4e00" <= ch <= "\u9fff" or "\u3400" <= ch <= "\u4dbf"
               or "\U00020000" <= ch <= "\U0002ebef")


def line_start_table(s: str) -> list[int]:
    starts = [0]
    pos = s.find("\n")
    while pos != -1:
        starts.append(pos + 1)
        pos = s.find("\n", pos + 1)
    return starts


def escape_min(s: str) -> str:
    """回写文本的最小 HTML 转义。"""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def filter_attrs_inside_code(attr_segs: list, segments: list) -> list:
    """剔除落在 code/skip 区间内的属性段（总纲：代码块不译优先于属性白名单）。

    attr_segs 元素为 (name, span, text, tag)（span 模式）或 (name, text, tag)
    （无 span 模式，此时无法判定，保留）。
    """
    spans = []
    for seg in segments:
        for it in seg.items:
            if it.kind == "code" and it.span:
                spans.append(it.span)
    if not spans:
        return attr_segs
    out = []
    for a in attr_segs:
        span = a[1]
        if isinstance(span, tuple) and len(span) == 2:
            if any(s0 <= span[0] and span[1] <= e0 for s0, e0 in spans):
                continue
        out.append(a)
    return out


_PUNCT_MAP = str.maketrans({
    "\uff0c": ", ", "\u3002": ". ", "\uff1a": ": ", "\uff1b": "; ",
    "\uff08": " (", "\uff09": ") ", "\uff01": "! ", "\uff1f": "? ",
})


def punct_halfwidth(s: str) -> str:
    """语体规范化：CJK 全角标点 → 半角（总纲 §5 语体规则）。

    仅映射全角标点字符本身，不影响 URL/标识符/代码；顿号、引号保留。
    """
    out = s.translate(_PUNCT_MAP)
    out = re.sub(r" +", " ", out)
    return out.strip()


# ---------------------------------------------------------------- 段的数据结构

class Item:
    """段内有序项。kind:
      text  — 可译文本节点（span=原始字节区间，text=unescape 后文本）
      code  — 不可译内联元素内容（span=内容字节区间，字节不动）
      void  — 空内联元素（br/hr/img…，span=None）
      gap   — 不可见结构间隔（注释/声明/pre/skip 块，span=None）
      iopen / iclose — 可译内联标签起止（tag=标签名，字节不动）
    """

    __slots__ = ("kind", "span", "text", "tag")

    def __init__(self, kind: str, span=None, text: str = "", tag: str = ""):
        self.kind = kind
        self.span = span
        self.text = text
        self.tag = tag


class Segment:
    """一个翻译段 = 一个块级元素的直接文本。"""

    __slots__ = ("tag", "items", "meta")

    def __init__(self, tag: str, items: list, meta: dict | None = None):
        self.tag = tag
        self.items = items
        self.meta = meta or {}

    # ---- 段串（含标记，供翻译）----
    def segment_string(self) -> str:
        out = []
        marker = 0
        for it in self.items:
            if it.kind == "text":
                out.append(it.text)
            elif it.kind in ("code", "void", "gap"):
                out.append(f"{MARK_OPEN}{marker}{MARK_CLOSE}")
                marker += 1
            elif it.kind == "iopen":
                out.append(f"{ITAG_OPEN}{it.tag}{ITAG_CLOSE}")
            elif it.kind == "iclose":
                out.append(f"{ITAG_OPEN}/{it.tag}{ITAG_CLOSE}")
        return _WS_RE.sub(" ", "".join(out)).strip()

    # ---- 规范化键（TM / 公共段判定；含标记：同文本不同布局视为不同键）----
    def norm_key(self) -> str:
        return normalize_text(self.segment_string())

    def word_count(self) -> int:
        return sum(count_words(it.text) for it in self.items
                   if it.kind == "text")

    def text_spans(self) -> list:
        return [it.span for it in self.items if it.kind == "text"]

    def token_signature(self) -> list:
        """期望 token 序列（结构校验用）。"""
        sig = []
        marker = 0
        for it in self.items:
            if it.kind in ("code", "void", "gap"):
                sig.append(("mark", marker))
                marker += 1
            elif it.kind == "iopen":
                sig.append(("open", it.tag))
            elif it.kind == "iclose":
                sig.append(("close", it.tag))
        return sig

    def first_span(self):
        for it in self.items:
            if it.kind == "text":
                return it.span[0]
        return None


def parse_segment_string(seg: Segment, translated: str):
    """把译文段串解析回 (文本片段列表, 错误信息)。

    校验：token 序列与原段一致；逐项走查映射 gap→text；
    未被任何 text 认领的 gap 其译文必须为空白。
    返回 (list[str] 与 Segment.text_spans() 等长, None) 或 (None, 原因)。
    """
    tokens = list(TOKEN_RE.finditer(translated))
    sig = seg.token_signature()
    if len(tokens) != len(sig):
        return None, f"token 数不符: 译 {len(tokens)} vs 原 {len(sig)}"
    for m, (kind, val) in zip(tokens, sig):
        s = m.group(0)
        if kind == "mark":
            if not (s.startswith(MARK_OPEN) and s.endswith(MARK_CLOSE)
                    and s[1:-1].isdigit()):
                return None, f"期望 \u2983{val}\u2984 处实得 {s!r}"
            if int(s[1:-1]) != val:
                return None, f"\u2983n\u2984 编号错位: {s!r} vs {val}"
        elif kind == "open":
            if s != f"{ITAG_OPEN}{val}{ITAG_CLOSE}":
                return None, f"开标记缺失/错位: 期望 {val} 实得 {s!r}"
        elif kind == "close":
            if s != f"{ITAG_OPEN}/{val}{ITAG_CLOSE}":
                return None, f"闭标记缺失/错位: 期望 /{val} 实得 {s!r}"
    n = len(tokens)
    claimed: list[int] = []
    next_gap = 0
    tokens_seen = 0
    for it in seg.items:
        if it.kind == "text":
            g = max(tokens_seen, next_gap)
            if g > n:
                return None, "gap 下标越界（译文 token 缺失）"
            claimed.append(g)
            next_gap = g + 1
        else:
            tokens_seen += 1

    def gap_range(gi: int):
        start = tokens[gi - 1].end() if gi > 0 else 0
        end = tokens[gi].start() if gi < n else len(translated)
        return start, end

    pieces = [translated[gap_range(g)[0]:gap_range(g)[1]] for g in claimed]
    claimed_set = set(claimed)
    for gi in range(n + 1):
        if gi not in claimed_set:
            s, e = gap_range(gi)
            if translated[s:e].strip():
                return None, f"gap {gi} 应为空但含译文: {translated[s:e]!r}"
    return pieces, None


# ---------------------------------------------------------------- 扫描器

class _BFrame:
    __slots__ = ("tag", "items")

    def __init__(self, tag):
        self.tag = tag
        self.items: list[Item] = []


class HTMLBlockScanner(HTMLParser):
    """解析 HTML 字节串 → (Segment 列表, 属性段列表)。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.view = ""            # latin-1 视图（1 char == 1 byte）
        self.line_starts = [0]
        self.segments: list[Segment] = []
        self.attr_segments: list[tuple] = []
        self._stack: list[_BFrame] = []
        self._skip_depth = 0
        self._pending_text = None     # 待定文本节点起点
        self._code_open = False
        self._code_start = -1
        self._code_frame = None
        self._title_done = False
        self.title_text = ""

    # ---- 偏移 ----
    def _off(self) -> int:
        line, col = self.getpos()
        return self.line_starts[line - 1] + col

    def _decode_slice(self, start: int, end: int) -> str:
        chunk = self.view[start:end]
        try:
            chunk = chunk.encode("latin-1").decode("utf-8")
        except UnicodeDecodeError:
            pass  # 非 UTF-8 文件：上层记录编码并另行转码
        return html.unescape(chunk)

    def _flush_text(self):
        if self._pending_text is None:
            return
        start = self._pending_text
        self._pending_text = None
        end = self._off()
        if start is None or start >= end:
            return
        text = self._decode_slice(start, end)
        if not text:
            return
        if self._stack and self._skip_depth == 0:
            self._stack[-1].items.append(Item("text", (start, end), text))

    def _mark(self, kind):
        """插入占位项；仅在会打断相邻文本时插入（去重：前一项须为 text）。"""
        if self._skip_depth != 0 or not self._stack:
            return
        items = self._stack[-1].items
        if items and items[-1].kind == "text":
            items.append(Item(kind))

    # ---- 事件 ----
    def handle_starttag(self, tag, attrs):
        self._flush_text()
        self._collect_attrs(tag, attrs)
        if tag in SKIP_TAGS or tag in PRE_BLOCK_TAGS:
            self._mark("gap")
            self._skip_depth += 1
            return
        if tag in CODE_INLINE_TAGS:
            if self._skip_depth == 0 and self._stack:
                self._code_open = True
                self._code_start = -1
                self._code_frame = self._stack[-1]
            else:
                self._skip_depth += 1 if self._skip_depth else 0
            return
        if tag in VOID_INLINE_TAGS:
            self._mark("void")
            return
        if tag in BLOCK_TAGS:
            # 隐式闭合：栈顶开块会被本标签终结时先闭合
            while self._stack and tag in CLOSERS.get(self._stack[-1].tag, ()):
                self._close_block()
            if self._stack:
                self._mark("gap")     # 子块边界：打断父块相邻文本
            self._stack.append(_BFrame(tag))
            return
        # 其余（可译内联/未知标签）：记录 iopen 占位
        if self._skip_depth == 0 and self._stack:
            self._stack[-1].items.append(Item("iopen", tag=tag))
        return

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag in BLOCK_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        self._flush_text()
        if tag in SKIP_TAGS or tag in PRE_BLOCK_TAGS:
            if self._skip_depth > 0:
                self._skip_depth -= 1
            self._mark("gap")
            return
        if tag in CODE_INLINE_TAGS:
            if self._skip_depth > 0:
                self._skip_depth -= 1
            elif self._code_open:
                off = self._off()
                if self._code_start >= 0 and self._code_start < off:
                    text = self._decode_slice(self._code_start, off)
                    self._code_frame.items.append(
                        Item("code", (self._code_start, off), text))
                else:
                    self._mark("void")
                self._code_open = False
                self._code_frame = None
            else:
                self._mark("void")  # 孤立 </code>：同样打断文本流
            return
        if tag in VOID_INLINE_TAGS:
            return
        if tag in BLOCK_TAGS:
            for i in range(len(self._stack) - 1, -1, -1):
                if self._stack[i].tag == tag:
                    while len(self._stack) > i:
                        self._close_block()
                    return
            # 孤立结束标签：仍会打断文本节点流，须占位防相邻 text 项
            self._mark("gap")
            return
        # 内联/未知标签：记录 iclose 占位
        if self._skip_depth == 0 and self._stack:
            self._stack[-1].items.append(Item("iclose", tag=tag))
        return

    def handle_data(self, data):
        start = self._off()
        if self._skip_depth > 0:
            self._pending_text = None
            return
        if self._code_open:
            if self._code_start < 0:
                self._code_start = start
            self._pending_text = None
            return
        if not data:
            return
        if self._pending_text is None:
            self._pending_text = start

    def handle_comment(self, data):
        self._flush_text()
        self._mark("gap")

    def handle_decl(self, decl):
        self._flush_text()
        self._mark("gap")

    def handle_pi(self, data):
        self._flush_text()
        self._mark("gap")

    def unknown_decl(self, data):
        self._flush_text()
        self._mark("gap")

    def close(self):
        super().close()
        self._flush_text()
        while self._stack:
            self._close_block()

    # ---- 块闭合与产出 ----
    def _close_block(self):
        if not self._stack:
            return
        frame = self._stack.pop()
        items = frame.items
        if any(it.kind == "text" and it.text.strip() for it in items):
            if frame.tag == "title" and not self._title_done:
                self.title_text = normalize_text("".join(
                    it.text for it in items if it.kind == "text"))
                self._title_done = True
            self.segments.append(Segment(frame.tag, items))

    # ---- 属性段 ----
    def _collect_attrs(self, tag, attrs):
        low = [(k.lower(), v) for k, v in attrs]
        wanted = set(TRANSLATABLE_ATTRS)
        adict = dict(low)
        if tag == "meta" and adict.get("name", "").lower() == "description":
            wanted.add("content")
        for k, v in low:
            if k in wanted and v and v.strip():
                self.attr_segments.append((k, v, tag))


def _extract_attr_spans(view: str, tag_start: int, wanted):
    """在原始标签字节区间内定位属性值字节区间。

    wanted: {attr_name_lower, ...}；返回 [(attr, (vstart, vend), value_text)]。
    """
    if tag_start >= len(view) or view[tag_start] != "<":
        return []
    i = tag_start + 1
    n = len(view)
    quote = None
    while i < n:
        c = view[i]
        if quote:
            if c == quote:
                quote = None
        elif c in "\"'":
            quote = c
        elif c == ">":
            break
        i += 1
    if i >= n:
        return []
    tag_text = view[tag_start:i]
    results = []
    for m in re.finditer(
            r"([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*(\"([^\"]*)\"|'([^']*)'|([^\s\">]+))",
            tag_text):
        name = m.group(1).lower()
        if name not in wanted:
            continue
        gi = 3 if m.group(3) is not None else (4 if m.group(4) is not None else 5)
        raw = m.group(gi)
        vstart = tag_start + m.start(gi)
        vend = vstart + len(raw)
        try:
            text = html.unescape(raw.encode("latin-1").decode("utf-8"))
        except UnicodeDecodeError:
            text = html.unescape(raw)
        results.append((name, (vstart, vend), text))
    return results


def scan_html(raw: bytes, with_attr_spans: bool = False):
    """扫描 HTML 字节串。

    返回 (segments: list[Segment], attr_segs: list)。
    with_attr_spans=True 时 attr_segs 为 [(name, (vstart, vend), text, tag)]；
    否则为 [(name, value_text, tag)]（不定位字节区间，成本低）。
    """
    scanner = HTMLBlockScanner()
    scanner.view = raw.decode("latin-1")
    scanner.line_starts = line_start_table(scanner.view)
    if with_attr_spans:
        def collect(tag, attrs, _self=scanner):
            low = [(k.lower(), v) for k, v in attrs]
            adict = dict(low)
            wanted = set(TRANSLATABLE_ATTRS)
            if tag == "meta" and adict.get("name", "").lower() == "description":
                wanted.add("content")
            if not any(k in wanted for k, _ in low):
                return
            line, col = _self.getpos()
            ts = _self.line_starts[line - 1] + col
            for name, span, text in _extract_attr_spans(_self.view, ts, wanted):
                _self.attr_segments.append((name, span, text, tag))
        scanner._collect_attrs = collect
    scanner.feed(scanner.view)
    scanner.close()
    return scanner.segments, scanner.attr_segments


# ---------------------------------------------------------------- 编码探测

_BOMS = ((b"\xef\xbb\xbf", "utf-8-sig"), (b"\xff\xfe", "utf-16-le"),
         (b"\xfe\xff", "utf-16-be"))


def detect_encoding(raw: bytes) -> tuple[str, str]:
    """返回 (encoding_state, declared_charset)。

    encoding_state: utf-8 / utf-8-sig / nonutf8:<declared|unknown>
    """
    for bom, enc in _BOMS:
        if raw.startswith(bom):
            if enc == "utf-8-sig":
                return "utf-8-sig", "utf-8"
            return f"nonutf8:{enc}", enc
    m = re.search(rb"""charset\s*=\s*["']?\s*([a-zA-Z0-9_\-]+)""", raw[:4096],
                  re.IGNORECASE)
    declared = m.group(1).decode("ascii", "replace").lower() if m else ""
    try:
        raw.decode("utf-8")
        return ("utf-8", declared or "utf-8")
    except UnicodeDecodeError:
        return (f"nonutf8:{declared or 'unknown'}", declared or "unknown")
