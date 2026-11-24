# Boost 1.78.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_78_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_78_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2021-12-08 03:45 GMT（原文日期行：December 8th, 2021 03:45 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.78.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 已知问题（Known Issues）

以下补丁由库作者提供，因发现时间过晚而未能纳入本次发布修复。

- Boost.Build（b2 构建系统框架）在某些情况下会静默跳过库头文件与二进制文件的安装，参见 [\#104](https://github.com/bfgroup/b2/issues/104)。

  - 已在 [PR#113](https://github.com/bfgroup/b2/pull/113) 中修复，[补丁](/patches/1_78_0/0001-b2-fix-install.patch)。

- Boost.Atomic（原子操作库）在以 UWP（通用 Windows 平台）为目标时构建失败，参见 [\#54](https://github.com/boostorg/atomic/issues/54)。[补丁](/patches/1_78_0/0002-atomic-fix-uwp-build.patch)。

## 新增库（New Libraries）

本版无新增库。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 新增 io_uring 后端，可选择用于所有 I/O 对象，包括套接字、定时器与 POSIX 描述符。

  - 新增文件支持，包括面向流文件与随机访问文件的新类。该特性目前支持 Windows 上的 I/O 完成端口与 Linux 上的 io_uring。

  - 新增对 POSIX 与 Windows（当 I/O 完成端口可用时）上可移植管道的支持。

  - 新增对已注册缓冲区（registered buffers）的支持，使用 io_uring 后端时会有专门优化。

  - 新增通道（channels）的实验性支持，可用于以消息形式发送完成事件（completion）并将其排队。

  - 对 `experimental::coro` 实施了多项改进。

  - 在 clang 使用 MSVC 运行时（runtime）时禁用 `aligned_alloc`。

  - 改用更快的 `ip::network_v4::canonical()` 实现。

  - 为常见用例添加模板特化，以缩短编译时间。

  - 将 `io_context` 执行器（executor）的大小缩减为单个指针。

  - 增大 `execution::any_executor` 与 `any_io_executor` 的小对象缓冲区。

  - 修复在禁用可变参数模板时的多签名（multi-signature）处理。

  - 修复与新版 gcc、clang 的兼容性。

  - 修复在 Solaris 上的编译。

  - 修复在使用 MSVC 构建时对 Qt 所定义宏的防御。

  - 改进 ssl 设施发出的错误消息。

  - 修复 `bind_executor` 与完成标记（completion token）的兼容性。

  - 修复定义 `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT` 时的构建错误。

  - 为 `awaitable<>` 补充缺失的移动赋值运算符。

  - 修复在 MSVC 上使用协程时因分配内存对齐不正确而导致的访问违例（access violation）。

  - 修复 `experimental::parallel_group` 中在执行上下文于并行操作仍待处理时被关闭所发生的清理问题。

  - 澄清了并发提示（concurrency hints）相关文档。

  - 新增关于 C++20 协程错误处理技术的文档。

  - 修复了多种警告。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_78_0/doc/html/boost_asio/history.html)。

- [Assert](/libs/assert/)：

  - 新增 `source_location::to_string`。

- [Atomic](/libs/atomic/)：

  - 在 Android 上，非 IPC 的等待与通知操作改用进程本地（process-local）futex 操作。

  - 新增对仅定义 `SYS_futex_time64` 系统调用的 Linux 目标平台（如 riscv32）的支持。

  - 针对 clang 8 在 32 位 x86 目标平台上对 64 位类型 `std::alignment_of` 结果不正确的问题增加了变通方案。

  - 新增 ulock 后端，用于 Darwin 系统上自 Mac OS 10.12、iOS 10.0、tvOS 10.0 或 watchOS 3.0 起的等待与通知操作。

  - 在 Windows 上，修正了当以 Windows 8 或更高版本为目标时 *`atomic-type`*::`always_has_native_wait_notify`（各原子类型的 `always_has_native_wait_notify`）与相应能力宏之间的不一致。库现在将在公共头文件中直接使用 `WaitOnAddress` 及相关 API，因此若用户通过定义 `BOOST_USE_WINAPI_VERSION`、`_WIN32_WINNT` 或类似宏要求 Windows 8 或更高版本，则需链接 `synchronization.lib`。在支持自动链接（auto-linking）的编译器（如 MSVC）上会自动完成链接。

  - 新增对含填充位（padding bits）类型（联合类型除外）的支持，前提是编译器提供清除填充位的途径。gcc 11 与 MSVC 14.2（编译器版本 19.27）及更新版本支持该特性，支持类似内建函数（intrinsics）的其他编译器亦然。在不允许清除填充位的编译器上，含填充位的类型总体仍不受支持，x86 目标平台上的 80 位 `long double` 除外。新增 `BOOST_ATOMIC_NO_CLEAR_PADDING` 能力宏，用于指示何时清除填充不受支持。

  - `atomic_ref` 与 `ipc_atomic_ref` 的初始化构造函数不再使用原子指令清除被引用对象中的填充位。这降低了原子引用构造的开销。

  - `atomic` 与 `ipc_atomic` 的初始化构造函数现在对枚举、类与浮点类型为 `constexpr`。对类与浮点类型而言，当编译器支持 `constexpr` 的 `std::bit_cast`、类型无填充字节且实现原生原子操作无需填充时，构造函数才是 `constexpr`。

  - 按照 C++20 的规定，`atomic` 与 `ipc_atomic` 的默认构造函数现在对所含对象执行值初始化（value initialization）。对没有用户自定义默认构造函数的类型而言，这意味着默认构造的原子对象将被零初始化。

  - 针对 AIX 上因汇编工具不支持数字标签而导致的编译错误增加了变通方案。（[PR#50](https://github.com/boostorg/atomic/pull/50)）

  - 针对 Visual Studio 2015（Update 3 之前版本）的编译错误增加了变通方案。（[\#52](https://github.com/boostorg/atomic/issues/52)）

  - 更多细节请参见[变更日志（changelog）](/doc/html/atomic/changelog.html)。

- [Beast](/libs/beast/)：

  - 本次维护更新包含若干次要缺陷修复与更新的 CI 报告。

  - 修复 zlib 实现中的安全漏洞 CVE-2016-9840。

  - 修复 WebSocket permessage_deflate 实现。使用 Beast WebSocket 时压缩性能应会有所提升。

  - 移除测试流与测试框架对 RTTI（运行时类型信息）的依赖。现在可以使用我们便捷的测试流来检查嵌入式异步通信代码！

  - 我们很想知道您或您的公司如何使用 Beast，欢迎在[使用 Beast 的公司与个人（Companies and Individuals Using Beast）](https://github.com/boostorg/beast/wiki/Companies-and-Individuals-Using-Beast)列表中添加条目。

  - 完整变更清单请参见[发布说明（Release Notes）](/libs/beast/doc/html/beast/release_notes.html)。

- [Core](/libs/core/)：

  - 为 `<boost/core/cmath.hpp>` 新增通用实现，在定义了 `BOOST_CORE_USE_GENERIC_CMATH` 或平台在 `<cmath>` 中未提供必要设施时启用。

  - 新增 `boost::core::type_name`：以字符串形式返回类型名称的工具函数。

  - 新增 `boost::span`：C++20 `std::span` 的 C++11 实现（Glen Fernandes）。

- [Describe](/libs/describe/)：

  - 新增 `has_describe_enumerators`、`has_describe_bases`、`has_describe_members`。

  - 新增 `enum_to_string`、`enum_from_string`。

  - 新增关系运算符与流插入运算符。

  - 新增 `descriptor_by_name`、`descriptor_by_pointer`。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 修复缺失的 `#include`，感谢 Denis Blank（[PR#54](https://github.com/boostorg/dll/pull/54)）。

  - 移除 TravisCI，改用 GitHub Actions CI。

- [Filesystem](/libs/filesystem/)：

  - **v4：** 当路径以目录分隔符结尾时，`path::filename` 与 `path::iterator` 不再返回隐式的尾随点（"."）元素，而是返回空路径，与 C++17 的 std::filesystem 一致。这也会影响其他依据迭代器或文件名定义的方法，例如 `path::stem`、`path::compare` 或 `lexicographical_compare`。例如 `path("a/b/") == path("a/b/.")` 不再成立。（[\#193](https://github.com/boostorg/filesystem/issues/193)）

  - **v4：** `path::lexically_normal` 不再在规范化路径中产生尾随点（"."）元素，并且会省略尾随点点（".."）元素之后的目录分隔符。

  - **v4：** `path` 的追加（append）操作现在会考虑被追加路径中的根名称（root name）与根目录（root directory）。若被追加路径为绝对路径，或存在根名称且与源路径不同，则结果路径等价于被追加路径；若存在根目录，则结果为根目录加上基于源路径根名称重新定位（rebase）的相对路径；否则行为与 v3 类似。（[\#214](https://github.com/boostorg/filesystem/issues/214)）

  - `path::lexically_normal` 现在会将规范化路径根名称中的目录分隔符转换为首选分隔符。

  - 优化 `path::assign`、`path::append`、`path::concat` 的重载及相应运算符，避免不必要的路径复制并减少代码冗余。

  - 在 POSIX 系统上，修复 `absolute(p, base)` 在 `p` 以根目录开头时返回带 `base.root_name()` 根名称路径的问题。此时 `p` 已是绝对路径，应原样返回。

  - 当输入路径完全由点（"."）与点点（".."）元素组成时，`create_directories` 不再报错。实现不再在内部使用递归，因此在极长路径上能更好地防止栈溢出。

  - 在 Windows 上，`remove` 现在支持删除只读文件。该操作会尝试在删除前重置只读属性。注意，这带来一种可能：若操作失败且属性原值恢复失败，只读属性可能保持未设置状态。这同样影响 `remove_all`。（[\#216](https://github.com/boostorg/filesystem/issues/216)）

  - 出错时 `remove_all` 现在返回 `static_cast<uintmax_t>(-1)`，与 C++17 std::filesystem 一致。

  - 修复一个链接错误：当用户代码包含 `boost/filesystem/path.hpp` 但未包含 `boost/container_hash/hash.hpp`，且编译器被设置为保留未使用的内联函数时，会出现对 Boost.ContainerHash（容器哈希函数库）函数的未解析引用。（[\#215](https://github.com/boostorg/filesystem/issues/215)）

  - 针对 MSVC 及兼容编译器在发布构建中消除路径全局对象清理的问题增加变通方案。若 Boost.Filesystem 共享库在进程中被反复加载与卸载，这可能导致内存泄漏。（[\#217](https://github.com/boostorg/filesystem/issues/217)）

- [Geometry](/libs/geometry/)：

  - 功能增强：

    - [PR#894](https://github.com/boostorg/geometry/pull/894) rtree 查询的优化与重构。

    - [PR#913](https://github.com/boostorg/geometry/pull/913) 多种算法中的 DynamicGeometry 与 GeometryCollection 支持（暂未载入文档）。

    - [PR#922](https://github.com/boostorg/geometry/pull/922) distance 算法中的 DynamicGeometry 与 GeometryCollection 支持（暂未载入文档）。

  - 已解决问题：

    - [\#867](https://github.com/boostorg/geometry/issues/867) rtree 查询迭代器在 k 值较大时使用最近邻（nearest）谓词性能不佳。

    - [\#870](https://github.com/boostorg/geometry/issues/870) boost::geometry::self_turns 中的编译错误。

    - [\#896](https://github.com/boostorg/geometry/issues/896) 在定义 `BOOST_GEOMETRY_NO_ROBUSTNESS` 时 get_turns 中的断言失败。

  - 缺陷修复：

    - [PR#906](https://github.com/boostorg/geometry/pull/906) 修复 macos-11 配合 clang-12 时 buffer 结果无效的问题。

    - [PR#921](https://github.com/boostorg/geometry/pull/921) 修复 C++20（多种编译器）与 gcc-5 下的编译错误。

    - 集合运算与 buffer 中的多项修复。

- [JSON](/libs/json/)：

  - 本库的独立（standalone）使用模式已弃用。

  - 允许外部库对 `value_to` 与 `value_from` 进行前置声明（forward declaration）。

  - 修复数字解析中的有符号整数溢出。

  - 新增对 MSVC `/Zc:implicitNoexcept-` 选项的支持。

- [Lambda2](/libs/lambda2/)（单头文件 Lambda 表达式库）：

  - 在 `operator<<` 与 `operator>>` 中为第一个实参为流的情形添加特例，以支持 `std::cout << _1`。

  - 新增 `operator->*`。

  - 新增 `first`、`second`。

- [Log](/libs/log/)：

  - 总体变更：

    - 更新对 `char16_t` 与 `char32_t` 的 `std::codecvt` 特化的检测，以兼容 C++17 及更高标准。（[PR#159](https://github.com/boostorg/log/pull/159)）

    - 为进程间消息队列的接收方法新增对 C++17 `std::byte` 类型的支持。

    - 在 Windows 上，当为 Windows 8 或更高版本构建本库时，库将在版本命名空间中使用 `nt62` 标签表示目标操作系统 ABI。例如，版本命名空间可命名为 `v2_mt_nt62`。该名称将成为库导出的所有符号的一部分。在构建 Boost 与您的代码时，请一致地使用 `BOOST_USE_WINAPI_VERSION` 宏来指定最低目标 Windows 版本。

    - 提升 `dump` 流操纵器的 SSSE3 与 AVX2 实现的性能。

    - 新增对 CMake 构建系统的支持。目前仅支持库本身的构建，测试仍使用 Boost.Build 运行。

  - 缺陷修复：

    - 修复 POSIX 系统上 `reliable_message_queue::open_or_create`（或等价构造函数）中的竞态条件。多个线程或进程在并发调用 `open_or_create` 的同时向同一队列发送或接收消息，可能破坏队列内容并导致进程崩溃。（[\#162](https://github.com/boostorg/log/issues/162)）

    - 为 Windows 上定义 `BOOST_LOG_WITHOUT_SETTINGS_PARSERS` 时因缺少 `boost_log_setup` 库导致 `b2 install` 失败的问题增加了变通方案。（[\#164](https://github.com/boostorg/log/issues/164)）

  - 更多细节请参见[变更日志（changelog）](/libs/log/doc/html/log/changelog.html)。

- [Math](/libs/math/)：

  - 新增对三次方根（cubic roots）的支持。

  - 新增多项标准库数学例程的 `constexpr` 版本支持。

  - 新增对贝塞尔（Bezier）多项式的支持。

  - 改进 tanh-sinh 积分在最坏情形下的性能。

  - 禁止在积分例程中无意使用整数类型。

  - 对误差函数（erf）逼近在结果与 1 相差不超过 2 ulp 时的情形进行小幅更新。

  - 允许 Bernoulli（伯努利数）代码在无原子整数类型的平台上使用。

  - 改进非中心卡方分布（non-central Chi Squared distribution）的众数（mode）计算。

  - 改进 `<cstdfloat>` 复值初等函数的某些边界情形，参见 [\#507](https://github.com/boostorg/math/issues/507)。

- [Multi-index Containers](/libs/multi_index/)：

  - 为基于键的索引（key-based indices）新增 `contains`（issue [\#35](https://github.com/boostorg/multi_index/issues/35)）。

  - 为基于键的索引新增 `merge` 操作。该功能在多个方面超出标准对（无序）关联容器的规定，最显著的包括：

    - 源索引可以是任意类型，包括非基于键的索引。

    - 提供部分合并：例如 `x.merge(y,first,last)` 仅合并 `y` 中位于 [first,last) 区间内的元素。

  - 对于序列索引（sequenced indices）与随机访问索引，先前版本的 `splice` 是破坏性的，即元素先以拷贝方式插入目标，再从源中删除。现在，`splice` 与基于键的索引中的 `merge` 一样基于节点转移实现，并同样扩展为接受任意类型的源索引：实际上，`splice` 可视为基于键的索引中 `merge` 所提供的同一功能的前端。出于向后兼容的考虑，当源容器与目标容器的分配器不相等时，`splice` 仍保留破坏性行为。

  - 文档已说明：索引迭代器类型仅依赖于 `node_type` 与该索引在其 `multi_index_container` 中的位置（哈希索引除外，其唯一性/非唯一性也是依赖项之一）。这对经 `merge` 或 `splice` 转移的元素的迭代器有效性有影响。该性质是 C++ 标准邮件列表中所称 [SCARY 迭代器（SCARY iterators）](https://wg21.link/n2980)的一种变体。目前（2021 年 8 月）标准容器尚未强制要求 SCARY 性质。

  - 迭代器的 SCARY 性质现在在[安全模式（safe mode）](/libs/multi_index/doc/tutorial/debug.html#safe_mode)下同样得到保留。

- [Multiprecision](/libs/multiprecision/)：

  - 重构 rational_adaptor，移除对 Boost.Rational（有理数库）的依赖并提升性能。

  - 修复 type_traits 与 clang 相关的问题，参见 [\#383](https://github.com/boostorg/multiprecision/issues/383)。

  - 修复有缺陷的 Lehmer GCD（最大公约数）例程，参见 [\#370](https://github.com/boostorg/multiprecision/issues/370)。

  - 修正 mpc_complex 构造函数，使有损转换必须显式进行，参见 [\#363](https://github.com/boostorg/multiprecision/issues/363)。

  - 修正若干杂项配置问题（Intel 内建函数（intrinsics）的使用与 Apple clang）。

  - 修正 unsigned char 类型的部分 iostream 运算符。

  - 修正 mpq_rational 到整数类型的转换，参见 [\#342](https://github.com/boostorg/multiprecision/issues/342)。

- [Nowide](/libs/nowide/)：

  - 破坏性变更：`utf8_codecvt` 的 UTF-32 特化的 `do_unshift` 现在正确返回 `noconv` 而非 `ok`。

  - 移除 `utf8_codecvt` 中针对 UTF-16 输出的多余分支。

  - 在 MSVC 中将 `utf8_codecvt` 与 Unicode 字符类型一起使用时抑制弃用警告。

  - 修复在 `filebuf` 已分配内部缓冲区之后设置自定义缓冲区（`setbuf`）时可能出现的双重释放（double-free）。

- [PFR](/libs/pfr/)（无宏结构体反射（Magic GET）库）：

  - 补充缺失的 `#include <memory>`，以便包含 `std::addressof`。

  - 修复处理空聚合（aggregate）时的 -Wzero-length-array 警告。

  - 修复 MSVC 编译器 ≤ 1920 版本上的编译问题（感谢 Alexey Romanov，即 @alexey-romanov）。

  - 新增基础 CMakeLists.txt 支持（感谢 @pdimov，即 Peter Dimov）。

  - 文档的多项改进，包括指向 https://github.com/apolukhin/pfr_non_boost 的链接。

  - 新增 misc/strip_boost_namespace.sh 脚本，用于移除 `boost::` 与 `BOOST_` 前缀。

- [Predef](/libs/predef/)：

  - 版本 1.13.1。

  - 修正 "epoch" 的拼写。

  - 补充 sparc.h 中缺失的括号（来自 tkoecker）。

  - 更新文档，改用 Rouge 代码高亮样式与 Amber 通用样式。

- [Regex](/libs/regex/)（正则表达式库）：

  - **破坏性变更：** 按照 Perl 的行为，将 `\B` 改为 `\b` 的反义。

  - 更改 w32_regex_traits.hpp，使其不再包含 windows.h。

  - 修复模糊测试（fuzzing）相关问题 [\#151](https://github.com/boostorg/regex/issues/151)、[\#152](https://github.com/boostorg/regex/issues/152)、[\#153](https://github.com/boostorg/regex/issues/153)、[\#156](https://github.com/boostorg/regex/issues/156)。

- [System](/libs/system/)：

  - 为 `error_code` 新增源位置（source location）支持。

  - 新增 `error_code::to_string`、`error_condition::to_string`、`error_code::what`。

  - `system_error::what()` 现在包含源位置（若存在）。

  - 新增 `result<T, E = error_code>`：一个持有值或错误之一的类，定义于 `<boost/system/result.hpp>`。

- [Utility](/libs/utility/)：

  - 库文档转换为 QuickBook 文档格式（感谢 Alan de Freitas，[PR#79](https://github.com/boostorg/utility/pull/79)）。

- [Variant2](/libs/variant2/)：

  - 新增 `<boost/variant2.hpp>`。

  - 新增 `unsafe_get<I>`。

  - 新增 `visit_by_index`。

  - 新增 `operator<<`。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)：

  - 包含 [B2 version 4.7.2](/tools/build/doc/html/#_version_4_7_2) 的发布。

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
