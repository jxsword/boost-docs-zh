# Boost 1.76.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_76_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_76_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2021-04-16 21:05 GMT（原文日期行：April 16th, 2021 21:05 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.76.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 新增库（New Libraries）

- 无新增库（原文标注 "No new libraries"）。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 新增 `ip::scope_id_type` 类型别名。

  - 新增 `ip::port_type` 类型别名。

  - 为 IP 地址新增 `std::hash` 特化。

  - 为 `ip::basic_endpoint<>` 新增 `std::hash` 特化。

  - 重构了 SFINAE 的使用，以改进编译时间。

  - 为定制点（customisation points）添加友元支持，并将大多数定制设为私有。

  - 将 `any_io_executor` 改为"强 typedef"风格的类。

  - 修复 `experimental::as_single`，使其与处理程序钩子（handler hook）弃用机制兼容。

  - 确保在所有平台上清理 pthread 条件变量属性。

  - 澄清了关于套接字与描述符的线程安全说明。

  - 确保在 macOS/FreeBSD 上 `socket()` 失败时不覆盖 `errno`。

  - 修复 `io_context` 与 `thread_pool` 执行器在移动赋值时的工作跟踪问题。

  - 确保内部 `call_stack` 对象仅从实现文件中访问。

  - 修复 I/O 对象的移动赋值，确保执行器保持在有效状态。

  - 修复 MSVC 下对"函数默认模板实参"编译器支持的检测。

  - 禁止将 `blocking.always` 属性与 `strand<>` 一起使用，因为它不会产生正确的语义。

  - 移除了已弃用的文件 `asio/impl/src.cpp`。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 修复 MSVC ARM 平台上的编译（[PR#49](https://github.com/boostorg/atomic/pull/49)）。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 本次更新包含若干小的缺陷修复，并改进了 CI 报告。

  - 我们很想知道您或您的公司如何使用 Beast，欢迎在[使用 Beast 的公司与个人](https://github.com/boostorg/beast/wiki/Companies-and-Individuals-Using-Beast)（Companies and Individuals Using Beast）列表中添加条目。

  - 完整变更列表请参见完整的[发布说明](/libs/beast/doc/html/beast/release_notes.html)。

- [Bind](/libs/bind/)（参数绑定库）：

  - 新增支持在 `boost::bind` 中使用 C++11 标准占位符。

  - 更新 `boost::apply`，改用可变参数模板与完美转发。

- [Container](/libs/continer/)（扩展容器库）（译注：原文链接即如此，应为 /libs/container/）：

  - 为所有容器添加 \[\[no-discard\]\] 属性，以捕获与未使用返回值相关的缺陷。

  - 以 Boost.Container 自有的异常类替换默认使用的标准异常类，显著减少了所包含文件的开销。例如：在 MSVC 19 上，`boost/container/vector.hpp` 的预处理文件大小从 1.5MB 减至 930KB。如果您仍想使用标准异常类，可以在使用任何 Boost.Container 类之前定义 `BOOST_CONTAINER_USE_STD_EXCEPTIONS`。

  - 修复的缺陷/问题：

    - [GitHub \#102："*flat_map::insert 在初始化列表与需要转换的 pair 上存在歧义*"](https://github.com/boostorg/container/issues/102)。

    - [GitHub \#139："*flat_map merge 与迭代器*"](https://github.com/boostorg/container/issues/139)。

    - [GitHub \#141："*small_vector 未传播所含类型移动操作的 no throw 特性*"](https://github.com/boostorg/container/issues/141)。

    - [GitHub \#164："*使用 `pmr::map` 搭配 `std::pair` 时编译错误；改用 `std::tuple` 则正常*"](https://github.com/boostorg/container/issues/164)。

    - [GitHub \#171："*deque::clear() 使用了未定义行为*"](https://github.com/boostorg/container/issues/171)。

- [Core](/libs/core/)（核心工具集库）：

  - 新增兼容的引用包装器（reference wrapper）之间的隐式转换。

  - 新增 `boost/core/cmath.hpp`，是 `<cmath>` 中浮点分类函数的可移植实现。

  - 新增 `boost/core/bit.hpp`，是 C++20 标准头文件 `<bit>` 的可移植实现。

  - 修复 C++20 下字符类型的 `BOOST_TEST_EQ`、`BOOST_TEST_NE`。

  - 修订分配器访问工具（现已支持 VS2013，且各变通方案均不使用 `allocator_traits`）。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - **破坏性变更**：`boost::dll::import` 已更名为 `boost::dll::import_symbol`，以避免与 C++20 的 `import` 关键字冲突。

  - 更新了文档，包括 FAQ（常见问题）章节。

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - 更新了与 WASI（WebAssembly 系统接口）平台的兼容性（[PR#169](https://github.com/boostorg/filesystem/pull/169)）。

  - 修复当路径为 "////" 时 `path::remove_filename` 抛出异常的问题（[\#176](https://github.com/boostorg/filesystem/issues/176)）。

  - 修复 `create_directories` 忽略内部发出的文件状态查询操作错误的问题。这可能导致 `create_directories` 返回错误的错误码（[\#182](https://github.com/boostorg/filesystem/issues/182)）。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 功能增强：

    - [PR#670](https://github.com/boostorg/geometry/pull/670) 新增 `to_wkt()` 与 `from_wkt()` 这两个 I/O 函数（感谢 Baidyanath Kundu）。

    - [PR#756](https://github.com/boostorg/geometry/pull/756) 非笛卡尔且稳健的凸包（convex hulls）。

    - [PR#768](https://github.com/boostorg/geometry/pull/768) 为关系运算（relops）、集合运算（setops）、索引、缓冲区（buffer）等添加伞式策略（umbrella strategies）（暂未写入文档）。

    - [PR#797](https://github.com/boostorg/geometry/pull/797) 新增 `azimuth()` 算法。

    - [PR#801](https://github.com/boostorg/geometry/pull/801) 提高了地理面积计算的精度。

    - [PR#820](https://github.com/boostorg/geometry/pull/820) 为 svg_mapper 添加 scale 参数。

  - 缺陷修复：

    - [PR#808](https://github.com/boostorg/geometry/pull/808) 修复启用 rtree 序列化时的编译错误（感谢 Tristan Carel）。

    - [PR#815](https://github.com/boostorg/geometry/pull/815) 修复 `buffer()` 中的问题。

    - 集合运算与缓冲区方面的各类修复。

  - 破坏性变更：

    - 移除了 `convex_hull::graham_andrew` 策略。

- [GIL](/libs/gil/)（通用图像库）：

  - **破坏性变更预告**：在下一个发布中，我们将停止支持 GCC 5，同时把最低要求的 C++ 标准版本从 C++11 改为 C++14。

- [Histogram](/libs/histogram/)（多维直方图库）：

  - 本发布包含关键修复，请检查您的结果是否受到影响。

  - 详情参见[发布说明](/libs/histogram/doc/html/histogram/history.html)。

- [Intrusive](/libs/intrusive/)（侵入式容器库）：

  - 减少了编译期依赖：

    - `linear_slist_algorithms` 的返回值改用简单的 node_ptr 而非 `std::pair`。

    - `list`/`slist` 改用 `operator <`/`operator ==` 而非 `std::equal_to`/`std::less`。

  - 修复 [GitHub \#54："*set.rbegin() 复杂度看似为 O(log(N))*"](https://github.com/boostorg/intrusive/issues/54)

- [Interprocess](/libs/interprocess/)（进程间通信库）：

  - 在提供原生宽字符 API 的操作系统（如 Windows）上，为命名资源新增 `wchar_t` API 支持。以下类已更新为支持 `wchar_t` 名称：

    - `file_mapping`

    - `managed_mapped_file`

    - `managed_shared_memory`

    - `managed_windows_shared_memory`

    - `shared_memory_object`

    - `windows_shared_memory_object`

    - `file_lock`

    - `named_condition`

    - `named_condition_any`

    - `named_mutex`

    - `named_recursive_mutex`

    - `named_semaphore`

    - `named_sharable_mutex`

    - `named_upgradable_mutex`

    - `message_queue`

  - 新增 `BOOST_INTERPROCESS_FORCE_NATIVE_EMULATION` 宏选项，用于禁用针对进程共享同步原语的通用仿真代码，改用原生 POSIX 或 WinAPI 函数。

  - 修复的缺陷：

    - [GitHub \#76（"*Cygwin 编译错误*"）](https://github.com/boostorg/interprocess/issues/76)。

    - [GitHub \#83（"*添加 BOOST_INTERPROCESS_FORCE_NATIVE_EMULATION 选项*"）](https://github.com/boostorg/interprocess/pull/83)。

    - [GitHub \#92（"*bufferstream：修正 MSVC 编译警告*"）](https://github.com/boostorg/interprocess/pull/92)。

    - [GitHub \#106（"*在 truncate_file 上使用 fallocate*"）](https://github.com/boostorg/interprocess/pull/106)。

    - [GitHub \#120（"*segment_manager 定制化*"）](https://github.com/boostorg/interprocess/issues/120)。

    - [GitHub \#122（"*尽可能将构造函数/赋值/swap 标记为 noexcept*"）](https://github.com/boostorg/interprocess/issues/122)。

    - [GitHub \#126（"*使用 clang-cl.exe 编译时出现 \_ReadWriteBarrier 已弃用警告*"）](https://github.com/boostorg/interprocess/issues/126)。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 来自 Bishop Fox 的[安全评估报告](https://cppalliance.org/pdf/C%20Plus%20Plus%20Alliance%20-%20Boost%20JSON%20Security%20Assessment%202020%20-%20Assessment%20Report%20-%2020210317.pdf)。

  - （[\#481](https://github.com/boostorg/json/issues/481)）重构了 `value_from` 的实现；用户定制现在总是优先于库提供的重载。

  - （[\#484](https://github.com/boostorg/json/issues/484)）修复部分浮点数解析不精确的问题。

  - （[\#485](https://github.com/boostorg/json/issues/485)）修复独立（standalone）模式下与 Boost 一同使用时的链接错误。

  - （[\#497](https://github.com/boostorg/json/issues/497)）修复 GCC 4.8 上的 Boost.Build 构建。

- [LexicalCast](/libs/lexical_cast/)（字符串↔数值等类型转换库）：

  - 移除了对 Boost.Math 的依赖（感谢 Peter Dimov，[\#37](https://github.com/boostorg/lexical_cast/issues/37)、[\#39](https://github.com/boostorg/lexical_cast/issues/39)）。

  - 改进了 CI 与覆盖率（感谢"The C++ Alliance"的 Sam Darwin，[\#38](https://github.com/boostorg/lexical_cast/issues/38)、[\#42](https://github.com/boostorg/lexical_cast/issues/42)）。

- [Log](/libs/log/)（日志库）：

  - 缺陷修复：

    - 修正 `asynchronous_sink` 前端 `unbounded_fifo_queue` 策略所用线程安全日志记录队列实现中的一处形式上的竞态条件。该竞态可被 TSAN 检出，但在当前大多数 CPU 架构与编译器上并非真实问题（[\#139](https://github.com/boostorg/log/issues/139)）。

    - 复制带 channel 属性的日志器（如 `channel_logger`）时，channel 属性现在会从原日志器深拷贝。这意味着修改新日志器中的 channel 不再影响原日志器。

    - 在模板参数中以新标签类型 `boost::log::use_std_allocator` 取代 `std::allocator<void>` 的使用，以消除 libc++ 关于前者在 C++17 及更高标准中被弃用的警告。该标签表明所实例化的模板内部应使用 `std::allocator` 的特化来分配动态内存，因此此变更没有功能性影响（[\#141](https://github.com/boostorg/log/issues/141)）。

    - Boost.Log 不再在 MinGW 与 MinGW-w64 上定义 `__MSVCRT_VERSION__` 宏。定义该宏会导致与 UCRT 不兼容，而 UCRT 在近期的 MinGW-w64 中已作为可选项提供（[PR#149](https://github.com/boostorg/log/pull/149)）。

  - 更多细节参见[变更日志](/libs/log/doc/html/log/changelog.html)。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - **破坏性变更**：现已移除对 C++03 的支持，使用本库现在需要符合 C++11 或更高标准的编译器。

  - 新增 Z 检验（Z-test）。

  - 为单变量与双变量统计新增执行策略（execution policy）支持：可启用并行执行（需要 C++17 与 `<execution>`）。

  - CI 测试的大幅更新/改进。

  - 双变量统计现已支持整数。

  - T 检验（T-Test）现已支持整数。

  - 线性回归现已支持整数。

  - 修正 beta 分布在端点处的概率密度函数（PDF）。

  - 修正某些多精度情形下 Stirling 近似的使用，修复 [\#396](https://github.com/boostorg/math/issues/396)。

  - 消除 clang 上的 -Wimplicit-int-float-conversion 警告。

  - 修复四元数/八元数中的若干 constexpr 问题。

  - 对 tanh_sinh 积分的小幅性能修复。

  - 更新超几何函数的内部缩放，以允许在多精度类型上使用 64 位（long long）指数。

- [Move](/libs/move/)（移动语义/emplace 辅助库）：

  - [Git Issue \#35："*新的 nothrow move 特征（traits）不完整*"](https://github.com/boostorg/move/issues/35)。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - **破坏性变更**：大规模重构与代码简化使 C++11 成为绝对要求。

  - 在头文件中使用 BOOST_TRY/CATCH，使代码可用于无异常环境。

  - 修正 pow 中的边界情形，修复 [\#277](https://github.com/boostorg/multiprecision/issues/277)。

  - 修正 lsb/msb 抛出的异常类型以与文档一致：修复 [\#257](https://github.com/boostorg/multiprecision/issues/257)。

  - 允许相关但不同类型（即使用相同分配器的类型）之间的移动与运算符操作，修复 [\#278](https://github.com/boostorg/multiprecision/issues/278)。

- [Nowide](/libs/nowide/)（Windows 下 UTF-8 标准 I/O 适配库）：

  - 修复文本文件流在使用 seek 或 sync 函数且换行符已被转换（如在 Windows 上）时丢弃字符的问题

  - 修复通过 `open` 复用已关闭文件流时潜在的释放后使用（use-after-free）缺陷

  - 修复使用已被移动或交换过的文件流时潜在的无效内存访问（当源流存在回退字符或被设为无缓冲模式时）

  - 通过不定义 `__MSVCRT_VERSION__` 修复与 UCRT 运行时的兼容性

  - 已知问题：文本文件的读取性能有所下降。二进制文件与写入不受影响。

- [Optional](/libs/optional/)（可选值容器库）：

  - 修复 MSVC C4702 警告。

- [Outcome](/libs/outcome/)（轻量级错误处理（result/outcome）库）：

  - 公告：

    - **破坏性变更**：在历时一年、历经三个主要的 Boost 发布预告这一即将到来的变更之后，本发布是 v2.2 分支的首次发布。相对于随 Boost 1.75 及更早版本发布的 Outcome v2.1，该分支包含多项重大破坏性变更，详情参见文档。

  - 功能增强：

    - VS2019.8 更改了启用协程（coroutine）的方式，导致 Outcome 无法在该编译器上编译。

    - 在 C++20 下，现在使用 C++20 的 `[[likely]]` 取代编译器特定标记，来指示 TRY 何时可能成功或失败。

    - **破坏性变更**：此前 `spare_storage(const basic_result|basic_outcome *) noexcept` 的值不会经 `BOOST_OUTCOME_TRY` 传播，导致在构造出错结果时捕获的堆栈回溯等信息在每个 `TRY` 点被丢弃。现通过为 `success_type<T>` 与 `failure_type<T>`，以及 `auto success(T &&, ...)` 与 `auto failure(T &&, ...)` 增加可选的 `spare_storage` 修复了此问题。

  - 缺陷修复：

    - 定义 `BOOST_NO_EXCEPTIONS` 后 Boost.Outcome 现在应能编译。感谢 Boost.Exception 的维护者 Emil 为我所作的修改，Boost.Outcome 现在可以在全局禁用 C++ 异常的情况下编译。但由于全局禁用异常时无法包含 `boost::exception_ptr`，您将无法使用它。

    - **破坏性变更**（[\#244](https://github.com/ned14/outcome/issues/244)）：令人震惊的是，`BOOST_OUTCOME_TRY` 自本库诞生以来在某些边界情形代码上一直是坏的，这需要对 TRY 的工作方式作出破坏性变更。更多细节参见[文档中的变更日志](https://boostorg.github.io/outcome/changelog.html)。

- [Parameter](/libs/parameter/)（函数命名参数库）：

  - 新增变通方案，修复 MSVC 2015 在将右值用作函数命名参数默认值时的错误编译（[PR#109](https://github.com/boostorg/parameter/pull/109)、[\#132](https://github.com/boostorg/log/issues/132)（译注：原文即如此，该链接指向 boostorg/log 仓库，疑为误链））。

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - 修复模板构造函数中 SFINAE 表达式缺失 `const` 的类型反射问题。现在，即使 LWG3050 未被修复，含有 `std::optional<std::chrono::duration<???>>` 字段的聚合类型反射也能在任意标准库实现上工作。

  - 比较函数现在为 `constexpr`（[\#52](https://github.com/boostorg/pfr/issues/52)）

  - 修复文档中大量拼写错误（感谢 Phil Miller，[\#63](https://github.com/boostorg/pfr/issues/63)）

- [PolyCollection](/libs/poly_collection/)（多态集合库）：

  - 针对影响 GCC 9.3-10.2 版本的 [GCC 缺陷](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=95888)实施了变通处理（issue [\#20](https://github.com/boostorg/poly_collection/issues/20)）。

- [Predef](/libs/predef/)（编译器/架构/OS 预定义宏库）：

  - 版本 1.13

  - 新增 `ARCH_PPC_64` 预定义宏。

  - 修复 `ARCH_WORD_BITS*` 的重定义警告/错误。

  - 新增 `ARCH_E2K`（Elbrus 2000）架构（由 Konstantin Ivlev 提供）。

  - 修复未处理高于 10.x 的近期 C++ 版本的问题。

  - 版本 1.12

  - 在 OpenBSD 上改用 endian.h 头文件。（Brad Smith）

  - 修复未处理版本号高于 9 的近期 stdcxx 的问题。

  - 修复直接包含 sub-BSD 操作系统头文件引发重定义警告的问题。

  - 新增对所有头文件直接包含的 CI 测试。

  - 新增 FreeBSD 上 clang 与 gcc 的 CI 测试。

  - 新增 `WORD_BITS` 系列预定义宏，用于检测架构字长。初始实现受 Mikhail Komarov 提交内容的启发。

  - 新增 Cygwin 32 与 64 位的 CI 测试。

- [PropertyTree](/libs/property_tree/)（属性树库）：

  - Property Tree 有了新的维护者。

  - 修复对已弃用 Boost.Bind 特性的使用。

  - 修复指向 Wikipedia 的链接。

  - 使用 BOOST_OVERRIDE 修复 GCC 警告。

  - 新增大范围的 CI 测试。

- [Regex](/libs/regex/)（正则表达式库）：

  - Regex 现在除 C++03 模式外均为仅头文件库。

  - 对 C++03 的支持现已弃用。

  - 本库现在可以在没有其余 Boost 组件的情况下"独立"（standalone）使用。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 改进 clang 上 C++11 之前构建的支持（[\#102](https://github.com/boostorg/stacktrace/issues/102)）。

  - 对"**不要在信号处理函数中使用 boost::stacktrace::stacktrace**"给出更醒目的警告（[\#71](https://github.com/boostorg/stacktrace/issues/71)）。

- [TypeTraits](/libs/type_traits/)（类型特征库）：

  - 修复 Visual Studio 托管代码项目的问题。

- [Variant2](/libs/variant2/)（Variant 的现代重实现库）：

  - 改进了双缓冲情形下生成的代码。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)（b2 构建系统框架）：

  - 包含 [B2 版本 4.4.1](/tools/build/doc/html/#_version_4_4_1) 的发布。

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
