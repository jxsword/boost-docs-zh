# Boost 1.90.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/boost_org_releases_1_90_0.md（原始 URL：https://www.boost.org/releases/1.90.0/，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2025-12-10 16:14 GMT（发布页原文无 GMT 日期行，取 GitHub Release boost-1.90.0 公开时间 2025-12-10T16:14:06Z）

## 总体注记（General Notes）

原文本版无总体注记（General Notes）章节。

## 新增库（New Libraries）

- [OpenMethod](/libs/openmethod)（开放式（多）方法库）：

  - 面向 C++17 及以上的开放式（多）方法（open (multi-)methods），来自 Jean-Louis Leroy。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）

  - 新增 `execution::inline_exception_handling` 属性，用于描述内联执行时所提供的异常处理保证。

  - 新增 `inline_executor`，它总是内联执行提交的函数。

  - 将 `associated_executor` 的默认候选执行器从 `system_executor` 改为 `inline_executor`。

  - 新增 `inline_or_executor<>` 适配器与 `inline_or()` 辅助函数：尽可能内联执行，否则委托给另一个执行器。

  - 新增 `dispatch`、`post` 与 `defer` 的重载：接受一个要在目标执行器上运行的函数对象，并把结果递交给完成处理程序。

  - 新增 `redirect_disposition` 完成令牌（completion token）适配器，作为 `redirect_error` 的通用对应物。

  - 用 `[[deprecated]]` 属性标注已弃用条目。

  - 新增配置参数 "reactor" / "reset_edge_on_partial_read"，决定使用 `epoll` 时部分读取是否消费边沿触发事件。

  - 新增配置参数 "reactor" / "use_eventfd" 与 "reactor" / "use_timerfd"，分别决定 `epoll` 后端是否使用 `eventfd` 与 `timerfd`。

  - 补上缺失的 `BOOST_ASIO_DISABLE_TIMERFD` 预处理检查。

  - 除 `std::experimental::source_location` 外，还实现了对 `std::source_location` 支持的编译期特性检查。

  - 停止使用已弃用的 `boost::array::c_array()` 函数。

  - 修复 `asio::awaitable` 移动赋值中的资源泄漏。

  - 修复 `ssl` 流移动赋值中的内存泄漏。

  - 修复 `kqueue` reactor（反应器）中的线程 sanitizer 问题。

  - 修复 `io_uring` 后端中的处理程序跟踪（handler tracking）参数。

  - 修复 `boost::asio::detail::null_thread` 中的未使用参数警告。

  - 改进基于宏的协程实现，确保使用 `__COUNTER__` 时 case 标签是确定性的。

  - 修复同步 SSL 流的 `shutdown`，使其像 `async_shutdown` 一样把 `error::eof` 重映射。

  - 在 Windows 上将 `stream_file` 与 `random_access_file` 改为把文件路径当作 UTF-8 编码字符串处理。

  - 为 `experimental::parallel_group` 与 `experimental::ranged_parallel_group` 新增检测空操作集的检查。

  - 移除针对 `_FORTIFY_SOURCE` 的变通（workaround），并为 `ip::basic_resolver_results` 增加地址长度检查。

  - 修复 `experimental::coro`，增加对 `max` 被定义为宏的防护。

  - 针对较新的 `libc++` 版本更新了 `std::aligned_alloc` 的检测。

  - 各类文档修复与改进。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_90_0/doc/html/boost_asio/history.html)。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - `http::parser` 默认拒绝非标准的报文尾（trailer）字段。

  - `http::basic_parser` 为报文尾字段使用专用回调。

  - 更新了 `http::field` 常量。

  - 修复 `flat_buffer` 与 `multi_buffer` 中分配器的移动/拷贝赋值。

  - 修复部分消费消息时 websocket permessage-deflate 的错误。

  - `http::buffer_body` 忽略空 chunk。

  - 新增 `http::basic_fields::contains` 成员函数。

  - 移除对 Boost.Preprocessor 与 Boost.StaticAssert 的依赖。

- [Bloom](/libs/bloom/)（布隆过滤器库）：

  - 新增批量（bulk）模式的插入与查找，以提升性能。

  - 将 `block`、`fast_multiblock32` 与 `fast_multiblock64` 的查找实现改为无分支（branchless），带来一定性能收益，对成功/失败混合查询尤其明显。

