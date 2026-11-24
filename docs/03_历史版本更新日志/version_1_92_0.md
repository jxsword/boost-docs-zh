# Boost 1.92.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/boost_org_releases_1_92_0.md（原始 URL：https://www.boost.org/releases/1.92.0/，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2026-08-12 11:41 GMT（发布页原文无 GMT 日期行，取 GitHub Release boost-1.92.0 公开时间 2026-08-12T11:41:32Z）

## 总体注记（General Notes）

- 在以往的发布中，Windows 的 `.dll` 文件由 `b2 install` 安装到库目录（默认 `<PREFIX>/lib`），Cygwin（译注：Windows 上的 POSIX 兼容环境）除外——在 Cygwin 上它们被安装到二进制目录（默认 `<PREFIX>/bin`）。

  现已改为统一将 `.dll` 文件安装到二进制目录，这是大多数用户期望的行为。

  为保持兼容，`b2 install` 新增了命令行选项 `--dlldir`，可用于覆盖该目录；如有需要，也可将其指向 `<PREFIX>/lib`。

- 由 `b2 install` 安装的 CMake 配置文件已更新，支持将仅头文件库作为 `find_package` 组件（component）来请求。

  也就是说，像 `find_package(Boost REQUIRED COMPONENTS mp11)` 这样的写法现在可以工作了（并定义目标 `Boost::mp11`），而以前不行（此前只有需编译库才被视为组件）。

  这与用 CMake 构建 Boost 时安装的 CMake 配置文件的行为一致，使得无论 Boost 如何构建与安装，都可以用同一种方式使用它。

  作为这项规范化工作的一部分，很少使用的 `COMPONENTS ALL` 请求特性已被移除。CMake 方式构建的 Boost 不支持它，`FindBoost` 也从未支持过它。

## 新增库（New Libraries）

本版无新增库（原文该栏目为空）。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）

  - 新增 `"scheduler"` / `"assume_continuation"` 配置参数，允许把投递（post）的处理程序加入快速的线程本地（thread-local）队列。

  - 新增用于调优 io_uring 后端的 `"reactor"` 配置参数：`io_uring_ring_count`、`io_uring_ring_size`、`io_uring_submit_batch_size` 与 `io_uring_iowait`。

  - 新增配置 `ssl::stream<>` 内部缓冲区大小的能力。

  - 新增前向声明头文件 `boost/asio/fwd.hpp`，以便在使用带版本命名空间时安全地前向声明 Asio 类名。

  - 新增在协程（coroutine）中使用 `cancel_after` 的示例。

  - 新增在 `BOOST_ASIO_NO_EXCEPTIONS` 下对 `co_composed` 的支持。

  - 补上 `io_context::poll_one()` 在 `concurrency_hint == 1` 时缺失的优化。

  - 将所有异常类改为内联实现，修复某些平台在分离编译（separate compilation）时出现的未定义符号错误。

  - 在 C++17 及更高标准下，将常量与 CPO（定制点对象）改为外部链接。

  - 在 Linux 上将"精简"互斥量（slim mutex）改为使用 futex。

  - reactor（反应器）在支持时改用 `MSG_DONTWAIT`，而不再把套接字设为非阻塞。

  - 修复 MSVC 上 `co_composed` 的两处崩溃：一处发生在使用多个完成签名（completion signature）时，另一处由对齐不足引起。

  - 修复 `cancel_after` 某个重载的返回类型。

  - 修复 `basic_streambuf::commit`/`consume` 中的整数截断问题。

  - 修复 SSL 流被移动时触发的缓冲区失效错误，并澄清了缓冲区失效语义。

  - 修复某些编译器上对完成处理程序使用 `post`、`dispatch` 或 `defer` 时出现的编译错误。

  - 修复 `parallel_group` 对非终结（non-terminal）取消请求的处理。

  - 修复由原子线程栅栏（thread fence）引发的若干线程 sanitizer 警告，并增加了额外的线程 sanitizer 插桩。

  - 修复 `basic_resolver_results` 中的有符号/无符号警告，并抑制了若干 switch 分支贯穿（fall-through）警告。

  - 修复 `experimental::channel` 在旧版 MSVC 上的编译。

  - 修复 NetBSD 与 OpenBSD 上 `multicast::enable_loopback` 套接字选项的大小。

  - 修复使用 `clang-cl` 时对标准库协程的检测。

  - 改进了文档内部的交叉引用。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_92_0/doc/html/boost_asio/history.html)。

