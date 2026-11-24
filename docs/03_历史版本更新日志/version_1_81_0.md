# Boost 1.81.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_81_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_81_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2022-12-14 17:44 GMT（原文日期行：December 14th, 2022 17:44 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.81.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 已知问题（Known Issues）

本版原文无"已知问题"栏目。

## 新增库（New Libraries）

- [URL](/libs/url/)（URL 解析库）：一个仅使用 C++11 即可对 URL 进行解析、修改与打印的库，由 Vinnie Falco 与 Alan de Freitas 开发。特性包括编译速度快、强不变量（invariant），并采用内存友好（memory-friendly）的方式实现严格合规。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 新增 `consign` 完成标记适配器（completion token adapter），可用于向完成处理程序（completion handler）附加额外的值。

  - 新增 `any_completion_handler<>`，可用于对完成处理程序进行类型擦除（type-erase）。

  - 新增 `experimental::co_composed`，支持使用 C++20 协程（coroutine）轻量地实现用户自定义异步操作。

  - 新增基于范围的 `experimental::make_parallel_group()` 重载。

  - 新增 `any_completion_executor`，即与完成处理程序相关联的执行器（executor）的类型擦除封装。

  - 为 `use_future` 的执行器补上缺失的 `context` 查询。

  - 为 `execution::any_executor<>` 与 `any_io_executor` 新增不抛出异常的构造函数重载。

  - 优化空 `execution::any_executor` 对象的表示，以提升拷贝与移动操作的性能。

  - 为 `std::reference_wrapper` 新增 `associated_cancellation_slot` 特化。

  - 更改 I/O 对象，使其以 const 引用返回其执行器。

  - 更改关联设施（associated traits），使所有双实参 `get` 函数使用推导出的返回类型。

  - 修复 `spawn` 实现，以捕获未处理的异常并在所生成（spawned）"线程"之外重新抛出。

  - 修复 `spawn`，确保完成处理程序通过正确的执行器分发。

  - 修复终态（terminal-state）`spawn` "线程"对象的清理。

  - 修复 `spawn` 与 `co_spawn` 实现，使其在正确的执行器上分发取消处理程序。

  - 更改 'dispatch' 的语义，使其表示执行器按原样使用。

  - 弃用 `execution::execute` 定制点（customisation point）与 sender/receiver 设施。

  - 新增 C++11 `parallel_group` 示例。

  - 修复示例代码，不再使用已弃用的 `resolve` 转换。

  - 修复 `experimental::channel_traits` 特化中的歧义。

  - 为 `R(error_code)` 签名新增特化的 channel 实现。

  - 将 `async_compose` 'self' 对象上的 `cancelled()` 设为公开。

  - 为 `async_compose` 'self' 对象新增 `io_executor_type` 与 `get_io_executor`。

  - 修复 Windows 重叠（overlapped）句柄的 `release()` 实现。

  - 为 `experimental::coro` 启用延迟等待（deferred awaiting），规范了 `experimental::use_coro`，并修复分配器处理。

  - 清理了 `experimental::promise`，并将其改为异步操作对象。

  - 对 `post`/`defer` 重载施加约束：仅当能够要求 `blocking.never` 时可用。

  - 更改描述符（descriptor）实现：设置非阻塞模式时若 `ioctl` 以 `ENOTTY` 失败，则回退到 `fcntl`。

  - 修复与使用 `sprintf` 相关的 Xcode 弃用警告。

  - 修复在内部线程上运行 `select_reactor::run` 时传递的实参。

  - 修复定义 `BOOST_ASIO_DISABLE_SMALL_BLOCK_RECYCLING` 时的编译错误。

  - 更新 clang 14 及更高版本上 C++20 协程支持的检测。

  - 更改标准库特性检测，面向 C++17 或更高版本时总是启用 `std::invoke_result`。

  - 修复 MSVC 上返回类型推导的检测。

  - 更新异步操作要求，放宽对关联执行器的要求。

  - 在实现说明（implementation notes）中新增 `io_uring`。

  - 更多细节请查阅[修订历史](/doc/libs/1_81_0/doc/html/boost_asio/history.html)。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 新增 `buffers_generator`。

  - 新增 `beast::http::message_generator`。

  - 新增 `buffer_ref`，使 beast 缓冲区可与 asio 一起使用。

  - 支持按操作取消（per-operation cancellation）。

  - 新增 C++20 awaitable 示例。

  - WebSocket 按消息压缩（per-message compression）选项。

  - WebSocket 超时选项 API。

  - 多个 Content-Length 的错误处理。

  - 支持默认完成（default-completion）与重绑定（rebind）。

