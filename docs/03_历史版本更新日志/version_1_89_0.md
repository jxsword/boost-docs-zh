# Boost 1.89.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/version_1_89_0.md（原始 URL：https://www.boost.org/users/history/version_1_89_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2025-08-14 02:16 GMT（原文日期行）

下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.89.0/source/）。原文注明下载链接由 The C++ Alliance（C++ 联盟）资助提供。

## 总体注记（General Notes）

原文本版无总体注记（General Notes）章节。

## 新增库（New Libraries）

- [Bloom](/libs/bloom/)（布隆过滤器库）：布隆过滤器（Bloom filters），来自 Joaquín M López Muñoz。

## 更新的库（Updated Libraries）

- [Any](/libs/any/)（类型安全的任意类型容器库）：

  - **初步支持 C++20 模块（C++20 Modules）**。更多信息见文档。

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 为 `execution_context`、`io_context` 与 `thread_pool` 新增接受分配器的构造函数，所提供的分配器用于分配与执行上下文关联的对象。

  - 新增配置参数 "timer" / "heap_reserve"，可用于为定时器队列堆所用的 vector 预留空间。

  - 新增配置参数 "resolver" / "threads"，指定 `async_resolve` 用于模拟异步地址解析的内部线程数。

  - 从便捷头文件 `boost/asio.hpp` 中移除 `deadline_timer`、`basic_deadline_timer` 与 `time_traits`。

  - 确保 `connect_pipe` 创建的 Windows 命名管道使用唯一名称，当 Asio 被用于多个相互独立的插件 DLL 时也不会冲突。

  - 使 `BOOST_ASIO_CONCURRENCY_HINT_SAFE` 与 `io_context` 默认构造函数保持一致。

  - 修正 `BOOST_ASIO_CONCURRENCY_HINT_UNSAFE_IO` 的文档，说明注册锁仍处于启用状态。

  - 为可选依赖新增独立的 `b2` 与 `cmake` 构建目标。

  - 为 `boost::asio::detail::throw_exception` 添加 `[[noreturn]]` 属性。

  - 修复 `co_spawn`，使其遵守"完成处理程序不可重入调用"这一异步操作要求。

  - 新增关于 `basic_signal_set` 异步信号安全性的文档说明。

  - 修复不同平台上各种小的编译错误。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_89_0/doc/html/boost_asio/history.html)。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 在基于汇编的 x86、AArch32、AArch64 与 PPC 后端中加入 TSAN 插桩。这可消除使用 Boost.Atomic 做线程同步的代码在 TSAN 下的误报。

  - 按 Boost 1.84 中的公告，移除对 Windows 10 之前 Windows 版本的支持。

    - 给 MinGW-w64 用户的提示：由于 MinGW-w64 上的 Windows SDK 头文件默认把 `_WIN32_WINNT` 定义为较旧的 Windows 版本，编译 Boost.Atomic 及使用 Boost.Atomic 的代码时可能需要定义 `_WIN32_WINNT=0x0A00` 或 `BOOST_USE_WINAPI_VERSION=0x0A00`。

  - 对 Windows CE 的支持已弃用（deprecation），将在未来发布中移除。

  - 新增限时等待操作支持。

  - 公开 `thread_pause` 操作，可用作自旋循环中的退避（backoff）手段。为 `thread_pause` 新增 PowerPC 支持并改进 AArch64 支持。

  - 移除 `BOOST_ATOMIC_NO_ATOMIC_FLAG_INIT` 宏定义。由于本库现在要求 C++11，`BOOST_ATOMIC_FLAG_INIT` 总是被支持。

  - 为原子枚举启用位运算。当枚举用于实现位掩码时这会很有用。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 修复

    - 在 `async_base` 中按条件定义 `immediate_executor_type`。

    - 为 `detail/cpu_info.hpp` 补上缺失的 `cstdint` 头文件。

    - 修复 `std::is_trivial` 弃用警告。

    - `handshake_timeout` 现在也适用于读取期间的关闭握手。

  - 改进

    - 以 `net::executor_work_guard` 取代 `detail/work_guard.hpp`。

    - 修复 MinGW 中构建测试的可移植性问题。

  - 文档

    - 从文档中移除已迁移的章节。

    - 从测试中移除多余的日志消息。

  - 致谢

    - yliu1021

