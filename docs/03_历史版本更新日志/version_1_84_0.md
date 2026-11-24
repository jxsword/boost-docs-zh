# Boost 1.84.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_84_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_84_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2023-12-13 23:54 GMT（原文日期行：December 13th, 2023 23:54 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.84.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目；原文开篇为下节"更新默认 Windows 目标版本"的总体性说明。

## 更新默认 Windows 目标版本（Updated default target Windows version）

Boost.WinAPI（供其他 Boost 库内部使用、用于定义 Windows SDK 组件的库）已更新为在可行的情况下默认面向 Windows 10 API。这意味着 Boost 库将默认面向 Windows 10，可能无法在更旧的 Windows 版本上运行；由 Boost 分发的预编译二进制文件同样如此。

受影响的库包括：

- Boost.Atomic

- Boost.Beast

- Boost.Chrono

- Boost.DateTime

- Boost.DLL

- Boost.Filesystem

- Boost.Interprocess

- Boost.Log

- Boost.Pool

- Boost.Process

- Boost.System

- Boost.Stacktrace

- Boost.Thread

- Boost.UUID

以及依赖于上述库的其他库。

用户可以在构建和使用 Boost 时将 `BOOST_USE_WINAPI_VERSION` 或 `_WIN32_WINNT` 定义为所需的版本号，从而更改该默认值。例如，要构建面向 Windows 7 的 Boost，可以使用类似如下的命令行：

```
b2 variant=release define=BOOST_USE_WINAPI_VERSION=0x0601 stage
```

但请注意，个别库对最低支持的 Windows 版本可能有各自的要求。

