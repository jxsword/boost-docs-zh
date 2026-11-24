# Boost 1.88.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_88_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_88_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2025-04-10 20:39 GMT（原文日期行：April 10th, 2025 20:39 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.88.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 新增库（New Libraries）

- [Hash2](/libs/hash2/)（可扩展哈希框架库）：一个可扩展的哈希框架，由 Peter Dimov 与 Christian Mazakas 开发。

- [MQTT5](/libs/mqtt5/)（MQTT 5.0 客户端库）：构建于 Boost.Asio 之上的 MQTT5 客户端库，由 Ivica Siladić、Bruno Iljazović 与 Korina Šimičević 开发。

## 更新的库（Updated Libraries）

- [Array](/libs/array/)（固定大小数组库）：

  - 文档转换为 AsciiDoc 文档格式（Christian Mazakas）。

  - 在合适之处添加了 `noexcept` 与 `constexpr`。

  - 将过时的函数标记为弃用。

  - 移除了过时的编译器变通方案。

  - 将 `array<T, 0>::begin()`、`cbegin()`、`end()`、`cend()` 改为返回 `nullptr`，从而支持 `constexpr`。这与 `std::array` 的行为一致。

  - 移除了库内自带的 `hash_value` 重载；`boost::hash` 现已原生支持类数组（array-like）类型。

  - `array<T, 0>` 现在可以用 `= {{}}` 初始化。

  - 新增 `operator<=>`。

  - 新增 `to_array`。

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 为 `local::basic_endpoint` 的多个成员函数添加 `noexcept` 限定，使其与 `ip::basic_endpoint` 保持一致。

  - 修复 `boost::asio::config` 类对整数值的处理。

  - 修复 `experimental::ranged_parallel_group` 中的一处"移动后使用"（use-after-move）错误。

  - 修复 `experimental::promise` 实现中一处错误的默认模板实参。

  - 修复 `io_uring` 实现：在 fork 之后，若内部描述符此前未曾注册，则不再尝试向 reactor（反应器）重新注册。

  - 修复 `thread_pool` 默认构造函数中一个未初始化的成员。

  - 修复向 `boost::asio::buffer` 函数传递 `std::span` 时出现的重载歧义问题。

  - 移除了弃用缓冲区功能删除之后遗留的一些多余宏定义。

  - 新增文档，澄清打开文件时 `file_base::flags` 的用法。

  - 新增关于可用运行时配置选项的概述文档。

  - 更新概述文档，以反映 `deferred` 作为默认完成标记（completion token）的用法。

  - 更新 `async_result` 文档，以反映该特征（traits）的特化当前须满足的类型要求。

- [Assert](/libs/assert/)（可定制断言宏库）：

  - 当定义了 `BOOST_ASSERT_HANDLER_IS_NORETURN` 时，`boost::assertion_failed` 与 `boost::assertion_failed_msg` 将以 `BOOST_NORETURN` 声明。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 缺陷修复：

    - 修复 `iequals` 函数中的越界访问。

  - 功能增强：

    - 更新 SSL 示例，校验对端证书的主机名。

    - 重构 CMakeLists。

    - 从示例中移除对 Boost.Scope 的依赖。

    - WebSocket 中的对端 ping 现在计为活动（activity）。

  - 文档：

    - 新增 Unix 域套接字（Unix domain socket）示例。

    - 文档新增"SSL/TLS 证书"章节。

    - 改进 `websocket::stream::async_close` 的文档。

  - 致谢：

    - Morten M. Neergaard