- [Charconv](/libs/charconv)（字符与数值互转库）：

  - 修复整数类型 `from_chars` 的性能退化。

  - 修复浮点类型 `to_chars` 在指定精度下的舍入与小数末位缺陷。

- [Cobalt](/libs/cobalt/)（协程异步库）：

  - 修复 generator 与 promise 的移动赋值。

  - 修复内部异常。

  - 新增 IO 库。Cobalt.io 以需编译库形式提供 asio 的一个大子集。

- [Compat](/libs/compat/)（标准库补丁库）：

  - 新增 `move_only_function.hpp`。

- [ContainerHash](/libs/container_hash/)（哈希库）：

  - 新增特征类（trait）`hash_is_avalanching`。

- [Conversion](/libs/conversion/)（类型转换库）：

  - 新增在 constexpr 中使用 `polymorphic_downcast` 与 `polymorphic_cast` 的能力（要求 C++20）。

- [Core](/libs/core/)（核心工具集库）：

  - 修复 `bit_ceil` 对输入 0 按规范返回 1。（[PR#199](https://github.com/boostorg/core/pull/199)）

  - 为 `boost::core::string_view` 新增 `std::format` 支持。（[\#190](https://github.com/boostorg/core/issues/190)）

- [Detail](/libs/detail/)（内部实现细节库）：

  - `BOOST_BITMASK` 生成的运算符现在使用枚举的底层类型来实现位运算符。这些运算符在可能时标记为 `noexcept` 与 `constexpr`。

  - `BOOST_BITMASK` 生成的函数 `bitmask_set` 已标记弃用。未来发布中 `BOOST_BITMASK` 将停止生成该函数。建议用户使用双重取反（`!!mask`）来测试值是否为零。这影响例如 Boost.Filesystem 中定义的枚举。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 修复 Cygwin 上的编译与导出。非常感谢 [Luohao Wang](https://github.com/Luohaothu) 提交的 PR！

  - 修复 FreeBSD 上的构建。感谢 [ash](https://github.com/agokhale) 的缺陷报告！

  - 新增与预处理选项对应的 `BOOST_DLL_USE_STD_FS` CMake 选项。感谢 [Yury Bura](https://github.com/yurybura) 提交的 PR！

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - 修复 `path::append` 中关于比较可能不相关对象指针的 ASAN 警告。（[\#335](https://github.com/boostorg/filesystem/issues/335)）

- [Geometry](/libs/geometry/)（几何算法库）：

  - 重大改进

    - [PR#1369](https://github.com/boostorg/geometry/pull/1369) 重写遍历（traversal）

    - [PR#1402](https://github.com/boostorg/geometry/pull/1402) 新增多面体曲面（polyhedral surface）几何

  - 功能增强

    - [PR#1404](https://github.com/boostorg/geometry/pull/1404) buffer（缓冲区）操作的性能改进

    - [PR#1405](https://github.com/boostorg/geometry/pull/1405) 避免头文件中的静态变量与函数

  - 破坏性变更

    - [PR#1401](https://github.com/boostorg/geometry/pull/1401) 移除已弃用的头文件

  - 已解决问题

    - [\#1221](https://github.com/boostorg/geometry/issues/1221) 整数坐标的直角（rectilinear）多边集合做差集时产生内部不连通的无效多边形

    - [\#1295](https://github.com/boostorg/geometry/issues/1295) 求交结果错误（结果多边形等于输入中最大的多边形）

    - [\#1349](https://github.com/boostorg/geometry/issues/1349) 多边形差集给出错误结果

    - [\#1382](https://github.com/boostorg/geometry/issues/1382) 缓冲区操作产生自相交

    - 各类错误与警告的修复

- [Hash2](/libs/hash2/)（可扩展哈希算法库）：

  - 新增 Blake2 算法（`blake2s_256`、`blake2b_512`）。

  - 新增 XXH3 算法（`xxh3_128`）。

- [Iterator](/libs/iterator/)（迭代器构建设施库）：

  - 修复 `filter_iterator` 的拷贝/转换构造函数，此前它可能产生无效迭代器。（[\#92](https://github.com/boostorg/iterator/issues/92)）

  - 移除 `iterator_facade` 中对 `is_trivial` 的使用，因为 C++26 已弃用它。（[\#93](https://github.com/boostorg/iterator/issues/93)）

  - `iterator_facade::operator[]` 现在总是返回代理（proxy），而不再有条件地返回值或代理。这使用户能够把引用绑定到该运算符的结果，无论值类型是否可平凡拷贝（trivially-copyable）。（[\#61](https://github.com/boostorg/iterator/issues/61)）

  - `iterator_facade::operator[]` 返回的代理现在支持把解引用运算符转发给被引用的值。这使得 `it[n]->foo()` 与 `(*it[n]).foo()` 表达式可以编译。

  - `iterator_facade::operator[]` 返回的代理在其赋值运算符中实现了完美转发（perfect forwarding）。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 全面改版文档。

  - 同时是范围的 optional（可空值）被归类为 optional。

  - 带基类的类型现在启用"被描述类"（described class）支持。

- [Log](/libs/log/)（日志库）：

  - 新增对 `BOOST_LOG_WITHOUT_ASIO` 配置宏的支持，可用于移除对 Boost.Asio 的依赖并禁用相关功能。

  - 在 `text_file_backend` 中组合日志文件名时，对文件计数器使用与 locale 无关的格式。这修复了 `file_collector::scan_for_files` 后续解析文件名失败的问题。（[PR#246](https://github.com/boostorg/log/pull/246)）

  - 新增 `wrap_filter` 实用工具，简化在过滤表达式中注入用户自定义函数对象的操作。（[\#195](https://github.com/boostorg/log/issues/195)）

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - 在构建中显式要求 C++14 的 `<type_traits>` 与 `constexpr`。

  - 汇集了多个平台上 GPU 支持的修复。

  - 修复 x = 0 时的下不完全伽马函数。

  - 修复 jSO 算法中的外部存档（external archive）错误。

  - 修复 ibeta 中的数值下溢。

  - 修复 a 与 b 取大值时的 ibeta 反函数。

  - 修复可变参数函数，使其在 C++26 下安全。

- [MQTT5](/libs/mqtt5/)（MQTT 5.0 客户端库）：

  - 修复 broker（服务器）列表中 URI 路径解析不正确的问题（[\#31](https://github.com/boostorg/mqtt5/issues/31)）。

  - 默认最大包大小（Maximum Packet Size）现在显式设置在 `CONNECT` 包中（[\#33](https://github.com/boostorg/mqtt5/issues/33)）。

  - 修复最大包大小取大值时 CPU 占用过高的缺陷（[\#33](https://github.com/boostorg/mqtt5/issues/33)）。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - **重大更新。**

  - 新增后端类型：`cpp_double_fp_backend`。

  - 修复与 Boost.Serialization 的命名空间冲突。

- [MySQL](/libs/mysql/)（MySQL 客户端库）：

  - `caching_sha2_password` 认证插件现在可以在没有 TLS 的情况下使用。这是 MySQL 8 及以上的默认行为。尝试在明文连接上使用该插件时不再以 `client_errc::auth_plugin_requires_ssl` 失败（[\#313](https://github.com/boostorg/mysql/issues/313)）。

  - 修复当目标数据库不存在且使用 `caching_sha2_password` 时，连接建立期间返回 `client_errc::incomplete_message` 的问题。现在返回适当的服务器端诊断。参见 issue [\#468](https://github.com/boostorg/mysql/issues/468) 与 [\#488](https://github.com/boostorg/mysql/issues/488)。

  - 握手算法现在对协议违规更具弹性（[\#469](https://github.com/boostorg/mysql/issues/469)）。

  - 修复因缺失 include 导致的 gcc-15 构建失败（[PR#475](https://github.com/boostorg/mysql/pull/475)）。感谢 [hhoffstaette](https://github.com/hhoffstaette) 提交的 PR。

  - 新增[与官方驱动程序对比的基准测试](https://www.boost.org/doc/libs/master/libs/mysql/doc/html/mysql/benchmarks.html)。

  - 优化 `metadata` 表示，使其构造更快、占用内存更少（[\#461](https://github.com/boostorg/mysql/issues/461)）。

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - 按照新的 Boost 推荐做法重写 C++20 模块。更多信息见文档。

  - 修复现代 clang 编译器上的 C++26 编译。感谢 [Valery Mironov](https://github.com/MBkkt) 的报告！

  - 支持"零长度数组"（Arrays of Length Zero）编译器扩展的类型。

  - 修复错别字。感谢 [Egor](https://github.com/TryKuhn) 指出这些问题！

  - 让 `boost::pfr::names_as_array(empty_struct{})` 返回 `std::array<std::string_view, 0>` 类型，以允许编译 `for (std::string_view name : boost::pfr::names_as_array(empty_struct{}))`。非常感谢 [sabudilovskiy](https://github.com/sabudilovskiy) 的缺陷报告！

- [process](/libs/process/)（进程管理库）：

  - 新增 `v1.hpp` 以模拟 v1 的 `process.hpp` include。

  - 修复 Windows 路径转义。

  - 修复退出码问题：terminate 与 async_wait 组合曾导致退出码值丢失。

- [Random](/libs/random/)（随机数生成器与分布库）：

  - 修复 `beta_distribution` 生成 NAN 的问题。

  - 提升 `beta_distribution::operator()` 的性能。

- [System](/libs/system/)（错误码与 system_error 库）：

  - 已移除桩（stub）需编译库；System 自 1.69 发布以来就是仅头文件库。

  - 这可能影响包含 `find_package(Boost COMPONENTS system ...)` 的 `CMakeLists.txt` 文件。最简单的修复是把 `system` 从组件列表中删掉，因为它已不再必要。若要保持与 1.69 之前 Boost 发布的兼容，可使用 `find_package(Boost COMPONENTS ... OPTIONAL_COMPONENTS system)`。

- [TypeIndex](/libs/type_index/)（运行时类型索引库）：

  - **初步支持 C++20 模块（C++20 Modules）**。更多信息见文档。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - 已弃用的 `boost::unordered::hash_is_avalanching` 现在是 `<boost/container_hash/hash_is_avalanching.hpp>` 中 `boost::hash_is_avalanching` 的 using 声明。请直接改用该头文件。`<boost/unordered/hash_traits.hpp>` 将来会被移除。

  - 为开放定址（open-addressing）容器新增 `pull(const_iterator)`。该操作可通过移动构造高效地移除并取回元素。

- [Histogram](/libs/histogram/)（多维直方图库）：

  - 更新 CMake 最低版本要求与 CMake 中的 Python 检测。

  - 改进文档

    - 新增示例：如何创建接受多种不可隐式转换值类型的轴

    - 展示当每个维度的数据已作为连续数据可用时，如何高效地将 `histogram::fill` 用于多维直方图

  - 不再使用已弃用的用户自定义字面量（user-defined literal）运算符形式。

  - 新增通过 b2 的模块化构建结构支持。

  - 修复 MSVC 中关于类型收窄的警告。

  - 新增 collector 累加器，可存储一个箱（bin）内的所有值。

  - 测试与 detail 命名空间中类的内部变更。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)（b2 构建系统框架）：

  - 包含 [B2 版本 5.3.2](/tools/build/doc/html/#_version_5_3_2) 的发布。

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

本次发布由 Marshall Clow、Glen Fernandes 与 Ion Gaztañaga 管理。

Copyright Rene Rivera 2006-2007.