- [Charconv](/libs/charconv/)（字符与数值互转库）：

  - 修复交叉编译时 CMake 对 quadmath 的检测。

  - 修复浮点 `to_chars` 中足够大的缓冲区反而报"不够大"错误的问题。

- [Compat](/libs/compat/)（标准库补丁库）：

  - 新增 `to_underlying.hpp`（由 Braden Ganetsky 贡献）。

- [Container](/libs/container/)（扩展容器库）：

  - 重新实现 `deque`。原实现基于 SGI 的原始数据结构（与 libstdc++ 类似）。主要变更：

    - `sizeof(deque)` 从 10 个字（word）减到 4 个字。可能是现有实现中最轻量的。

    - `sizeof(deque::iterator)` 从 4 个字减到 2 个字（与 libc++ 和 MSVC 类似）。

    - 重新实现了多个内部算法，以加速 deque 分段（segmented）结构的相关操作。

    - 默认值略有调整：64 位平台默认改用 1024 字节块，而非经典 SGI 的 512 字节块。

    - 新实现便于未来进一步衍生 deque 类变体与优化。

  - 修复的缺陷/issue：

    - [GitHub \#248："boost-1.80.0 引入的 flat_map 插入缓慢"](https://github.com/boostorg/container/issues/248)。

    - [GitHub \#254："C++20 std::erase_if"](https://github.com/boostorg/container/issues/254)。

    - [GitHub \#293："UBSAN 报告非对齐访问错误"](https://github.com/boostorg/container/issues/293/)。

    - [GitHub \#294："CMake：添加使用仅头文件库 Boost::container 的选项"](https://github.com/boostorg/container/pull/294)。

    - [GitHub \#300："用 Clang 20 构建时的警告"](https://github.com/boostorg/container/issues/300)。

    - [GitHub \#304："将 boost::container::small_vector 与自定义分配器一起使用"](https://github.com/boostorg/container/issues/304)。

    - [GitHub \#305："-Wstrict-prototypes 警告"](https://github.com/boostorg/container/pull/305)。

    - [GitHub \#307："修复所有 MSVC 警告 C4146（无符号取负）实例"](https://github.com/boostorg/container/pull/307)。

    - [GitHub \#309："boost v1.86 引入的 boost::container::static_vector 性能回退"](https://github.com/boostorg/container/issues/309)。

    - [GitHub \#306："new_allocator.hpp 错误：'\_\_cpp_sized_deallocation' 未定义，取值为 0 \[-Werror,-Wundef](https://github.com/boostorg/container/issues/306)"\]。

    - [GitHub \#310："flat_map：在 emplace 与 emplace_hint 文档中写明正确的类型"](https://github.com/boostorg/container/issues/310)。

    - [GitHub \#312："flat_map std::allocator::is_always_equal 已弃用"](https://github.com/boostorg/container/issues/312)。

    - [GitHub \#317："部分回退 Issue \#209 的修改——编译器警告"](https://github.com/boostorg/container/pull/317/)。

    - [GitHub \#321："devector 无法与 pmr 分配器一起工作"](https://github.com/boostorg/container/pull/321/)。

- [Conversion](/libs/conversion/)（类型转换库）：

  - 移除对 Boost.SmartPtr 的依赖。

- [Core](/libs/core/)（核心工具集库）：

  - 重新实现了 `boost/core/lightweight_test.hpp` 中定义的 `BOOST_TEST_THROWS` 与 `BOOST_TEST_NO_THROW` 宏，以避免某些编译器在 `if`/`else` 块中使用这些宏时产生警告。此变更的副作用是：宏之后必须写分号。（[PR#205](https://github.com/boostorg/core/pull/205)）

  - 当编译器提供 `std::data` 与 `std::size` 时，`boost::data` 与 `boost::size` 现在分别是它们的别名。这解决了编译器同时找到 `boost::` 与 `std::` 两套候选（例如由 ADL 引起）时的潜在歧义。（[PR#206](https://github.com/boostorg/core/pull/206)）

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 修复将 `std::error_code` 传给 `boost::system::error_code&` 引发的问题。非常感谢 [Thomas Klausner](https://github.com/0-wiz-0) 的修复（[PR#106](https://github.com/boostorg/dll/pull/106)）。

  - 修复 CMake 安装。非常感谢 [Yury Bura](https://github.com/yurybura) 的修复（[PR#103](https://github.com/boostorg/dll/pull/103)）。

  - 修复 `size` 变量遮蔽。

- [DynamicBitset](/libs/dynamic_bitset/)（动态位集库）：

  - 新增 C++20 迭代器。

  - 允许选择底层容器类型。

  - 以 C++20 或更高标准编译时新增 constexpr 支持。

  - 提升 push_back()、pop_back() 与 lowest_bit() 的效率。

  - 将来自 basic_string 的构造函数改为 explicit。

  - 移除若干依赖。

  - 新增 push_front()、pop_front()、find_first_off()、find_next_off()，以及来自 C 风格字符串与 basic_string_view 的构造函数（后者需 C++17 或更高）。

  - 将流插入器改为在输出期间抛出异常时设置 badbit。

  - 将流提取器改为重抛来自底层 vector 的任何异常。

  - 将文档移植到 MrDocs（译注：C++ 文档生成器）与 Antora（译注：文档站点生成工具）。

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - `permissions` 操作成功完成时清除传入的 `error_code` 实参。（[PR#338](https://github.com/boostorg/filesystem/pull/338)）

  - 在 Windows 上，针对要求 SMB 签名时 `directory_iterator` 构造函数在 Samba 3.0.2 共享上报 "Invalid Signature"（无效签名）错误的情形增加变通。（[\#334](https://github.com/boostorg/filesystem/issues/334)）

- [Flyweight](/libs/flyweight/)（享元模式库）：

  - 修复 Clang 19 及更高版本因支持 [P0522R0](https://wg21.link/p0522r0) 引起的编译错误。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 重大改进

    - [GitHub \#1409："为多面体曲面实现 is_valid 算法"](https://github.com/boostorg/geometry/pull/1409)。

  - 功能增强

    - [GitHub \#1413："添加 convert 支持的组合"](https://github.com/boostorg/geometry/pull/1413)。

    - [GitHub \#1417："改进文档"](https://github.com/boostorg/geometry/pull/1417)。

    - [GitHub \#1423："避免 traverse 中的栈溢出"](https://github.com/boostorg/geometry/pull/1423)。

  - 已解决问题

    - [GitHub \#1006："bg::projections::detail::epsg_to_parameters 导致过长的编译时间"](https://github.com/boostorg/geometry/issues/1006)。

    - 各类错误与警告的修复。

- [GIL](/libs/gil/)（通用图像库）：

  - 功能增强

    - [GitHub \#773："改进文档（直方图与错别字）。修复最新 sphinx 版本的构建。"](https://github.com/boostorg/gil/pull/773)。

  - 已解决问题

    - [GitHub \#778："修复 Clang 构建"](https://github.com/boostorg/gil/pull/778)。

- [Interprocess](/libs/interprocess/)（进程间通信库）：

  - 若干小的文档修复。

  - 修复的缺陷：

    - [GitHub \#245："修复 UBSan 运行时错误（加载 'boost::interprocess::mode_t'）"](https://github.com/boostorg/interprocess/pull/245)。

    - [GitHub \#269："若干文档修复与模板参数重命名"](https://github.com/boostorg/interprocess/pull/269)。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 移除对 Boost.Align 与 Boost.StaticAssert 的依赖。

  - 改用更快的哈希算法。

- [LexicalCast](/libs/lexical_cast/)（字符串与数值等类型转换库）：

  - 针对浮点特殊值到整数与 bool 的转换增加更多测试与修复。修复从 `float` 到 `bool` 词法转换时编译器警告 C4804。

  - 移除对 Boost.TypeTraits 的依赖。非常感谢 [Romain Geissler](https://github.com/Romain-Geissler-1A) 完成主要工作（[PR#87](https://github.com/boostorg/lexical_cast/pull/87)）。

  - 从隐式类型转换改为显式类型转换以避免编译器警告。非常感谢 [bmagistro](https://github.com/bmagistro) 提交的 PR（[PR#85](https://github.com/boostorg/lexical_cast/pull/85)）。

  - 修复文档错误。非常感谢 [ivanpanch](https://github.com/ivanpanch) 提交的 PR（[PR#86](https://github.com/boostorg/lexical_cast/pull/86)）。

  - 修复在无 `wchar_t` 内建类型平台上 `unsigned short` 到 `wstring` 转换的回归。

- [Locale](/libs/locale/)（本地化与 Unicode 文本处理库）：

  - 修复 B2 构建文件，避免在仅请求静态版本时构建各 Boost 库的动态版本（[PR#266](https://github.com/boostorg/locale/pull/266)）。

  - 当请求 ISO8859-1 或 ISO8859-8 编码时，若所选 Windows locale 不支持该 ISO8859 编码，允许分别改用 Windows 代码页 1252 或 1255，而不是使用 "C"（经典）locale。

  - 启用针对 Cygwin 标准库在把某些过长 UTF-8 序列转换为 UTF-16 时问题的变通。

- [Log](/libs/log/)（日志库）：

  - 修复 `value_ref` 访问（visitation）中错失的优化。

  - 修复 `text_file_backend` 中日志文件轮转可能出现的漫长而无效的循环。当日志文件名模式不含文件计数器且日志文件大小超过 `rotation_size` 上限时，sink 后端会不断尝试以不同计数器值打开新日志文件，结果每次都打开同一个文件。（[\#252](https://github.com/boostorg/log/issues/252)）

  - 使 `text_file_backend` 中的文件大小检查对整数溢出更健壮。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - 新增子库：反向模式自动微分（Reverse-Mode Automatic Differentiation）。

  - 新增常量：`log_pi`。

  - 为 `logit`、`logistic_sigmoid` 与 `logistic` 分布添加正确的提升策略（promotion policy）支持。

  - 对特殊函数的大量修复与边界情形修补。

- [Mp11](/libs/mp11/)（C++11 元编程库）：

  - 更新 `mp_reverse_fold` 以支持定长列表。

- [MQTT5](/libs/mqtt5/)（MQTT 5.0 客户端库）：

  - 移除对 Boost.Spirit 的依赖。

  - 自动重连现在在任何传输层错误时触发，而不再限于一个小的白名单（[\#38](https://github.com/boostorg/mqtt5/issues/38)）。

  - 为 Logger 接口新增 `at_transport_error` 回调。

- [MSM](/libs/msm/)（有限状态机库，Meta State Machine）：

  - 翻新并更新文档，改用 Antora。

  - 新增后端 `backmp11`：大幅缩短编译时间、API 经过重构并带有若干新特性。要求 C++17，详情见文档。

  - 修复缺陷 [GitHub \#87："boost::any 在 1.86 中不再能作为 boost::msm 的 Kleene 事件使用"](https://github.com/boostorg/msm/issues/87)。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - 对较新的 `cpp_double_fp_backend` 的测试与覆盖进行重大改进。

- [MySQL](/libs/mysql/)（MySQL 客户端库）：

  - 弃用对 4.0 之前 Clang 版本的支持。这些编译器可能仍能工作，但不再在 CI（持续集成）中主动测试。

  - 新增保证与 MySQL 9.x 兼容的测试。

  - 新增保证与最高至 Clang 20、GCC 15 兼容的测试。

- [Parser](/libs/parser/)（解析器组合库）：

  - 修复将仅移动（move-only）可调用对象与闭包一同使用时的非法构形（ill-formed）（[PR#284](https://github.com/boostorg/parser/pull/284)）

  - 修复 `GlobalState` 解析器模板参数中别扭的 `const` 不兼容（[\#250](https://github.com/boostorg/parser/issues/250)）。

  - 修复某些情形下使用排列解析器（permutation parser）时的非法构形（[\#268](https://github.com/boostorg/parser/issues/268)）。

  - 修复序列解析中的错误：某些属性可能被序列中后续解析器覆盖（[\#279](https://github.com/boostorg/parser/issues/279)）。

  - 修复 opt 解析器的处理：即使产生它的解析器已失败，`std::optional` 属性仍可能残留值（[\#279](https://github.com/boostorg/parser/issues/279) 与 [\#285](https://github.com/boostorg/parser/issues/285)）。

  - 多项运行时优化（[\#245](https://github.com/boostorg/parser/issues/245)、[PR#254](https://github.com/boostorg/parser/pull/254)、[PR#255](https://github.com/boostorg/parser/pull/255)、[PR#256](https://github.com/boostorg/parser/pull/256)）。

  - 适度的编译期与代码体积优化（[\#250](https://github.com/boostorg/parser/issues/250)）。

  - 使 `transform` 支持 `constexpr`（[PR#275](https://github.com/boostorg/parser/pull/275)）。

  - 缓解"移动还是转发（move-versus-forward）"警告（[\#272](https://github.com/boostorg/parser/issues/272)）。

  - 修正 `if_` 指令属性类型的文档（[\#278](https://github.com/boostorg/parser/issues/278)）。

  - 修正文档中许许多多的错别字（[PR#271](https://github.com/boostorg/parser/pull/271)）。

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - 新增基于 C++26 解包到参数包（destructuring into a pack）的实现，**修复了本库大多数已知限制**并避免过度的模板实例化。新实现可通过新宏 `BOOST_PFR_USE_CPP26` 显式启用/禁用。非常感谢 [Jean-Michaël Celerier](https://github.com/jcelerier) 提交的 PR（[PR#194](https://github.com/boostorg/pfr/pull/194)）。

  - 对 CMake 的多项修复。非常感谢 [Alexander Grund](https://github.com/Flamefire) 提交的 PR！

- [Random](/libs/random/)（随机数生成器与分布库）：

  - 修复从 SeedSeq 构造 xoshiro 系列生成器的问题。

- [Redis](/libs/redis/)（Redis 客户端库）：

  - **取消（cancellation）**方面的重要变更：

    - 改进 `async_exec()` 中的逐操作支持，并新增对 `asio::cancel_after` 的支持。请求现在可以在任意时刻取消，且取消不会以任何方式干扰其他请求。Pull request [PR#310](https://github.com/boostorg/redis/pull/310) 与 [\#226](https://github.com/boostorg/redis/issues/226)。

    - 弃用 `request::config` 中的 `cancel_on_connection_lost` 与 `cancel_if_not_connected` 标志。要限制 `async_exec` 可能耗时，请改用 `asio::cancel_after`。`cancel_on_connection_lost` 默认值已改为 `false`。Pull request [PR#329](https://github.com/boostorg/redis/pull/329) 与 [PR#334](https://github.com/boostorg/redis/pull/334)。

    - 弃用对 `cancel` 传入 `operation::resolve`、`connect`、`ssl_handshake`、`reconnection` 与 `health_check` 的调用。用户应改用 `cancel(operation::run)`。Pull request [PR#321](https://github.com/boostorg/redis/pull/321)。

    - 在 `async_run()` 中新增逐操作取消支持。Issue [\#319](https://github.com/boostorg/redis/issues/319)。

  - 新增使用 `config::setup` 的**自定义 setup 请求**支持。设置这些字段后，用户可以用任意的其他请求取代库生成的 `HELLO` 请求。Issue [\#302](https://github.com/boostorg/redis/issues/302) 与 pull request [PR#303](https://github.com/boostorg/redis/pull/303)。

  - 弃用 `request::config::hello_with_priority`。如果需要在任何其他请求之前执行某请求，请改用 `config::setup`。Pull request [PR#305](https://github.com/boostorg/redis/pull/305)。

  - **Valkey**（译注：Redis 的开源分支）长期支持（LTS）：自本版本起我们保证 Valkey 兼容性。Issue [\#296](https://github.com/boostorg/redis/issues/296)。

  - 新增 `request::append()` 函数，用于拼接请求对象。Issue [\#341](https://github.com/boostorg/redis/issues/341)。

  - 健康检查算法重新设计，避免高负载下的误报。`PING` 命令现在只在连接空闲时发出，而不再周期性发出。Issue [\#104](https://github.com/boostorg/redis/issues/104)。

  - 新增 `config::read_buffer_append_size`，可控制连接读缓冲区的扩容。Pull request [PR#283](https://github.com/boostorg/redis/pull/283)。

  - 新增 `usage::bytes_rotated`，度量从服务器读取并解析数据时的数据复制量。Pull request [PR#311](https://github.com/boostorg/redis/pull/311)。

  - 缺陷修复：

    - 修复把包含中间错误的响应解析进 `generic_response` 时抛出异常的缺陷。Issue [\#287](https://github.com/boostorg/redis/issues/287)。

    - 修复 `connection` 与 `basic_connection` 的 `cancel()` 函数中可能导致取消被忽略的若干竞态条件。Issue [\#318](https://github.com/boostorg/redis/issues/318)。

    - 空密码但用户名非默认值的用户现在能通过正确认证。Issue [\#298](https://github.com/boostorg/redis/issues/298)。

    - 修复一个可能导致 `HELLO` 期间出错后，重连期间后续 `HELLO` 尝试也失败的问题。Issue [\#290](https://github.com/boostorg/redis/issues/290)。

    - `HELLO` 期间的错误现在会被正确记录。Issue [\#297](https://github.com/boostorg/redis/issues/297)。

- [SmartPtr](/libs/smart_ptr/)（智能指针库）：

  - 已移除由弃用宏 `BOOST_SP_ENABLE_DEBUG_HOOKS`、`BOOST_SP_USE_STD_ALLOCATOR` 与 `BOOST_SP_USE_QUICK_ALLOCATOR` 启用的功能。

  - 头文件 `<boost/smart_ptr/detail/quick_allocator.hpp>` 已标记为弃用，将在未来发布中移除。

  - 不再支持定义 `BOOST_NO_CXX11_HDR_ATOMIC` 的配置；现在要求符合标准的 C++11 `<atomic>`。

  - 弃用宏 `BOOST_AC_USE_SPINLOCK`、`BOOST_AC_USE_PTHREADS`、`BOOST_SP_USE_SPINLOCK` 与 `BOOST_SP_USE_PTHREADS` 已不再生效。

  - `atomic_count`、`sp_counted_base` 与 `spinlock` 的平台特定实现已不再使用并被移除。

  - 不再支持定义 `BOOST_NO_CXX11_HDR_MUTEX` 的配置；现在要求符合标准的 C++11 `<mutex>`。

  - 移除 `boost/smart_ptr/detail/` 中一些未使用的头文件。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 修复缺失的 include。感谢 [Orgad Shaneh](https://github.com/orgads) 的修复！

  - 修复 `libbacktrace_impls.hpp` 中的 URL，感谢 [Jonathan Wakely](https://github.com/jwakely)。

- [StaticString](/libs/static_string/)（固定容量字符串库）：

  - 使 `to_static_[w]string()` 在 C++26 下与 `std::to_[w]string()` 对齐。

  - 移除 `to_static_[w]string()` 中额外缓冲区的使用。

  - 新增 `resize_and_overwrite()`。

- [STLInterfaces](/libs/stl_interfaces/)（迭代器/范围定制点 CRTP 基类库）：

  - 修复 GCC 14 下的非法构形（[PR#80](https://github.com/boostorg/stl_interfaces/pull/80)）。

  - 修复将仅移动可调用对象与闭包一同使用时的非法构形。

- [Test](/libs/test/)（单元测试框架库）：

  - 修复 Windows Clang 上的几个警告。

- [TypeIndex](/libs/type_index/)（运行时类型索引库）：

  - 移除对 Boost.Core 的依赖。

  - 所有测试现在也在 CMake 中运行。非常感谢 [Alexander Grund](https://github.com/Flamefire) 的若干修复与帮助。

- [URL](/libs/url/)（URL 解析库）：

  - `segments_view` 与 `segments_encoded_view` 新增常数时间的基于迭代器的子视图构造函数。

  - 新增 zone-id 设置器（例如用于 IPv6 链路本地地址）。

  - 主机设置器现在接受/传播 zone-id。

  - 修复：`resolve` 现在在所有情况下都复制引用片段（fragment）（[\#920](https://github.com/boostorg/url/issues/920)）。

  - 修复：`encoded_host_address` 的断言将 zone-id 计入。

  - 重构：以 `BOOST_CORE_STATIC_ASSERT` 取代 `BOOST_STATIC_ASSERT`（[\#934](https://github.com/boostorg/url/issues/934)）。

  - 重构：为段子视图保留绝对（absolute）语义（[\#939](https://github.com/boostorg/url/issues/939)）。

- [Uuid](/libs/uuid/)（UUID 生成与解析库）：

  - `string_generator` 现在在 C++14 及更高标准下为 `constexpr`。

  - 新增头文件 `boost/uuid/constants.hpp`。

  - 将 `boost/uuid/uuid_generators.hpp` 重命名为 `boost/uuid/generators.hpp`。旧名称为兼容而保留。

- [Variant2](/libs/variant2/)（Variant 的现代重实现库）：

  - 更多函数标记为 `constexpr`，包括 `~variant`。这在 C++20 之前无关紧要，但现在有意义。

## 更新的工具（Updated Tools）

原文本版无"更新的工具（Updated Tools）"章节。

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