- [Conversion](/libs/conversion/)（类型转换库）：

  - 在示例与库代码中使用现代 C++。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 为 `boost::dll::shared_library` 新增接受 `native_handle_t` 的构造函数。非常感谢 [Tiago Matos](https://github.com/tgmatos) 提交的 [PR#82](https://github.com/boostorg/dll/pull/82)！

  - 移除了对 Spirit、SmartPtr、Move、TypeTraits 与 Function 等多个 Boost 库的依赖，DLL 的编译变得更加轻量。

  - API 中改用 `std::error_code&` 取代 `boost::system::error_code&`。这并非破坏性变更，因为 `boost::system::error_code` 可转换为 `std::error_code&`。

  - `boost::dll::import_*` 系列函数现在返回 `std::shared_ptr` 而非 `boost::shared_ptr`。可定义 `BOOST_DLL_USE_BOOST_SHARED_PTR` 恢复旧行为，但请注意该宏将在未来某个 Boost 发布中移除。

  - 在示例与库代码中使用现代 C++。

  - 遇到损坏的二进制文件时，`boost::dll::library_info` 现在总是抛出异常。已更新文档并添加了一些测试。

  - 在 FAQ（常见问题）中说明了为什么缺少 `RTLD_NODELETE` 以及为什么没有 `.release()` 方法，并给出了可能的变通方案建议。

  - 更新了关于构建与使用该库的信息。当平台需要时，CMake（构建系统）目标现在会链接 `-ldl`。

  - 修复 Windows 上长路径情形下 `detail::path_from_handle` 的实现。

  - 文档中着重说明库的 `boost/dll/smart_*` 部分是实验性且不完整的。

  - 修复库的 `boost/dll/smart_*` 部分中的多处名称修饰（name mangling）问题。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 功能增强：

    - [PR#1370](https://github.com/boostorg/geometry/pull/1370) 放宽椭球归一化（spheroidal normalization）中的半周期检查。

    - [PR#1368](https://github.com/boostorg/geometry/pull/1368) 在 rtree 空间谓词中传递伞式策略（umbrella strategies）。

    - [PR#1367](https://github.com/boostorg/geometry/pull/1367) 改进遍历（traversal）。

    - [PR#1361](https://github.com/boostorg/geometry/pull/1361) 在整数坐标的随机网格上测试集合运算。

    - 新增了若干测试用例。

    - 在部分代码中以 `using` 取代 `typedef`。

  - 已解决问题：

    - [PR#1364](https://github.com/boostorg/geometry/pull/1364) 修复多个策略（添加 getter、修复编译错误与警告）。

    - [\#629](https://github.com/boostorg/geometry/issues/629) 消除坐标转换与未使用参数引发的警告。

    - 各类错误与警告的修复。

- [Graph](/libs/geometry/)（图结构与算法库）（译注：原文该条目链接误指向 /libs/geometry/）：

  - 缺陷修复：

    - 重写 `maximum_weighted_matching` 的实现，解决了多个问题。

    - 确保 `named_graph` 在使用前已完成初始化。

    - 将 `is_straight_line_drawing` 中的自定义几何代码替换为 Boost.Geometry，修复极小角度下结果不正确的问题。

    - 修复 `undirected_dfs` 中对 `finish_edge` 的错误回调。

  - 性能改进：

    - `adjacency_list`：对基于 `vector` 的存储，移除 `add_vertex` 内部对 `resize`/`reserve` 的多余调用！快速基准测试显示图构建时间缩短约 10%。

    - `lengauer_tarjan_dominator_tree`：以 `std::vector` 取代 `std::deque`，对大图获得约 40% 的性能提升。

  - 总体改进：

    - 以 C++14 语言特性取代若干 Boost 工具的使用。

    - 以 C++14 语言特性现代化示例代码。

    - 文档与构建系统的各类修复。

    - `vertex_by_property` 不再要求图可变。

    - 修复 `cycle_canceling` 与 Clang 19 的编译问题。

- [Iterator](/libs/iterator/)（迭代器构建设施库）：

  - 停止支持 C++03 与古老编译器，代码库更新为使用 C++11 与 MP11，并减少了对 MPL 的使用（[PR#82](https://github.com/boostorg/iterator/pull/82)）。

  - 新增 `min_category` 特征（traits），它是 `minimum_category` 的可变参数等价物，不依赖 MPL。`minimum_category` 已弃用，将在未来发布中移除。

  - 将 `enable_if_convertible` 特征抽取到单独的头文件 `enable_if_convertible.hpp`。该特征此前定义在 `iterator_adaptor.hpp` 中，包含该头文件时仍会提供 `enable_if_convertible`。此依赖仅为向后兼容而保留，将在未来发布中移除。建议用户按需自行添加对 `enable_if_convertible.hpp` 的包含。

  - 为多种产生类型的迭代器特征新增 `*_t` 变体。

  - `filter_iterator` 与 `transform_iterator` 现在使用空基类优化（EBO，empty base optimization），在被适配的函数对象无状态时缩小迭代器体积。

  - `zip_iterator` 现在原生支持以 `boost::tuple`、`std::tuple` 与 `std::pair` 作为迭代器元组，无需再包含 Fusion 支持头文件。

  - 当被包装的函数是函数指针时，`function_output_iterator` 不再允许默认构造。此前这种构造会创建一个函数指针值未初始化的迭代器，而这样的迭代器无法使用。

  - `generator_iterator.hpp` 与 `shared_container_iterator.hpp` 头文件已移至 `boost/iterator` 目录下。`boost` 目录下的原头文件为向后兼容仍保留，但将在未来发布中移除。建议用户更新其包含语句。

  - `shared_container_iterator` 现在内部使用 `std::shared_ptr` 引用容器。对 `boost::shared_ptr` 的支持仍保留，但由于 `boost::shared_ptr` 现在内部被包在 `std::shared_ptr` 中，迭代器构造会产生性能开销。建议使用 `std::shared_ptr` 引用容器。

- [Locale](/libs/locale/)（本地化与 Unicode 文本处理库）：

  - 将所需的 ICU 最低版本提升至 4.8.1。

  - 停止支持 ICU 50.1。

  - 修复对以浮点格式字符串输入的整数的解析（[PR#241](https://github.com/boostorg/locale/pull/241)）。

  - ICU 后端支持 `uint64_t` 值的解析与格式化（[PR#246](https://github.com/boostorg/locale/pull/246)）。

  - 在更多平台上支持 `char8_t`。

- [Lockfree](/libs/lockfree/)（无锁容器与队列库）：

  - 新增 `spsc_value`，一个基于三重缓冲区（triple-buffer）的无锁单生产者单消费者（SPSC）值容器。

- [Log](/libs/log/)（日志库）：

  - 在 C++20 及更高标准模式下禁用 `std::codecvt<char16_t>` 与 `std::codecvt<char32_t>` 本地化设施（locale facets），因为它们在 C++20 中已被弃用。这意味着在 C++20 及更高标准中，与 `char16_t` 和 `char32_t` 之间的字符编码转换不再可用。

  - 修复使用 CMake 与 MinGW-w64 时的构建问题（[PR#241](https://github.com/boostorg/log/pull/241)）。

  - 修复 `text_file_backend` 在以下情形下使用的文件计数不正确的问题：后端被配置为向既有文件追加写入、正在写入的文件名模式中没有计数占位符而目标文件名模式中有、且日志文件直接写入目标存储（[\#245](https://github.com/boostorg/log/issues/245)）。

- [Mp11](/libs/mp11/)（C++11 元编程库）：

  - 修复 `mp_from_sequence` 处理非整数值的问题（1.83.0 因引入偏移量支持而意外破坏）。

- [MySQL](/libs/mysql/)（MySQL 客户端库）：

  - `connection_pool` 现在即使存在大量正在建立会话的连接也能正确调整大小。旧算法在某些条件下可能导致连接池未按预期调整大小（[\#395](https://github.com/boostorg/mysql/issues/395)）。

  - 新增 `any_connection::connection_id`。该函数获取连接的 ID，随后可在 `KILL` SQL 语句中使用以取消查询。该函数等价于官方 C API 中的 `mysql_thread_id`（[\#408](https://github.com/boostorg/mysql/issues/408)）。

  - 在 `connection` 或 `any_connection` 上已有操作进行中时再启动异步操作，不再触发未定义行为，而是以 `client_errc::operation_in_progress` 失败（[\#405](https://github.com/boostorg/mysql/issues/405)）。

  - 当 `connection` 或 `any_connection` 正处于多函数操作（multi-function operation）中时再启动操作，不再产生可能危险的报文错配，而是以 `client_errc::engaged_in_multi_function` 失败（[\#448](https://github.com/boostorg/mysql/issues/448)）。

  - 改进了在未建立会话时使用连接的诊断信息。操作现在以 `client_errc::not_connected` 失败（[\#450](https://github.com/boostorg/mysql/issues/450)）。

  - 修复 `connection` 与 `any_connection` 中与按操作取消（per-operation cancellation）相关的竞态条件。在先前版本中，如果取消信号在一个中间异步操作已完成之后、其处理程序被调用之前发出，该信号会被忽略。现在不再如此（[\#199](https://github.com/boostorg/mysql/issues/199)）。

  - `field` 从 `std::string_view` 构造与赋值的函数现在在 C++17 即可用，而不再要求 C++20。这些函数此前由标准特性测试宏（feature-test macro）守卫，仅在 C++20 可用，现已替换为 Boost.Config 的等价宏。

  - 新增使用 C++20 协程（coroutine）的 HTTP 服务器示例。

  - 新增关于同步与异步代码衔接的文档页。它取代了原先含竞态条件的同步连接池代码片段。

  - 改进了其他一些示例与文档页。

- [Nowide](/libs/nowide/)（Windows 下 UTF-8 标准 I/O 适配库）：

  - 使 `getenv` 线程安全（[PR#191](https://github.com/boostorg/nowide/pull/191)）。

- [PolyCollection](/libs/poly_collection/)（多态集合库）：

  - 新增 `boost::variant_collection`，一个行为上类似 `std::vector<std::variant<...>>` 的封闭式多态集合。

- [SmartPtr](/libs/smart_ptr/)（智能指针库）：

  - 修复宽字符流的 `operator<<`（1.87.0 中意外破坏）。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - MSVC 实现改用 `GetModuleNames` 确定完整模块路径。非常感谢 [Daniel Krügler](https://github.com/Dani-Hub) 提交的 [PR#198](https://github.com/boostorg/stacktrace/pull/198)！

  - 改为打印相对地址，以便日后在不知道基址的情况下解码。可通过定义 `BOOST_STACKTRACE_DISABLE_OFFSET_ADDR_BASE` 禁用该逻辑。非常感谢 [Maciej Czarnecki](https://github.com/McCzarny) 提交的 [PR#200](https://github.com/boostorg/stacktrace/pull/200)。

  - 将所有 Stacktrace 库暴露为 b2（Boost 构建工具）特性（feature），以便更好地控制构建并明确显示构建了哪些库。更多信息参见"配置与构建"（Configuration and Build）章节。非常感谢 [Uilian Ries](https://github.com/uilianries) 在 [PR#202](https://github.com/boostorg/stacktrace/pull/202) 中对该特性的初始实现。

  - 修复 MinGW 下 `stacktrace_from_exception` 的构建。感谢 [crhilton](https://github.com/crhilton) 提供修复。

- [TypeIndex](/libs/type_index/)（运行时类型索引库）：

  - 修复 Boost.TypeIndex 在 1.84 中引入的一处未定义行为（UB），该问题曾导致库无法在 clang-20 上构建。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - 文档迁移为使用 Antora 的多页格式。

- [Variant2](/libs/variant2/)（Variant 的现代重实现库）：

  - 索引改用最小的合适无符号类型。

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
