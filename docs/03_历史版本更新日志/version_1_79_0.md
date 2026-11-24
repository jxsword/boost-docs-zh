# Boost 1.79.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_79_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_79_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2022-04-13 14:22 GMT（原文日期行：April 13th, 2022 14:22 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.79.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 已知问题（Known Issues）

以下补丁由库作者提供，因发现时间过晚而未能纳入本次发布修复。

- Boost.JSON（JSON 解析与序列化库）的 `array::erase` 可能发生段错误（segfault），参见 [\#692](https://github.com/boostorg/json/issues/692)。[补丁](/patches/1_79_0/0001-json-array-erase-relocate.patch)。

## 新增库（New Libraries）

本版无新增库。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 新增 `bind_allocator`。

  - 新增 `file_base::sync_all_on_write` 标志。

  - 补充缺失的 `basic_file::release()` 实现。

  - 为信号集（signal sets）新增按操作取消（per-operation cancellation）支持。

  - 将 `recycling_allocator` 作为公共接口的一部分公开。

  - 为若干函数添加 `nodiscard` 属性。

  - 新增 OpenSSL 3.0 兼容性。

  - 新增支持将既有 `SSL*` 接管（adopt）进 `ssl::stream<>`。

  - 在所有构建配置中启用 `executor_work_guard<>`。

  - 在使用 clang 时启用可移动的套接字 iostream。

  - 修复 `bind_cancellation_slot` 与 `bind_executor` 同旧式完成标记（completion token）的兼容性。

  - 修复 `experimental::append` 与 `experimental::prepend` 的 `associator` 特化。

  - 修复 `associated_allocator` 主模板。

  - 修复套接字 `async_receive_from` 与文件 `write_some_at` 的 `io_uring` 实现。

  - 修复 `io_uring` 特性检测。

  - 修复 `experimental::coro` 的按操作取消。

  - 修复 `experimental::promise` 的类型擦除完成处理程序中的内存管理。

  - 修复 `ssl::stream` 的移动 `operator=` 实现。

  - 修复 `any_io_executor` 实现，使其在同时定义 `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT` 与 `BOOST_ASIO_SEPARATE_COMPILATION` 时也能正常工作。

  - 修复使用 `sockatmark()` 系统调用时 `basic_socket::at_mark()` 的实现。

  - 更改回收分配器（recycling allocator），使其以默认对齐作为分配的最小对齐。

  - 针对 Apple clang 明显存在的协程代码生成（codegen）缺陷增加了变通方案。

  - 在 Windows 上，更改文件支持，使其以与 `fopen()` 相同的共享模式打开文件。

  - 在 Linux 上，修复 UNIX 域套接字实现以正确处理 `EAGAIN`。

  - 修复 `experimental::basic_channel::reset()` 与 `experimental::basic_concurrent_channel::reset()` 的实现。

  - 修复 `experimental::promise` 中潜在的未定义行为。

  - 更改 `co_spawn` 实现，使其在某些情形下经由执行器（executor）分发取消信号。

  - 修复了多处头文件包含问题。

  - 修复了多种警告。

  - 多项文档增强，包括：

    - 新增 Asio 异步模型概述。

    - 以异步模型为主线重写了参考与要求文档。

    - 更新了 `dispatch()`、`post()` 与 `defer()` 的文档。

    - 补充了串口按操作取消的文档。

    - 澄清了分配器所作的非并发保证。

    - 将 `io_context` 参考文档回退为使用 `executor_work_guard`。

    - 为 `make_strand()`、`make_work_guard()`、`ip::address_v4`、`ip::address_v6`、`experimental::basic_channel` 与 `experimental::basic_concurrent_channel` 添加了更详细的参考文档。

    - 重新编排并扩展了概述（Overview）文档，以覆盖近期新增的特性。

  - 新增展示经由本地套接字传递文件描述符的 C++11 示例。

  - 新增以异步操作封装基于回调的 API 的 C++14 示例。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_79_0/doc/html/boost_asio/history.html)。

