# Boost 1.85.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_85_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_85_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2024-04-15 17:38 GMT（原文日期行：April 15th, 2024 17:38 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.85.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 已知问题（Known Issues）

以下是库作者提供的补丁，因发现过晚而未能在本发布中修复。

- Container

  - 由于库中的未定义行为（UB），`flat_map`/`multimap` 容器在某些编译器上可能崩溃或返回无效结果，参见 [\#273](https://github.com/boostorg/container/issues/273)。[补丁](/patches/1_85_0/0001-container-fix-flat_map.patch)。

## 新增库（New Libraries）

- [Charconv](/libs/charconv/)（字符与数值互转库）：C++11 下 `<charconv>` 的高质量实现，由 Matt Borland 开发。

- [Scope](/libs/scope/)（作用域守卫工具集库）：作用域守卫（scope guard）工具集合与 `unique_resource` 封装，由 Andrey Semashev 开发。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 修复 `async_result` 主模板的 concept（概念）检查，正确处理左值限定的完成签名（completion signature）。

  - 修复使用 `bind_allocator`、`bind_executor`、`bind_immediate_executor` 与 `bind_cancellation_slot` 完成标记（completion token）适配器相互适配时可能出现的编译错误。

  - 修改 `experimental::ranged_parallel_group` 操作，使其在调用完成处理程序时移动 `completion_order` 向量。

  - 修复 `ip::basic_resolver_query`、`io_context::strand` 与 `coroutine` 上关于已弃用隐式拷贝构造函数的警告。

  - 更新用于初始化 Winsock 的版本规格。

  - 修复 `co_spawn`，使取消导致的异常正确传播到完成处理程序。

  - 添加 `std::launder` 调用，修复 `awaitable<>` 内部存储中的未定义行为。

  - 在文件支持的 Windows 实现中补上缺失的 `file_base::append` 标志处理。

  - 更新套接字与描述符实现，增加更多在 `ioctl` 调用失败时回退到 `fcntl` 的情形。

  - 修复 `boost/asio/experimental/parallel_group.hpp` 头文件，使其自包含。

  - 修复 channel 与 `experimental::coro` 同时用于同一编译单元时的编译错误。

  - 文档补上缺失的 `CancellationSlot` 类型要求。

  - 修复异步操作发起函数推导返回类型的文档超链接。

  - 其他小规模文档更新。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 新增 RISC-V 上 `pause` 指令的支持（[PR#65](https://github.com/boostorg/atomic/pull/65)）。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - API 变更：

    - 状态码列表已更新，以符合 IANA 注册表。

  - 缺陷修复：

    - `buffers_cat.hpp` 中的不可达代码警告。

    - `websocker_server_awaitable` 示例中的连接错误处理。

    - 高级服务器示例中对 `async_write` 的并发调用。

    - zlib 与 minizip 的命名冲突。

    - 调用 `SSL_set_tlsext_host_name()` 之后应更新 host 字符串。

  - 功能增强：

    - 为 `bind_wrapper` 与 `bind_front_wrapper` 特化了 `asio::associator`。

    - 为错误类别（error category）message 函数添加非分配重载。

  - 文档：

    - 说明何时调用 `http::message::prepare_payload()` 是可选的。

    - 受 `basic_stream::expires_after()` 影响的操作。

    - `teardown()` 与 `async_teardown()` 是定制点。

    - 首次使用后移动或拷贝 `http::serializer` 是未定义行为。

    - `websocket::permessage_deflate` 应在执行 WebSocket 握手之前配置。

    - http 读操作中的 `bytes_transferred` 报告 HTTP 解析器消费的字节数。

  - 致谢：

    - Emile Cormier、JohannesWilde、yhzx233

- [Bimap](/libs/bimap/)（双向映射库）：

  - 修复侧集合（side collections）的异构查找（[PR#42](https://github.com/boostorg/bimap/pull/42)）。

- [Bind](/libs/bind/)（参数绑定库）：

  - 不再支持 C++03，需要 C++11 编译器（包括 GCC 4.7 或更高版本，以及 MSVC 12.0（VS 2013）或更高版本）。

- [Conversion](/libs/conversion/)（类型转换库）：

  - 移除对 `boost::lexical_cast` 的过时提及——它已不属于该库。感谢 [Danil Sidoruk](https://github.com/eoan-ermine) 提交的 PR [PR#28](https://github.com/boostorg/conversion/pull/28)！

- [Core](/libs/core/)（核心工具集库）：

  - 新增 `boost/core/functor.hpp` 头文件，其中的 `functor` 类模板用于将原始函数包装成函数对象类。

  - 修改 `null_deleter`、`fclose_deleter` 与受检删除器（checked deleter）的定义，使其不再把命名空间 `boost` 带入实参依赖查找（ADL）。用户可能需要显式限定被调用函数的命名空间，或添加 `using` 声明。

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - `path::generic_path` 与 `path::generic_string` 方法现在会移除返回路径中重复的目录分隔符。

  - **v4：** `path::generic_path`、`path::generic_string`、`path::make_preferred` 与 `path::lexically_normal` 在路径根名称（root name）中避免反斜杠与正斜杠之间的相互转换。例如，在 Windows 上，`path("\\\\?\\c:\\foo").generic_string()` 现在返回 `\\?\c:/foo` 而非 `//?/c:/foo`。类似地，`path("\\\\host/share/foo/..").lexically_normal()` 现在返回 `\\host\share`。

  - **v4：** 若两个路径中任一不存在，`equivalent` 现在会指示错误。

  - **v4：** 当输入路径的 `relative_path()` 为空时，`absolute` 现在返回带末尾目录分隔符的路径（[\#301](https://github.com/boostorg/filesystem/issues/301)）。

  - 新增接受单个 `error_code& ec` 实参的 `unique_path` 重载。该重载使用默认路径模型生成唯一路径。

  - 若输入路径为相对路径且不包含文件系统中存在的元素，`weakly_canonical` 现在生成绝对路径（[\#300](https://github.com/boostorg/filesystem/issues/300)）。

  - 为 `copy_file` 与 `copy` 操作新增 `copy_options::ignore_attribute_errors` 选项。该新选项允许忽略复制文件属性时可能出现的错误（[\#179](https://github.com/boostorg/filesystem/issues/179)）。

  - 在 Linux 上，基于 `sendfile` 与 `copy_file_range` 系统调用的 `copy_file` 后端会尝试为目标文件预分配存储。这可以减少文件系统碎片，并在空闲空间不足时提供早期错误指示。并非所有文件系统都支持该特性；若不支持存储预分配，文件复制照常进行。

  - 在支持 POSIX.1-2008 定义的 [`fdopendir`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fdopendir.html)、`openat` 及相关 API 的 POSIX 系统上，以及在 Windows 上，`recursive_directory_iterator` 现在在迭代期间使用文件描述符/句柄而非路径来查询文件状态并打开嵌套目录。这使得目录迭代对文件系统的并发修改更具韧性。

  - 移除了此前声明弃用的 API。具体包括 `path` 与 `recursive_directory_iterator` 的部分成员函数，以及 `is_regular`、`copy_directory`、`symbolic_link_exists`、`complete`、`copy_option`、`symlink_option`，还有 `boost/filesystem/convenience.hpp` 与 `boost/filesystem/path_traits.hpp` 头文件。文档中提到了被移除组件的可能替代方案。

  - 从容器类型（如 `std::vector<char>`）构造、赋值与追加 `path` 的支持现在默认禁用。用户仍可通过定义 `BOOST_FILESYSTEM_DEPRECATED` 启用该功能。该功能仍处于弃用状态，并将在未来发布中彻底移除。

- [Function](/libs/function/)（多态函数包装库）：

  - 不再支持 C++03，需要 C++11 编译器（包括 GCC 4.7 或更高版本，以及 MSVC 12.0（VS 2013）或更高版本）。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 功能增强：

    - [PR#1247](https://github.com/boostorg/geometry/pull/1247) 使用 `if constexpr` 宏取代条件宏。

    - [PR#1242](https://github.com/boostorg/geometry/pull/1242) 将策略传递给按侧排序（sort by side）。

    - [PR#1234](https://github.com/boostorg/geometry/pull/1234) 新增 clang/mac/darwin/arm64 的 CMake 文件。

  - 已解决问题：

    - [\#1231](https://github.com/boostorg/geometry/issues/1231)、[\#1244](https://github.com/boostorg/geometry/issues/1244) 修复 CCW（逆时针）多边形无效的集合运算。

    - [\#1259](https://github.com/boostorg/geometry/issues/1259) 修复 CUDA NVCC 编译器的编译错误。

    - [\#1250](https://github.com/boostorg/geometry/issues/1250) 修复线串（linestring）缓冲区返回错误内部多边形。

    - [\#1230](https://github.com/boostorg/geometry/issues/1230) 修复 union 运算扰动一个点并返回错误结果。

    - [\#1229](https://github.com/boostorg/geometry/issues/1229) 修复 union 产生自相交。

    - [PR#1248](https://github.com/boostorg/geometry/pull/1248) 通过将封闭聚类（closed clusters）中的 turn 设为不可遍历，修复缓冲区问题。

    - [PR#1246](https://github.com/boostorg/geometry/pull/1246) 修复 converter 与 is_base_of 的编译。

    - 各类错误与警告的修复。

- [Iterator](/libs/iterator/)（迭代器构建设施库）：

  - 对 C++03 的支持已弃用，将在未来发布中移除。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 现在使用 Boost.Endian 处理字节序。

  - 对 Boost.System 与 Boost.Container 组件的别名已弃用，并**将在 1.87.0 中完全移除**。

  - 基于 Boost.Describe 描述的类，其转换支持私有成员。

  - `visit` 新增右值引用重载。

  - 新增对路径类类型（path-like types）的转换支持。

  - 解析到描述类时正确考虑继承成员。

  - 禁用自引用序列的转换。

  - 修复 `visit` 中的引用处理。

- [LEAF](/libs/leaf/)（轻量级错误处理库）：

  - 用于在线程间传输错误对象与异常的新 API：`try_capture_all`。

  - `result<T>` 能够传输经 `try_capture_all` 捕获的异常。

  - `result<T>` 传输动态捕获的错误对象时效率更高。

  - 旧的 `make_shared_context`/`capture` API 已弃用，将在下一发布中移除。

  - 移除在异常中传输动态捕获错误对象的支持。

- [LexicalCast](/libs/lexical_cast/)（字符串与数值等类型转换库）：

  - 大幅重写内部逻辑，将优化路径与基于 C++ 标准库 I/O 的流分离：

    - 基于标准库的流在更少的情形下构造，带来**更好的性能**；

    - 更少的模板实例化与更简单的代码；

    - 始终使用 `std::char_traits`（不再使用来自输入/输出类型的自定义 traits，因为它会导致链接期或运行期错误）；

    - 修复前向声明的 boost::array 的误用（感谢 [13steinj](https://github.com/13steinj) 提交报告 [\#64](https://github.com/boostorg/lexical_cast/issues/64)！）；

    - 遵循 C++ 标准库的趋势，放弃对 `volatile` 输入类型的支持。

  - 优化从 std::basic_string_view 与 boost::basic_string_view 的转换 [\#30](https://github.com/boostorg/lexical_cast/issues/30)。

  - 移除对 Boost.NumericConversion 与 Boost.MPL 的依赖。修复浮点类型转换为算术类型的若干情形。

  - 库现在可在 `-fno-sanitize-recover=integer` 下正常编译并工作 [\#45](https://github.com/boostorg/lexical_cast/issues/45)。

- [Locale](/libs/locale/)（本地化与 Unicode 文本处理库）：

  - 修复 C++20 模式下因缺少 `char8_t` 的 typeinfo 导致的链接问题。

  - 修复使用自带 IConv 的 ICU 时的 IConv 编译标志。

  - 如文档所述，`collator` 如会抛异常，现在也只在构造时抛出。

  - `collator` 不再派生自 `std::collator`，以避免当前后端不可用时可能的类型混淆 [PR#216](https://github.com/boostorg/locale/pull/216)。

  - 检测到有缺陷的 IConv 库时（例如某些 MacOS 版本）抛出异常，而不是无限循环 [PR#218](https://github.com/boostorg/locale/pull/218)。

  - 将 `date_time` 的分辨率降至秒，因为毫秒并不总是容易获得并会造成困惑 [\#221](https://github.com/boostorg/locale/issues/221)。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - 新增一组优化算法：

    - 差分进化（Differential Evolution）[PR#1062](https://github.com/boostorg/math/pull/1062)

    - JSO [PR#1065](https://github.com/boostorg/math/pull/1065)

    - 随机搜索（Random Search）[PR#1071](https://github.com/boostorg/math/pull/1071)

    - CMA-ES [PR#1074](https://github.com/boostorg/math/pull/1074)

  - 修复非中心 F（NCF）生存函数中的除以 0 警告。

  - 修复 `ccmath::floor`/`ceil` 对大实参超出 constexpr 深度限制而失败的问题。

  - 提高 `quartic_roots` 的精度。

  - 修复 libstdc++14 的 cstdfloat 数值极限检测宏。

  - 修复 MSVC UCRT 在使用 C++14 时于 complex.h 中定义 `_Complex_I` 的问题 [PR#1060](https://github.com/boostorg/math/pull/1060)。

  - 改进 cstdfloat 的 iostream 支持 [PR#1066](https://github.com/boostorg/math/pull/1066)。

  - 修复在非独立环境中使用独立（standalone）模式时 Boost.Config 宏的重复定义。

  - 代码覆盖率显著提升，并附带相关缺陷修复。

- [MSM](/libs/msm/)（有限状态机库，Meta State Machine）：

  - **重大更新**。后端更新（back11）。要求 C++11。文档现在将其作为默认（后端）。

  - **重大新特性**。新前端（PlantUML）。要求 C++20。

  - 各类缺陷修复（编译器错误与警告、延迟事件的优先级）。

- [Multi-index Containers](/libs/multi_index/)（多索引容器库）：

  - 修复文档错误。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - 修复来自 C++23 `<limits>` 的弃用警告 [PR#575](https://github.com/boostorg/multiprecision/pull/575)。

  - 修复小位数的 cpp_bin_float [PR#577](https://github.com/boostorg/multiprecision/pull/577)。

  - 修复 `-Wpessimizing-move` [PR#580](https://github.com/boostorg/multiprecision/pull/580)。

  - 新增 codecov 覆盖率运行。

  - 减少 cpp_dec_float 乘法中的截断 [PR#585](https://github.com/boostorg/multiprecision/pull/585)。

  - 修复 `complex_adaptor` 以符合精度要求 [PR#597](https://github.com/boostorg/multiprecision/pull/597)。

  - 修复 tommath 破坏性变更的影响 [PR#603](https://github.com/boostorg/multiprecision/pull/603)。

  - 修复可转换为 number 的类型参与算术运算符重载的问题 [\#608](https://github.com/boostorg/multiprecision/issues/608)。

- [MySQL](/libs/mysql/)（MySQL 客户端库）：

  - **破坏性变更**：Boost.MySQL 现在要求链接新的 **Boost.Charconv** 需编译库。这解决了一个区域设置依赖问题，提高了效率，并为新的客户端 SQL 格式化特性提供支撑。

  - 新增对**连接池（connection pools）**的实验性支持，可复用会话并提供内建的重连与错误处理。

  - 新增对**类型擦除连接**（`any_connection` 类）的实验性支持。`any_connection` 不是模板，具有更简单的连接建立与重连语义。

  - 新增对**客户端 SQL 格式化函数**（`format_sql` 与 `format_sql_to`）的实验性支持。它们支持在客户端安全地组装查询，从而实现批量插入、动态过滤或 PATCH 式更新等模式。

  - 修复影响 `close_statement` 与 `async_close_statement` 的性能问题，该问题可能在应用代码中造成显著延迟。

  - 新增对使用 `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT` 构建的支持。

  - 已弃用的执行接口（`connection::query`、`connection::start_query`、`connection::execute_statement`、`connection::start_statement_execution` 及其异步对应版本）现在会触发警告，因其计划在 Boost 1.86 中移除。

  - 修复导致部分错误消息被截断的缺陷。

  - 警告清理。使用 `-Wall` 与 `-Wextra` 构建时现已无警告。

  - 所有 `field_view` 构造函数现在都是稳定的。

  - 库内部已用 sans-io 方式重写，以降低复杂度。

- [Odeint](/libs/numeric/odeint/)（常微分方程求解库）：

  - **破坏性变更**：该库现在显式要求 C++14，而非通过包含 Boost.Math 隐式要求。

  - 修复与 Thrust 1.10.0 的兼容性。

  - 移除 C++03 时代的 Boost 组件：

    - Array

    - Bind

    - Function

    - Static_assert

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - `boost::pfr::get_name` 现在可在部分编译器上处理局部类型。感谢 [Bela Schaum](https://github.com/schaumb) 提交的 PR [PR#152](https://github.com/boostorg/pfr/pull/152)！

  - 移除未使用的实现细节。感谢 [Denis Mikhailov](https://github.com/denzor200) 提交的 PR [PR#154](https://github.com/boostorg/pfr/pull/154)。

  - 允许从 `boost::pfr::structure_to_tuple` 抛出异常。感谢 [Denis Mikhailov](https://github.com/denzor200) 提交缺陷报告 [\#155](https://github.com/boostorg/pfr/issues/155)。

  - 字段反射技巧现已在文档中描述。感谢 [\#150](https://github.com/boostorg/pfr/issues/150) 中的所有讨论参与者！

- [Random](/libs/random/)（随机数生成器与分布库）：

  - 新增 splitmix64 伪随机数生成器（PRNG）[PR#89](https://github.com/boostorg/random/pull/89)。

- [System](/libs/system/)（错误码与 system_error 库）：

  - 不再支持 C++03，需要 C++11 编译器（包括 GCC 4.8 或更高版本，以及 MSVC 14.0（VS 2015）或更高版本）。

  - 已弃用的头文件 `boost/system/cygwin_error.hpp` 已被移除。

  - 不再支持原始且已过时的（32 位）MinGW。MinGW-w64（64 位与 32 位）仍受支持。

  - `operator&` 现在可用于 `result<void>`（通过接受一个无参函数实现）。

  - 为 `result` 新增 `operator|=`。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - **重大新特性：从任意异常获取堆栈回溯**。在一些 POSIX 平台上，`std::stacktrace::from_current_exception()` 现在返回当前异常对象的堆栈回溯，就像在抛出异常的位置捕获的一样。非常感谢 Andrei Nekrashevich 在 `libsfe` 中对该构想进行原型验证。

  - 修复 Windows 上 `boost_stacktrace_windbg` 的内存消耗问题。感谢 [ycyclop](https://github.com/ycyclop) 报告该问题 [\#111](https://github.com/boostorg/stacktrace/issues/111)，感谢 [Thiago A. Correa](https://github.com/correa) 提供更多信息，感谢 [Andrei Karpovskii](https://github.com/akarpovskii) 提供可行的修复方案。

  - 修复非隐藏可见性（non hidden visibility）下的库构建。感谢 [Jan Bouwer](https://github.com/JBouwer) 提供报告与修复方法的信息。

  - 文档新增关于异步信号安全（async signal safety）的独立章节。非常感谢 [tworonix](https://github.com/tworonix) 在 [\#131](https://github.com/boostorg/stacktrace/issues/131) 中指出该问题，感谢 [itrofimow](https://github.com/itrofimow) 提供相关信息。

- [STLInterfaces](/libs/stl_interfaces/)（迭代器/范围定制点 CRTP 基类库）：

  - 在 C++20 及更高标准中修改 `iterator_interface` 对输入迭代器的行为，以更贴近 C++20 concept（概念）。

  - 从 `iterator_interface` 移除隐藏友元（hidden friends），修复关于 concept 以不同约束被重复定义的错误。

  - 新增 `v3` 内联命名空间，其中包含基于推导 this（deducing this）而非 CRTP 的新 `iterator_interface`（C++23 及更高标准）。

  - 为 `closure::operator()` 新增右值限定重载，以防止悬垂临时对象。

- [Test](/libs/test/)（单元测试框架库）：

  - 遵循库专属的 `_NO_LIB` 宏 [PR#406](https://github.com/boostorg/test/pull/406)。

  - 针对有意不可达的代码，抑制 `__builtin_unreachable()` 引发的 MSVC C4702 警告。

  - 修复 `boost::function` 流输出错误 [PR#411](https://github.com/boostorg/test/pull/411)。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - 对 `value_type` 或 `init_type`（如适用）实参优化 `emplace()`，绕过创建中间对象。实参本身已与中间对象同类型。

  - 对 map 类容器的 `k,v` 实参优化 `emplace()`，将对象的构造延迟到确定要插入元素之时。该优化在 map 的 `key_type` 可移动构造或 `k` 实参本身就是 `key_type` 时生效。

  - 修复对带显式拷贝构造函数的分配器（allocator）的支持（[PR#234](https://github.com/boostorg/unordered/pull/234)）。

  - 修复 `unordered_multimap::find(k, hash, eq)` 的 const 版本中的缺陷（[PR#238](https://github.com/boostorg/unordered/pull/238)）。

- [Variant](/libs/variant/)（非递归可辨识联合库）：

  - 移除更多 C++11 之前的宏与变通方案。

- [Wave](/libs/wave/)（C/C++ 预处理器实现库）：修复的缺陷：

  - [\#200](https://github.com/boostorg/wave/issues/200)：发出的 pragma 缺少结尾换行。

  - [\#202](https://github.com/boostorg/wave/issues/202)：在 `BOOST_WAVE_BSIZE` 边界调用 fill 时 YYMARKER 未更新。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)（b2 构建系统框架）：

  - 包含 [B2（Boost 构建工具）版本 5.1.0](/tools/build/doc/html/#_version_5_1_0) 的发布。

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