- [Container Hash](/libs/container_hash/)（哈希支持库）：

  - **重大更新。**

  - `boost::hash` 的特化已被移除；它现在总是调用 `hash_value`。

  - 对 `BOOST_HASH_NO_EXTENSIONS` 的支持已被移除。扩展总是启用。

  - 现在支持所有标准容器，包括 `std::forward_list` 与无序关联容器。

  - 现在开箱即用地支持用户自定义容器（拥有返回迭代器的 `begin()` 与 `end()` 成员函数的类型）。

  - 现在开箱即用地支持已描述（described）的结构体与类（使用 `BOOST_DESCRIBE_STRUCT` 或 `BOOST_DESCRIBE_CLASS` 标注的类型）。

  - `hash_combine` 已得到改进。

  - 字符串哈希的性能（以及由上述改进带来的质量）已提升。针对字符串的 `boost::hash` 现在可在 64 位模式下通过 SMHasher 测试。

  - 文档已大幅修订以反映这些变更。

- [Core](/libs/core/)（核心工具集库）：

  - `empty_value` 的成员现已标记为 `constexpr`。

  - 新增 `fclose_deleter`，一个对指向 `std::FILE` 的指针调用 `std::fclose` 的删除器（deleter）。

  - `boost/core/bit.hpp` 中的位操作工具现在显式要求输入为无符号整数（[\#129](https://github.com/boostorg/core/issues/129)）。

  - `bit_width` 现在返回 `int` 而非输入实参类型的值。此变更遵循 [LWG3656](https://cplusplus.github.io/LWG/issue3656) 的决议。

- [Describe](/libs/describe/)（枚举/结构体成员描述宏库）：

  - 为使 `enumerators.hpp`、`bases.hpp` 与 `members.hpp` 在使用 `-pedantic` 选项时也能被包含，`BOOST_DESCRIBE_ENUM` 的调用已从 `modifiers.hpp` 移至单独的头文件 `modifier_description.hpp`。由此，`modifiers.hpp` 不再包含 `enum.hpp`。依赖此隐式包含的代码可能失败，需要改为自行包含 `enum.hpp`。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 修复 Windows 平台上 `path_from_handle` 的实现，感谢 @SaltfishAmi 提交的错误报告 [57](https://github.com/apolukhin/Boost.DLL/issues/57)。

- [Filesystem](/libs/filesystem/)（可移植文件系统操作库）：

  - **弃用：** 自字符容器（如 `std::vector<char>` 或 `std::list<wchar_t>`）构造、赋值与追加 `path` 在 **v3** 中已弃用，并在 **v4** 中移除。请改用字符串类型或迭代器。

  - **弃用：** `boost/filesystem/path_traits.hpp` 头文件已弃用，并将在未来发布中移除。该头文件包含 `path` 的实现细节，不应在用户代码中使用。

  - 此前已弃用的 API 现在在使用时会产生编译警告。要抑制这些警告，可在编译用户代码时定义宏 `BOOST_FILESYSTEM_ALLOW_DEPRECATED`。

  - 修复在不支持 `*at` API 的 POSIX 系统上因缺少 include 而导致的编译问题（[\#250](https://github.com/boostorg/filesystem/issues/250)）。

  - 在 Windows 10 之前的版本上，针对构造目录迭代器时产生 `ERROR_INVALID_PARAMETER` 的网络共享文件系统新增了变通方案（[PR#246](https://github.com/boostorg/filesystem/pull/246)、[\#245](https://github.com/boostorg/filesystem/issues/245)）。

  - 在 Windows 上，修复路径以 "\\?\ 前缀开头时 `weakly_canonical` 以 `ERROR_INVALID_FUNCTION` 错误码失败的问题（[\#247](https://github.com/boostorg/filesystem/issues/247)）。

  - 在 `path` 构造函数、赋值与追加操作中新增对 `std::string_view`、`boost::string_view` 与 `boost::container::string`（以及各自 `wchar_t` 对应类型）的支持（[\#208](https://github.com/boostorg/filesystem/issues/208)）。

  - 接受迭代器对的 `path` 构造函数、赋值与追加操作将不再接受值类型不属于受支持路径字符类型的迭代器。

  - 在 Windows 上，改进 `directory_iterator` 与各种挂载文件系统以及 7.21 之前版本 Wine 的兼容性（[\#255](https://github.com/boostorg/filesystem/issues/255)、[\#266](https://github.com/boostorg/filesystem/issues/266)）。

  - 在 Windows 上，去重（deduplicated）文件现在被报告为普通文件而非重解析（reparse）文件（[\#262](https://github.com/boostorg/filesystem/issues/262)）。

- [Fusion](/libs/fusion/)（异构容器与算法库）：

  - 新增 `fusion::identity_view`（[PR#240](https://github.com/boostorg/fusion/pull/240)）。

  - 为 `fusion::transform_view` 新增对关联序列（associative sequence）的支持（[PR#239](https://github.com/boostorg/fusion/pull/239)）。

  - 修复 `fusion::reverse_view` 与关联序列一起使用时的编译问题（[PR#237](https://github.com/boostorg/fusion/pull/237)）。

  - 修复 Clang 13 的 -Wdeprecated-copy 警告（[PR#261](https://github.com/boostorg/fusion/pull/261)）。

  - 小规模的依赖重组。现在 `boost::ref` 与 `boost::noncopyable` 改用 Boost.Core 提供的版本（[PR#249](https://github.com/boostorg/fusion/pull/249)）。

  - 新增 Linux 与 MacOS 上 clang 与 gcc 的 CI 测试，修复 Windows 上的 CI 测试（[PR#245](https://github.com/boostorg/fusion/pull/245)、[PR#236](https://github.com/boostorg/fusion/pull/236)）。

  - 改进文档并修复拼写错误（[\#234](https://github.com/boostorg/fusion/issues/234)、[PR#235](https://github.com/boostorg/fusion/pull/235)、[PR#238](https://github.com/boostorg/fusion/pull/238)）。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 已解决问题（Solved issues）：

    - [\#1048](https://github.com/boostorg/geometry/issues/1048) Index：修复 IndexableGetter 按值返回 Indexable 时的悬垂引用（dangling reference）

    - [\#1076](https://github.com/boostorg/geometry/issues/1076) Union：在极少数情况下可能遗漏一个多边形

    - [\#1081](https://github.com/boostorg/geometry/issues/1081) Union：因精度原因可能遗漏内环（interior ring）

  - 缺陷修复（Bugfixes）：

    - [\#1063](https://github.com/boostorg/geometry/issues/1063) Intersection：修复简单球面多边形求交中的一处缺陷

    - [\#1064](https://github.com/boostorg/geometry/issues/1064) Formulas：修复测地线正算（direct）公式中的一致性问题

    - [\#1088](https://github.com/boostorg/geometry/issues/1088) Point：修复自定义点类型的一处回归

    - 各类修复：缺失的 include 文件、警告、C++20 编译错误与文档

- [Histogram](/libs/histogram/)（多维直方图库）：

  - **重大更新。**

  - 新增 `accumulators::fraction`，用于计算比例（fraction）、其方差与置信区间。

  - 新增比例的区间计算器：`utility::clopper_pearson`、`utility::wilson_interval`、`utility::jeffreys_interval`、`utility::wald_interval`，可以以任意置信水平计算区间。

  - 新增 `utility::confidence_level` 与 `utility::deviation` 类型，分别用于以概率或以标准差倍数向所有区间计算器传递置信水平。

  - 修复 C++20 下内部的 `sub_array` 与 `span`。

- [Iterator](/libs/iterator/)（迭代器构建设施库）：

  - `function_output_iterator` 现在支持将所赋的值完美转发（perfect forwarding）给被包装的函数对象（[PR#73](https://github.com/boostorg/iterator/pull/73)）。

  - 修复自另一个 `function_input_iterator` 后置递增结果构造 `function_input_iterator` 的编译问题（[\#75](https://github.com/boostorg/iterator/issues/75)）。

  - 基于 `iterator_facade` 的迭代器后置递增的结果现在支持 `operator->`。`(it++)->foo` 等价于 `(*it++).foo`，后者此前即受支持。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 新增 `object::stable_erase`。

  - 新增针对 `std::istream` 的 `parse` 重载以及针对 `value` 的 `operator>>`。

  - 为 `value` 新增右值引用限定的访问器。

  - 转换特征（traits）经过重新设计。

  - 新增对已描述（described）类与枚举、`std::optional`、`std::variant` 以及类空类型（null-like types，包括 `std::nullptr_t`、`std::nullopt_t` 与 `std::monotype`（译注：原文即如此，应为 `std::monostate`））的转换支持。

  - 新增自 `value` 到用户类型的无异常转换。

- [LexicalCast](/libs/lexical_cast/)（字符串↔数值等类型转换库）：

  - 修复转换 volatile 算术类型时的编译问题。感谢 Giovanni Cerretani 提交的错误报告 [\#50](https://github.com/boostorg/lexical_cast/issues/50)。

  - 移除对已弃用头文件的使用。感谢 Michael Ford 提交的 [PR#53](https://github.com/boostorg/lexical_cast/pull/53)。

- [Locale](/libs/locale/)（本地化与 Unicode 文本处理库）：

  - **重大更新，含部分破坏性变更（breaking changes）。**

  - 现在要求 C++11 支持，放弃对 C++03 及更早标准的支持。

  - 部分枚举已转换为 enum class——可避免命名冲突。

  - 以细粒度配置选项取代 `-sICU_LINK_LOCALE` 与 `-sICU_LINK`，与 Boost.Regex 中的做法一致。

  - 修复 libiconv 的检测，使 Boost.Locale 能够（重新）在部分平台上构建。

  - 移除 `std::auto_ptr` 的使用与支持。

  - 使 Windows 上使用 `wchar_t` 的 `codecvt` 假定/使用 UTF-16 编码。

  - 性能改进：使 `basic_format`、`date_time` 与 `hold_ptr` 可移动，修复格式缓存的使用。

  - 使 Boost.Locale 与更多 ICU 版本兼容（尤其是测试）。

  - 修复部分类的 RTTI 定义（可见性问题）。

  - 修复 ICU 后端与部分 libc++ 版本的兼容性。

  - 修复部分运算符的返回值，使其正确返回非 const 的 `*this`。

  - 修复 `date_time` 中年份负向滚动时的整数溢出。

  - 处理或抑制大量警告，使构建日志更干净。

  - 新增对更多 Windows 代码页（codepage）的支持。

  - 修复对 ISO-2022-JP 等 Windows 代码页的支持。

- [Nowide](/libs/nowide/)（Windows 下 UTF-8 标准 I/O 适配库）：

  - 修复 MSVC 上测试的构建失败。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 该库**不再使用 COM 初始化**。感谢 Alex Guteniev 提交错误报告、澄清并提交 [PR#123](https://github.com/boostorg/stacktrace/pull/123)！

  - 在 b2（Boost 构建工具）中检测 libbacktrace 可用性时，该库现在可以使用 `BOOST_STACKTRACE_BACKTRACE_INCLUDE_FILE` 宏的值，感谢 Ben Gemmill 提交的错误报告 [\#115](https://github.com/boostorg/stacktrace/issues/115)。

  - 新增 `BOOST_STACKTRACE_BACKTRACE_FORCE_STATIC` 宏，用于在使用 libbacktrace 时强制使用单个 `backtrace_state` 静态实例。感谢 Rasmus Thomsen 提交的错误报告 [\#118](https://github.com/boostorg/stacktrace/issues/118)！

  - 仅包含 `boost/stacktrace/stacktrace.hpp` 头文件时避免未解析引用。感谢 Long Deng 提交的错误报告 [\#116](https://github.com/boostorg/stacktrace/issues/116)。

  - 通过在 Windows 平台上不调用 `strlen` 优化堆栈回溯打印。感谢 Alex Guteniev 提交的错误报告 [\#122](https://github.com/boostorg/stacktrace/issues/122)。

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - 改进 C++14 模式下可聚合初始化（aggregate initializable）类型的检测，感谢 Denis Mikhailov 提交的 [PR#97](https://github.com/boostorg/pfr/pull/97)。

  - 抑制 clang-tidy 警告，感谢 Alexander Malkov 提交的 [PR#109](https://github.com/boostorg/pfr/pull/109) 与 [PR#104](https://github.com/boostorg/pfr/pull/104)。

  - 若编译器支持折叠表达式（fold expression）则加以使用。感谢 Jean-Michaël Celerier 提交的 [PR#96](https://github.com/boostorg/pfr/pull/96)。

- [STLInterfaces](/libs/stl_interfaces/)（迭代器/范围定制点 CRTP 基类库）：

  - 修复在 C++20 之前的迭代器（`value_type` 为 const 限定）中两个不合式（ill-formed）的 `iterator_interface` 运算符。

- [System](/libs/system/)（错误码与 system_error 库）：

  - 现在可定义宏 `BOOST_SYSTEM_DISABLE_THREADS` 以禁用 `<mutex>` 的使用（例如在单线程 libstdc++ 上）。

  - 为 `result<>` 新增 `value_type`、`error_type`、`in_place_value`、`in_place_error`。

  - 为 `result<>` 新增 `emplace`。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - **重大更新。**

  - 新增基于开放寻址（open addressing）的快速容器 `boost::unordered_flat_map` 与 `boost::unordered_flat_set`。

  - 为所有容器新增 CTAD（类模板实参推导）推导指引（deduction guide）。

  - 按照 [LWG issue 2713](https://cplusplus.github.io/LWG/issue2713) 的规定补上缺失的构造函数。

- [Variant](/libs/variant/)（非递归可辨识联合库）：

  - 避免头文件的递归包含，感谢 Nathan Sidwell 提交的错误报告 [\#101](https://github.com/boostorg/variant/issues/101)。

  - 移除对已弃用头文件的使用，感谢 Michael Ford 提交的 [PR#96](https://github.com/boostorg/variant/pull/96)。

  - 修复 clang 在 C++23 模式下的编译，感谢 Ed Catmur 提交的 [PR#98](https://github.com/boostorg/variant/pull/98)。

- [Variant2](/libs/variant2/)（Variant 的现代重实现库）：

  - 新增对 `boost::json::value_from` 与 `boost::json::value_to` 的支持。

## 更新的工具（Updated Tools）

本版原文无该栏目。

## 已测试的编译器（Compilers Tested）

Boost 的主要测试编译器如下：

- Linux：

  - Clang：3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++11：3.4, 11.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++14：3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 5.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++17：6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++20：11.0.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - GCC：4.6.3, 11, 12

  - GCC，C++11：4.7.3, 4.8.5, 11, 12

  - GCC，C++14：5.4.0, 6.4.0, 7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC，C++17：7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC，C++20：8.0.1, 9.1.0, 10, 11, 12

- OS X：

  - Apple Clang：11.0.3

  - Apple Clang，C++11：11.0.3

  - Apple Clang，C++14：11.0.3

  - Apple Clang，C++17：11.0.3

  - Apple Clang，C++20：11.0.3

- Windows：

  - Visual C++：10.0, 11.0, 12.0, 14.0, 14.1, 14.2, 14.3

## 致谢（Acknowledgements）

本次发布由 Marshall Clow 与 Glen Fernandes 管理。
