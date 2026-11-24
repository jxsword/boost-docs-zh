# Boost 1.77.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_77_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_77_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2021-08-11 14:25 GMT（原文日期行：August 11th, 2021 14:25 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.77.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 新增库（New Libraries）

- [Describe](/libs/describe/)（反射库）：一个 C++14 反射库，由 Peter Dimov 开发。提供用于描述枚举项（enumerator）与结构体/类成员的宏，以及查询这些信息的基础设施。

- [Lambda2](/libs/lambda2/)：一个 C++14、无依赖的单头文件 lambda 库，由 Peter Dimov 开发。允许通过诸如 `_1 + 5`、`_1 % 2 == 0`、`_1 > _2` 或 `_1 == ' ' || _1 == '\t'` 之类的表达式构造简单函数对象。

## 更新的库（Updated Libraries）

- [Any](/libs/any/)（类型安全的任意类型容器库）：

  - 新增 `boost::anys::basic_any`——一种带可定制小对象优化（Small Object Optimization）的数据类型，其实例可持有任何满足 ValueType 要求的类型的实例（非常感谢 Ruslan Arutyunyan @rarutyun）。如果您不确定是否真的需要它，请改用 `boost::any`。

  - 开始使用 GitHub Actions CI 进行额外测试。

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 新增对单个异步操作取消（cancellation）的支持。

  - 新增 `associator` 特征（traits），用于以泛型方式转发关联器（associators）。

  - 更改 Asio 中实现的所有异步操作，使其以右值引用调用完成处理程序（completion handler）。

  - 新增对具有多个完成签名（completion signature）的异步操作的支持。

  - 为 `awaitable<>` 新增 `operator&&` 与 `operator||`，使协程可以简单地并行等待。

  - 新增 `experimental::as_tuple` 完成标记适配器。

  - 新增 `experimental::append` 完成标记适配器。

  - 新增 `experimental::prepend` 完成标记适配器。

  - 新增 `experimental::deferred` 完成标记（completion token），允许异步操作的延迟执行。

  - 新增 `experimental::parallel_group` 类与 `experimental::make_parallel_group` 函数。

  - 新增 `experimental::promise`，允许异步操作的即时（eager）执行与同步。

  - 新增 `experimental::coro` 类模板：一个 C++20 协程原语，能够同时结合异步等待（`co_await`）与产出（`co_yield`）。

  - 为 `ssl::stream<>` 新增移动赋值。

  - 更改 `co_spawn`，使协程的初始步骤通过 `dispatch` 分发至执行器（executor）。

  - 在与异步操作一同使用时，为 `any_executor` 与 `any_io_executor` 启用额外优化。

  - 为 `awaitable<>` 添加 `nodiscard` 属性。

  - 增加默认回收分配器（recycling allocator）中缓存槽位的数量。

  - 更改默认分配器行为以遵循对齐要求，从而支持超对齐（over-aligned）类型。

  - 确保反向名称解析中的结果字符串总是被初始化。

  - 修复 `use_awaitable_t::executor_with_default` 中的递归模板实例化问题。

  - 修复 `any_io_executor` 的相等运算符，使其基于目标执行器正确返回结果。

  - 修复 `strand<>`，避免使用可能已被移走的执行器。

  - 确保在检测编译器特性时，不将针对 gcc 的测试用于 clang。

  - 禁用 MSVC 自带 clang 的协程支持。

  - 修复定义 `OPENSSL_NO_SSL_INTERN` 时与新版 LibreSSL 的兼容性。

  - 修复 `posix::basic_stream_descriptor` 的移动操作，使其可配合非默认执行器工作。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_77_0/doc/html/boost_asio/history.html)。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 新增用于构造原子引用对象的工厂函数 `make_atomic_ref` 与 `make_ipc_atomic_ref`。

  - 为 `atomic_ref` 与 `ipc_atomic_ref` 新增 C++17 模板实参推导指引（deduction guides），允许在模板实参可从构造函数实参推导时省略它们。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 本次维护更新包含若干次要缺陷修复与更新的 CI 报告。

  - 我们很想知道您或您的公司如何使用 Beast，欢迎在[使用 Beast 的公司与个人（Companies and Individuals Using Beast）](https://github.com/boostorg/beast/wiki/Companies-and-Individuals-Using-Beast)列表中添加条目。

  - 完整变更清单请参见[发布说明（Release Notes）](/libs/beast/doc/html/beast/release_notes.html)。

- [Conversion](/libs/conversion/)（类型转换库）：

  - `boost::implicit_cast` 现在为 `constexpr`（[\#25](https://github.com/boostorg/conversion/issues/25)）。

  - 修复失效链接（[PR#23](https://github.com/boostorg/conversion/pull/23)）。

  - 开始使用 GitHub Actions CI 进行额外测试。

- [Core](/libs/core/)（核心工具集库）：

  - 修改 `boost/core/uncaught_exceptions.hpp` 以兼容 Mac OS 10.4 及更早版本。（[PR#92](https://github.com/boostorg/core/pull/92)）

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 在 `boost::dll::library_info` 中增加对畸形 ELF 的更多运行期检查。

  - 在 `boost::dll::library_info` 中，当 `.symtab` 为空或缺失时使用 ELF `.dynsym` 节的信息。

  - 在 `boost::dll::library_info` 中列出受保护的 ELF 符号，因为它们可用于导入（[\#50](https://github.com/boostorg/dll/issues/50)）。

  - 移除 POSIX 环境下多余的 `wchar_t` 到 char 的转换，感谢 Vladislav Shchapov（[PR#49](https://github.com/boostorg/dll/pull/49)）。

  - 开始使用 GitHub Actions CI 进行额外测试。

- [Filesystem](/libs/filesystem/)（可移植文件系统操作库）：

  - **隆重推出 Boost.Filesystem v4。** 库的这一新版本移除了 v3 的全部弃用特性，并做出多项破坏性 API 变更，旨在使 Boost.Filesystem 与 C++17 引入的 std::filesystem 更加兼容。这些差异在发布说明与文档中以 **v3** 与 **v4** 标签描述，并在单独章节中汇总。用户可在编译代码时将 `BOOST_FILESYSTEM_VERSION` 宏定义为 3 或 4 来选择 Boost.Filesystem 版本。无需为每个库版本单独编译 Boost.Filesystem——单个二进制文件同时支持 v3 与 v4。用户应避免在同一应用中同时使用 v3 与 v4，因为这可能导致隐蔽的缺陷。目前 v3 为默认版本；未来发布中 v4 将成为默认版本，最终 v3 将被移除。v4 已可使用，但仍处于开发之中，未来可能还有破坏性 API 变更。

  - **v4：** 当路径仅由根名称或根目录组成时，`path::filename`、`path::stem` 与 `path::extension` 不再将其视为文件名。例如在 Windows 上，`path("C:").filename()` 过去返回 "C:"，`path("C:\\").filename()` 过去返回 "\\"（译注：原文该处引号残缺）；现在两者均返回空路径。（[\#88](https://github.com/boostorg/filesystem/issues/88)、[\#194](https://github.com/boostorg/filesystem/issues/194)）

  - **v4：** `path::stem` 与 `path::extension` 不再将"以点开头且无其他点"的文件名视为带扩展名。以点开头的文件名通常被视为扩展名为空的文件名。在大多数类 UNIX 系统上，前导点用于指示隐藏文件。（[\#88](https://github.com/boostorg/filesystem/issues/88)）

  - **新增：** 改进对 Windows 上各类路径前缀的支持。新增本地设备前缀（local device prefix，"\\.\）的支持与 NT 路径前缀（NT path prefix，"\\?\）的实验性支持（译注：原文该处引号残缺）。这些前缀将包含在路径的根名称中。注意，在 Boost.Filesystem v3 中使用这些前缀可能产生意外结果（例如 `path("\\\\.\\").stem() == "\\\\"`）。建议仅在 Boost.Filesystem v4 中使用这些前缀。

  - 重构 `path::lexically_normal` 实现，消除规范化路径中点（"."）元素在某些情形下的重复。

  - **新增：** 在 Linux 上新增对 `statx` 与 `getrandom` 系统调用的运行期检测。当系统调用在编译期存在但在运行期以 `ENOSYS` 失败时（例如在限制该系统调用的 Docker 容器中，即使宿主机上可用），这会很有用。（[\#172](https://github.com/boostorg/filesystem/issues/172)）

  - **新增：** 支持在构建库时禁用各种系统 API 的使用。当库配置脚本检测到某 API 存在但因故不得使用时（例如运行期检测在目标系统上不工作），这会很有用。更多细节请参见库文档中对配置宏的说明。

  - **新增：** 为 `copy_file` 操作新增 `copy_options::synchronize_data` 与 `copy_options::synchronize` 选项。这些选项允许将写入的数据与属性同步到永久存储。这些选项在性能上代价较高，但可确保复制数据的可靠性。注意，自 Boost.Filesystem 1.74.0 起，`copy_file` 在 POSIX 系统上会执行隐式数据同步。本发布增加了对更多平台的支持，并默认禁用数据同步，同时允许调用方显式请求同步。（[\#186](https://github.com/boostorg/filesystem/issues/186)）

  - 在 POSIX 系统上，为内部发出的部分系统调用新增对 `EINTR` 错误码的处理。特别是，`close` 上的 `EINTR` 此前可能被忽略，在 HP-UX 上会导致文件描述符泄漏。

  - 在基于 Linux `sendfile` 与 `copy_file_range` 系统调用的 `copy_file` 实现中，新增对指示特定文件系统不支持该系统调用的错误码的处理，并回退到通用的 `read`/`write` 循环。这应能修复 `copy_file` 在 [eCryptFS](https://www.ecryptfs.org/) 及可能的其他文件系统上失败的问题。（[\#184](https://github.com/boostorg/filesystem/issues/184)）

  - `copy_file_range` 系统调用现在自 Linux 内核 4.5 起即被使用，而此前仅在 5.3 及以上启用。当 `copy_file_range` 跨文件系统复制给定文件失败时，`copy_file` 实现将回退到 `sendfile` 或 `read`/`write` 循环。

  - 基于 Linux `sendfile` 与 `copy_file_range` 系统调用的 `copy_file` 实现将不会用于已知包含生成内容文件的文件系统。这些系统调用与此类文件不兼容，复制它们会产生零大小文件。将改用通用的 `read`/`write` 循环。目前列入黑名单的文件系统有：procfs、sysfs、tracefs 与 debugfs。

  - 在基于 `read`/`write` 循环的 `copy_file` 实现中，增大了用于临时存储的缓冲区上限，并考虑目标文件系统的块大小以获得更优性能。

  - 在 Windows CE 上，调用 `current_path` 获取进程当前路径现在会报错失败，而不是成功返回一个根路径。该平台不支持当前目录。在先前版本的 Boost.Filesystem 中，更改当前路径已会以类似方式失败。

  - 在 `canonical` 中，修复当先前的符号链接被解析为与原始路径根不同的绝对路径时，对指向根之上目录的符号链接的检查。

  - 在 `canonical` 中，新增对调用期间可解析符号链接最大数量的限制。该限制目前至少为 40 个符号链接。

  - 在 Windows 上，`canonical` 与 `weakly_canonical` 现在对结果路径中的根目录分隔符使用 `path::preferred_separator`。这修复了 Windows API 无法处理 UNC 路径与以 Win32 文件系统前缀（"\\?\）开头的路径中的通用分隔符而导致的"找不到文件"错误（译注：原文该处引号残缺）。（[\#87](https://github.com/boostorg/filesystem/issues/87)、[\#187](https://github.com/boostorg/filesystem/issues/187)）

  - **新增：** 新增接受 `base` 路径作为实参的 `weakly_canonical` 重载。

  - 在 Windows 上，当输入路径包含文件系统中不存在但被后续点点（".."）元素抵消的元素时，`weakly_canonical` 不再报错失败。例如，若 "C:\a" 目录不存在，`weakly_canonical("C:\\a\\..")` 此前会失败。（[\#201](https://github.com/boostorg/filesystem/issues/201)）

  - 在 Windows 上的 `read_symlink` 中，修正重解析点（reparse point）处理。对于某些挂载点（例如由 [Box](https://www.box.com/) 云存储驱动创建的）以及打印名称为空的目录联接点（directory junction），该操作会返回空路径。新实现现在会解析重解析点的替代名称（substitute name），并尝试据此重构 Win32 路径。（[\#187](https://github.com/boostorg/filesystem/issues/187)）

  - 在 Windows 上，当标准库支持以宽字符路径打开文件时，`boost/filesystem/fstream.hpp` 提供的文件流在 libc++ 7.0 及更高版本上将使用宽字符路径。（[\#181](https://github.com/boostorg/filesystem/issues/181)）

  - 在 Windows 上，若 Windows 配置为[开发者模式（Developer mode）](https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development)，创建符号链接应不再需要提升的权限。

  - 在部分编译器上，Boost.Filesystem 内部使用的全局对象现在会在用户的全局析构函数被调用之后再销毁。这允许在程序终止阶段调用 Boost.Filesystem 方法。这尤其涉及用于字符编码转换、可通过调用 `path::imbue` 安装的路径 locale（本地化环境）。受支持的编译器包括 MSVC、GCC 与 Clang，以及其他支持通过 `#pragma section`（适用于 MSVC 兼容编译器）或 `__attribute__ ((init_priority))`（适用于 GCC 兼容编译器）自定义程序初始化顺序的编译器。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 功能增强：

    - [PR#812](https://github.com/boostorg/geometry/pull/812) distance 与 comparable_distance 的伞式策略（umbrella strategies）（暂未载入文档）。

    - [PR#840](https://github.com/boostorg/geometry/pull/840) 多种算法的伞式策略（暂未载入文档）。

    - [PR#850](https://github.com/boostorg/geometry/pull/850) 引入 DynamicGeometry 与 GeometryCollection 概念及部分算法中的支持（暂未载入文档）。

    - [PR#855](https://github.com/boostorg/geometry/pull/855) 与策略相关的多项改进。默认策略现已随算法一并提供。

  - 已解决问题：

    - [\#865](https://github.com/boostorg/geometry/issues/865) rtree 序列化中抛出异常。

    - [\#439](https://github.com/boostorg/geometry/issues/439) box（盒）球面面积计算无效。

    - [\#838](https://github.com/boostorg/geometry/issues/838) union_() 结果无效。

    - [\#851](https://github.com/boostorg/geometry/issues/851) 地理坐标系下 segment/box 相离（disjoint）结果无效。

    - [\#861](https://github.com/boostorg/geometry/issues/861) intersection() 结果无效。

  - 缺陷修复：

    - [PR#832](https://github.com/boostorg/geometry/pull/832) 修复 box 球面与地理面积计算。

    - [PR#853](https://github.com/boostorg/geometry/pull/853) 修复地理坐标系下 segment/box 相离判断。

    - [PR#866](https://github.com/boostorg/geometry/pull/866) 修复根节点元素数少于最小值时 rtree 的序列化。

    - [PR#886](https://github.com/boostorg/geometry/pull/886) 修复 knn rtree 查询缺陷，该缺陷导致 k 值较大时查询缓慢。

    - 集合运算与 buffer（缓冲区）中的多项修复。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - `value_to` 支持 `TupleLike` 类型。

  - `value_to` 与 `value_from` 支持 `std::array` 及类似类型。

  - 新增从 `string` 到 `std::string_view` 的隐式转换运算符。

  - 为 json 类型新增 `std::hash` 特化。

  - 修复 `object` 与 `key_value_pair` 中的分配错误。

  - 修复从构成空区间的一对迭代器构造 `array` 时的崩溃。

- [LexicalCast](/libs/lexical_cast/)（字符串↔数值等类型转换库）：

  - 修复将超出 int 可表示范围的浮点值赋给 int 的问题。

  - 开始使用 GitHub Actions CI 进行额外测试。

- [Log](/libs/log/)（日志库）：

  - 修复 riscv32 目标平台的编译。（[PR#150](https://github.com/boostorg/log/pull/150)）

- [Mp11](/libs/mp11/)（C++11 元编程库）：

  - 新增 `mp_intersperse`、`mp_split`、`mp_join`。

- [Multi-index Containers](/libs/multi_index/)（多索引容器库）：

  - 维护性工作。

- [Nowide](/libs/nowide/)（Windows 下 UTF-8 标准 I/O 适配库）：

  - 允许在 `main` 之前使用 `iostream` 类（尽力而为，适用于大多数环境）。

  - 修复重定向输入/输出情形下 `cin`/`cout`/`cerr` 中 `rdbuf` 的初始化。

  - 修复使用 `putback()` 之后 `cin::unget()` 的边界情形。

  - 修复移动赋值后 `filebuf` 的 `close` 可能被延迟的问题。

  - 提升 `utf8_codecvt` 的性能。

- [PFR](/libs/pfr/)（无宏结构体反射（Magic GET）库）：

  - 现在采用基于 MurMur Hash 的 hash_combine() 实现，以减少冲突次数并提升 `boost::pfr::hash_value()` 的质量。

  - 现已支持 Visual Studio 2017 的 C++14 模式（感谢 Denis Mikhailov，即 @denzor200）。

  - 修复了 inspect 工具发现的问题。

  - 修复了部分警告，包括移除 include/boost/pfr/detail/fields_count.hpp 中多余的分号（[\#72](https://github.com/boostorg/pfr/issues/72)）。

  - 为继承类型新增编译期断言（感谢 Denis Mikhailov，即 @denzor200）。

  - 在开启强制拷贝消除（guaranteed copy elision）的情况下，现在可以对含不可移动字段的聚合（aggregate）进行反射。

  - 修复拼写问题。

  - 开始使用 GitHub Actions CI 进行额外测试。

- [PropertyTree](/libs/property_tree/)（属性树（JSON/INI/XML 解析）库）：

  - 这是一个维护性发布。

  - 扩展 CI 中的编译器覆盖。

  - 修复 CMakeLists.txt 的 Boost 兼容性。

- [System](/libs/system/)（错误码与 system_error 库）：

  - 从 `error_category` 到 `std::error_category` 的转换运算符得到改进，不再需要 `<map>` 或 `<mutex>`。

  - `error_category` 的比较运算符现在是内联友元（inline friend）而非成员函数（前一变更的副作用）。

  - `error_condition` 现在延迟调用 `generic_category()`，避免在真正需要之前实例化该对象。

  - `error_condition::failed` 与 `error_condition::message` 已撤销弃用，`operator bool()` 现在再次返回 `failed()` 的结果。

  - system 类别现在不调用 `generic_category()`，以避免实例化该对象。

  - `default_error_condition` 的返回值在某些情况下改为来自 generic 类别的 `error_condition`，而非来自 system 类别。当输入 `error_code` 来自 system 类别且不对应任何 `errc_t` 值时，在 POSIX 上会发生这种情况。

  - `error_code` 与 `std::error_code` 的互操作性得到大幅改进。现在可以从 `std::error_code` 构造 `boost::system::error_code`，也可以将 `boost::system::error_code` 传给接受 `std::error_code&` 的函数。

  - 新增 `error_condition` 的流插入运算符。

- [Uuid](/libs/uuid/)（UUID 生成与解析库）：

  - 新增 `to_chars`，用于以无分配方式写入 uuid 字符串（[PR#116](https://github.com/boostorg/uuid/pull/116)）。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)（b2 构建系统框架）：

  - 包含 [B2 version 4.6.1](/tools/build/doc/html/#_version_4_6_1) 的发布。

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
