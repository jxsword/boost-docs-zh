# Boost 1.75.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_75_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_75_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2020-12-11 19:50 GMT（原文日期行：December 11th, 2020 19:50 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.75.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 已知问题（Known Issues）

Boost.Operators（运算符定义库）目前与 C++20 编译器**不兼容**，某些情况下在调用比较运算符时可能表现为运行期的无限递归或无限循环。该问题由 C++20 引入的新运算符改写（operator rewriting）行为引起。作为变通方案，建议用户以 C++17 或更早的 C++ 标准为目标。更多细节见 [\#65](https://github.com/boostorg/utility/issues/65)。

## 新增库（New Libraries）

- [JSON](/libs/json/)（JSON 解析与序列化库）：C++11 实现的 JSON 解析、序列化与 DOM，由 Vinnie Falco 与 Krystian Stasiowski 开发。

  - 编译快速，仅需 C++11

  - 简单安全的现代 API，支持分配器

  - 可脱离 Boost 编译，定义 `BOOST_JSON_STANDALONE` 即可

  - 可选仅头文件库模式，无需链接库

- [LEAF](/libs/leaf/)（轻量级错误处理库）：面向 C++11 的轻量级错误处理库，由 Emil Dotchevski 开发。

  - 小巧的单头文件形式，无依赖。

  - 为最大效率设计（"正常"（happy）路径与"出错"（sad）路径）。

  - 即使携带大型负载也不进行动态内存分配。

  - 任意错误类型的 O(1) 传递（与调用栈深度无关）。

  - 可在启用或不启用异常处理的情况下使用。

- [PFR](/libs/pfr/)（无宏结构体反射库）：面向用户自定义类型、无需宏或样板代码的基础反射，由 Antony Polukhin 开发。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 启用 Windows 上对 UNIX 域套接字的支持。

  - 为 `ip::basic_resolver` 新增可转换执行器（executor）的构造与赋值。

  - 新增多态执行器与（已弃用的）处理程序调用钩子之间的兼容性。

  - 新增 `experimental::as_single` 完成标记（completion token）适配器。

  - 通过使用 `_POSIX_VERSION` 检测是否受支持，在更多平台上添加了对 `MSG_NOSIGNAL` 的支持。

  - 新增在 Windows 上使用 libpthread 编译的能力。

  - 新增针对 Intel C++ 编译器的变通方案。

  - 增强对没有自定义执行器的处理程序的检测与优化支持。

  - 减少 Windows 上定时器取消的锁竞争。

  - 恢复了此前移除的空指针检查，因为它对性能有可测量的影响。

  - 修复 `executor` 概念（concept），以测试 const 限定的 `execute()`。

  - 修复 `any_executor` 在不支持 RTTI 的构建中的支持。

  - 修复 `thread_pool` 单元测试，使其在没有 RTTI 支持时也能工作。

  - 修复 Windows 上 clang 的 C++20 协程（coroutine）兼容性。

  - 修复与 Windows Runtime 的若干兼容性问题。

  - 修复因新增 `asio::query` 引起的名称遮蔽（shadow name）警告。

  - 修复 linux 上"相等表达式的逻辑或"警告。

  - 修复无害的 switch 贯穿（fallthrough）警告。

  - 补充缺失的 `push/pop_options.hpp` 包含。

  - 抑制"以零作为空指针常量"警告。

  - 修复逗号运算符警告。

  - 更新文档，澄清 Windows 上何时使用 `select` 反应器（reactor）。

  - 修复 `any_executor` 比较与转换可能引起的歧义。

  - 新增对 MSVC 19.8 上非实验性 C++20 协程的检测。

  - 修复与 uClibc 的兼容性。

  - 修复面向较旧 C++ 标准或一致性较低的编译器时，`strand<>` 对 Networking TS（网络技术规范）执行器的适配。

  - 更多细节请查阅[修订历史](/doc/libs/1_75_0/doc/html/boost_asio/history.html)。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 实现了地址查找算法的 SSE2 与 SSE4.1 版本，该算法用于内部锁池实现。这可能在高度竞争的情形下提升等待与通知操作的性能。

  - 修复 AArch64 目标上因立即数按位（逻辑）运算生成错误指令而可能引发的编译错误（[\#41](https://github.com/boostorg/atomic/issues/41)）。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 本次更新包含缺陷修复，并支持来自 Boost.Asio 的 `BOOST_ASIO_ENBALE_HANDLER_TRACKING` 编译开关（译注：宏名原文即如此拼写，应为 `BOOST_ASIO_ENABLE_HANDLER_TRACKING`）：

  - 我们很想知道您或您的公司如何使用 Beast，欢迎在[使用 Beast 的公司与个人](https://github.com/boostorg/beast/wiki/Companies-and-Individuals-Using-Beast)（Companies and Individuals Using Beast）列表中添加条目。

  - 完整变更列表请参见完整的[发布说明](/libs/beast/doc/html/beast/release_notes.html)。

- [Container](/libs/container/)（扩展容器库）：

  - 新增 `devector` 容器。

  - 修复的缺陷/问题：

    - [\#152](https://github.com/boostorg/container/issues/152) 基于树的容器处理仅移动（move-only）类型有问题。

    - [\#156](https://github.com/boostorg/container/issues/156) vector 编译错误。

    - [PR#157](https://github.com/boostorg/container/pull/157) 补充缺失的包含。

    - [\#159](https://github.com/boostorg/container/issues/159)：pmr::monotonic_buffer_resource 在大型单次分配时崩溃。

    - [\#160](https://github.com/boostorg/container/issues/160)：uses_allocator 的使用需要 remove_cvref_t。

    - [\#162](https://github.com/boostorg/container/issues/162)：MSVC x86 上 small_vector 按值传参时崩溃。

    - [\#161](https://github.com/boostorg/container/issues/161)：polymorphic_allocator(memory_resource\*) 的非标准扩展带来麻烦。

    - [PR#163](https://github.com/boostorg/container/pull/163)：为带选项的 small_vector 提供 container_rebind。

    - [\#165](https://github.com/boostorg/container/issues/165)：共享库与 memory_resource 内联成员的链接错误。

    - [PR#166](https://github.com/boostorg/container/pull/166)：修复版权头文件中的编码错误。

    - [PR#167](https://github.com/boostorg/container/pull/167)：GCC 4.4 下 "error: the address of 'msg' will always evaluate as 'true'" 警告。

    - [\#169](https://github.com/boostorg/container/issues/169)：clang11 上构建 dlmalloc_ext_2_8_6.c 产生大量警告。

- [Endian](/libs/endian/)（字节序处理库）：

  - `endian_arithmetic` 不再继承自 `endian_buffer`

  - 定义 `BOOST_ENDIAN_NO_CTORS` 时，非对齐的 `endian_buffer` 与 `endian_arithmetic` 为 C++03 POD，以便使用 `__attribute__((packed))`

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - **新增**：添加 `creation_time` 操作，可获取文件创建时间（受 [PR#134](https://github.com/boostorg/filesystem/pull/134) 启发）。

  - `last_write_time(p, ec)` 操作失败时的返回值已改为 `std::time_t` 可表示的最小值，而非 -1。

  - `hard_link_count(p, ec)` 操作失败时的返回值已改为 `static_cast<uintmax_t>(-1)`，而非 0。

  - 在 POSIX 系统上，若路径解析为非普通文件，`file_size` 现在将报告错误码 `errc::function_not_supported`。此前报告的是 `errc::operation_not_permitted`。

  - 在 Linux 上，许多操作现在尽可能在内部使用 `statx` 系统调用，从而减少从文件系统查询的信息量并可能提升性能。`statx` 系统调用自 Linux 内核 4.11 引入。

  - 移除了部分 `path` 方法返回类型的 const 限定。某些情况下这会阻碍调用点的移动构造与移动赋值（[\#160](https://github.com/boostorg/filesystem/issues/160)）。

  - 在 OpenBSD 4.4 及更新版本上，使用 `statvfs` 系统调用获取文件系统空间信息（受 [PR#162](https://github.com/boostorg/filesystem/pull/162) 启发）。

  - 在 Windows 上，若提供的路径不能标识已存在的文件，`space` 现在会返回错误（[\#167](https://github.com/boostorg/filesystem/issues/167)）。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 警告：继随 Boost 1.73 发布的 C++03 弃用通知之后，Boost.Geometry 从现在起要求具备完整 C++14 能力的编译器。

  - 功能增强：

    - [PR#726](https://github.com/boostorg/geometry/pull/726) 为面积（area）、包络（envelope）、扩展（expand）添加伞式策略（umbrella strategies）（暂未写入文档）。

    - [PR#733](https://github.com/boostorg/geometry/pull/733) 新增将 std::array\<\> 适配到 Point 概念（concept）的示例（感谢 Ben FrantzDale）。

    - [PR#745](https://github.com/boostorg/geometry/pull/745) 在几何模型与算术中添加 constexpr。

    - [PR#747](https://github.com/boostorg/geometry/pull/747) 新增可选的 traits::make（暂未写入文档）。

    - [PR#748](https://github.com/boostorg/geometry/pull/748) 现代化类型特征（type traits）的用法。

    - [PR#759](https://github.com/boostorg/geometry/pull/759) 以标准 static_assert 取代 MPL_ASSERT。

    - [PR#767](https://github.com/boostorg/geometry/pull/767) 现代化 tuple 的用法。

  - 已解决问题：

    - [\#716](https://github.com/boostorg/geometry/issues/716) 悬空的代理引用。

  - 缺陷修复：

    - 集合运算与缓冲区方面的各类修复。

- [GIL](/libs/gil/)（通用图像库）：

  - **破坏性变更预告**：在下一个发布中，我们将停止支持 GCC 5，也可能把最低要求的 C++ 标准版本从 C++11 改为 C++14。

- [Histogram](/libs/histogram/)（多维直方图库）：

  - 本次更新包含：

    - 针对边界情形的缺陷修复

    - 小幅文档改进

    - 针对最新编译器以及按 C++20 标准编译时新出现警告的修复

  - 完整变更列表参见完整的[发布说明](/libs/histogram/doc/html/histogram/history.html)。

- [Interprocess](/libs/interprocess/)（进程间通信库）：

  - 修复的缺陷：

    - [\#127](https://github.com/boostorg/interprocess/issues/127)：使用 boost interprocess 1.74 与 basic_managed_shared_memory 时静态断言失败。

- [Intrusive](/libs/intrusive/)（侵入式容器库）：

  - 修复的缺陷：

    - [PR#48](https://github.com/boostorg/intrusive/pull/48)：修复 MSVC"条件表达式内赋值"警告。

    - [PR#49](https://github.com/boostorg/intrusive/pull/49)：修复空控制语句警告。

    - [\#52](https://github.com/boostorg/intrusive/issues/52)：BOOST_INTRUSIVE_BSR_INTRINSIC 中的无效转换。

- [Log](/libs/log/)（日志库）：

  - 缺陷修复：

    - 修正 `text_file_backend` 在日志文件轮转时生成目标文件名（基于 `set_target_file_name_pattern` 方法设置的模式）时所使用的文件计数器（[\#125](https://github.com/boostorg/log/issues/125)）。

    - 将 `basic_sink_frontend` 中的 volatile 版本计数器替换为原子操作（[\#128](https://github.com/boostorg/log/issues/128)）。

    - 在 `asynchronous_sink` 前端中，解决了 `flush` 与 `run` 方法之间可能发生的冲突（当 `run` 由用户线程而非前端生成的内部专用线程调用时）（[\#131](https://github.com/boostorg/log/issues/131)）。

  - 更多细节参见[变更日志](/libs/log/doc/html/log/changelog.html)。

- [Move](/libs/move/)（移动语义/emplace 辅助库）：

  - 修复的缺陷：

    - [\#30](https://github.com/boostorg/move/issues/30)：(void) C 风格强转是一种不可移植的抑制编译器警告的方式。

- [Mp11](/libs/mp11/)（C++11 元编程库）：

  - 新增 `mp_pairwise_fold`（由 Barry Revzin 建议）

  - 移除 `mp_invoke`（请改用 `mp_invoke_q`）

- [Optional](/libs/optional/)（可选值容器库）：

  - `boost::none` 现以 `constexpr` 声明。

  - 修复 [issue \#78](https://github.com/boostorg/optional/issues/78)。

- [Outcome](/libs/outcome/)（轻量级错误处理（result/outcome）库）：

  - 公告：

    - 在历时一年、历经三个主要的 Boost 发布预告这一即将到来的变更之后，本发布是 v2.1 分支的最终发布。自 Boost 1.76 起，v2.2 分支成为默认。相对于 Outcome v2.1，该分支包含多项重大破坏性变更，详情参见文档。

  - 功能增强：

    - 原先通过 ADL 发现的事件钩子（event hooks）已被策略指定（policy-specified）的事件钩子取代。原因在于：脆弱性（一旦有人改动某些内容，钩子可能悄然自行失效）、编译器缺陷（编译器设置的差异会导致发现错误的钩子，或仅发现部分钩子），以及最终用户根本难以使用。为向后兼容，可让策略指定的事件钩子默认回落到 ADL 发现的钩子：将 `OUTCOME_ENABLE_LEGACY_SUPPORT_FOR` 设为小于 `220` 的值以启用模拟。

    - 改进了 `OUTCOME_GCC6_CONCEPT_BOOL` 的配置。较旧的 GCC 使用基于布尔的概念（concepts）语法，而较新的 GCC 遵循标准。然而，何时使用旧式与标准语法的确切逻辑此前未被充分理解，导致 Outcome 会因传给 GCC 的选项不同而编译失败。新逻辑在 GCC 8 或更旧时总是使用旧式语法；否则当且仅当 GCC 处于 C++20 或更高模式时使用标准语法。这有望解决 GCC 上的边界情形构建失败。

  - 缺陷修复：

    - 定义 `BOOST_NO_EXCEPTIONS` 后 Boost.Outcome 现在应能编译。感谢 Boost.Exception 的维护者 Emil 为我所作的修改，Boost.Outcome 现在可以在全局禁用 C++ 异常的情况下编译。但由于全局禁用异常时无法包含 `boost::exception_ptr`，您将无法使用它。

    - [\#236](https://github.com/ned14/outcome/issues/236) 在协程（coroutine）支持中，`final_suspend()` 不是 `noexcept`，尽管 C++20 标准要求如此。此问题已修复，但仅当您的编译器实现了 `noop_coroutine` 时生效。此外，若 `noop_coroutine` 可用，我们将使用返回协程句柄的高效 `await_suspend()` 变体，这应能显著改进代码生成与上下文切换性能。

- [Polygon](/libs/polygon/)（多边形布尔运算库）：

  - 修复 `event_comparison_type`、`vertex_equality_predicate_type` 与 `voronoi_predicates` 的 C++20 兼容问题。（Glen Fernandes）

- [Preprocessor](/libs/preprocessor/)（预处理器元编程库）：

  - 在支持 \_\_VA_OPT\_\_ 的 C++20 模式下，当可变参数数据为空时，可变参数个数已被修正为 0。这也意味着在此 C++20 模式下，空数组、空列表与空可变参数数据之间的相互转换现在有效。最终用户可阅读"variadic macros"（可变参数宏）主题中的"C++20 Support For Variadic Macros"（C++20 对可变参数宏的支持）部分，了解库中空可变参数数据的更多信息。

  - 新增宏 BOOST_PP_IS_STANDARD()，用于判定当前使用的预处理器是否为符合 C++ 标准的预处理器。若干预处理器（包括当前默认的 VC++ 预处理器）通常可与本库正常配合使用，但需要各种内部变通处理，它们不被视为符合 C++ 标准的预处理器。而大多数预处理器——包括 gcc、clang 以及 VS2019 中新推出但尚未成为默认的 VC++ 预处理器等——都是符合 C++ 标准的预处理器。

  - 对于符合 C++ 标准的预处理器，config/limits.hpp 中定义的若干上限现在可以为单个翻译单元（TU）调高。最终用户应阅读"limitations"（限制）主题，了解如何调整以及哪些上限可调。

  - 对于符合 C++ 标准的预处理器，为允许最大数量的 FOR 与 WHILE 迭代，用户自定义宏中起始的 'r' 与 'd' 迭代编号现在从 1 开始，而非如先前发布那样从 2 开始。如果用户自定义宏使用了这些迭代编号（大概率不会），这可能构成破坏性变更；但此变更对于修复处理最大数值的数值/逻辑运算时的若干晦涩缺陷，以及让用户自定义宏能够被调用到正确的最大次数，都是必要的。对于不符合 C++ 标准的预处理器，则未做此变更，因为这些不符合标准的 C++ 预处理器通常存在限制，无法运行最大数量的循环结构；且我们认为不给这些更脆弱的预处理器引入潜在的破坏性变更更好。我们还认为，除了修复若干晦涩的预处理器缺陷并提供可能的最大用户自定义宏调用次数之外，此变更之所以可行，还因为起始的 'r' 与 'd' 迭代编号的实际取值从未被文档记载过，文档只说明这些编号在每次迭代中递增。

  - 本库已升级为假定任何可与之配合使用的编译器都支持可变参数宏。表面上这意味着本库现在面向 C++11 及以上，然而大多数主流编译器（包括 gcc、clang 与 VC++）在 C++98/C++03 模式下也支持可变参数宏，只要使用这些编译器时未开启对 C++98/C++03 的严格一致性检查。

- [Rational](/libs/rational/)（有理数库）：

  - 修复 Rational 运算符，使其在新的 C++20 `operator ==` 改写规则下不失效。（Glen Fernandes）

- [Signals2](/libs/signals2/)（线程安全信号槽库）：

  - 修正 C++ 分配器模型支持，修复 C++20 标准模式下的编译。（Glen Fernandes）

- [System](/libs/system/)（错误码与 system_error 库）：

  - 平台特定头文件 `windows_error.hpp`、`linux_error.hpp` 与 `cygwin_error.hpp` 现发出弃用消息，并计划移除。

  - `generic_category()` 与 `system_category()` 的旧名称现发出弃用消息，并计划移除。

  - `error_condition::failed` 已弃用并计划移除。`error_condition` 的 `operator bool()` 已恢复为旧含义 `value() != 0`。此举是为与 `std::error_condition` 保持兼容，因为下一发布预计将进一步改进与 `<system_error>` 的互操作性。*请注意这不影响* `error_code::failed`，后者依然健在可用。

  - 出于相同原因，接受缓冲区参数的 `error_condition::message` 重载已弃用并计划移除。*请注意这不影响* `error_code::message`。

- [uBLAS](/libs/numeric/ublas/)（线性代数（BLAS 风格）库）：

  - 修正 C++ 分配器模型支持，修复 C++20 标准模式下的编译。（Glen Fernandes 与 Conrad Poelman）

- [VMD](/libs/vmd/)（可变宏数据（预处理器扩展）库）：

  - VMD 数字解析已升级，支持最终用户更改 Preprocessor 库中的数字上限。

  - 新增宏 BOOST_VMD_IS_GENERAL_IDENTIFIER，支持解析匹配 VMD 标识符语法的预处理器记号输入，而无需将该标识符注册为特定标识符。

- [Wave](/libs/wave/)（C/C++ 预处理器实现库）：

  - 新增 C++20 记号，包括三路比较运算符（宇宙飞船运算符）\<=\>

  - 修复的缺陷：

    - [\#94](https://github.com/boostorg/wave/issues/94)：修复重扫描（rescanning）下 \_\_LINE\_\_ 与 \_\_FILE\_\_ 的错误行为

## 已测试的编译器（Compilers Tested）

Boost 的主要测试编译器如下：

- Linux：

  - Clang：3.0, 4.0.1, 6.0.1

  - Clang，C++0x：3.0

  - Clang，C++11：3.0, 3.1, 3.2, 3.3, 3.4, 4.0.1, 6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0

  - Clang，C++14：3.5.0, 3.6.0, 3.7.1, 3.8.0, 3.9.1, 4.0.0, 4.0.1, 5.0.2, 6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0

  - Clang，C++17：5.0.2, 6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0

  - GCC：4.4.7, 4.5.3, 4.6.3, 5.4.0, 8.0.1

  - GCC，C++0x：4.4.7

  - GCC，C++11：4.7.3, 4.8.5, 4.9.4, 5.4.0, 6.4.0, 7.1.0, 8.0.1

  - GCC，C++14：5.4.0, 5.5.0, 6.4.0, 7.1.0, 7.3.0, 8.0.1

  - GCC，C++17：7.3.0, 8.0.1

  - Intel，C++14：18.0

- OS X：

  - Apple Clang：9.0.0, 9.1.0, 10.0.0, 11.0.0

  - Apple Clang，C++11：9.0.0, 9.1.0, 10.0.0, 11.0.0

  - Apple Clang，C++14：9.0.0, 9.1.0, 10.0.0, 11.0.0

  - Apple Clang，C++17：9.1.0, 10.0.0, 11.0.0

  - Apple Clang，C++1z：9.0.0

  - Apple Clang，C++2a：10.0.0, 11.0.0

- Windows：

  - GCC：3.4.5, 4.1.2, 4.2.4, 4.3.3, 4.4.0, 4.5.4

  - GCC，C++0x：4.6.4

  - GCC，C++11：4.7.3, 4.8.1, 4.9.3

  - GCC，C++14：5.1.0, 5.2.0, 5.3.0, 6.1.0, 6.2.0, 6.3.0, 6.4.0

  - GCC，C++17：7.1.0, 7.2.0, 7.3.0

  - Visual C++：7.1, 8.0, 9.0, 10.0, 11.0, 12.0, 14.0, 14.1

- FreeBSD：

  - Clang：4.0.0

  - Clang，C++11：4.0.0

  - Clang，C++14：4.0.0

  - Clang，C++1z：4.0.0

Boost 的其他测试编译器包括：

- Linux：

  - Clang：3.0, 3.8.1, 3.9.1, 4.0.1, 5.0.2, 6.0.1

  - Clang，C++0x：3.0

  - Clang，C++11：3.0, 3.1, 3.2, 3.3, 3.4, 4.0.1, 6.0.1, 7.0.0, 8.0.0

  - Clang，C++14：3.5.0, 3.6.0, 3.7.1, 3.8.0, 3.9.1, 4.0.0, 4.0.1, 5.0.2, 6.0.1, 7.0.0, 8.0.0

  - Clang，C++17：5.0.2, 6.0.1, 7.0.0, 8.0.0

  - GCC：4.4.7, 4.5.3, 4.6.3, 4.9.4, 5.4.0, 5.5.0, 8.0.1

  - GCC，C++0x：4.4.7

  - GCC，C++11：4.7.3, 4.8.5, 4.9.4, 5.4.0, 6.4.0, 7.1.0, 8.0.1

  - GCC，C++14：5.4.0, 5.5.0, 6.3.0, 6.4.0, 7.1.0, 7.3.0, 8.0.1, 8.1.0

  - GCC，C++17：7.3.0, 8.0.1

  - Intel，C++14：18.0

- OS X：

  - Apple Clang：9.0.0, 9.1.0, 10.0.0

  - Apple Clang，C++11：9.0.0, 9.1.0, 10.0.0

  - Apple Clang，C++14：9.0.0, 9.1.0, 10.0.0

  - Apple Clang，C++17：9.1.0, 10.0.0

  - Apple Clang，C++1z：9.0.0

  - Apple Clang，C++2a：10.0.0

- Windows：

  - GCC：3.4.5, 4.1.2, 4.2.4, 4.3.3, 4.4.0, 4.5.4

  - GCC，C++0x：4.6.4

  - GCC，C++11：4.7.3, 4.8.1, 4.9.3

  - GCC，C++14：5.1.0, 5.2.0, 5.3.0, 6.1.0, 6.2.0, 6.3.0, 6.4.0

  - GCC，C++17：7.1.0, 7.2.0, 7.3.0

  - Visual C++：7.1, 8.0, 9.0, 10.0, 11.0, 12.0, 14.0, 14.1

- FreeBSD：

  - Clang：4.0.0

  - Clang，C++11：4.0.0

  - Clang，C++14：4.0.0

  - Clang，C++1z：4.0.0

## 致谢（Acknowledgements）

本次发布由 Marshall Clow、Michael Caisse 与 Glen Fernandes 管理。