Windows API 版本号列表参见[此页面](https://msdn.microsoft.com/en-us/library/6sehtctf.aspx)。

## 新增库（New Libraries）

- [Cobalt](/libs/cobalt/)（C++20 协程基础算法与类型库）：面向 C++20 协程（coroutine）的基础算法与类型，由 Klemens Morgenstern 开发。

- [Redis](/libs/redis/)（Redis 异步客户端库）：构建于 Boost.Asio 之上的 Redis 异步客户端库，由 Marcelo Zimbres Silva 开发。

## 更新的库（Updated Libraries）

- [Any](/libs/any/)（类型安全的任意类型容器库）：

  - 不再支持 C++03（[PR#26](https://github.com/boostorg/any/pull/26)）。

  - 修复参考文档的生成问题。参考文档现在不会再被 Boost.PFR 的参考文档覆盖。感谢 Peter Dimov 排查该问题。

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 改为要求以 C++11 作为最低语言标准。不再支持 C++03。

  - 从 `boost::asio::execution` 命名空间中移除了已弃用的功能。

  - 移除了已弃用的调用（invocation）与分配（allocation）挂钩（hook）。

  - 为 channel（通道）新增 `try_send_via_dispatch` 与 `try_send_n_via_dispatch` 函数。

  - 新增 Asio 占位符（placeholder）与 `std::bind` 之间的兼容性。

  - 改进对具有多个完成签名（completion signature）的 channel 的 C++11 支持。

  - 修复 channel 异步操作与 `any_completion_handler` 之间的兼容性问题。

  - 修复 `any_completion_handler` 与使用 `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT` 编译之间的兼容性问题。

  - 新增缺失的相等运算符，用于比较属于同一类别的混合执行器属性类型（executor property types）。

  - 修复基于 `spawn` 的栈式协程（stackful coroutine）在完成签名以 `std::exception_ptr` 开头的异步操作中使用时会导致程序终止的问题。

  - 修复访问默认构造的 `any_completion_handler` 对象的关联器（associator）时可能发生的崩溃。

  - 修复 `ssl::stream<>` 类的 `async_handshake` 操作，使其可与默认化的完成标记（completion token）配合工作。

  - 将所有示例更新为以 C++11 作为最低语言标准。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 不再支持 C++03，要求的最低语言版本为 C++11。

  - 新增对精度降低的 x87 扩展双精度（extended double）类型的支持，该类型用于 FreeBSD 与 OpenBSD（[\#14](https://github.com/boostorg/atomic/issues/14)）。

  - 对早于 Windows 10 的 Windows 版本的支持已弃用，并将在 Boost 1.87 中移除。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 新增对 `immediate_executor` 的支持。

  - 移除已弃用的分配与调用挂钩（hook）。

  - 在完成 `transfer_op` 时使用显式类型 std::size_t。

  - 以 `BOOST_ASIO_INITFN_AUTO_RES` 取代 `BOOST_ASIO_INITFN_RESULT_TYPE`。

  - `server-flex-awaitable` 示例会重置解析器。

  - 修正 `websocket::stream::async_ping`/`pong` 的处理程序要求。

  - 更新 `websocket::stream::async_write_some` 的文档。

- [Chrono](/libs/chrono/)（时间度量与时钟库）：

  - 不再支持 C++03。

- [ContainerHash](/libs/container_hash/)（哈希支持库）：

  - 不再支持 C++03。

- [Conversion](/libs/conversion/)（类型转换库）：

  - 不再支持 C++03（[PR#27](https://github.com/boostorg/conversion/pull/27)）。

- [Core](/libs/core/)（核心工具集库）：

  - `boost::swap` 工具函数已更名为 `boost::core::invoke_swap`，以避免在实参不可交换（not swappable）时形成潜在的无限递归。新函数定义于 `boost/core/invoke_swap.hpp`，在功能上与 `boost::swap` 等价。旧的 `boost::swap` 名称出于向后兼容考虑予以保留，但已弃用并将在未来发布中移除。其 `noexcept` 规范已被移除，以避免由编译期递归引起的编译错误。在过渡期间可定义 `BOOST_ALLOW_DEPRECATED_SYMBOLS` 或 `BOOST_ALLOW_DEPRECATED` 以抑制弃用警告（[\#148](https://github.com/boostorg/core/issues/148)）。

  - 头文件 `boost/swap.hpp`、`boost/utility/swap.hpp` 与 `boost/core/swap.hpp` 已弃用并将被移除。请改用 `boost/core/invoke_swap.hpp`。可定义 `BOOST_ALLOW_DEPRECATED_HEADERS` 或 `BOOST_ALLOW_DEPRECATED` 以抑制弃用警告。

- [CRC](/libs/crc/)（循环冗余校验计算库）：

  - 对 C++03 的支持已弃用，并将在 1.86 发布中移除。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 不再支持 C++03（[PR#66](https://github.com/boostorg/dll/pull/66)）。

- [Endian](/libs/endian/)（字节序处理库）：

  - 不再支持 C++03。

- [Filesystem](/libs/filesystem/)（可移植文件系统操作库）：

  - 如 Boost 1.82.0 中所公告，不再支持 C++03。要求 C++11 或更高版本的编译器。

  - 修复部分接受 `error_code& ec` 实参的 `directory_entry` 观测器（observer）在成功返回时未清除错误码的问题（[\#291](https://github.com/boostorg/filesystem/issues/291)）。

  - 在 Windows 上，改进了日期与时间转换的健壮性，并新增对 1970 年 1 月 1 日之前日期的支持（[\#293](https://github.com/boostorg/filesystem/issues/293)）。

  - 移除了自 Boost.Filesystem 1.79.0 起已弃用的 Windows CE 支持。

  - 移除了 `boost/filesystem/string_file.hpp` 头文件。该头文件自 Boost.Filesystem 1.79.0 起已弃用。

  - **弃用：** 对早于 Windows 10 的 Windows 版本的支持已弃用，并将在 Boost 1.87 中移除。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 已解决问题（Solved issues）：

    - [\#1138](https://github.com/boostorg/geometry/issues/1138) 修复两个多边形的差集（difference）运算

    - [\#1183](https://github.com/boostorg/geometry/issues/1183) 修复 union_ 结果多边形不完整的问题

    - [\#1184](https://github.com/boostorg/geometry/issues/1184) 修复 intersection（求交）运算

    - [\#1186](https://github.com/boostorg/geometry/issues/1186) 修复 union_ 对内环（inner ring）的不当赋值

    - 各类错误与警告的修复

- [Heap](/libs/heap/)（优先队列家族库）：

  - 对 C++03 的支持已弃用，并将在 1.86 发布中移除。新要求为 C++14。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 实现直接解析到用户类型。

  - 为 optional 与 variant 新增转换类别（conversion categories）。

  - 放宽自迭代器对（iterator pair）构造的迭代器要求。

  - 修复越过输入缓冲区读取的问题。

  - 修复初始化列表构造函数选择不一致的问题。

- [LEAF](/libs/leaf/)（轻量级错误处理库）：

  - `result<T>` 类标记为 `nodiscard`。

  - 新增成员 typedef `result<T>::value_type`。

  - `verbose_diagnostic_info` 将到字符串的转换推迟至进入错误处理作用域时才进行。

  - 改进对嵌入式开发的支持。

  - 改进与 Visual Studio 2015 的兼容性（感谢 godmaycrying）。

  - 若干小缺陷修复与改进。

  - 停止支持 GCC 4.8 与 4.9。

- [LexicalCast](/libs/lexical_cast/)（字符串↔数值等类型转换库）：

  - 不再支持 C++03（[PR#62](https://github.com/boostorg/lexical_cast/pull/62)）。

  - 修复 clang 下的 -Wdeprecated-copy-with-dtor 警告。感谢 [Romain Geissler](https://github.com/Romain-Geissler-1A) 提交的 [PR#59](https://github.com/boostorg/lexical_cast/pull/59)！

  - 移除对 Boost.Range 的依赖（[PR#63](https://github.com/boostorg/lexical_cast/pull/63)）。

- [Locale](/libs/locale/)（本地化与 Unicode 文本处理库）：

  - WinAPI 后端的 `to_title` 现在原样返回字符串，而不是返回空字符串。

  - 改进对 `char8_t` 与 `std::u8string` 的支持。

  - 修复使用负时间值时的差一（off-by-one）错误（[PR#198](https://github.com/boostorg/locale/pull/198)）。

  - 修复格式字符串中大括号转义处理的问题（[\#194](https://github.com/boostorg/locale/issues/194)）。

  - 修复部分构建错误与警告，其中显著的是 MSVC 上的一处，见 [\#189](https://github.com/boostorg/locale/issues/189)。

- [Lockfree](/libs/lockfree/)（无锁容器与队列库）：

  - 对 C++03 的支持已弃用，并将在 1.86 发布中移除。新要求为 C++14。

- [Log](/libs/log/)（日志库）：

  - 不再支持 C++03。要求 C++11 或更高版本的编译器。

  - 当使用符合要求、足以启用 Boost.Regex v5 的 C++11 编译器构建时，Boost.Log 不再链接 Boost.Regex 预编译库，因为 Boost.Regex v5 是仅头文件库。

  - 对早于 Windows 10 的 Windows 版本的支持已弃用，并将在 Boost 1.87 中移除。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - 改进 ccmath 的错误检测。

  - 移除对已弃用的 `std::numeric_limits<>::has_denorm` 的使用，见 [1028](https://github.com/boostorg/math/issues/1028)。

  - 修正非中心 t 分布（non-central t distribution）不收敛的缺陷，见 [1035](https://github.com/boostorg/math/issues/1035)。

  - 调整 Bessel 函数对 ₁F₁ 的逼近，以避免在负整数处求 tgamma，见 [1034](https://github.com/boostorg/math/issues/1034)。

  - 避免 `ibeta` 中的虚假溢出与除零，见 [1006](https://github.com/boostorg/math/issues/1006)。

  - 提高使用 Sterling 近似（译注：原文即如此，应为 Stirling 近似）计算 tgamma 时的精度，完成了始于 [1007](https://github.com/boostorg/math/pull/1007) 的工作。

  - 修复大初始猜测值下 `inverse_discrete_quantile` 的问题，见 [1007](https://github.com/boostorg/math/pull/1007)。

  - 改进 Newton（牛顿）求根，见 [1000](https://github.com/boostorg/math/pull/1000)。

  - 修复非零中心情形下 `median_absolute_deviation` 的问题，见 [997](https://github.com/boostorg/math/pull/997)。

  - 修正 `cstdfloat.hpp` 以适配 gcc-14。

  - 更新以支持 \<stdfloat\> 中声明的新类型。

  - 将 `hypergeometric_distribution` 改用 64 位而非 32 位整数，以避免不必要的溢出与使用上的限制。

- [Multi-index Containers](/libs/multi_index/)（多索引容器库）：

  - 修复在不支持 ADL（参数依赖查找）的旧编译器中一个与序列化相关的编译期缺陷（issue [\#70](https://github.com/boostorg/multi_index/issues/70)）。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - 在测试中将 `boost::array` 改为 `std::array`，修复 [567](https://github.com/boostorg/multiprecision/issues/567)。

  - 修正 `cpp_int::eval_convert_to` 使其为 `noexcept`，修复 [553](https://github.com/boostorg/multiprecision/issues/553)。

  - 确保更改全局精度时，当前线程的精度也随之更改。

  - 修复 `rational_adaptor` 的构造缺陷，修复 [540](https://github.com/boostorg/multiprecision/issues/540)。

- [MySQL](/libs/mysql/)（MySQL 客户端库）：

  - 新增 `connection::reset_connection` 与 `connection::async_reset_connection`。这些函数清理会话状态（包括预处理语句、变量、锁等），而无需关闭并重新打开连接。

  - 新增 MySQL 服务器 v8.1.0 引入的错误码。

  - 为反序列化函数新增模糊测试（fuzz testing）。

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - **重大新特性：字段名反射（reflection）。** 新增 `constexpr` 函数 `boost::pfr::get_name<N, T>()`，返回一个 `std::string_view`，内容为聚合类型 `T` 中索引为 `N` 的字段的名称。要求 C++20。若该功能可用，则 `BOOST_PFR_CORE_NAME_ENABLED` 被定义为 1。非常感谢 [Denis Mikhailov](https://github.com/denzor200)、[Bela Schaum](https://github.com/schaumb) 与 [X-Ryl669](https://github.com/X-Ryl669) 提交的 [PR#129](https://github.com/boostorg/pfr/pull/129) 及其实现思路。

  - `for_each_field()` 在 C++17 下现为 `constexpr`。非常感谢 [Alexander Karatarakis](https://github.com/alexkaratarakis) 提交的 [PR#134](https://github.com/boostorg/pfr/pull/134)。

- [Predef](/libs/predef/)（编译器/架构/OS 预定义宏库）：

  - 版本 1.15.0。

  - 新增对 Microsoft STL 的检测（来自 Henrik Gaßmann）。

- [Random](/libs/random/)（随机数生成器与分布库）：

  - 不再支持 C++03。

  - 修复测试中使用 Boost.Multiprecision 时的溢出问题。

- [Ratio](/libs/ratio/)（编译期分数运算库）：

  - 不再支持 C++03。

  - 对 `BOOST_RATIO_EXTENSIONS` 的支持已被移除。Ratio 现在基于标准 `<ratio>` 头文件实现。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 不再支持 C++03。感谢 [Alex](https://github.com/leha-bot) 提交的 [PR#139](https://github.com/boostorg/stacktrace/pull/139)。

  - 修复 PIE（位置无关可执行文件）二进制文件下 `addr2line` 的问题。感谢 [ja2142](https://github.com/ja2142) 提交的 [PR#138](https://github.com/boostorg/stacktrace/pull/138)！

  - 修复 MinGW-w64 12 及以上版本的构建。感谢 [yhsb2k](https://github.com/yhsb2k) 提交的 [PR#140](https://github.com/boostorg/stacktrace/pull/140)！

  - 补上缺失的 include。感谢 [Francesco Ballarin](https://github.com/francesco-ballarin) 提交的 [PR#143](https://github.com/boostorg/stacktrace/pull/143)！

- [System](/libs/system/)（错误码与 system_error 库）：

  - 新增对 `result<U&, E>` 的支持。

  - 为 `result` 新增 `operator|`。

  - 为 `result` 新增 `operator&`。

  - 为 `result` 新增 `operator&=`。

- [Test](/libs/test/)（单元测试框架库）：

  - 不再支持 C++03。

  - 修复 glibc 2.2 - 2.17 下 PRIxPTR 的使用问题（[PR#392](https://github.com/boostorg/test/pull/392)）。

  - 修复 MSVC 警告 C5263"对临时对象调用 'std::move' 会阻止拷贝消除（copy elision）"（[PR#390](https://github.com/boostorg/test/pull/390)）。

- [Thread](/libs/thread/)（可移植线程库）：

  - 不再支持 C++03。

- [TypeIndex](/libs/type_index/)（运行时类型索引库）：

  - 不再支持 C++03。

  - `BOOST_TYPE_INDEX_REGISTER_RUNTIME_CLASS((A)(B)(C)(D))` 的语法改为 `BOOST_TYPE_INDEX_REGISTER_RUNTIME_CLASS(A, B, C, D)`。

  - 移除对 Boost.PP 的依赖。

- [TypeOf](/libs/typeof/)（表达式类型推导工具库）：

  - 不再支持 C++03。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - **重大更新。**

  - 新增 `boost::concurrent_flat_set`。

  - 为并发容器新增 `[c]visit_while` 操作，含串行与并行两种变体。

  - 新增自 `boost::concurrent_flat_(map|set)` 高效移动构造 `boost::unordered_flat_(map|set)` 的能力，反之亦然。

  - 为并发容器新增批量访问（bulk visitation）以提升查找性能。

  - 新增调试模式下检测用户代码对并发容器进行非法重入（reentrancy）的机制。

  - 为所有容器及其（非本地）迭代器类型新增 Boost.Serialization 支持。

  - 为开放寻址（open addressing）容器与并发容器新增对花式指针（fancy pointer）的支持。这使得诸如使用 Boost.Interprocess 分配器在共享内存中构造容器等场景成为可能。

  - 修复封闭寻址（closed addressing）容器本地迭代器的成员指针访问运算符（operator->）缺陷（[PR#221](https://github.com/boostorg/unordered/pull/221)，感谢 GitHub 用户 vslashg 发现并修复该问题）。

  - 自本发布起，`boost::unordered_[multi]set` 与 `boost::unordered_[multi]map` 仅支持 C++11 及更高版本。

- [variant](/libs/variant/)（非递归可辨识联合库）：

  - 不再支持 C++03（[PR#107](https://github.com/boostorg/variant/pull/107)）。

  - 移除对 Boost.Move 与 Boost.Bind 的依赖。

- [Wave](/libs/wave/)（C/C++ 预处理器实现库）：修复以下缺陷：

  - [\#188](https://github.com/boostorg/wave/issues/188)：遇到 `"#pragma\n"` 时发生段错误（segmentation fault）

## 更新的工具（Updated Tools）

本版原文无该栏目。

## 已测试的编译器（Compilers Tested）

Boost 的主要测试编译器如下：

- Linux：

  - Clang，C++03：3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++11：3.4, 11.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++14：3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 5.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++17：6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++20：11.0.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - GCC，C++03：4.6.3, 11, 12

  - GCC，C++11：4.7.3, 4.8.5, 11, 12

  - GCC，C++14：5.4.0, 6.4.0, 7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC，C++17：7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC，C++20：8.0.1, 9.1.0, 10, 11, 12

- OS X：

  - Apple Clang，C++03：11.0.3

  - Apple Clang，C++11：11.0.3

  - Apple Clang，C++14：11.0.3

  - Apple Clang，C++17：11.0.3

  - Apple Clang，C++20：11.0.3

- Windows：

  - Visual C++：10.0, 11.0, 12.0, 14.0, 14.1, 14.2, 14.3

## 致谢（Acknowledgements）

本次发布由 Marshall Clow 与 Glen Fernandes 管理。