- [Assert](/libs/assert/)（可定制断言宏库）：

  - `source_location().file_name()` 与 `source_location().function_name()` 现在返回 `""` 而非 `"(unknown)"`。

  - 新增从 `std::source_location` 构造 `source_location` 的构造函数。

  - 更改 `BOOST_CURRENT_LOCATION`，使其行为更贴近 `std::source_location::current()`，例如可在顶层使用或作为函数默认实参使用。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 修复面向通用 Windows 平台（UWP）的编译。（[\#54](https://github.com/boostorg/atomic/issues/54)）

  - 新增 `BOOST_ATOMIC_NO_DARWIN_ULOCK` 配置宏。该宏影响 Darwin 系统上的编译，禁用基于 `ulock` 的等待与通知操作实现。这有助于满足 Apple App Store 的要求。（[\#55](https://github.com/boostorg/atomic/issues/55)）

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 补充 file_body 测试缺失的头文件包含。

  - 修复失败情形下的 WebSocket 握手响应。

  - 修复 `file_posix` 与 `file_win32` 的追加（append）打开模式。

  - 修复 Windows 上以 append/append_existing 标志打开文件的问题。

  - 修复 clang-cl 下 `file_win32` 与 `file_stdio` 的 UTF-8 路径处理。

  - 在 drone CI 中新增 ARM64 构建。

  - 修复 async_base 文档链接。

  - 新增以 append/append_existing 模式打开文件的测试。

  - 更新 CI 以纳入 gcc 11、clang 12、msvc 14.3。

  - 在 CMake 工作流中新增独立测试。

  - 我们很想知道您或您的公司如何使用 Beast，欢迎在[使用 Beast 的公司与个人（Companies and Individuals Using Beast）](https://github.com/boostorg/beast/wiki/Companies-and-Individuals-Using-Beast)列表中添加条目。

  - 完整变更清单请参见[发布说明（Release Notes）](/libs/beast/doc/html/beast/release_notes.html)。

- [Core](/libs/core/)（核心工具集库）：

  - 使 `boost::pointer_traits` 对 SFINAE 友好，解决 LWG3545。（Glen Fernandes）

  - 新增 `boost::allocator_traits`，其使用各独立的分配器访问特征（traits）。该实现支持 C++03 及以上。（Glen Fernandes）

  - 更新分配器访问特征，使其在 C++03 下支持 C++11 分配器模型的大部分内容。（Glen Fernandes）

  - `boost/iterator.hpp` 已弃用，将在未来发布中移除。该头文件定义的 `boost::iterator` 模板等价于 `<iterator>` 头文件中的 `std::iterator`。但由于 `std::iterator` 本身在 C++17 中已被弃用，建议用户从代码中移除 `boost::iterator` 或 `std::iterator` 的使用。

  - 新增 `boost::core::verbose_terminate_handler`：一个供传给 `std::set_terminate` 的工具函数，会将未捕获异常的信息打印到 `stderr`。

- [Describe](/libs/describe/)（枚举/结构体成员描述宏库）：

  - 在 `BOOST_DESCRIBE_STRUCT` 中启用对联合（union）的支持，并更新示例以检查 `std::is_union<T>`。

  - 新增定义 `fmtlib` 类格式化器（formatter）的示例。

  - 新增定义 `fmtlib` 枚举格式化器的示例。

  - 新增打印成员指针的示例。

- [Filesystem](/libs/filesystem/)：

  - **v3：** `path::replace_extension` 现在依据 **v3** 的 `path::extension` 定义而非 **v4** 的定义工作。

  - 修复路径追加（appending）与拼接（concatenation）运算符在实参类型可转换为 `path` 或为兼容字符串类型时的编译问题。（[\#223](https://github.com/boostorg/filesystem/issues/223)）

  - 在支持 `fdopendir` 与 `O_NOFOLLOW` 的 POSIX 系统上以及 Windows 上，`remove_all` 现已针对 [CVE-2022-21658](https://www.cve.org/CVERecord?id=CVE-2022-21658) 提供防护。该漏洞是一个竞态条件：第三方进程可将 `remove_all` 正在并发处理的目录替换为目录符号链接，诱使 `remove_all` 跟随该符号链接删除链接目录中的文件，而不是移除符号链接本身。（[\#224](https://github.com/boostorg/filesystem/issues/224)）

  - 在 Windows 上，当操作系统支持时（Windows 10 1709 及更高版本），`remove` 与 `remove_all` 的实现改用 POSIX 语义删除文件。在支持 POSIX 语义时，文件一经标记删除，其文件名即从文件系统命名空间中移除，即使文件仍处于打开与使用状态。在传统 Windows 语义下，文件名会一直保留在文件系统命名空间中，直到指向该文件的最后一个文件句柄关闭；这导致已标记删除的文件仍可被打开，且无法创建同名新文件。（[\#216](https://github.com/boostorg/filesystem/issues/216)）

  - 在 Windows 上，`remove` 与 `remove_all` 现在支持删除只读目录。删除只读非目录文件的支持此前已添加。

  - 在 Windows 上，`directory_iterator` 的内部实现经过重构，以更好地利用现代 Windows API，在处理符号链接时可能提升性能。

  - 在 Windows 上，尽可能提前初始化内部 WinAPI 函数指针，使 Boost.Filesystem 操作可以在全局构造函数中被调用。该特性仅在 MSVC、GCC、Clang 及兼容编译器上受支持。

  - 在 Windows 上，当待调整大小的文件已被打开时，`resize_file` 应不再报错失败。

  - 在 Android 11.0（API 级别 30）之前的版本上禁用 `statx` 系统调用。该系统调用被 seccomp 列入黑名单，会在运行期导致进程终止。（[\#229](https://github.com/boostorg/filesystem/issues/229)）

  - **弃用：** `boost/filesystem/string_file.hpp` 头文件已弃用，将在未来发布中移除。`boost/filesystem.hpp` 默认不再包含该头文件。建议用户自行实现相关功能或迁移到其他实现。

  - **弃用：** Windows CE 支持已弃用，将在未来发布中移除。Windows CE 已多年未测试，很可能已无法工作。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 重大变更：

    - [PR#977](https://github.com/boostorg/geometry/pull/977) 默认关闭重缩放（rescaling）。这避免了集合运算与 buffer（缓冲区）中的许多相关缺陷。

  - 功能增强：

    - [PR#923](https://github.com/boostorg/geometry/pull/923) 为笛卡尔坐标系下的点/几何对象新增 closest_points 算法。

    - [PR#939](https://github.com/boostorg/geometry/pull/939) 为其他坐标系与几何对象组合（不含 box）新增 closest_points 算法。

    - [PR#961](https://github.com/boostorg/geometry/pull/961) 新增 Web Mercator（网络墨卡托）投影。

    - [PR#966](https://github.com/boostorg/geometry/pull/966) simplify 中改用更高效的笛卡尔距离策略。

  - 已解决问题：

    - [\#956](https://github.com/boostorg/geometry/issues/956) simplify 算法在闭合性（closure）不正确时的结果问题。

    - [\#962](https://github.com/boostorg/geometry/issues/962) R-tree 反序列化时因加载因子（load factor）导致的运行期错误。

    - [\#971](https://github.com/boostorg/geometry/issues/971) ARM 平台上因使用 long double 影响 R-tree 插入耗时。

  - 缺陷修复：

    - [PR#936](https://github.com/boostorg/geometry/pull/936) 修复包含极点（pole）的多边形的包络（envelope）计算。

    - [PR#948](https://github.com/boostorg/geometry/pull/948) 修复接近子午线的线段的球面与地理包络。

    - [PR#974](https://github.com/boostorg/geometry/pull/974) 修复针对 NaN 坐标的椭球归一化（spheroidal normalization）工具。

    - 集合运算与 buffer 中的多项修复。

- [Integer](/libs/integer/)（整数类型选择库）：

  - 优化 `integer_log2` 实现，内部改用位运算。这样可以利用大多数现代 CPU 提供的位指令。（[\#31](https://github.com/boostorg/integer/issues/31)）

- [IO](/libs/io/)（I/O 辅助设施库）：

  - 新增空流缓冲区 `boost::io::basic_nullbuf` 与空输出流 `boost::basic_onullstream`（Glen Fernandes）。

- [Iterator](/libs/iterator/)：

  - 在 `counting_iterator` 中，新增对 gcc、clang 及兼容编译器在部分目标平台上支持的内置 128 位整数类型的支持。

  - 消除 gcc 关于 `counting_iterator` 中已弃用隐式拷贝赋值运算符的警告。

- [JSON](/libs/json/)：

  - 本库的独立（standalone）使用模式已移除。希望继续使用独立版 JSON 的用户可切换至 [C++ Alliance fork](https://github.com/CPPAlliance/standalone-json.git)。

  - 新增 `std::error_code` 重载。

  - 为 `error_code` 添加 `boost::source_location`（源位置）支持。

  - 新增对 JSON Pointer 的支持。

  - 序列化期间字符串自然增长（按需扩容）。

- [LEAF](/libs/leaf/)：

  - 支持 FreeRTOS（嵌入式实时操作系统）及其他嵌入式平台。

  - 改进诊断信息。

  - 改进配置宏。

  - 在 `__GNUC__` 下 `BOOST_LEAF_CHECK` 使用语句表达式（statement expressions）。

  - 修复符号 demangling（名称还原）缺陷。

- [Log](/libs/log/)：

  - 总体变更：

    - 在 `text_file_backend` 中，新增支持在启用文件轮转（file rotation）且日志文件名使用文件计数器时，向先前写入的日志文件追加。

    - **破坏性变更：** `file_collector` 接口已变更：

      - `scan_for_files` 方法返回一个 `scan_result` 结构，其中包含扫描期间收集的信息；

      - 新增 `is_in_storage` 方法，用于测试路径是否指向目标存储目录内的文件。

    - 新增 `invoke_manip` 流操纵器（stream manipulator），可用于将用户的函数注入流输出表达式。

  - 缺陷修复：

    - 修复用户多次调用 `text_file_backend::scan_for_files` 时，第二次及后续调用未发现任何新文件会导致文件计数器被置零的问题。（[\#179](https://github.com/boostorg/log/issues/179)）

  - 更多细节请参见[变更日志（changelog）](/libs/log/doc/html/log/changelog.html)。

- [Multi-index Containers](/libs/multi_index/)：

  - 将排序索引（ranked indices）中 `count` 操作的效率从 `O(log(n) + count)` 提升至 `O(log(n))`。由 Damian Sawicki 贡献。

  - 维护性工作。

- [Nowide](/libs/nowide/)：

  - 修复某些平台上的编译问题（例如 MinGW-w64 与 Cygwin 上的 GCC 11）。

  - 修复使用 `BOOST_USE_WINDOWS_H` 与 `WIN32_LEAN_AND_MEAN` 时缺少头文件包含的问题。

  - 在同时使用 `boost::nowide::stat` 与 `boost::nowide::stat_t` 时新增健全性检查。

- [Optional](/libs/optional/)：

  - 修复 [issue \#98](https://github.com/boostorg/optional/issues/98)。

  - 修复 [issue \#92](https://github.com/boostorg/optional/issues/92)。

  - 新增对 `BOOST_NO_IOSTREAM` 的支持。

  - 对齐存储（aligned storage）现在使用 `unsigned char` 而非 `char`，以避免未定义行为（UB）。

  - 定位 new（placement new）现在使用 cv 限定符未修饰的 `value_type`，以避免未定义行为（UB）。

- [Predef](/libs/predef/)（编译器/架构/OS 预定义宏库）：

  - 版本 1.14.0。

  - 新增对 LoongArch（龙芯架构）的检测（来自 Zhang Na）。

- [QVM](/libs/qvm/)（二维/三维/四维向量与矩阵库）：

  - 在 C++17 下新增 `constexpr` 支持。

  - 改进单头文件分发版本。

- [Smart Pointers](/libs/smart_ptr/)（智能指针库）：

  - 新增 `boost::get_allocator_pointer`，用于从 `boost::allocate_unique` 的结果中获取分配器（Allocator）指针（Glen Fernandes）。

- [System](/libs/system/)：

  - 为 `throw_exception_from_error` 新增 `boost::source_location` 参数。

  - 为 `errc::errc_t`、`std::error_code`、`std::errc`、`std::exception_ptr` 新增 `throw_exception_from_error` 重载。

  - `result<T>::value` 现在通过默认实参自动向 `throw_exception_from_error` 提供 `BOOST_CURRENT_LOCATION`。

  - 新增接受源位置（source location）的 `errc::make_error_code` 重载。

- [ThrowException](/libs/throw_exception/)（统一异常抛出设施库）：

  - 新增 `boost::throw_with_location`：对不使用 Boost.Exception（增强异常库）的程序而言，它是比 `BOOST_THROW_EXCEPTION` 更轻量的替代方案。

- [Unordered](/libs/unordered/)：

  - 所有容器均已更新，支持异构（heterogeneous）的 `count`、`equal_range` 与 `find`。

  - 所有容器现在都实现了成员函数 `contains`。

  - 所有容器均已实现 `erase_if`。

  - 所有容器均已更新，支持异构的 `erase` 与 `extract`。

  - 更改 `reserve` 的行为为立即（eager）分配。

  - 测试套件中的多项警告修复。

  - 更新代码，内部改用 `boost::allocator_traits`。

  - 切换为斐波那契散列（Fibonacci hashing）。

  - 文档改用 AsciiDoc 文档格式编写，不再使用 QuickBook 文档格式。

- [Variant2](/libs/variant2/)（Variant 的现代重实现库）：

  - 为 `monostate` 新增 `operator<<`。

- [Wave](/libs/wave/)：

  - 构建 Wave 本身现在要求 C++11。

  - 修复的缺陷：

    - [\#135](https://github.com/boostorg/wave/issues/135)：数组下标中的逗号运算符在 C++20 中已被弃用。

    - [\#137](https://github.com/boostorg/wave/issues/137)：简单未知指令 => found_unknown_directive 未被调用，井号（pound）被剥离。

    - [\#138](https://github.com/boostorg/wave/issues/138)：空的 ifdef 块在缺少空白时未发出行（line）指令。

    - [\#143](https://github.com/boostorg/wave/issues/143)：解析 `__has_include()` 在存在尾随记号（token）时失败。

    - [\#145](https://github.com/boostorg/wave/issues/145)：sanitizer（净化器）对 reset_version() 发出告警。

    - [\#147](https://github.com/boostorg/wave/issues/147)：不同枚举类型之间的位运算已被弃用。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)：

  - 包含 [B2 version 4.8.2](/tools/build/doc/html/#_version_4_8_2) 的发布。

## 已测试的编译器（Compilers Tested）

Boost 的主要测试编译器如下：

- Linux：

  - Clang：3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 12.0.0

  - Clang，C++11：3.4, 11.0.0

  - Clang，C++14：3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 5.0, 12.0.0

  - Clang，C++17：6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0, 12.0.0

  - Clang，C++20：11.0.0, 12.0.0, 13.0.0

  - GCC：4.6.3, 11

  - GCC，C++11：4.7.3, 4.8.5, 11

  - GCC，C++14：5.4.0, 6.4.0, 7.3.0, 8.0.1, 9.1.0, 11

  - GCC，C++17：7.3.0, 8.0.1, 9.1.0, 11

  - GCC，C++20：8.0.1, 9.1.0, 10, 11

- OS X：

  - Apple Clang：11.0.3

  - Apple Clang，C++11：11.0.3

  - Apple Clang，C++14：11.0.3

  - Apple Clang，C++17：11.0.3

  - Apple Clang，C++20：11.0.3

- Windows：

  - Visual C++：10.0, 11.0, 12.0, 14.0, 14.1, 14.2

## 致谢（Acknowledgements）

本次发布由 Marshall Clow、Michael Caisse 与 Glen Fernandes 管理。