- [Assert](/libs/assert/)（可定制断言宏库）：

  - 修复同时定义 `BOOST_ENABLE_ASSERT_HANDLER` 与 `BOOST_ENABLE_ASSERT_DEBUG_HANDLER` 这一罕见情形下的 `BOOST_VERIFY`。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - `websocket::stream` 接受关闭码 1014（bad gateway，坏网关）。

  - `http::basic_parser` 忽略报文尾（trailer）中的连接类与分帧类字段。

  - `http::parser` 丢弃报文尾中携带的分帧与连接控制字段。

  - `http::basic_parser` 拒绝 HTTP/1.0 请求中的 chunked 传输编码。

  - `http::basic_parser` 拒绝同时出现 `Content-Length` 与 `Transfer-Encoding` 的情形，无论字段顺序如何。

  - `http::basic_parser` 拒绝 `Transfer-Encoding` 不以 chunked 结尾的请求。

  - `http::basic_parser` 校验 chunk 扩展中的带引号字符串（quoted-string）。

  - `http::message::prepare_payload` 拒绝带正文（body）的 1xx 响应。

  - `websocket::stream` 拒绝最高位置位的 64 位帧长度。

  - 文件操作在成功时清除 `error_code`。

  - `server-flex-awaitable` 示例将取消派发到任务的 strand（串行执行域）。

  - 移除了对 Boost.Functional 的依赖。

- [Charconv](/libs/charconv/)（字符与数值互转库）：

  - 新增 CUDA 支持，使整数的 `to_chars` 与 `from_chars` 均可在 CUDA kernel（核函数）中使用。

  - 修复 PPC64LE 上 Clang 的支持问题：该平台将 `long double` 与 `__float128` 保持为不同类型，而此前这一情形被 `static_assert` 判定为非法。

- [ContainerHash](/libs/container_hash/)（哈希库）：

  - 对处于无值状态（valueless）的 `std::variant` 实例进行哈希不再抛出异常。

