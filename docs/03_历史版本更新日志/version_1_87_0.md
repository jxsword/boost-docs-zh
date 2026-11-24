# Boost 1.87.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_87_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_87_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2024-12-12 00:52 GMT（原文日期行：December 12th, 2024 00:52 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.87.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 新增库（New Libraries）

- [Parser](/libs/parser/)（解析器构建框架库）：用于构建解析器的框架，由 Zach Laine 开发。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 新增支持将字节 span（byte spans）与字节 span 序列用作缓冲区序列（buffer sequences）。这意味着它们可以直接传给 `async_read` 等 I/O 操作。

  - 新增对通用处置（disposition）的支持。处置是可用于检验异步操作是否无错完成的类型，包括 `error_code` 与 `exception_ptr`，并可通过特化 `disposition_traits` 类模板扩展到用户类型。标准类型 `std::error_code` 与 `std::exception_ptr` 被识别为处置。

  - 为 `boost::asio::use_future` 完成标记（completion token）、基于 `boost::asio::awaitable<>` 的协程（coroutine）、`boost::asio::spawn()` 以及 `boost::asio::experimental::cancellation_condition` 添加了处置支持。

  - 新增 `execution_context::service_maker` 抽象基类。`service_maker` 是传递给执行上下文（execution context）构造函数的对象，允许在上下文构造时添加服务。

  - 新增 `boost::asio::config`，提供对与执行上下文关联的配置参数的访问。该类供 Asio 内部使用，或供构建于 Asio 之上的库与用户提供的抽象使用，通常用于细调行为，例如启用或禁用某些优化。具体配置源（如 `boost::asio::config_from_env`、`boost::asio::config_from_concurrency_hint` 与 `boost::asio::config_from_string`）可传给 `io_context` 或 `thread_pool` 构造函数。

  - 新增 Asio 的 `io_context` 与 `thread_pool` 实现可识别的初始一组配置参数。

  - 移除了部分此前已弃用的设施。

  - 弃用 `basic_io_object` 与 `deadline_timer`。

  - 为关联绑定器（associating binders）添加右值限定的 `operator()` 重载。

  - 新增对 Boost 模块化构建结构的支持。

  - 修复对返回仅移动（move-only）类型的函数使用 `spawn()` 的问题。

  - 修复 `co_composed`，使其不再要求 concept（概念）支持。

  - 修复 epoll 反应器：fork 之后不再尝试重新注册普通文件描述符。

  - 修复 `ssl::detail::engine` 移动赋值中的一处泄漏。

  - 修复定义 `BOOST_ASIO_DISABLE_SMALL_BLOCK_RECYCLING` 时的编译错误。

  - 修复使用 Clang 19 时的编译错误。

  - 修改 `thread_pool::join()`，确保它也能停止随后通过 `thread_pool::attach()` 加入线程池的线程。

  - 修复 `io_uring_prep_write_fixed` 与 `io_uring_prep_read_fixed` 用于面向流操作时传入的偏移量。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_87_0/doc/html/boost_asio/history.html)。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 修复内存重新分配时原子等待状态列表的初始化（[\#72](https://github.com/boostorg/atomic/issues/72)）。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - API 变更：

    - 为 `basic_fields::insert()` 添加 `error_code` 重载。

    - 为 `websocket::stream::get_status` 添加查询 permessage-deflate 状态的重载。

  - 缺陷修复：

    - 修复 `http::basic_stream` 内调用 `net::dispatch` 的"移动后使用"（use-after-move）问题，该问题会在超时引发 `bad_executor` 异常。

    - 移除了发起函数（initiating functions）中的修改型操作。

    - 修复 `teardown_tcp_op` 中的取消处理。

    - 在调用 `on_finish_impl` 之前设置 `basic_parser` 的 `state_`。

    - 移除 `clamp` 函数的 static 说明符。

    - 处理测试中的 `-Wattributes` 警告。

    - 处理测试中的不可达代码警告。

  - 功能增强：

    - 为 `beast::http` 命名空间中的类型添加前向声明头文件。

    - 使 `http::parser` 能使用带 `error_code` 重载的 `basic_fields::insert()`。

    - 使 `http::basic_parser` 中的 `header_limit_` 也作用于报文尾（trailer）头字段。

    - 改进 `http::basic_parser`，使其更早返回 `http::error::header_limit`。

    - 新增对 Boost 模块化构建结构的支持。

  - 致谢：

    - Jackarain、Saleh Hatefinya、René Ferdinand Rivera Morell

- [Charconv](/libs/charconv)（字符与数值互转库）：

  - 修复 PPC64LE 架构上以 `__ibm128` 作为 long double 格式的支持。

  - 修复 Windows ARM64 平台上内建函数（intrinsics）的使用。

  - 修复使用 `std::float128_t` 或 `__float128` 时以指定精度进行 fixed（定点）格式化的问题。

- [Cobalt](/libs/cobalt)（C++20 协程库）：

  - 移除 `get_executor` 必须返回 const 引用的要求。

  - 新增 experimental/composition。

- [Compat](/libs/compat/)（标准库补丁库）：

  - 新增 `to_array.hpp`（由 Ruben Perez Hidalgo 贡献）。

- [Container](/libs/container/)（扩展容器库）：

  - 为 `static_vector` 与 `small_vector` 新增 `stored_size` 选项。

  - 修复的缺陷/issue：

    - [GitHub \#261："尾迭代器不可解引用"](https://github.com/boostorg/container/issues/261)。

    - [GitHub \#288："将 flat_map::extract_sequence 与 small_vector 一起使用时的编译错误"](https://github.com/boostorg/container/issues/288)。

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - 如 1.84.0 中所公告，不再支持 Windows 10 之前的版本。

  - 在 Windows 上，`canonical` 现在基于 `GetFinalPathNameByHandleW` WinAPI 函数。副作用是盘符会被转为大写，这使得结果路径的互操作性更好（[\#325](https://github.com/boostorg/filesystem/issues/325)）。

  - **v4：** 若输入路径带有末尾目录分隔符，`canonical` 的结果路径不再保留该分隔符。

  - 当以可转换为 `path` 的用户自定义类型实参（同时也是一个或多个 `Source` 类型）调用 `path` 构造函数或成员函数时，现在默认选择到 `path` 的转换。这在某些情况下可以解决实参转换歧义，但也可能导致次优的转换路径。若需要其他转换路径，建议用户使用显式类型转换（[\#326](https://github.com/boostorg/filesystem/issues/326)）。

  - 针对 FreeBSD 9 及更早版本上 `dirfd` 是宏的问题添加了变通方案（[\#328](https://github.com/boostorg/filesystem/issues/328)）。

- [Flyweight](/libs/flyweight/index.html)（享元（Flyweight）模式库）：

  - 新增 [`concurrent_factory`](/libs/flyweight/doc/tutorial/configuration.html#concurrent_factory)，一个基于 Boost.Unordered 并发容器的工厂，在多线程场景下性能出色。

  - 将此前文档声明为不抛异常的 `boost::flyweight` 操作标记为 `noexcept`（issue [\#15](https://github.com/boostorg/flyweight/issues/15)）。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 功能增强：

    - 在部分代码中以 `using` 取代 `typedef`。

    - 在部分代码中用别名（alias）现代化元函数。

    - 新增对模块化构建结构的支持。

    - 补全 CMake 覆盖（新增 GitHub Actions 的 CMake 测试）。

    - 改进文档工作流。

    - 更新 Qt 与 WxWidgets 示例。

    - 新增 enumerate，为 C++17 与 C++23 做准备。

  - 破坏性变更：

    - 移除已弃用的重缩放（rescaling）代码。

  - 已解决问题：

    - [\#1309](https://github.com/boostorg/geometry/issues/1309) 修复部分缺失的 qbk（QuickBook 文档格式）包含文件。

    - [\#1226](https://github.com/boostorg/geometry/issues/1226) [\#1326](https://github.com/boostorg/geometry/issues/1326) 修复环（ring）上多余回合（round）的问题。

    - [\#1293](https://github.com/boostorg/geometry/issues/1293) [\#1294](https://github.com/boostorg/geometry/issues/1294) [\#1295](https://github.com/boostorg/geometry/issues/1295) 修复穿越非聚类环（non clustered rings）的遍历。

    - [\#893](https://github.com/boostorg/geometry/issues/893) [\#1299](https://github.com/boostorg/geometry/issues/1299) 修复非 union 条件下的阻塞环（blocking rings）。

    - [\#1342](https://github.com/boostorg/geometry/issues/1342) 修复在与 touch（相触）组合时丢弃起始 turn 的问题。

    - [\#1288](https://github.com/boostorg/geometry/issues/1288) [\#1345](https://github.com/boostorg/geometry/issues/1345) 修复对（非完美）touch 的处理。

    - [\#1279](https://github.com/boostorg/geometry/issues/1279) 修复 `covered_by` 的错误结果。

    - 各类错误与警告的修复。

- [Iterator](/libs/iterator/)（迭代器构建设施库）：

  - `function_output_iterator` 现在符合 `std::output_iterator` concept（概念）（[\#85](https://github.com/boostorg/iterator/issues/85)）。

- [Interprocess](/libs/interprocess/)（进程间通信库）：

  - 将 Boost 依赖数量从 11 个（总计）减至 7 个。

  - 弃用 `<boost/interprocess/containers/*.hpp>` 头文件。它们是 2011 年 **Boost.Container** 的最初来源，但已不再维护。经过长期过渡，Boost.Interprocess 为兼容一直保留这些头文件。它们将在未来的 Boost 发布中移除。

  - 新增针对 Cygwin（译注：Windows 上的 POSIX 兼容环境）的若干变通方案。回归测试现可在 Cygwin64 上运行。

  - **ABI（应用二进制接口）破坏性变更**：`segment_manager` 现在使用支持超对齐（over-aligned）类型的新实现，并修复了若干既有缺陷。如需取得 Boost 1.87 之前的 ABI，可在包含 Boost.Interprocess 头文件之前用 `#define` 将 `BOOST_INTERPROCESS_SEGMENT_MANAGER_ABI` 定义为 `1`。

  - 修复的缺陷：

    - [GitHub \#152（"在 shared_memory_object 中处理 EINTR"）](https://github.com/boostorg/interprocess/issues/152)。

    - [GitHub \#173（"托管共享内存段的值未对齐"）](https://github.com/boostorg/interprocess/issues/173)。

    - [GitHub \#192（"managed_windows_shared_memory 在销毁时崩溃"）](https://github.com/boostorg/interprocess/issues/192)。

    - [GitHub \#199（"char_wchar_holder 赋值运算符中 m_is_wide 缺失或误用"）](https://github.com/boostorg/interprocess/issues/199)。

    - [GitHub \#210（"boost::interprocess::ipcdetail::sync_handles::obtain_mutex 中的缺陷"）](https://github.com/boostorg/interprocess/issues/210)。

    - [GitHub \#215（"SPARC 32 位上 boost/interprocess/segment_manager 的对齐问题"）](https://github.com/boostorg/interprocess/issues/215)。

    - [GitHub \#217（"managed_map_file 的 find_or_construct 未返回按 Cache 对齐的内存"）](https://github.com/boostorg/interprocess/issues/217)。

    - [GitHub \#230（"interprocess::ipcdetail::intermodule_singleton 在 MinGW 上不工作"）](https://github.com/boostorg/interprocess/issues/230)。

    - [GitHub \#236（"get_current_process_creation_time 中的浮点误差导致 intermodule_singleton 失败"）](https://github.com/boostorg/interprocess/issues/236)。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 直接序列化（direct serialization）。

  - 为 Boost.JSON 类型添加 GDB 美化打印器（pretty printers）。

  - 到结构体（struct）的转换忽略未知键。

  - 简化了 `value_to` 的异常包装行为。

  - 移除了已弃用的初始化列表（initializer list）行为。

  - 移除了已弃用的类型别名。

  - 在 ARM64 的 MinGW 上使用正确的 64 位全乘法。

  - 修复 `parse_into` 对错误大小元组的处理。

  - 检查输入大小是否超过序列允许的大小。

  - 修复 `value_ref` 在 GCC 14 上的段错误。

- [LexicalCast](/libs/lexical_cast/)（字符串与数值等类型转换库）：

  - 移除对 Boost.Integer 的依赖，从而缩短编译时间。

- [Log](/libs/log/)（日志库）：

  - 以 C++ 标准库的等价物取代 Boost.Thread 同步原语。这可能改善多线程性能，但也有影响用户的后果：

    - 不再支持 Boost.Thread 的线程中断。Boost.Log 不再对 Boost.Thread 用于实现线程中断的 `thread_interrupted` 异常做特殊处理，该异常将与其他异常一样被处理。特别地，用户指定的异常处理程序现在可能在 `thread_interrupted` 异常挂起时被调用。

    - 对于定时等待操作，超时现在使用 std::chrono 时间单位。这意味着 `bounded_ordering_queue` 与 `unbounded_ordering_queue` 类支持的 `ordering_window` 具名参数现在接受 `std::chrono::duration` 值，而非 Boost.DateTime 的 `boost::posix_time::time_duration`。

    - 当线程同步原语指示错误时，抛出 `std::system_error` 异常，而非 Boost.Thread 异常类型。

  - `strictest_lock` 新增对 C++ 标准库锁类型的支持。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - **重大更新。**

  - 许多特殊函数与分布现支持 CUDA（NVCC 与 NVRTC）与 SYCL。

  - 新增 mapairy、holtsmark 与 saspoint5 分布，参见 [1163](https://github.com/boostorg/math/pull/1163)。

  - 新增 landau 分布，参见 [1159](https://github.com/boostorg/math/pull/1159)。

  - 修复 beta 分位数（quantile）中的意外异常，参见 [1169](https://github.com/boostorg/math/issues/1169)。

- [Move](/libs/move/index.html)（移动语义/emplace 辅助库）：

  - 修复的缺陷：

    - [Git Issue \#56："std 类型的前向声明在某些平台上导致编译错误"](https://github.com/boostorg/move/issues/56)。

- [Mp11](/libs/mp11/)（C++11 元编程库）：

  - 新增 `mp_lambda`（由 Joaquin M Lopez Munoz 贡献）。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - 使 `float128` 可平凡复制（trivially copyable）。

  - 即使在非 GNU 模式下也将 `__float128` 视为浮点类型。

- [MySQL](/libs/mysql/)（MySQL 客户端库）：

  - **对实验性 API 的破坏性变更**：

    - `connection_pool` 的线程安全特性经过重新设计，以克服用户使用经验中发现的一些设计缺陷。`pool_params` 新增布尔选项 `thread_safe`（默认为 `false`）。设置后，部分连接池函数会改变行为以便安全并发使用。其实现方式是内部创建 strand（串行执行域），在需要时向其派发（dispatch），并重新接线取消信号。当 `pool_params::thread_safe` 为 `false` 时，适用通常的 Asio 执行器（executor）语义，无额外开销。

    - 移除 `pool_executor_params`，由 `pool_params::connection_executor` 与 `pool_params::thread_safe` 取代。

    - 完全移除 `connection_pool::async_get_connection` 的内建超时功能。该函数现在支持按操作取消，可用 `asio::cancel_after` 实现相同功能。

    - 现在销毁 `connection_pool` 会取消未完成的异步操作，与其他 Asio I/O 对象一致。这可防止资源泄漏：未完成的 `async_run` 操作会延长连接池的生命周期直到操作完成，可能导致连接池对象永远不被销毁。

    - 当连接尚不可用而 `async_get_connection` 操作被取消时，该操作现在一致地以 `client_errc::pool_not_running`、`client_errc::no_connection_available` 或 `client_errc::pool_cancelled` 失败，取决于连接池状态（此前会以 `client_errc::timeout` 或连接池内部 `async_connect` 操作遇到的最后一个错误码失败）。该信息现在包含在输出的诊断对象中。

    - 移除 `client_errc::timeout` 与 `client_errc::cancelled`。

    - 在未运行的连接池上调用 `async_get_connection` 不再立即失败，而是等待 `async_run` 被调用。

    - `sequence` 现在返回拥有（owning）类型。这使得在延迟（deferred）异步操作中与 `with_params` 一起使用是安全的。`format_sequence_view` 更名为 `format_sequence`。

    - `sequence` 已移至单独头文件 `boost/mysql/sequence.hpp`。

  - `any_connection`、客户端 SQL 格式化（含 `format_sql` 与 `with_params`）与 `connection_pool` 已提升为稳定 API。

  - 现在新代码推荐使用 `any_connection`，而非 `connection` 及其别名 `tcp_connection`、`tcp_ssl_connection` 与 `unix_connection`。

  - 新增 `with_params`，一种新的 `ExecutionRequest`，封装查询模板字符串与用于展开查询的参数。执行时它使用客户端 SQL 格式化展开查询并发送给服务器执行。这是运行带参数的简单查询的新推荐方式。

  - 新增 `with_diagnostics`，一个适配器完成标记，将异步函数抛出的异常转换为包含 `diagnostics` 对象，与同步抛异常函数的行为一致。

  - `with_diagnostics(asio::deferred)` 现在是 `any_connection` 与 `connection_pool` 中所有操作的默认完成标记。这使 `co_await conn.async_connect(params)` 之类的表达式与 `conn.connect(params)` 行为一致。注意 `connection` 及其类型别名尚未更新为该行为。

  - `connection_pool` 中的异步函数现在支持按操作取消。

  - 所有异步操作现在支持 `asio::cancel_after`、`asio::cancel_at` 及类似要求绑定执行器的完成标记，可用于传给 `asio::async_initiate` 的发起调用。

  - `connection` 与 `any_connection` 现在通过标记的立即执行器（immediate executor）派发立即完成。

  - 修复使用未连接过的 `any_connection` 导致崩溃的问题。

  - 移除 `field` 中可能抛异常的构造函数上的错误 `noexcept` 说明符。

  - 修复可能导致写缓冲区大小超过所配置缓冲区大小上限的问题。

  - 大幅更新文档与示例，使其更具针对性并反映新的推荐最佳实践。

- [Optional](/libs/optional/)（可选值库）：

  - **破坏性变更。** 停止支持 C++03，现在最低要求 C++11（至少需要部分 C++11 特性）。

  - 移除对 Boost.Utility 的依赖。

  - 移除对 Boost.Predef 的依赖。

  - 移除对 Boost.StaticAssert 的依赖。

  - 移除对 Boost.Move 的依赖。

  - 部分关系运算的实现略有提速。

  - **警告。** 未来发布中我们计划为 `optional` 引入范围（range）接口，使 `std::ranges::range<optional<T>>` 为 `true`。这可能会影响基于 `std::ranges::range` 等谓词做决策的程序中的重载决议。

  - 标签 `in_place_init` 与 `in_place_init_if` 变为 `inline constexpr`，从而在可执行文件中留下更小的占用。这解决了 [issue \#103](https://github.com/boostorg/optional/issues/103)。

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - 新增 `boost::pfr::for_each_field_with_name` 函数。非常感谢 [Lena](https://github.com/Baduit) 提交的 [PR#171](https://github.com/boostorg/pfr/pull/171)！

  - 对字段少而规模大的结构体，编译时间**显著**改善。非常感谢 [Zachary Wassall](https://github.com/runer112) 提交的 [PR#120](https://github.com/boostorg/pfr/pull/120)。

  - 修复 `pragma` 指令。

  - **初步支持 C++20 模块（C++20 Modules）**。更多信息见文档。

  - 修复 core_name14_disabled.hpp 中的未使用变量警告。感谢 [Anarthal (Rubén Pérez)](https://github.com/anarthal) 提交的 [PR#183](https://github.com/boostorg/pfr/pull/183) 与 [PR#187](https://github.com/boostorg/pfr/pull/187)。

  - C++17 下聚合体字段数的默认上限从 100 提高到 200。

  - 修复 GCC 不识别 -Wundefined-var-template 的警告。

  - 多处编译时间的小改进。

- [Process](/libs/process)（进程管理库）：

  - （v2）在 Windows 上实现 `async_wait` 的取消。

  - （v2）新增 `FORCE_DISABLE_CLOSE_RANGE`。

  - （v2）ext：针对 BSD 与 Solaris 的多项 ext 修复。

  - （v2）不可用的 ext 函数现在可以编译并给出 `operation_not_supported` 错误（包括 IOS）。

  - （v2）多处链接修复。

  - （v2）从链接库中移除 filesystem——使用哪个 filesystem 库现在只影响头文件。

  - （v1）添加针对 1.88 的弃用通知。

- [SmartPtr](/libs/smart_ptr/)（智能指针库）：

  - 不再支持 C++03，需要 C++11 编译器。包括 GCC 4.8 及更高版本，以及 MSVC 14.0 及更高版本。

  - 宏 `BOOST_SP_ENABLE_DEBUG_HOOKS`、`BOOST_SP_USE_STD_ALLOCATOR`、`BOOST_SP_USE_QUICK_ALLOCATOR`、`BOOST_AC_USE_SPINLOCK`、`BOOST_AC_USE_PTHREADS`、`BOOST_SP_USE_SPINLOCK` 与 `BOOST_SP_USE_PTHREADS` 启用的功能已弃用，相关支持将在未来发布中移除。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 新增 `Boost::stacktrace_from_exception` CMake 目标。非常感谢 [int mian](https://github.com/void-mian) 提交的 [PR#189](https://github.com/boostorg/stacktrace/pull/189)！

  - MSVC 静态构建不再导出 `boost_stacktrace_impl_return_nullptr`。非常感谢 [huangqinjin](https://github.com/huangqinjin) 提交的 [PR#186](https://github.com/boostorg/stacktrace/pull/186)。

  - 修复 Windows 下使用 clang 时与 `ole32.lib` 与 `Dbgeng.lib` 的自动链接。

  - 修复文档中缺失的命名空间。感谢 [Mats Taraldsvik](https://github.com/meastp) 提交的 [PR#181](https://github.com/boostorg/stacktrace/pull/181)。

  - 修复缺失的 `std::exception` 包含。感谢 [Julien Schueller](https://github.com/jschueller) 提交的 [PR#178](https://github.com/boostorg/stacktrace/pull/178)。

  - 修复 GCC 报告的类型转换错误。感谢 [agent_J](https://github.com/jplcz) 提交的 [PR#175](https://github.com/boostorg/stacktrace/pull/175)。

  - 修复从命令行设置 B2（Boost 构建工具）`from_exception` 特性的问题。感谢 [Dmitry Arkhipov](https://github.com/grisumbras) 提交的 [PR#194](https://github.com/boostorg/stacktrace/pull/194)。

- [STLInterfaces](/libs/stl_interfaces/)（迭代器/范围定制点 CRTP 基类库）：

  - 修正对序列容器 `swap` 的错误文档要求；期望的返回类型是 `void` 而非 `bool`（[\#71](https://github.com/boostorg/stl_interfaces/issues/71)）。

  - 为 `view_adaptor.hpp` 中适配器的数据成员添加 `[[no_unique_address]]`（[\#65](https://github.com/boostorg/stl_interfaces/issues/65)）。

  - 对支持 deducing this（推导 this）但未通过 `__cpp_explicit_this_parameter` 宣告该支持的较新版本 Clang 与 MSVC，启用 deducing this（[PR#68](https://github.com/boostorg/stl_interfaces/pull/68)）。

- [Test](/libs/test/)（单元测试框架库）：

  - 修复使用哑条件（dummy conditions）时对 clang-tidy 的支持（[PR#348](https://github.com/boostorg/test/pull/348)）。

  - 修复与 clang 的动态链接（[PR#431](https://github.com/boostorg/test/pull/431)）。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - **重大更新。**

  - 新增基于节点的并发容器 `boost::concurrent_node_map` 与 `boost::concurrent_node_set`。

  - 为并发容器新增 `insert_and_visit(x, f1, f2)` 及类似操作，允许在插入之后立即访问元素（相比之下，`insert_or_visit(x, f)` 仅在*未*发生插入时访问元素）。

  - 在 `boost::concurrent_flat_set` 的某些操作中，访问（visitation）改为独占加锁，以便安全地进行元素的可变修改（[PR#265](https://github.com/boostorg/unordered/pull/265)）。

  - 在 Visual Studio Natvis 中，支持任何分配器使用花式指针（fancy pointer）的容器。这适用于任何花式指针类型，只要为该花式指针类型编写了正确的 Natvis 定制点"Intrinsic"函数。

  - 为所有容器与迭代器添加 GDB 美化打印器。对于分配器使用花式指针的容器，只有为该花式指针类型本身编写了正确的美化打印器才能工作。

  - 修复开放定址（open-addressing）容器的 `std::initializer_list` 赋值问题（[PR#277](https://github.com/boostorg/unordered/pull/277)）。

  - 通过在内部将可调用对象的 `std::reference_wrapper` 传给迭代器对重载，允许将不可复制的可调用对象传给并发容器的 `insert_{and|or}_[c]visit` 的 `std::initializer_list` 重载。

- [URL](/libs/url/)（URL 解析库）：

  - feat：`set_params` 支持 `encoding_opts`（[\#856](https://github.com/boostorg/url/issues/856)）。

  - refactor：API 不再使用已弃用的 variant2 别名（[\#857](https://github.com/boostorg/url/issues/857)）。

  - refactor：`query_rule` 的解释保持一致（[\#864](https://github.com/boostorg/url/issues/864)）。

- [UUID](/libs/uuid/)（UUID 生成与解析库）：

  - 恢复了在 1.86 中意外丢失的构造 `constexpr uuid` 的能力。

- [Wave](/libs/wave/)（C/C++ 预处理器实现库）：

  - 修复的缺陷：

    - [GitHub \#220："C++20 下 stringify 参数为空时段错误"](https://github.com/boostorg/wave/issues/220)。感谢 [Lu HongYi](https://github.com/jwnhy/)。

    - [GitHub \#222："被包含文件首行为空白时不生成行指令（line directive）"](https://github.com/boostorg/wave/issues/222)。感谢 [Nick Nobles](https://github.com/njnobles)。

  - 构建改进，包括模块化构建支持，感谢 [René Rivera](https://github.com/grafikrobot)。

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

本次发布由 Marshall Clow、Glen Fernandes 与 Ion Gaztañaga 管理。
