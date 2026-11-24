# Boost 1.86.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_86_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_86_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2024-08-14 16:07 GMT（原文日期行：August 14th, 2024 16:07 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.86.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 新增库（New Libraries）

本版无新增库（原文明确写明"No new libraries."）。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 修改 `default_completion_token` 特征（traits）的主模板，使其选择 `deferred` 作为默认完成标记（completion token）。因此，大多数异步操作的发起函数默认会返回一个延迟（deferred）异步操作。

  - 新增 `is_completion_condition` 特征，并为 `async_read`、`async_read_at`、`async_write` 与 `async_write_at` 的重载补上缺失的默认完成标记。

  - 新增 `is_connect_condition` 特征，并在完成标记使用默认值时用它消除 `async_connect` 重载的歧义。

  - 扩展完成标记适配器 `as_tuple`、`bind_allocator`、`bind_cancellation_slot`、`bind_executor`、`bind_immediate_executor` 与 `redirect_error`，使它们可用作部分完成标记适配器。

  - 新增 `cancel_after` 与 `cancel_at` 完成标记适配器。

  - 修改所有完成标记适配器，确保它们在适配过程中正确传播异步操作的 I/O 执行器（executor）。

  - 将 `co_composed` 移出 `experimental` 命名空间。

  - 新增 `composed`，它从有状态的实现创建发起函数对象。它与 `co_composed` 类似，但面向普通函数对象而非 C++20 协程（coroutine）。

  - 修改 `detached` 完成标记，使其可用于具有多个完成签名（completion signature）的异步操作。

  - 修改 `async_initiate`，允许空的可变参数完成签名列表，表示异步操作永不完成。

  - 新增自动推导完成标记类型的 `async_initiate` 重载。

  - 新增 `async_immediate`，实现一个立即完成的平凡异步操作，若有可用的关联立即执行器（immediate executor）则使用之。

  - 启用 `associator` 特征基于 SFINAE 的部分特化。

  - 若干缺陷修复、编译器/平台兼容性改进以及小幅优化。

  - 文档与示例的各类更新。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_86_0/doc/html/boost_asio/history.html)。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 在 OpenBSD 上改用 [futex(2)](https://man.openbsd.org/OpenBSD-6.2/futex.2) 系统调用，因为较新的 OpenBSD 版本已移除对 `syscall(2)` 的支持。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - API 变更：

    - 新增 HTTP 状态码 418 `I'm a teapot`（我是一个茶壶）。

  - 缺陷修复：

    - `read_size_hint_db()` 中的收窄转换。

    - 使用默认完成标记时产生歧义的重载。

    - `http::basic_fields` 移动赋值运算符中 `static_assert` 位置不当。

    - WebSocket 部分写操作中 `bytes_transferred` 下溢。

    - `websocket::stream::read_size_hint()` 的结果不超过 `read_message_max`。

    - 测试中的各类警告。

    - 示例中 SSL 关闭操作的错误处理。

    - 为 zlib 中的贯穿（fallthrough）分支添加标注。

    - `basic_stream::ops::transfer_op` 中对过期定时器的处理。

    - `test::basic_stream` 构造函数重载的歧义。

    - `http::parser` 对最后一个 chunk 的部分解析。

  - 功能增强：

    - `server_flex_awaitable` 示例支持优雅关闭。

    - 简化 awaitable 示例。

    - 新增模糊测试（fuzzing）目标。

    - 移除部分示例中对 `std::bind` 的多余使用。

    - `ssl_stream` 不再使用 `flat_stream`。

  - 文档：

    - `ssl_stream` 与 `flat_stream` 标记为弃用。

    - 代码片段与示例中以 `net::ssl::stream` 为准。

    - 新增"SSL/TLS 关闭流程"（SSL/TLS Shutdown Procedure）章节。

  - 致谢：

    - tyler92、Ruslan Zakirov、Orgad Shaneh、Alexander Kernozhitsky

- [Charconv](/libs/charconv)（字符与数值互转库）：

  - 修复 PPC64LE 架构的支持。

  - 修复对 Alpine Linux 等提供 `<quadmath.h>` 头文件但未提供编译库的平台的支持。

  - 修复整数类型 `from_chars` 的首字符模式匹配。

  - 修复基数大于 10 时整数的溢出检测。

  - 新增对 `std::float16_t` 与 `std::bfloat16_t` 的原生支持，不再使用交换格式（interchange formats）。

- [Cobalt](/libs/cobalt)（C++20 协程库）：

  - 新增对 `asio::cancel_after` 的支持。

  - 使 `asio::deferred` 可被 `co_await`，因为它是 Asio 的默认标记。

  - 新增 `noop` 工具。

  - 新增对栈式协程/纤程（fiber）的实验性支持。

  - 修复 channel 与协程类型的可移动性。

- [Compat](/libs/compat/)（标准库补丁库）：

  - 新增 `bind_front.hpp`、`bind_back.hpp`、`invoke.hpp`、`mem_fn.hpp`、`integer_sequence.hpp` 与 `type_traits.hpp`。

  - 新增 `function_ref.hpp`。

- [Container](/libs/container/)（扩展容器库）：

  - 修复的缺陷/issue：

    - [GitHub \#285："devector\<\>::push_front 在 clear() 之后触发断言"](https://github.com/boostorg/container/issues/285)。

    - [GitHub \#280："多个容器在移动赋值时不支持不可移动类型"](https://github.com/boostorg/container/issues/280)。

    - [GitHub \#279："small_vector 无法回退使用栈空间"](https://github.com/boostorg/container/issues/279)。

    - [GitHub \#277："移除对 boost::static_assert 的依赖"](https://github.com/boostorg/container/issues/277)。

    - [GitHub \#275："使用自定义键比较时编译失败"](https://github.com/boostorg/container/issues/275)。

    - [GitHub \#273："flat_map/vector 在追加时崩溃（内存损坏）"](https://github.com/boostorg/container/issues/273)。

    - [GitHub \#269："GCC 下 flat_multimap::emplace 不对元素排序"](https://github.com/boostorg/container/issues/269)。

    - [GitHub \#266："32 位下 small_vector\<T\> 在栈上未对齐"](https://github.com/boostorg/container/issues/266)。

    - [GitHub \#259："全局变量"](https://github.com/boostorg/container/issues/259)。

    - [GitHub \#245："flat_tree::insert 有序范围不断言有序性"](https://github.com/boostorg/container/issues/245)。

    - [GitHub \#241："flat_map 应支持与 std::map 相同的接口"](https://github.com/boostorg/container/issues/241)。

- [Core](/libs/core/)（核心工具集库）：

  - 新增 `boost/core/pointer_in_range.hpp` 头文件，其中的 `pointer_in_range` 函数模板用于检查指针是否位于给定范围内（Glen Fernandes）。

  - 修复抽象类的 `type_name`（[\#172](https://github.com/boostorg/core/issues/172)）。

  - 修复 MSVC 禁用原生 `wchar_t` 类型时 `boost/core/type_name.hpp` 的编译错误（[\#173](https://github.com/boostorg/core/issues/173)）。

  - 针对 MSVC 一个导致 `empty_value` 与嵌套类一起使用时出现编译错误的[缺陷](https://developercommunity.visualstudio.com/t/Compiler-bug:-Incorrect-C2247-and-C2248/10690025)添加了变通方案（[PR#175](https://github.com/boostorg/core/pull/175)）。

- [CRC](/libs/crc/)（CRC 校验库）：

  - 不再支持 C++03，需要 C++11 编译器（包括 GCC 4.6 或更高版本，以及 MSVC 10.0（VS 2010）或更高版本）。

  - 移除对 Array、Config、Integer 与 TypeTraits 的依赖。该库现在是独立的。

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - `is_empty` 操作现在更好地防范文件系统的并发修改。

  - 在 POSIX 系统上，`is_empty` 若作用于普通文件或目录之外的文件，现在会指示错误。

  - 在 Windows 上，修复 `file_size` 与 `is_empty` 作用于符号链接而非其指向的文件的问题（[\#313](https://github.com/boostorg/filesystem/issues/313)）。

  - `directory_entry::refresh` 在条目引用的文件不存在时不再抛出异常。这使得 `directory_entry::status` 与 `directory_entry::symlink_status` 以及基于它们的方法，与对应的独立操作行为类似。文件不存在的事实仍通过相应 `directory_entry::refresh` 重载返回的 `error_code` 指示，也可通过检验 `directory_entry::status` 或 `directory_entry::symlink_status` 调用返回的文件类型是否为 `file_type::file_not_found` 来判断（[\#314](https://github.com/boostorg/filesystem/issues/314)）。

  - 修复 `weakly_canonical` 在输入路径为相对路径时，以当前路径而非调用中指定的基路径检验路径元素存在性的问题。

  - 在 Windows 上，修复输入路径以 ".." 开头时 `weakly_canonical` 产生错误结果路径的问题（[\#311](https://github.com/boostorg/filesystem/issues/311)）。

- [Format](/libs/format/)（类型安全 printf 风格格式化库）：

  - 不再支持 C++03，需要 C++11 编译器（包括 GCC 4.7 或更高版本，以及 MSVC 12.0（VS 2013）或更高版本）。

- [Function](/libs/function/)（多态函数包装库）：

  - 移除对 Boost.TypeTraits 的依赖。

  - 恢复了 1.85 中意外丢失的 `argN_type` typedef。

- [GIL](/libs/gil/)（通用图像库）：

  - 新增：

    - 为 `istream_device` 与 `ostream_device` 类添加 `tell()` 与 `error()` 函数（[PR#747](https://github.com/boostorg/gil/pull/747)）。

  - 变更：

    - `color_converted_view` 函数不再忽略自定义颜色转换器（[PR#726](https://github.com/boostorg/gil/pull/726)）。

    - 针对与 WinAPI `min()` 与 `max()` 宏的冲突添加变通方案（[PR#745](https://github.com/boostorg/gil/pull/745)）。

    - GIL 中 `boost::filesystem` 的使用现在可通过 CMake 选项 `BOOST_GIL_USE_BOOST_FILESYSTEM` 配置（[PR#743](https://github.com/boostorg/gil/pull/743)）。

  - 修复：

    - 修复 `convolve_2d` 中的卷积（[PR#723](https://github.com/boostorg/gil/pull/723)）。

    - 归一化二维高斯核以避免图像变暗（[PR#725](https://github.com/boostorg/gil/pull/725)）。

    - 修复路径字符串转换函数中对 `std::wstring` 的缓冲区大小错误，避免在 I/O 相关函数中使用 `std::wstring` 路径时发生缓冲区溢出（[PR#746](https://github.com/boostorg/gil/pull/746)）。

  - 致谢：

    - Christoph Gringmuth、Christopher Kormanyos、nicolacandussi、Dirk Stolle、Olzhas Zhumabek

- [Graph](/libs/graph/)（图结构与算法库）：

  - *重大*更新：C++14 成为新的最低标准；这一部分由依赖决定（依赖至少要求 C++11），一部分出于自主选择。如需更旧标准的支持，请联系维护者。

  - 移除对 Boost.Regex 的直接依赖。

  - 修复若干因未显式包含公共头文件导致的编译错误。

  - `isomorphism`：修复文档；忽略 `vertex_max_invariant` 参数，改为廉价计算上排除界（upper exclusive bound）；修复关联属性映射（Associative Property Map）的缺陷；将空间效率从与最大不变量大小成线性改为与 g1 的大小成线性。

  - `boykov_kolmogorov_max_flow`：修复具名参数重载。

  - `adj_list_edge_iterator`：修复 maybe-uninitialized 警告。

  - `hawick_circuits`：新增可选限制搜索深度的参数，从而可提前返回可能次优的答案。

  - `disjoint_sets`：通过移除对集合代表元的冗余查找，改进 `link_sets` 的性能。

  - `maximum_adjacency_search`：重构并增加更多测试。

  - `property`：使用 `BOOST_ATTRIBUTE_NO_UNIQUE_ADDRESS` 消除空间浪费。

  - `labeled_graph`：修复 `remove_labeled_vertex`，使其确实同时移除标签。

  - `r_c_shortest_paths`：修复单解变体并不总是返回最短路径的缺陷。

  - `read_graphviz`：修复栈溢出（oss-fuzz issue 66719）与非关键字子图解析。

  - 众多杂项改进：失效链接、笔误等。

- [Interprocess](/libs/interprocess/)（进程间通信库）：

  - 修复的缺陷：

    - [GitHub \#191（"vectorstream：支持大于 INT_MAX 的文件大小"）](https://github.com/boostorg/interprocess/pull/191)。

    - [GitHub \#198（"offset_ptr 文档的小修复"）](https://github.com/boostorg/interprocess/pull/198)。

    - [GitHub \#202（"允许在匿名内存中映射 message_queue"）](https://github.com/boostorg/interprocess/pull/202)。

    - [GitHub \#207（"cmake：链接系统库"）](https://github.com/boostorg/interprocess/pull/207)。

    - [GitHub \#214（"文档：修复 GitHub 链接"）](https://github.com/boostorg/interprocess/pull/214)。

- [Intrusive](/libs/intrusive/)（侵入式容器库）：

  - 修复缺陷 [GitHub \#86：注释中的无效 UTF-8 字符](https://github.com/boostorg/intrusive/issues/86)。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 对 GCC 5.0 之前版本的支持已弃用，并**将在 Boost 1.88.0 中停止**。

  - 抛异常的访问器函数新增 `source_location` 参数。

  - 新增解析选项：容忍无效的 UTF-16 代理对（surrogate pairs）并产出 [WTF-8](https://simonsapin.github.io/wtf-8/)。

  - 新增返回 `system::result` 的访问器函数。

  - 处理直接解析中缺失的错误情形。

- [LexicalCast](/libs/lexical_cast/)（字符串与数值等类型转换库）：

  - 修复包含一个或多个 `\0` 字符的 `std::basic_string_view` 与 `boost::basic_string_view` 的转换。该问题于 1.85.0 引入。

- [leaf](/libs/leaf/)（轻量级错误处理库）：

  - 更优的 `verbose_diagnostic_info` 实现。

  - 缺陷修复。

  - 为类 `result<>` 添加 `[[nodiscard]]`。

- [Locale](/libs/locale/)（本地化与 Unicode 文本处理库）：

  - `conv::utf_to_utf` 新增自定义分配器（allocator）支持。

  - 默认不构建示例。

- [Log](/libs/log/)（日志库）：

  - 针对 MinGW-w64 上在 CMake 中使用 `windres.exe` 编译事件日志资源文件的问题添加了变通方案（[PR#231](https://github.com/boostorg/log/pull/231)）。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - 修正 Bessel（贝塞尔）函数在无穷远处的结果，参见 [1143](https://github.com/boostorg/math/issues/1143)。

  - 改进非中心 T 分布的数值稳定性，参见 [scipy20693](https://github.com/scipy/scipy/issues/20693)。

  - 修正 `float_next`/`float_prior` 在无穷远处的行为。

  - 防止非中心 beta 分布出现虚假下溢，参见 [scipy20693](https://github.com/scipy/scipy/issues/20693)。

  - 改进 Heuman Lambda 函数的精度。

  - 改进偏态正态（Skew Normal）分布的求根，参见 [1120](https://github.com/boostorg/math/issues/1120)。

  - 大量小修复与代码覆盖率的提升。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - 确保 `eval_convert_to()` 处理超大数字时不会终止程序，参见 [618](https://github.com/boostorg/multiprecision/pull/618)。

  - 修复 `sinc` 实现，使其与 Boost.Math 的行为一致。

  - 修复 cpp_int 取模运算中的除零。

  - 修复大于 128 位整数的下溢行为一致性，参见 [626](https://github.com/boostorg/multiprecision/issues/626)。

- [MySQL](/libs/mysql/)（MySQL 客户端库）：

  - 早已弃用的函数 `query`、`start_query`、`execute_statement` 与 `start_statement_execution`（及其异步等价物）已被移除。

  - **对实验性 API 的破坏性变更**：

    - 移除 `identifier` 类（客户端 SQL 格式化）。请改用新的格式说明符（format specifiers）特性。

    - 自定义格式化器所需的接口已变更，以适配新的格式说明符 API。

    - `any_connection::async_connect` 现在要求其 `connect_params` 实参在操作完成前保持存活。接受 `const connect_params*` 的重载已被移除。

    - `character_set::name` 现在是 `const char*` 而非 `string_view`，因为 MySQL 字符集名称不能包含 NULL 字符。

    - `any_connection` 内部缓冲区现在限制为 64MB。如需读写更大的行，请调大 `any_connection_params::max_buffer_size`。`connection` 及其辅助 typedef 不受此限制。

    - `any_connection_params::initial_read_buffer_size` 更名为 `initial_buffer_size`。

    - `pool_params::initial_read_buffer_size` 更名为 `initial_buffer_size`。

  - 新实验性 API：**管道（pipelines）**。管道可将多个请求合并进单个网络分组以提升效率。管道可用于运行文本查询、准备、执行与关闭语句、重置会话状态以及设置连接的字符集。

  - 客户端 SQL 格式化现在开箱即支持范围（ranges）。可使用新的 `sequence` 函数进一步定制格式化。批量插入与批量查询等用例可借助该功能显著简化。

  - 客户端 SQL 格式化现在支持修改值格式化方式的格式说明符。`{:i}` 将字符串格式化为动态 SQL 标识符，`{:r}` 输出未转义的原始内容。

  - 静态接口（`static_results` 与 `static_execution_state`）现在通过 `pfr_by_name` 与 `pfr_by_position` 支持 Boost.Pfr 类型。新增 `underlying_row_t` 以支持此类类型。

  - `date` 与 `datetime` 现在可从 C++20 `std::chrono::local_time` 构造并可转换为后者。

  - 新增 `any_connection_params::max_buffer_size`，允许为连接的内部缓冲区设置上限。

  - 新增 `is_fatal_error`，用户现在可区分致命（需要关闭并重新打开连接）与非致命错误码。

  - 新增 `formattable_ref`，一个类型擦除的引用类型，可引用任何满足 `Formattable` concept（概念）的类型。

  - 修复 MSVC 下的 ODR（单一定义规则）违规：当 Boost.MySQL 与在不同编译单元中同样使用 `asio::coroutine` 的代码一起使用时，可能在 release 构建中引发崩溃。

- [Odeint](/libs/numeric/odeint/)（常微分方程求解库）：

  - 新增 CMake 选项 `BOOST_NUMERIC_ODEINT_NO_ADAPTORS` 以减少依赖，参见 [82](https://github.com/boostorg/odeint/issues/82)。

  - 修复 CMake 对 MPI 的检测。

- [Process](/libs/process/)（进程管理库）：

  - 将旧的 boost.process 移至 v1 子目录与内联命名空间（inline namespace）。弃用 process/*.hpp 的 v1 头文件。

  - 将 v2 转变为需编译库。

  - 修复 Alpine Linux / musl 上的使用。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - **重大新特性：Windows 上从任意异常获取堆栈回溯**。`std::stacktrace::from_current_exception()` 现在可在 Windows 平台上工作。非常感谢 [huangqinjin](https://github.com/huangqinjin) 提交的实现 [PR#159](https://github.com/boostorg/stacktrace/pull/159)。现在在 POSIX 与 Windows 上，`from_current_exception()` 函数都返回当前异常对象的堆栈回溯，就像在抛出异常的位置捕获堆栈一样。

  - 修复包含很少使用的 Windows SDK 头文件的问题，这些头文件可能与其他使用 Windows SDK 的代码冲突。感谢 [Marat Abrarov](https://github.com/mabrarov) 修复该问题 [PR#157](https://github.com/boostorg/stacktrace/pull/157)。

  - 构建选项 `boost.stacktrace.from_exception` 现在在 MacOS 上正常工作。感谢 [Peter Dimov](https://github.com/pdimov) 提供修复 [PR#166](https://github.com/boostorg/stacktrace/pull/166)。

  - 修复断言表达式中的笔误。感谢 [Kilian Henneberger](https://github.com/Ukilele) 提交缺陷报告 [\#164](https://github.com/boostorg/stacktrace/issues/164)。

  - 修复变量遮蔽（shadowing）警告。感谢 [Nigel Stewart](https://github.com/nigels-com) 提交缺陷报告 [\#141](https://github.com/boostorg/stacktrace/issues/141)。

  - 新增 AIX 上 `dladdr` 的最小支持。非常感谢 Clément Chigot 提交实现 [PR#114](https://github.com/boostorg/stacktrace/pull/114)。

  - 新增 `Boost::stacktrace` CMake 别名，指向该平台上受支持最佳的 Boost.Stacktrace 实现。感谢 [Alex](https://github.com/leha-bot) 提供该特性 [PR#167](https://github.com/boostorg/stacktrace/pull/167)。

  - CMake 大幅改进：多处修复、新增大量测试、改进 CI。非常感谢 [Peter Dimov](https://github.com/pdimov) 的所有改进。

  - 修复通过 `PATH` 查找进程时 addr2line 的工作。感谢 [Schreischildkroete](https://github.com/Schreischildkroete) 提交缺陷报告，感谢 [Jens Richter](https://github.com/j-jr-richter) 提供修复 [\#72](https://github.com/boostorg/stacktrace/issues/72)。

- [Test](/libs/test/)（单元测试框架库）：

  - 修复配置步骤中的 `-Wundef`。

  - 修复 MSVC 上"不可达 return"编译错误。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - 当 `<memory_resource>` 头文件可用时，新增容器 pmr 别名。别名 `boost::unordered::pmr::[container]` 指向使用 `std::pmr::polymorphic_allocator` 分配器类型的 `boost::unordered::[container]`。

  - 为开放定址（open-addressing）容器与并发容器加入内部计算并提供受哈希函数质量影响的统计指标的能力。该功能由全局宏 `BOOST_UNORDERED_ENABLE_STATS` 启用。

  - 雪崩（avalanching）哈希函数现在必须通过 `is_avalanching` typedef 标记，其内嵌的 `value` 常量须为 `true`（通常将 `is_avalanching` 定义为 `std::true_type`）。`using is_avalanching = void` 已弃用，但为向后兼容仍允许使用。

  - 新增 Visual Studio Natvis 框架对容器与迭代器的自定义可视化。这适用于所有分配器使用裸指针的容器。本发布中，分配器使用花式指针（fancy pointer）的容器与迭代器暂不支持，后续发布可能解决。

- [UUID](/libs/uuid/)（UUID 生成与解析库）：

  - *重大*更新。

  - 不再支持 C++03，需要 C++11 编译器（包括 GCC 4.8 或更高版本、MSVC 14.0（VS 2015）或更高版本，以及 MinGW-w64）。

  - 将 Boost 依赖数量从 39 个（总计）减至仅 5 个。

  - 更新以反映较新的 [RFC 9562](https://datatracker.ietf.org/doc/rfc9562/)。

  - 新增基于时间的 UUID 生成器。

  - *许多*其他改进，参见[修订历史](/libs/uuid/doc/html/uuid.html#changes)。

- [Wave](/libs/wave/)（C/C++ 预处理器实现库）：

  - 将一处 `vsprintf` 用法替换为更安全的 `vsnprintf`。

  - 修复的缺陷：

    - [\#197](https://github.com/boostorg/wave/issues/197)：有符号溢出处理不当（未定义行为且缺失除法检查）。

- [WinAPI](/libs/winapi/)（Win32 API 薄封装库）：

  - 新增 `BOOST_USE_WINAPI_VERSION` CMake 选项，允许用户指定 Boost 面向的 Windows 版本。

## 更新的工具（Updated Tools）

- [BoostBook](/tools/boostbook/)（BoostBook 文档格式，基于 DocBook 的文档中间格式）：

  - DTD 已更新：`method-group` 元素内部现在允许 `constructor`、`copy-assignment` 与 `destructor` 元素。

  - Doxygen（文档生成器）生成的文档有多处修复与改进：

    - 修复 Doxygen 生成的枚举值初始化器中重复的等号。

    - 禁用函数实参的字母序排序。可通过将新的 `boost.sort.params` XSL 参数设为 1 重新启用排序。

    - 新增对自定义类成员分组的支持。参见 Doxygen 标签 `@name` 与 `@{`/`@}`。

    - 新增对 Doxygen 引用类、方法、枚举、变量等的支持（参见 `@ref` 标签）。

    - 新增对 `@remark` 与 `@important` 标签的支持。

    - 新增对 `@parblock` 标签的支持，可用于在期望单个段落实参的标签（如 `@returns`）下放置多个段落。

    - 指向实现细节的模板参数默认值现在被隐藏，与函数参数默认值类似。

    - 改进未命名枚举的呈现。不再显示 `@0` 之类的合成名称；名称或者省略，或在需要引入指向该枚举文档的链接时显示为 `[unnamed]`。

    - 将"另见"（`@sa`）块改为内联显示，与"返回"（Returns）类似。

    - 修复多个异常说明（`@throws`）的呈现。

    - 新增对抛出行为的自由格式描述的支持。若 `@throws` 标签后的异常类型为 "~"，则输出中省略异常类型，后续描述直接显示在"Throws"章节中。

    - 移除返回类型与模板参数中的多余空格。

- [Build](/tools/build/)（b2 构建系统框架）：

  - 包含 [B2（Boost 构建工具）版本 5.2.1](/tools/build/doc/html/#_version_5_2_1) 的发布。

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