- [Container](/libs/container/)（扩展容器库）：

  - 新增由 Joaquín M. López Muñoz 设计的新容器 `boost::container::hub`。

    更多信息参见 Container 文档中的"Hub Container"章节。

  - 修复的缺陷/issue：

    - P2363R5 实现中的重载决议保护缺失（[\#334](https://github.com/boostorg/container/issues/334)）。

    - 对 `small_vector<std::string>` 使用 `erase` 时的编译错误（[\#336](https://github.com/boostorg/container/issues/336)）。

    - `uses_allocator_construction.hpp`：缺少 `#include …​/config_end.hpp`（[\#338](https://github.com/boostorg/container/issues/338)）。

  - 为 `boost::container::vector`、`boost::container::static_vector` 与 `boost::container::small_vector` 新增 `unchecked_emplace_back` 与 `unchecked_push_back`。

  - 实现 C++23 提案 [P1518](https://wg21.link/P1518) 的变更：修改所有容器的分配器扩展构造函数（allocator-extended constructor），使容器的推导指引（deduction guide）不再过度受限。

- [Conversion](/libs/conversion/)（类型转换库）：

  - 实现了 C++20 模块 `boost.conversion`。非常感谢 [Fedor Osetrov](https://github.com/fdr400) 提交的 PR（[PR#43](https://github.com/boostorg/conversion/pull/43)）！

- [Decimal](/libs/decimal/)（IEEE 754 十进制浮点数库）：

  - 新增初步的 CUDA 支持，使 `decimal32_t`、`decimal64_t` 与 `decimal128_t` 可用于 CUDA kernel（核函数）。

  - 新增 `decompose` 函数，返回未经规格化（即保持当前群组/cohort）的尾数、指数与符号。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 修复由 `shared_library` 构造 `smart_library` 的构造函数（[PR#114](https://github.com/boostorg/dll/pull/114)）。非常感谢 [R. Savchenko](https://github.com/stima) 提交的 PR！

  - 实现了 C++20 模块 `boost.dll`。非常感谢 [Fedor Osetrov](https://github.com/fdr400) 提交的 PR（[PR#110](https://github.com/boostorg/dll/pull/110)、[PR#111](https://github.com/boostorg/dll/pull/111)、[PR#112](https://github.com/boostorg/dll/pull/112)）！

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - 将模板版本的 `initial_path` 标记为弃用（deprecation），并已从 **v4** 中移除。请改用非模板版本。

  - 在更多 POSIX 平台上改用 `readdir` 而非 `readdir_r`，具体包括 Mac OS 及其他 Apple 操作系统、FreeBSD、OpenBSD、DragonFly BSD、NetBSD、QNX 6.0 及更高版本、Solaris 10 及更高版本以及基于 Illumos 的系统。建议 Solaris 上的 gcc 用户在构建 Boost 时根据目标 Solaris 版本定义相应的 SunOS_5_x 宏（例如 `SunOS_5_11`）。（[\#349](https://github.com/boostorg/filesystem/issues/349)）

  - 对 `readdir` 非线程安全平台的支持已弃用，并将在未来发布中移除。虽然 POSIX.1-2024 之前并不强制要求，但在现代系统上，当不同线程使用各自独立的 `DIR` 对象时 `readdir` 是线程安全的，且某些系统已将 `readdir_r` 标记为弃用。POSIX.1-2024 已相应更新，并将 `readdir_r` 标记为过时（obsolescent），计划在规范的未来版本中移除。

  - 在 POSIX 平台上处理 `opendir`、`readdir` 及等价调用返回的 `EINTR` 错误码。虽无文档记载，但据报道该错误码可能出现在 Apple 操作系统和某些 BSD 系统上。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 功能增强（`geometry`）：

    - 移除 `varray` 实现，改用 Boost.Container 的 `static_vector`（[PR#1458](https://github.com/boostorg/geometry/pull/1458)）。

    - 重构并削减杂项 Boost 依赖（[PR#1459](https://github.com/boostorg/geometry/pull/1459)）。

    - 改进 Andoyer 反解（译注：大地测量学中计算两点间测地线的经典公式）在短距离下的精度（[PR#1461](https://github.com/boostorg/geometry/pull/1461)）。

  - 已解决问题（`geometry`）：

    - 单元测试 `index_rtree_exceptions_rst` 失败（[\#1399](https://github.com/boostorg/geometry/issues/1399)）。

    - GCC 上的性能回退（[\#1452](https://github.com/boostorg/geometry/issues/1452)）。

    - 缺少引用指南（citation guidelines）（[\#714](https://github.com/boostorg/geometry/issues/714)）。

    - 两个几乎完全相同的矩形没有交集（[\#1471](https://github.com/boostorg/geometry/issues/1471)）。

    - 各类错误与警告的修复。

- [Graph](/libs/graph/)（图结构与算法库）：

  - 新增用于基于模块度（modularity）聚类的 Louvain 社区发现算法（[PR#453](https://github.com/boostorg/graph/pull/453)）。

  - 移除对 Boost.StaticAssert 的依赖（[PR#450](https://github.com/boostorg/graph/pull/450)）。

  - 修复缺陷与正确性问题：

    - 修正 `adjacency_list` 序列化中使用的类型（[PR#443](https://github.com/boostorg/graph/pull/443)）。

    - 初始化 `adjacency_list.hpp` 中的 `edge_property_type`（[PR#505](https://github.com/boostorg/graph/pull/505)）。

    - 修复访问器（accessor）返回类型错误（[PR#504](https://github.com/boostorg/graph/pull/504)）。

  - 类型现代化与代码卫生：

    - 补齐缺失的 `const` 限定符，并在多个头文件中以 `using` 取代 `typedef`（[PR#508](https://github.com/boostorg/graph/pull/508)）。

    - 移除 `random.hpp`、`bandwidth.hpp` 与 `king_ordering.hpp` 中的收窄转换（narrowing conversion）（[PR#497](https://github.com/boostorg/graph/pull/497)、[PR#498](https://github.com/boostorg/graph/pull/498)、[PR#499](https://github.com/boostorg/graph/pull/499)）。

    - 以 `std::shuffle` 取代已弃用的 `std::random_shuffle`（[PR#513](https://github.com/boostorg/graph/pull/513)）。

    - 消除 `-Wunused-*` 警告并移除无用的测试变量（[PR#510](https://github.com/boostorg/graph/pull/510)、[PR#511](https://github.com/boostorg/graph/pull/511)、[PR#512](https://github.com/boostorg/graph/pull/512)）。

    - 清除 GCC 的 `-Wsign-compare` 警告（[PR#514](https://github.com/boostorg/graph/pull/514)）。

  - 文档：整体更新文档并迁移到新的视觉设计（[PR#469](https://github.com/boostorg/graph/pull/469)、[PR#491](https://github.com/boostorg/graph/pull/491)、[PR#509](https://github.com/boostorg/graph/pull/509)、[PR#517](https://github.com/boostorg/graph/pull/517)、[PR#519](https://github.com/boostorg/graph/pull/519)）。

- [Hash2](/libs/hash2/)（可扩展哈希算法库）：

  - 新增对 `std::optional` 的内建支持。

  - 新增对 `std::variant`、`std::monostate` 的内建支持。

- [Heap](/libs/heap/)（优先队列（堆）家族库）：

  - 本版本是支持 C++14 的最后一个版本。未来发布将要求 C++17。

- [ICL](/libs/icl/)（区间容器库，Interval Container Library）：

  - 从版本 22 开始，libc++ 更改了其关联容器的一些查找算法，其方式破坏了 ICL 的假设与行为。本次对库内部进行了重构以解决该问题，使 ICL 对 C++ 委员会未来关于关联容器非异构查找的决议保持健壮（[PR#54](https://github.com/boostorg/icl/pull/54)、[LWG4752](https://cplusplus.github.io/LWG/issue4572)）。

  - 修复与 C++20 相关的问题：`std::iter_value_t<element_iterator>` 以及 GCC 10-12 对改写的关系运算符（rewritten relational operators）的处理（[PR#54](https://github.com/boostorg/icl/pull/54)）。

  - 修复 GCC 10-11 的代码生成（codegen）缺陷（[PR#54](https://github.com/boostorg/icl/pull/54)）。

- [Interprocess](/libs/interprocess/)（进程间通信库）：

  - 修复的缺陷：

    - AIX 构建修复：修正 `get_invalid_systemwide_thread_id` 的返回类型（[PR#280](https://github.com/boostorg/interprocess/pull/280)）。

    - `message_queue_t` 中的锁覆盖的代码范围超出预期（[\#281](https://github.com/boostorg/interprocess/issues/281)）。

- [Iterator](/libs/iterator/)（迭代器构建设施库）：

  - 在 C++14 及更高标准中新增 `is_*_iterator_v` 变量模板，与对应的迭代器特征（traits）等价。

  - `distance` 与 `advance` 算法现在加了约束：要求迭代器实参的 `is_iterator` 返回 `true`。（[PR#96](https://github.com/boostorg/iterator/pull/96)）

- [LexicalCast](/libs/lexical_cast/)（字符串与数值等类型转换库）：

  - 实现了 C++20 模块 `boost.lexical_cast`。非常感谢 [Fedor Osetrov](https://github.com/fdr400) 提交的 PR（[PR#96](https://github.com/boostorg/lexical_cast/pull/96)）！

- [Lockfree](/libs/lockfree/)（无锁容器与队列库）：

  - 本版本是支持 C++14 的最后一个版本。未来发布将要求 C++17。

  - 新增 `boost::lockfree::mpsc_weak_queue`，一个多生产者单消费者（MPSC）队列。虽然 `push` 与 `pop` 各自都是无等待（wait-free）的，但该队列不满足可线性化（linearizable），并且生产者如果在交换尾指针与链接自身节点之间停滞，可能永久性地破坏队列，因此它不是严格意义上的无锁（lock-free）队列。

  - 新增 `boost::lockfree::bounded_ticket_queue`，一个基于环形缓冲区的有界 MPMC（多生产者多消费者）队列。在单生产者单消费者配置下，该队列满足可线性化且无等待。在多生产者或多消费者配置下，已占取槽位后停滞的线程可能阻塞整体进展，因此该队列不是严格意义上的无锁队列。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - 为 Student's T 分布与非中心 F 分布新增自由度（degree of freedom）求取器。

  - 修复 CUDA 编译问题：主机（host）函数此前在编译期间被错误地标记为 device 函数。

  - 扩大了分布函数的测试覆盖，由此带来若干溢出（overflow）修复。

- [Mp11](/libs/mp11/)（C++11 元编程库）：

  - 改进了若干算法的性能（由 Jonathan Poelen 贡献）。

- [MQTT5](/libs/mqtt5/)（MQTT 5.0 客户端库）：

  - 当客户端已在运行时，`mqtt_client::async_run` 现在会立即以 `client::error::already_running` 完成（[\#54](https://github.com/boostorg/mqtt5/issues/54)）。

  - 修复解码来自 broker（服务器）的数据包时缺失的若干长度检查。此前畸形数据包可能导致越界读取或过度的内存分配。非常感谢 [Team-Atlanta](https://github.com/Team-Atlanta) 报告这些问题。

- [MSM](/libs/msm/)（有限状态机库，Meta State Machine）：

  - 新特性（`backmp11` 后端）：

    - 提供用于日志支持的观察者（observer）API（[\#220](https://github.com/boostorg/msm/issues/220)）

    - 无需转换即可将 Kleene 事件转发给动作（action）与守卫（guard）（[\#229](https://github.com/boostorg/msm/issues/229)）

    - 确保基本异常保证并将异常传播给调用方（[\#221](https://github.com/boostorg/msm/issues/221)）

    - 提供反射 API 以及对 Boost.Serialization、Boost.JSON 与 nlohmann/json 的序列化支持（[\#197](https://github.com/boostorg/msm/issues/197)）

    - 重做终止（terminate）与中断（interrupt）状态处理，并提供 `machine_state` 枚举（[\#244](https://github.com/boostorg/msm/issues/244)）

    - 可配置的事件池与内联存储（[\#239](https://github.com/boostorg/msm/issues/239)）

    - 现已提供 API 参考与示例

  - 缺陷修复（`backmp11`）：

    - 状态机在未运行时仍处理事件（[\#198](https://github.com/boostorg/msm/issues/198)）

  - **破坏性变更（`backmp11`）**：

    - 为降低内存占用，`process_event(…​)` 中的事件不再自动入队；请在动作中使用 `enqueue_event(…​)`（[\#178](https://github.com/boostorg/msm/issues/178)）

    - 后端不再向前端转发构造函数参数，前端必须可默认构造。如需自定义构造函数，请在后端中定义（[\#232](https://github.com/boostorg/msm/issues/232)）

    - 已移除弃用的 API `process_queued_events()` 与 `process_single_queued_event()`，请改用 `process_event_pool(…​)`

    - 默认活动状态切换策略设为"after source exit"（源状态退出后），以符合 UML 规范。其他选项不符合 UML，将被移除（[\#222](https://github.com/boostorg/msm/issues/222)）

    - 后端改用自带新枚举值的 `process_result` 类型，不再沿用 `back` 命名空间的枚举别名。旧枚举值已弃用（[\#242](https://github.com/boostorg/msm/issues/242)）并将被移除

  - fix(back, back11)：正交区域（orthogonal region）中事件延迟（event deferral）引发无限递归（1.78 引入的回归）（[\#184](https://github.com/boostorg/msm/issues/184)）

- [MultiIndex](/libs/multi_index/)（多索引容器库）：

  - 花式指针（fancy pointer）支持得到扩展：`multi_index_container` 的迭代器现在通过分配器（allocator）的 pointer 类型来存储对元素的引用。特别地，这意味着使用 [Boost.Interprocess](/libs/interprocess) 分配器时，迭代器现在可以放入共享内存。

  - 修复哈希索引在超大容器规模下重哈希（rehash）时的性能问题（[PR#94](https://github.com/boostorg/multi_index/pull/94)）。由 Daniel Král 贡献。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - 为 float128 新增 `data()` 成员函数，与库中其余部分保持一致。

  - 修复阻碍 Clang 编译 constexpr 表达式模板的问题。

- [MySQL](/libs/mysql/)（MySQL 客户端库）：

  - 新增配置服务器默认字符集的方式，使字符集追踪更智能。可用于避免冗余的 `SET NAMES` 语句。参见 `pool_params::charset_strategy` 与 `connect_params::server_default_charset`（[PR#511](https://github.com/boostorg/mysql/pull/511)）。

  - 将 `pool_params::ping_interval` 的默认值从 1 小时缩短为 10 秒。这改进了失效连接的检测（[PR#512](https://github.com/boostorg/mysql/pull/512)）。

  - 通过降低接收不完整消息时数据轮转（rotation）的频率优化了读缓冲区（[PR#501](https://github.com/boostorg/mysql/pull/501)）。由 `@vsoulgard` 贡献。

  - CI 测试用的 TLS 证书现改为动态生成，而非提交进代码仓库。这清除了漏洞扫描器产生的报告（[PR#505](https://github.com/boostorg/mysql/pull/505)）。

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - C++20 模块 `boost.pfr` 现在也在启用与不启用 `import std` 两种情况下进行测试。非常感谢 [Fedor Osetrov](https://github.com/fdr400) 提交的 PR（[PR#233](https://github.com/boostorg/pfr/pull/233)）！

- [PolyCollection](/libs/poly_collection/)（多态集合库）：

  - 依照 WG21（C++ 标准委员会）论文 [P2944R3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p2944r3.html)，`variant_collection_value_type_impl<Ts...>` 的关系运算符现在仅当所有 `Ts...` 都具备对应关系运算符时才可用。

  - 修复与 libc++ v21 及以上版本的不兼容问题（[PR#34](https://github.com/boostorg/poly_collection/pull/34)）。

- [Redis](/libs/redis/)（Redis 客户端库）：

  - 修复 `connection` 中的一处未定义行为：当尝试取消一个已完成但其处理程序尚未被调用的请求时触发。原因是 `std::deque` 上 erase-remove 用法不当（[PR#428](https://github.com/boostorg/redis/pull/428)）。由 `@L0rentz` 贡献。

  - 优化缓冲区轮转（buffer rotation），降低单个网络分组到达大量小消息时的 CPU 消耗（[PR#415](https://github.com/boostorg/redis/pull/415)）。

  - 为 `config` 结构体的所有成员添加了初始化器。现在可以使用指派初始化器（designated initializer）创建 `config` 对象（[PR#424](https://github.com/boostorg/redis/pull/424)）。

  - 从 CMake 中移除了 standalone（独立使用）工作流。这是一种未文档化的、面向内部开发的以 CMake 使用 Boost.Redis 的方式（[PR#409](https://github.com/boostorg/redis/pull/409)）。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 实现 C++20 模块：

    - `boost.stacktrace_dump` 模块，对应 safe_dump 接口

    - 每种 unwind/collect 实现方式对应一个 `boost.stacktrace_<backend>` 模块

    - `boost.stacktrace` 模块，暴露当前可用的最佳后端实现。非常感谢 [Fedor Osetrov](https://github.com/fdr400) 提交的 PR（[PR#230](https://github.com/boostorg/stacktrace/pull/230)、[PR#227](https://github.com/boostorg/stacktrace/pull/227)）！

  - C++20 模块 `boost.stacktrace` 现在也在启用与不启用 `import std` 两种情况下进行测试。非常感谢 [Fedor Osetrov](https://github.com/fdr400) 提交的 PR（[PR#231](https://github.com/boostorg/stacktrace/pull/231)）！

  - 修复 MinGW 上 `Boost::from_exception` 的链接。非常感谢 [Orgad Shaneh](https://github.com/orgads) 提交的 PR（[PR#225](https://github.com/boostorg/stacktrace/pull/225)）！

- [System](/libs/system/)（错误码与 system_error 库）：

  - 修复 `unwrap_and_invoke` 对返回 `void` 的函数的处理。

- [TypeIndex](/libs/type_index/)（运行时类型索引库）：

  - C++20 模块 `boost.type_index` 现在也在启用与不启用 `import std` 两种情况下进行测试。非常感谢 [Fedor Osetrov](https://github.com/fdr400) 提交的 PR（[PR#47](https://github.com/boostorg/type_index/pull/47)）！

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - 为库中所有容器新增与 C++20 ranges（范围）的互操作性：`insert_range`（并发容器另有 `insert_range_(or|and)_[c]visit`）、`std::from_range` 构造及相关 CTAD（译注：构造函数实参推导）推导指引。同时提供 `boost::unordered::from_range` 构造标签，作为 C++23 `std::from_range` 的替代（或在其不可用时使用）。

  - 修复封闭定址（closed-addressing）容器在超大容器规模下重哈希时的性能问题（[PR#348](https://github.com/boostorg/unordered/pull/348)）。由 Daniel Král 贡献。

- [URL](/libs/url/)（URL 解析库）：

  - 修复 `normalize_path` 中的堆缓冲区溢出：针对无 authority 的 URL，其规格化路径以 `//` 开头的情形（[PR#995](https://github.com/boostorg/url/pull/995)）。

  - 修复 `ipv6_address_rule` 中的未初始化读取：当内嵌 IPv4 地址前面没有 `h16` 时触发，例如 `https://[::.`（[PR#994](https://github.com/boostorg/url/pull/994)）。

  - 修复大小写不敏感比较、哈希与 `format` 中无符号整数溢出 sanitizer 的发现项（[PR#994](https://github.com/boostorg/url/pull/994)）。

  - 修复 `url_base::edit_params` 中已解码查询（query）长度的跟踪（[PR#990](https://github.com/boostorg/url/pull/990)）。

  - 第三轮安全评审修复：从空源复制 `url_view`、两处错误的 `noexcept` 说明符，以及反向迭代段（segment）时的解码长度跟踪（[PR#988](https://github.com/boostorg/url/pull/988)）。

- [Wave](/libs/wave/)（C/C++ 预处理器实现库）：

  - 引入数字分隔符（C++14）、`module` 关键字（C++20）与 `size_t` 字面量（C++23）。

  - 修复的缺陷：

    - `find_include_file` 错误地把目录当作 include 文件接受（[\#243](https://github.com/boostorg/wave/issues/243)）。

    - 当 `expanding_object_like_macro` 返回 `true` 时，预定义宏（`__FILE__`、`__LINE__`、`__INCLUDE_LEVEL__`）会被展开两次（[\#246](https://github.com/boostorg/wave/issues/246)）。

## 更新的工具（Updated Tools）

- [B2](/tools/build/)（Boost 构建工具，原名 bjam）：

  - 包含 [B2 版本 5.5.3](https://www.boost.org/tools/build/doc/html/#_version_5_5_3) 的发布。

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
