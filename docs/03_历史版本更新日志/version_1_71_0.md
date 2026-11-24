# Boost 1.71.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_71_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_71_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2019-08-19 15:31 GMT（原文日期行：August 19th, 2019 15:31 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Variant2（Variant 的现代重实现库）：`std::variant` 的 never-valueless（永不陷入无值状态）、强保证实现，作者 Peter Dimov。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Uuid（UUID 生成与解析库）——破坏性变更：MD5 命名式 UUID 生成被修正为在所有字节序系统上结果一致；定义 `BOOST_UUID_COMPAT_PRE_1_71_MD5` 可保持与 1.66 至 1.70 兼容的结果；不影响基于 SHA1 的默认命名式生成。
- Test（单元测试框架库）——破坏性变更：对使用极旧头文件的情形开始显示弃用警告，相关头文件将在未来版本移除。新特性：`BOOST_TEST` 可用于比较抽象类型。
- Core（核心工具集）——弃用：`<boost/detail/sp_typeinfo.hpp>` 标记弃用并将在未来版本移除，应改用 `<boost/core/typeinfo.hpp>`。
- Endian（字节序处理库）——弃用：已弃用的旧名称移入弃用专用头文件 `endian.hpp`；新增 `endian_load`/`endian_store` 与 `float`/`double` 支持。
- Log（日志库）——默认行为变更：sink 后端对尾部换行的处理收紧，仅在格式化消息尚未以换行结尾时才追加换行（此前版本无条件追加）；新增 `auto_newline` 格式化器与流操纵器，sink 构造支持任意函数对象作 filter/format 参数（可直接传 C++11 lambda）。
- Container（扩展容器库）——`deque`、`static_vector`、`small_vector` 现可通过 `deque_options`、`static_vector_options`、`small_vector_options` 配置块大小、对齐、增长因子与异常行为。
- Parameter——支持完美转发（可检测 `BOOST_PARAMETER_HAS_PERFECT_FORWARDING`）：启用的函数与构造函数不再受 `BOOST_PARAMETER_MAX_ARITY` 限制；新增参数类别限定符 forward/consume/move_from 与一批代码生成宏。
- Asio（网络与底层 I/O 库）——使用 clang 时协程 TS 支持要求 C++17 或更高。
- SmartPtr（智能指针库）——`weak_ptr` 新增别名构造函数、`weak_ptr<T>::empty()`，新增 `enable_shared_from`/`shared_from`/`weak_from`。

另有 36 项常规缺陷修复与改进（Align、Any、Beast、CircularBuffer、Core、DynamicBitset、Fiber、Filesystem、Flyweight、Histogram、IoStreams、Interprocess、Intrusive、LexicalCast、Math、Metaparse、Move、MultiIndex、Outcome、PolyCollection、Stacktrace、Variant、YAP 等库），见英文原文存档。
