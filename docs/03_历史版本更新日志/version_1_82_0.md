# Boost 1.82.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_82_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_82_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2023-04-14 03:08 GMT（原文日期行：April 14th, 2023 03:08 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.82.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 已知问题（Known Issues）

以下为库作者提供的补丁，这些补丁发现得过晚，来不及在本发布中修复。

- Filesystem

  - 在 OpenBSD 上编译可能失败，原因是该平台对共享库 `-Wl,--no-undefined` 编译器标志的支持存在问题，见 [\#283](https://github.com/boostorg/filesystem/issues/283)。[补丁](/patches/1_82_0/0001-filesystem-fix-openbsd-build.patch)。

  - 在 Windows 上，对 SMBv1 共享中的目录创建目录迭代器可能以 `ERROR_INVALID_LEVEL` 错误码失败，见 [\#284](https://github.com/boostorg/filesystem/issues/284)。[补丁](/patches/1_82_0/0002-filesystem-fix-win-smbv1-dir-iterator.patch)。

## 弃用 C++03 支持公告（Notice of Dropping C++03 Support）

以下库将在两个发布之后的 1.84 发布中放弃对 C++03 的支持：

- Align

- Any

- Asio

- Atomic

- Bind

- Chrono

- ContainerHash

- Conversion

- DLL

- Endian

- Filesystem

- Function

- Functional

- Io

- LexicalCast

- Log

- Random

- Ratio

- SmartPtr

- System

- Stacktrace

- Thread

- Timer

- TypeIndex

- Typeof

- Unordered

- Variant

本发布（1.82）与下一个发布（1.83）将是为上述库及其大多数依赖提供 C++03 支持的最后两个发布。

上述库以及 Boost 大部分库的新基线要求将是 C++11。由于旧版编译器常因缺少支持或存在缺陷而只部分实现了 C++11，哪些编译器被视为满足 C++11 要求可能因库而异。

不过，一般的规则是：如果编译器完全不识别某个 C++11 关键字或语法（例如使用 `noexcept`、使用 `constexpr`，或定义 `=delete` 函数会立即导致编译错误），或编译器完全不提供所需的 C++11 头文件（例如尝试包含 `<atomic>` 或 `<chrono>` 失败），或编译器提供的某个 C++11 特性或头文件完全不可用，则该编译器不被视为 C++11 编译器。

例如，这排除了 14.0 之前的 Microsoft Visual C++，以及 4.8 之前的 GCC。

## 新增库（New Libraries）

- [Mysql](/libs/mysql/)（MySQL 客户端库）：基于 Boost.Asio 的 MySQL 数据库服务器 C++11 客户端，由 Ruben Perez 开发。

## 更新的库（Updated Libraries）

- [Any](/libs/any/)（类型安全的任意类型容器库）：

  - 现在使用 `core/enable_if.hpp` 头文件，而非已弃用的 `utility/enable_if.hpp`。感谢 Michael Ford 提交的 [PR#25](https://github.com/boostorg/any/pull/25)。

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 新增自定义操作立即完成时完成处理程序（completion handler）执行方式的能力。

  - 为缓冲区（buffer）类型新增用户自定义字面量（user-defined literals）。

  - 新增协议类型 `local::seq_packet_protocol`，用于表示使用 `SOCK_SEQPACKET` 的 `AF_UNIX`。

  - 通过 `signal_set::add` 的可选实参暴露 `sigaction()` 标志。

  - 更改 `allocator_binder`、`executor_binder` 与 `cancellation_slot_binder`，支持检测未特化的关联器（associator）。

  - 修复 `associated_cancellation_slot<reference_wrapper>::get()` 中的歧义。

  - 修复 `awaitable<>` 对包含 `std::exception_ptr` 的完成签名（completion signature）的处理。

  - 修复 `experimental::channel<>` 在 `cancel` 之后 `try_send` 失败的问题。

  - 修复线程池无内部线程时 `thread_pool::join()` 死锁的问题。

  - 修复使用 `io_uring` 时管道（pipe）的 `release()`。

  - 修复 `io_uring` 后端中的数据初始化与清理问题。

  - 修复 `get_associated_executor()` 执行上下文（execution context）重载中的悬垂引用问题。

  - 确保 `experimental::channel<>` 关闭后仍可接收已缓冲的消息。

  - 修复 `any_completion_handler` 的赋值运算符。

  - 约束 `any_completion_handler` 的构造函数，防止意外拷贝。

  - 改用 `uint64_t` 表示 OpenSSL 选项，以匹配 OpenSSL 3。

  - 修复 `deferred` 与多个完成签名的互操作性。

  - 修复 channel，新增对 C++11 与 C++14 的部分支持。

  - 为 `co_composed` 与 `awaitable<>` 协程在等待打包（packaged）异步操作时补上缺失的处理程序跟踪（handler tracking）源位置（source location）支持。

  - 修复若干"潜在空指针解引用"与变量遮蔽（shadow variable）警告。

  - 修复 `asio::buffer` 与 `const_buffers_1`、`mutable_buffers_1` 一起使用时的重载选择。

  - 禁用针对当前 Windows 版本的运行期检查，除非面向较旧的 Windows。

  - 修复缓冲流包装器与可移动构造流（如 `ssl::stream<>`）之间的兼容性。

  - 修复 `basic_socket_acceptor::async_accept` 与推导返回类型 lambda 的兼容性。

  - 修复 `as_tuple` 与旧式完成标记（completion token）的兼容性。

  - 修复 `redirect_error` 与新式完成标记的兼容性。

  - 修复一个 Windows 特有的潜在程序终止问题，该问题源于本应允许从析构函数逃逸的异常。

  - 防止对布尔表达式进行无意的 `co_await`。

  - 修复 `experimental::use_coro` 中的结果处理与自定义分配器支持。

  - 修复 `is_async_operation` 与 `completion_signature_of` 的可变参数模板模拟（variadic template emulation）。

  - 修复 `experimental::promise` 中对已移动（moved-from）结果的错误复用。

  - 修复 `experimental::coro` 配合自定义分配器使用的问题。

  - 修复 Windows 上面向流的文件中 `seek_cur` 的行为。

  - 文档的若干增补与修改。

  - 更多细节请查阅[修订历史](/doc/libs/1_82_0/doc/html/boost_asio/history.html)。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 当为支持 AVX 的 x86 目标编译时，128 位原子加载与存储现在使用向量指令。

  - 对于 32 位 x86 目标，具有 `memory_order_seq_cst` 语义的 64 位原子加载与存储现在会发出内存排序指令。

  - 移除了 Boost.Atomic 1.73 中弃用的 `atomic<T>::storage()` 访问器与 `atomic<T>::storage_type` 类型。建议用户改用 `atomic<T>::value()` 与 `atomic<T>::value_type`。

- [Beast](/libs/beast)（基于 Asio 的 HTTP/WebSocket 库）：

  - 新增 `error_code` 使用源位置（source_location）的支持。

  - `tcp_stream` 使用定时器（timer）的正确执行器（executor）。

  - error category 使用数字 ID。

  - `file_body` 支持 seek。

- [ContainerHash](/libs/container_hash/)（哈希支持库）：

  - 新增针对 `std::nullptr_t` 的 `hash_value` 重载。

  - 新增 `is_tuple_like` 以及针对类元组（tuple-like）类型的 `hash_value` 重载。

  - 字符串哈希改用 [mulxp1_hash](https://github.com/pdimov/mulxp_hash)。这同时提升了质量与速度。

- [Core](/libs/core/)（核心工具集库）：

  - 新增 `boost/core/snprintf.hpp` 头文件，提供 `snprintf`、`vsnprintf` 及其 `wchar_t` 对应版本的可移植定义。

  - 弃用 `boost/core/is_same.hpp` 与 `boost::core::is_same`。该头文件将在未来发布中移除。建议用户改用 Boost.TypeTraits 或 C++ 标准库类型特征（type traits）。

  - 为 `boost::ref` 的成员函数及相关方法添加 `noexcept`。

  - 为 `boost::swap` 函数添加 `noexcept`，视类型是否支持不抛出异常的 swap 操作而定。

  - 新增 `boost::core::launder`，即 `std::launder` 的可移植实现。

  - 新增 `BOOST_CORE_ALIGNOF`，即 `alignof` 的可移植实现。

  - 新增 `boost::core::max_align_t`（`std::max_align_t` 的可移植等价物）与 `boost::core::max_align`（`max_align_t` 的对齐要求）。

  - 新增 `boost::core::memory_resource`，即 C++17 `std::pmr::memory_resource` 的可移植等价物。

  - 新增 `boost/core/serialization.hpp`，一组原语集合，使各库能够为其类型实现 Boost.Serialization 支持而无需包含 Serialization 头文件（从而避免使库依赖 Serialization）。

  - 新增 `boost::data`，即 `std::data` 的实现。

  - 新增 `boost::size`，即 `std::size` 的实现。

  - 更新 `boost::span` 以使用 `boost::data`，从而新增自 `std::initializer_list` 进行范围构造的支持。

  - 新增 `boost::identity`，即 `std::identity` 的实现。该设施已从 Boost.Functional 移入。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 避免从 size_t 到 uint32_t 的隐式转换，感谢 Travers Biddle 提交的 [PR#57](https://github.com/boostorg/dll/pull/57)。

- [Filesystem](/libs/filesystem/)（可移植文件系统操作库）：

  - 修复可能因 `path` 转换构造函数对所接受实参过于宽松而导致的编译错误（[\#273](https://github.com/boostorg/filesystem/issues/273)）。

  - **v4：** `path::remove_filename` 现在保留结尾的目录分隔符（[\#271](https://github.com/boostorg/filesystem/issues/271)）。

  - 新增 `path::remove_filename_and_trailing_separators`，从路径中移除文件名及其前面的目录分隔符。该行为类似于 Filesystem **v3** 中的 `path::remove_filename`，但在 **v4** 中同样可用。

  - 新增 `path::replace_filename`，用于替换路径中的文件名。

  - 更新库版本选择的实现，以避免 ODR（单一定义规则）违规（[\#279](https://github.com/boostorg/filesystem/issues/279)）。

  - 在 Windows 上，针对查询 SMBv1 共享中文件的文件属性新增了变通方案。此前，SMBv1 共享中的目录可能被误报为普通文件。该问题不影响 SMBv2 或更高版本（[\#282](https://github.com/boostorg/filesystem/issues/282)）。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 重大改进（Major improvements）：

    - [PR#1045](https://github.com/boostorg/geometry/pull/1045) 为（多）线串（linestring）与（多）多边形支持地理坐标系 buffer（缓冲区）

  - 改进（Improvements）：

    - [PR#1114](https://github.com/boostorg/geometry/pull/1114) 可比较距离（comparable distance）：新增对动态几何对象的支持

    - [PR#1046](https://github.com/boostorg/geometry/pull/1046) 为 box 与几何对象组合支持 covered_by()

  - 已解决问题（Solved issues）：

    - [\#705](https://github.com/boostorg/geometry/issues/705) WKT：允许制表符与换行符

    - [\#1109](https://github.com/boostorg/geometry/issues/1109)、[\#1108](https://github.com/boostorg/geometry/issues/1108) union（并集）运算的修复

    - 示例中的各类修复

  - 破坏性变更（Breaking changes）：

    - 空多边形的 WKT 输出现在为 POLYGON()，以与其他几何对象的表示保持一致

- [Histogram](/libs/histogram/)（多维直方图库）：

  - 以 `boost::core` 中的实现取代 `detail::span` 与 `detail::make_span`。

  - 文档改进。

  - 在某些情形下保护 `std::min` 与 `std::max` 的使用，由 Han Jiang 贡献（流行的 Windows 头文件会非法设置 min/max 宏，因此需要变通处理）。

  - 新增测试，以便在未来捕获库中未受保护的 min、max 标识符的使用。

  - 修复以支持最新的 clang-14 以及 gcc-11+ 中的推导指引（deduction guides）。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 新增 `set_at_pointer`。

  - 新增 `boost::hash` 支持。

  - 支持调用方提供的序列化器（serializer）存储。

  - `value_to` 对 `std::optional` 支持缺失元素。

  - 修复解析器在转义字符内部挂起的问题。

  - 使 `sentinel()` 返回唯一的指针。

- [Locale](/libs/locale/)（本地化与 Unicode 文本处理库）：

  - `get_system_locale` 及其依赖方现在按照 POSIX 的定义正确地优先使用 `LC_ALL` 而非 `LC_CTYPE`（[PR#144](https://github.com/boostorg/locale/pull/144)）。

  - `utf8_codecvt::out` 对尾部（UTF）代理项（surrogate）返回 `partial`。

  - 新增 `boost::locale::util::locale_data` 用于解析 locale。

  - `boost::locale::info::encoding()` 的结果现按文档为大写形式，例如 "UTF-8" 而非 "utf-8"。

  - 支持 M49 国家/地区代码，如 `en_001` 或 `en_150`（[PR#148](https://github.com/boostorg/locale/pull/148)）。

  - 将 `en_US_POSIX` 视为 `C` locale 的别名（[PR#148](https://github.com/boostorg/locale/pull/148)）。

  - 改进缺少分词（segmentation）支持（即无 ICU）时的错误信息（[PR#149](https://github.com/boostorg/locale/pull/149)）。

  - 修复编译器警告。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - **弃用 C++11 支持**：现在要求以 C++14 作为最低标准。最低测试编译器版本现为 Clang-5、GCC-5 或 MSVC-14.1。

  - 新增用于多项式求值的 Estrin 方法。

  - 修复非中心分布（non-central distributions）中的多个问题，以支持更大的非中心参数（non-centrality），见 [939](https://github.com/boostorg/math/pull/939)。

  - 新增 CMake（构建系统）install 目标。

  - 修正 `special_functions.hpp`，禁用所有无法在无异常环境中使用的内容。

  - 使条件数（condition number）计算在 C++14 下可用。

  - 修复 `constexpr` 表驱动函数，避免代码并非实际 `constexpr` 时的大幅性能下降，见 [923](https://github.com/boostorg/math/issues/923)。

  - 改进 tanh_sinh 的边界处理，见 [894](https://github.com/boostorg/math/pull/894)。

  - 新增 Linux arm64、s390x 与 Apple M1 测试，并修正测试用例以处理 128 位 long double。

  - 改进 `constexpr` 数学函数，以更好地处理无穷大与 NaN。

  - 使各积分器（integrator）满足 const 正确性（const-correct）。

  - 修复函数下溢情形下 tanh_sinh 积分器的问题，见 [898](https://github.com/boostorg/math/issues/898)。

  - 不再使用 `std::cbrt`，因为部分平台仍不支持它。

  - 防止非中心 T 分布触发虚假的 FE_INVALID 浮点异常，见 [892](https://github.com/boostorg/math/pull/892)。

  - 修复二项分布（binomial distribution）的边界情形。

  - 改进 `ibeta` 对极小实参的处理，见 [884](https://github.com/boostorg/math/pull/884)。

  - 改进 `ibeta` 对无穷大与 NaN 的处理，见 [878](https://github.com/boostorg/math/issues/878)。

  - 改进 `powm1` 的错误处理，见 [781](https://github.com/boostorg/math/issues/781)。

  - 改进求根器的区间夹逼（bracketing），在指数极大或极小时更快完成夹逼。

  - 修复求根的边界情形，见 [873](https://github.com/boostorg/math/issues/873)。

  - 大量杂项警告修复。

  - 在使用需要 C++17 的特性时新增断言，以便在以更低标准版本调用编译器时获得更好的错误信息。

- [Multi-index Containers](/libs/multi_index/doc/index.html)（多索引容器库）：

  - 序列化现在使用 `unsigned long` 而非 [collection_size_type](/libs/serialization/doc/wrappers.html#collection_size_type)；为反映此变更，`multi_index_container` 序列化的[类版本号](/libs/serialization/doc/tutorial.html#versioning)从 2 提升到 3。对于对 `collection_size_type` 值作特殊处理的自定义存档（archive）类型，读取旧存档可能失败：此时应全局定义宏 `BOOST_MULTI_INDEX_ENABLE_SERIALIZATION_COMPATIBILITY_V2` 以确保读取操作的向后兼容。

  - 维护性工作。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - **弃用 C++11 支持**：现在要求以 C++14 作为最低标准。最低测试编译器版本现为 Clang-5、GCC-5 或 MSVC-14.1。

  - 新增前向声明（forward declaration）头文件。

  - 更新与 Eigen 的互操作性，不再依赖 Eigen 的内部细节，见 [479](https://github.com/boostorg/multiprecision/issues/479)。

  - 新增 CMake install 目标。

  - 修复独立（standalone）情形下 `cpp_dec_float` 自字符串构造的问题，以获得更好的错误处理，见 [499](https://github.com/boostorg/multiprecision/issues/499)。

  - 在 C++17 模式下移除冗余定义，见 [530](https://github.com/boostorg/multiprecision/pull/530)。

  - 修复独立情形下 `itrunc` 与 `ltrunc` 的错误处理。

  - 修复解析八进制字符串时存储可能未初始化的问题。

  - 新增 arm64 与 s390x 的 CI（持续集成）测试。

  - 为 `powm` 补上缺失的表达式模板展开（unpacking）代码，见 [506](https://github.com/boostorg/multiprecision/issues/506)。

- [Nowide](/libs/nowide/)（Windows 下 UTF-8 标准 I/O 适配库）：

  - 新增接受（`std::`）string 实例的 `convert_string` 重载。

  - 新增 `quoted`，用于将（带引号的 UTF-8）路径（`std::filesystem` 或 `boost::filesystem`）输出到流（[PR#170](https://github.com/boostorg/nowide/pull/170)）。

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - 实现了 `boost::pfr::is_implicitly_reflectable` 以及将聚合类型特化为可反射/不可反射的机制，感谢 Denis Mikhailov 提交的 [PR#111](https://github.com/boostorg/pfr/pull/111)。

  - 实现了按元素类型获取聚合中元素的 `boost::pfr::get`。

  - 实现了用于检测库反射支持的 `BOOST_PFR_ENABLED` 宏，感谢 Denis Mikhailov 提交的 [PR#86](https://github.com/boostorg/pfr/pull/86)。

  - 修复缺失的终止字符，感谢 Denis Mikhailov 提交的 [PR#114](https://github.com/boostorg/pfr/pull/114)。

  - 修复 `boost/pfr/config.hpp` 在旧编译器上的编译，感谢 Denis Mikhailov 提交的 [PR#118](https://github.com/boostorg/pfr/pull/118)。

  - 为旧编译器中损坏的 C++17 结构化绑定（structured binding）提供变通方案，感谢 Denis Mikhailov 提交的 [PR#119](https://github.com/boostorg/pfr/pull/119)。

  - 避免 -Wzero-as-null-pointer-constant 警告，感谢 Markus F.X.J. Oberhumer 提交的 [PR#117](https://github.com/boostorg/pfr/pull/117)。

  - 修复多处拼写错误，感谢 Denis Mikhailov。

  - 补上缺失的 `#pragma once`，感谢 [caozhanhao](https://github.com/caozhanhao) 提交的 [PR#121](https://github.com/boostorg/pfr/pull/121)。

  - 文档的多处修复与改进。

- [Process](/libs/process)（进程管理库）：

  - 为 V2 新增外部（extern）进程管理（仍为实验性）。

  - V1 中的 `wait_for` 与 `wait_until` 已弃用——它们将在未来被移除！

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 修复文档与注释中的拼写错误，感谢 Chocobo1 提交的 [PR#132](https://github.com/boostorg/stacktrace/pull/132)。

  - 修复定义了 `BOOST_STACKTRACE_BACKTRACE_FORCE_STATIC` 时 `backtrace_create_state` 的多线程标志检测。

- [StaticString](/libs/static_string/)（固定容量字符串库）：

  - 与 Boost.Core `string_view` 及 `std::string_view` 的互操作性。

- [Test](/libs/test/)（单元测试框架库）：

  - 修复若干未使用变量警告。

  - 修复 sprintf 弃用警告。

  - 修复 `basic_cstring::rfind` 中的未定义行为。

  - 通过 GitHub Actions 新增 CI（持续集成）。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - **重大更新。**

  - 新增基于节点（node-based）的开放寻址容器 `boost::unordered_node_map` 与 `boost::unordered_node_set`。

  - 按照 [P2363](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2363r5.html) 的规定，将异构查找（heterogeneous lookup）扩展到更多成员函数。

  - 以基于扩展乘常数（extended multiplication by a constant）的新算法取代开放寻址容器此前的后混合（post-mixing）过程。

  - 修复内部 `emplace` 实现中的缺陷：栈上局部类型未使用容器的分配器正确构造，从而破坏了使用分配器构造（uses-allocator construction）。

- [URL](/libs/url/)（URL 解析库）：

  - 新增带自动百分号编码（percent-encoding）的 `url::format`。

  - 新增 URL 路由（router）示例。

  - 新增 `set_params` 便捷函数。

  - 支持到 `string_view` 的隐式转换。

  - 解析构造函数改为隐式。

  - `string_token::arg` 拥有虚析构函数与切片（slice）保护。

  - 支持 `BOOST_URL_DISABLE_THREADS`。

  - 改进与缺陷修复：

    - WIN32_LEAN_AND_MEAN 宏重定义警告

    - 比较操作区分缺失与空的组件

    - 检测带有类似空端口段的 `hier_part_rule`

    - 段（segment）按"如同已规范化"的比较在根之上也能正常工作

    - hier-part 的 path-rootless 情形会将无效段纳入考虑

    - 端口号在溢出时被置为 0

    - IPv4 转字符串的溢出检测算法

- [Variant](/libs/variant/)（非递归可辨识联合库）：

  - 现在使用 core/addressof 而非已弃用的 utility/addressof。感谢 Michael Ford 提交的 [PR#105](https://github.com/boostorg/variant/pull/105)。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)（Boost.Build 构建系统框架）：

  - 包含 [B2 version 4.9.4](/tools/build/doc/html/#_version_4_9_4) 的发布。

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
