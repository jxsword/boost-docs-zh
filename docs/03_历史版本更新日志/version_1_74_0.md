# Boost 1.74.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_74_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_74_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2020-08-14 05:02 GMT（原文日期行：August 14th, 2020 05:02 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.74.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 新增库（New Libraries）

- [STLInterfaces](/libs/stl_interfaces/)（迭代器/范围定制点 CRTP 基类库）：一组用于简化 STL 视图、迭代器与序列容器编写的 CRTP 基类库，由 Zach Laine 开发。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 新增拟议标准执行器（executors）的实现（[P0443r13](http://wg21.link/P0443r13)、[P1348r0](http://wg21.link/P1348r0) 与 [P1393r0](http://wg21.link/P1393r0)）。

  - 为 Asio 的 I/O 设施新增对拟议标准执行器的支持。

    - 所提供的执行器现已满足拟议标准执行器的要求。这些类也继续满足 Networking TS（网络技术规范）执行器模型的既有要求。

    - 所有 I/O 对象、异步操作与工具均可与新拟议标准执行器以及既有 Networking TS 执行器互操作。

    - 引入 `any_io_executor` 类型别名，作为所有 I/O 对象默认的运行期多态执行器。其默认为 `execution::any_executor<>` 模板。如需向后兼容，可定义 `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT`，改用旧的 `asio::executor` 多态包装器。

    - 可通过定义 `BOOST_ASIO_NO_TS_EXECUTORS` 禁用对既有 Networking TS 执行器模型的支持。

  - 为 `basic_waitable_timer` 新增可转换的移动构造与赋值。

  - 使用 `gcc` 10 时启用 C++20 协程（coroutine）支持。

  - 新增启动 awaitable 的 `co_spawn` 重载。

  - 为 `use_awaitable_t` 的默认执行器适配器新增构造函数重载，以支持执行器类型之间的转换。

  - 通过新增成员 `as_default_on()` 与 `as_default_on_t<>`，支持将 `detached_t` 用作默认完成标记（completion token）。

  - 为 `ssl::stream<>` 新增移动构造函数。

  - 将 `ssl::stream<>` 的写操作改为对聚合写（gather-write）缓冲区序列进行线性化。

  - 定义 `BOOST_ASIO_NO_DEPRECATED` 时，新增对已弃用的 `asio_handler_invoke`、`asio_handler_allocate` 与 `asio_handler_deallocate` 钩子的编译期检测。

  - 实施了多项性能优化。

  - 为处理程序跟踪（handler tracking）新增源码位置支持。

  - 对 `handlerviz.pl` 工具实施了多种改进。

  - 新增 `handlerlive.pl` 工具，用于处理处理程序跟踪输出，生成"存活"（live）处理程序列表。

  - 新增 `handlertree.pl` 工具，用于过滤处理程序跟踪输出，仅保留树中产生指定处理程序的那些事件。

  - 为基于 clang 的 Embarcadero C++ 编译器添加适配修改。

  - 修复多线程并发初始化 Windows I/O 完成端口后端时可能发生的死锁。

  - 修复 `async_compose`，使其在被以左值传入时能配合可复制处理程序工作。

  - 修复 `co_spawn` 中的完成签名推导。

  - 从 `executor_binder` 实现中移除多余的 `Executor` 基类。

  - 文档与示例的各类修复与改进。

  - 更多细节请查阅[修订历史](/doc/libs/1_74_0/doc/html/boost_asio/history.html)。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 为 `atomic_ref` 中的部分操作补充缺失的 `const` 限定符。

  - 新增 ARMv8-A 上对 `yield` 指令的支持。该指令在自旋循环内部使用，以降低 CPU 功耗。

  - 新增对 C++20 [等待与通知操作](/doc/html/atomic/interface.html#atomic.interface.interface_wait_notify_ops)的支持。实现包括涉及内部锁池的通用后端，以及针对 Windows、Linux、FreeBSD、DragonFly BSD 与 NetBSD 的专用后端。原子类型提供新方法 `has_native_wait_notify`、静态布尔常量 `always_has_native_wait_notify`，以及一组能力宏（capability macros），可用于检测实现是否支持给定类型的原生等待与通知操作。

  - 将 `atomic_flag` 的内部表示改为使用 32 位存储。这使某些平台上 `atomic_flag` 的等待与通知操作更为高效。

  - 新增内部锁池大小的构建期配置支持。用户可定义 `BOOST_ATOMIC_LOCK_POOL_SIZE_LOG2` 宏来指定锁池大小的以 2 为底的对数。默认值为 8，即锁池大小为 256，较上一发布所用的 64 有所增加。

  - 新增一组专用于[进程间通信](/doc/html/atomic/interface.html#atomic.interface.interface_ipc)的原子类型：`ipc_atomic_flag`、`ipc_atomic` 与 `ipc_atomic_ref`。建议用户将使用非 IPC 类型进行进程间通信的代码移植到新类型。新类型提供与其非 IPC 对应类型相同的操作集合，但存在以下差异：

    - 大多数操作新增了前置条件：给定原子对象的 `is_lock_free` 必须返回 `true`。若编译期已知此前置条件不满足，库将产生编译期错误。

    - 所提供的全部操作都是地址无关的（address-free），即原子对象（对于 `ipc_atomic_ref` 则为其引用的对象）可位于进程共享内存中，或以多个不同地址映射到同一进程。

    - 新的 `has_native_wait_notify` 操作与 `always_has_native_wait_notify` 常量指示对原生进程间等待与通知操作的支持。若该支持不存在，相关操作将以忙等待循环实现，效率较低，但仍是地址无关的。另外还提供一组单独的能力宏来指示该支持。

  - 新增 C++20 引入的 `atomic_unsigned_lock_free` 与 `atomic_signed_lock_free` 类型。这两个类型分别指示无符号与有符号整数的原子对象类型，要求为无锁，并最好原生支持等待与通知操作。

  - 新增面向 ARMv8-A（AArch32 与 AArch64 两者）的 gcc 汇编后端。新后端用于实现编译器内建函数不支持的操作（包括 AArch64 上的 128 位操作），也可在编译器内建函数不可用时使用。小端与大端目标均受支持。AArch64 后端支持 ARMv8.1 与 ARMv8.3 中定义的扩展。

  - 基于 gcc 汇编块的旧式 ARM 后端（用于 ARMv7 及更旧目标）新增对大端目标的支持。此前该后端假定小端内存布局，这对 64 位操作影响重大。

  - 在 x86 上通过使用 `lock` 前缀指令取代 `mfence`，提升了 seq_cst 存储与线程栅栏（thread fence）的性能。这意味着这些操作不再影响非临时（non-temporal）存储——这一点此前同样未获保证。如需为非临时内存访问排序，请使用专用指令与内建函数。

  - 修复 x86 目标上 80 位 `long double` 的能力宏问题：即使 128 位原子操作可用，也未指示无锁操作。

  - 修复 Alpha 目标上 gcc asm 块的编译。

  - 在 gcc `__sync*` 内建函数后端中，修复了大对象（大于指针大小）的存储与加载操作可能是非原子的问题。该实现目前假定小对象在所有现代架构上都能以单条指令原子存储。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 本次更新包含缺陷修复，并支持 Boost.Asio 的以下变更：

  - Beast 支持 `BOOST_ASIO_NO_DEPRECATED`。定义此宏可帮助识别您的 Beast 与 Asio 代码中使用已弃用 Asio 接口的部分。

  - Beast 也支持 `BOOST_ASIO_NO_TS_EXECUTORS`。定义此宏可识别对现已可能过时的 [Networking TS](https://cplusplus.github.io/networking-ts/draft.pdf)（网络技术规范）执行器的使用。

  - Asio 将默认使用[标准执行器（Standard Executors）](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p0443r11.html)模型。可通过定义 `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT` 阻止此行为，此时将默认使用 Networking TS 模型。设置该开关不会阻止程序显式使用标准执行器模型中的执行器。

  - 我们很想知道您或您的公司如何使用 Beast，欢迎在[使用 Beast 的公司与个人](https://github.com/boostorg/beast/wiki/Companies-and-Individuals-Using-Beast)（Companies and Individuals Using Beast）列表中添加条目。

  - 完整变更列表请参见完整的[发布说明](/libs/beast/doc/html/beast/release_notes.html)。

- [Bimap](/libs/bimap/)（双向映射库）：

  - 修正分配器用法（修复 C++20 编译）。（Glen Fernandes）

- [Config](/libs/config/)（编译器/平台特性检测与配置宏库）：

  - 实现 `BOOST_NO_CXX11_OVERRIDE` 与 `BOOST_OVERRIDE`。（Glen Fernandes）

- [Core](/libs/core/)（核心工具集库）：

  - 实现了分配器访问工具，以逐一特征（traits）与函数的形式提供 `allocator_traits` 的替代。它们在可能时支持 C++11 分配器模型，并为 C++98 兼容提供回退。现已被 Circular_Buffer、Wave、Lockfree、Heap、Smart_Ptr、Dynamic_Bitset、Format、Bimap 等库使用。（Glen Fernandes）

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 多项修复，使 `library_info` 能处理空共享对象。

  - 修复 C++98 与 C++11 模式下的编译（[\#28](https://github.com/boostorg/dll/issues/28)）。

  - 修复 `smart_library` 的名称修饰（mangling）（感谢 XiaLiChao82，[\#37](https://github.com/boostorg/dll/issues/37)）。

- [Endian](/libs/endian/)（字节序处理库）：

  - 在 `endian_reverse` 中启用作用域枚举类型。

  - 在 `endian_reverse_inplace` 中启用 `bool`、`enum`、`float`、`double`。

  - 新增针对数组的 `endian_reverse_inplace` 重载。

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - 移除了 Windows 上符号链接与硬链接支持的编译期检查，改用运行期检查（[PR#142](https://github.com/boostorg/filesystem/pull/142)）。

  - 修复 Windows 上 `canonical` 与 `read_symlink` 中对重解析点（reparse points）的处理。这也会影响实现中涉及 `canonical` 与 `read_symlink` 的其他算法（[PR#100](https://github.com/boostorg/filesystem/pull/100)、[\#85](https://github.com/boostorg/filesystem/issues/85)、[\#99](https://github.com/boostorg/filesystem/issues/99)、[\#123](https://github.com/boostorg/filesystem/issues/123)、[\#125](https://github.com/boostorg/filesystem/issues/125)）。

  - 修复 Windows 上如果同一符号链接被并发打开，`read_symlink` 可能失败或以共享冲突（sharing violation）错误导致其他操作失败的问题（[\#138](https://github.com/boostorg/filesystem/issues/138)）。

  - 修复 `is_symlink(directory_entry)` 总是返回 `false` 的问题，即使该目录项实际指向符号链接（[PR#148](https://github.com/boostorg/filesystem/pull/148)）。

  - 为 `directory_entry` 与 `error_code` 补充缺失的状态检查操作重载（如 `is_directory(directory_entry, error_code&)`）。移除了不接受 `error_code` 参数的重载上不正确的 `noexcept` 说明。

  - `copy_file` 实现已更新为按 C++20（\[fs.op.copy.file\]/4.1）的要求对源文件与目标文件执行检查。特别地，若源文件或目标文件不是普通文件，或源路径与目标路径标识同一文件，该操作将失败。

  - 在 POSIX 系统上，若目标文件被覆盖，`copy_file` 现在还会将源文件权限复制到目标文件。

  - **新增**：在 Linux 上添加了基于 `sendfile` 与 `copy_file_range` 系统调用的 `copy_file` 实现，可提升文件复制性能，在网络文件系统上尤为明显。

  - **弃用**：与 `copy_file` 操作一起使用的 `copy_option` 枚举已弃用。作为替代，新增了新枚举 `copy_options`（注意末尾的 's'）。新枚举包含与 C++20 中 `copy_options` 枚举类似的值。旧枚举值已映射到新枚举。旧枚举将在未来发布中移除。

  - **新增**：添加 `copy_options::skip_existing` 选项，允许 `copy_file` 操作在目标文件已存在时不覆盖它而直接成功。

  - **新增**：添加 `copy_options::update_existing` 选项，允许 `copy_file` 操作在目标文件已存在时，仅当其最后写入时间早于替换文件时才条件性地覆盖目标文件。

  - **新增**：`copy_file` 现在返回 `bool`，指示文件是否被复制。

  - **新增，破坏性变更**：`copy` 操作已被扩展与重构，以实现 C++20 \[fs.op.copy\] 规定的行为。这包括对 `copy_options::recursive`、`copy_options::copy_symlinks`、`copy_options::skip_symlinks`、`copy_options::directories_only`、`copy_options::create_symlinks` 与 `copy_options::create_hard_links` 选项的支持。该操作会依据指定选项执行额外检查。以默认 `copy_options` 对目录应用 `copy` 现在还会复制该目录中的文件（但不包括嵌套目录及其中文件）。

  - **新增**：添加接受两个路径的 `create_directory` 重载。第二个路径指向一个已存在目录，用作待创建目录权限属性的来源。

  - **弃用**：`copy_directory` 操作已弃用，推荐使用新的 `create_directory` 重载。注意这两个操作的路径参数顺序相反。

  - 在 POSIX 系统上，若其中一个路径未能解析到文件，`equivalent` 现在返回来自操作系统的实际错误码。此前该函数会返回错误码 1（[\#141](https://github.com/boostorg/filesystem/issues/141)）。

  - `equivalent` 不再使用文件大小与最后修改时间来判定两个路径是否指向同一文件。若文件在 `equivalent` 调用期间被修改，这些检查可能导致假阴性。

  - **新增**：添加接受 `error_code` 参数的 `absolute` 重载。

  - 以 `current_path()` 作为参数默认值且同时具有 `error_code` 参数的操作，将使用 `current_path(error_code& ec)` 重载获取当前路径，从而使其失败经由 `error_code` 参数报告而非抛出异常。

  - 出错时 `space` 现在将 `space_info` 结构成员初始化为 -1，符合 C++20（\[fs.op.space\]/1）的要求。

  - Windows 上的 `space` 现在接受指向任意文件的路径，而不仅限于目录。这与 POSIX 系统一致，也符合 C++20 中对该操作的描述（[\#73](https://github.com/boostorg/filesystem/issues/73)）。

  - **新增**：为 Windows CE 添加 `temp_directory_path` 实现（[PR#25](https://github.com/boostorg/filesystem/pull/25)）。

  - **新增**：改进与 [WASI](https://wasi.dev/)（WebAssembly 系统接口）平台的兼容性（[PR#144](https://github.com/boostorg/filesystem/pull/144)）。

  - **新增**：改进对 Embarcadero 编译器的支持（[PR#130](https://github.com/boostorg/filesystem/pull/130)）。

  - **新增**：添加基于 `getrandom`（Linux）、`arc4random_buf`（OpenBSD/FreeBSD/CloudABI）与 BCrypt（Windows）系统 API 的 `unique_path` 操作实现。

  - **弃用**：在 Windows 上使用 MSVC 兼容编译器对系统库进行自动链接（auto-linking）已弃用，将在未来发布中移除。这影响链接 Boost.Filesystem 静态库的用户。建议用户更新其项目构建系统：要么使用 Boost.Filesystem 的动态库，要么在链接器命令行中显式指定 Boost.Filesystem 的依赖。使用 Boost.Filesystem 动态库的用户不受影响。

- [Flyweight](/libs/flyweight/index.html)（享元模式容器库）：

  - 维护性工作。

- [Format](/libs/format/)（类型安全 printf 风格格式化库）：

  - 修正分配器用法（修复 C++20 编译）。（Glen Fernandes）

- [Geometry](/libs/geometry/)（几何算法库）：

  - 功能增强：

    - [PR#720](https://github.com/boostorg/geometry/pull/720) 新增 R-tree 构造函数（感谢 Caian Benedicto）。

    - 缓冲区（buffer）、集合运算与关系运算方面的多种改进。

  - 已解决问题：

    - [\#709](https://github.com/boostorg/geometry/issues/709) 对无平凡拷贝赋值的对象调用了 memcpy。

    - [\#721](https://github.com/boostorg/geometry/issues/721) bgi::detail::rtree::visitors::insert 中的编译错误。

    - [\#727](https://github.com/boostorg/geometry/issues/727) MSVC 警告：条件表达式恒为常量。

  - 缺陷修复：

    - [PR#700](https://github.com/boostorg/geometry/pull/700) distance 算法缺失默认策略的情形。

    - [PR#738](https://github.com/boostorg/geometry/pull/738) 正测地线公式（direct geodesic formulas）中经度超出范围。

- [GIL](/libs/gil/)（通用图像库）：

  - 新增：

    - 新增从任意图像的右值引用初始化 `any_image` 的构造函数（[PR#486](https://github.com/boostorg/gil/pull/486)）。

    - 实现了反转 `kernel_2d` 的机制（[PR#489](https://github.com/boostorg/gil/pull/489)）。

  - 变更：

    - **破坏性变更**：以 Boost.Variant2 取代 Boost.Variant（[PR#474](https://github.com/boostorg/gil/pull/474)），完成了对 Boost.MPL 使用的移除（Boost 1.72.0 变更中添加的 [PR#274](https://github.com/boostorg/gil/pull/274) 所缺失的部分）。

    - apply_operation 到 visit 改用完美转发（[PR#491](https://github.com/boostorg/gil/pull/491)）。

  - 移除：

    - **破坏性变更**：移除了对 Boost.Variant 的依赖。

  - 修复：

    - 修复因溢出导致的 RGB8 到 CMYK32 的无效转换（[PR#470](https://github.com/boostorg/gil/pull/470)）。

    - 修复从其他图像构造 `image` 的问题（[PR#477](https://github.com/boostorg/gil/pull/477)）。

    - 修复 "plane_view_t is not a class or namespace name" 错误（[PR#481](https://github.com/boostorg/gil/pull/481)）。

    - 修复 `interleaved_view` 工厂使用 `point<std::ptrdiff_t>` 表示维度的问题（[PR#487](https://github.com/boostorg/gil/pull/487)）。

    - 修复文档，将教程中以 MPL 的用法替换为 MP11（[PR#494](https://github.com/boostorg/gil/pull/494)）。

    - 修复 `numeric/kernel.hpp` 中缺失的头文件，使其自包含（[PR#502](https://github.com/boostorg/gil/pull/502)）。

  - 致谢：

    - Samuel Debionne、Pranam Lashkari、Mateusz Loskot、Debabrata Mandal

- [Heap](/libs/heap/)（优先队列家族库）：

  - 修正 `skew_heap` 中顶部节点的析构。（Glen Fernandes）

  - 修正并简化分配器的使用。（Glen Fernandes）

- [Integer](/libs/integer/)（整数类型选择库）：

  - 修复 C++20 模式下 clang 10 中 `gcd` 的编译。

  - 改进对 Embarcadero 编译器的支持（[PR#21](https://github.com/boostorg/integer/pull/21)）。

- [Iterator](/libs/iterator/)（迭代器构建设施库）：

  - `boost/function_output_iterator.hpp` 头文件现已弃用。用户应将其包含替换为 `boost/iterator/function_output_iterator.hpp`（[PR#51](https://github.com/boostorg/iterator/pull/51)）。

  - 改进对 Embarcadero 编译器的支持（[PR#55](https://github.com/boostorg/iterator/pull/55)）。

- [LexicalCast](/libs/lexical_cast/)（字符串↔数值等类型转换库）：

  - 修复缺失 `override` 的警告（感谢 EugeneZelenko，[\#35](https://github.com/boostorg/lexical_cast/issues/35)、[\#34](https://github.com/boostorg/lexical_cast/issues/34)）。

  - 修复 Embarcadero 编译器的问题（感谢 Edward Diener）。

- [Log](/libs/log/)（日志库）：

  - 缺陷修复：

    - syslog sink 后端现在会校验用户设置的本地地址与目标地址的 IP 版本。两个地址必须与 sink 后端构造时通过 `ip_version` 命名参数指定的 IP 版本相同（默认假定为 IPv4）。当地址是通过主机名解析获得时，仅考虑 IP 版本匹配的地址（[\#119](https://github.com/boostorg/log/issues/119)）。

  - 新特性：

    - 多个组件的移动构造函数与移动赋值运算符被标记为 `noexcept`。

    - 新增 `range_manip` 流操纵器（stream manipulator），可用于输出范围（range）的元素，可选以分隔符分隔。

    - 新增 `tuple_manip` 流操纵器，可用于输出元组（tuple）或任何其他异构序列的元素，可选以分隔符分隔。

    - 新增 `optional_manip` 流操纵器，可用于输出可能不存在的值。

  - 更多细节参见[变更日志](/libs/log/doc/html/log/changelog.html)。

- [Mp11](/libs/mp11/)（C++11 元编程库）：

  - 改进了大 `N` 时 `mp_with_index<N>` 的编译性能。

  - 新增 `tuple_transform`（由 Hans Dembinski 贡献）。

- [Multi-index Containers](/libs/multi_index/)（多索引容器库）：

  - 仿照 C++17 关联容器引入的类似接口，新增[节点提取与插入](/libs/multi_index/doc/tutorial/basics.html#node_handling)功能。与不提供此类功能的标准库序列容器不同，该特性还扩展到了非基于键的索引。

  - 澄清了关于读/写键提取器（key extractors）的文档（issue [\#32](https://github.com/boostorg/multi_index/issues/32)）。

  - 维护性工作。

- [Nowide](/libs/nowide/)（Windows 下 UTF-8 标准 I/O 适配库）：

  - 本库现在要求符合 C++11 的编译器与标准库

  - LFS：在底层系统支持的情况下，添加对大于 2 GB 文件的支持

  - 通用 UTF 转换函数现在可在 `boost::nowide::utf` 命名空间中使用

  - 添加对以 UTF-8 路径使用 `stat` 的支持

- [Outcome](/libs/outcome/)（轻量级错误处理（result/outcome）库）：

  - 公告：

    - v2.1 分支预计于 2020 年底退役，由 v2.2 分支成为默认。您现在就可以使用未来的 v2.2 分支：[`better_optimisation`](https://github.com/ned14/outcome/tree/better_optimisation)。相对于 Outcome v2.1，该分支包含多项重大破坏性变更，详情参见首页。

  - 功能增强：

    - **破坏性变更**：`void` 结果与 outcome 在显式构造期间不再默认构造类型。此前，若从非出错的 `result<void>` 显式构造 `result<T>`，会默认构造 `T`。这种做法被发现会带来无益的意外，因此已被禁用。

    - 新宏 `OUTCOME_ENABLE_LEGACY_SUPPORT_FOR`。宏 `OUTCOME_ENABLE_LEGACY_SUPPORT_FOR` 可用于在使用较新版本的 Outcome 时，将较旧的命名与特性别名为较新的命名与特性。

    - 概念（concepts）现在改用蛇形命名（snake case）而非驼峰命名。Outcome 最初实现时，曾认为 C++20 概念会采用驼峰命名。这在 C++20 发布前被更改，Outcome 的概念也相应改名。这不会破坏 Outcome v2.1 中的任何代码，因为提供了兼容性别名。但针对 Outcome v2.2 编译的代码需要升级，除非将 `OUTCOME_ENABLE_LEGACY_SUPPORT_FOR` 设为 `210` 或更低。

    - 概念现在位于 `OUTCOME_V2_NAMESPACE::concepts` 命名空间。此前概念位于 `convert` 命名空间，现在位于其专属命名空间。

    - 新增概念 `basic_result<T>` 与 `basic_outcome<T>`。最终用户此前发现，在 `is_basic_result<T>` 与 `value_or_error<T>` 之间存在一个无益的空档：他们想要一个匹配"属于 `basic_result` 一类但又不完全是指定类型"的概念。现已添加填补该空档的概念。

    - 自 Outcome v2.2 起，`TRY` 操作的工作方式有所不同。这是一项严重的破坏性变更，改变了 `OUTCOME_TRY()` 的使用语法。可在 Outcome v2.1 与 v2.2 的变更列表中找到适用于升级代码的正则表达式。

  - 缺陷修复：

    - [\#224](https://github.com/ned14/outcome/issues/224) Apple 随 Xcode 11.4（当前最新）发布的 clang 尚未打上我多年前提交的、修复 `noexcept(std::is_constructible<T, void>)` 编译失败的 LLVM clang 修复补丁。因此不再等待 Apple 修复其 clang，在 Outcome 中加入变通处理。

    - 备用存储（spare storage）无法在无值策略类（no-value policy classes）内部使用。由于当时编写代码时的一次明显失误，备用存储 API 的原型有误，导致它们无法在策略类内部工作。抱歉。

- [PolyCollection](/libs/poly_collection/)（多态集合库）：

  - 修复 `boost::type_erasure::any` 与 `boost::any` 之间的内部歧义问题（issue [\#17](https://github.com/boostorg/poly_collection/issues/17)）。

  - 维护性工作。

- [SmartPtr](/libs/smart_ptr/)（智能指针库）：

  - 为 `shared_ptr`、`weak_ptr`、`local_shared_ptr` 新增 `owner_equals`。

  - 为 `shared_ptr`、`weak_ptr` 新增 `owner_hash_value`。

  - 新增 `owner_equal_to`、`owner_hash`。

  - 为 `shared_ptr`、`local_shared_ptr` 新增 `std::hash` 特化。

  - 为 `weak_ptr` 新增 `boost::hash` 支持以及 `std::hash`、`std::equal_to` 特化。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 修复以 `-fno-exceptions` 编译时的构建错误（感谢 Jeremiah Rodriguez，[\#91](https://github.com/boostorg/stacktrace/issues/91)）。

- [System](/libs/system/)（错误码与 system_error 库）：

  - `operator bool()` 现在返回 `failed()` 而非 `value() != 0`。

- [Type_Traits](/libs/type_traits/)（类型特征库）：

  - 实现 `conjunction`、`disjunction`、`negation`、`is_trivially_copyable`、`is_scoped_enum` 与 `is_unscoped_enum`。（Glen Fernandes）

- [Variant](/libs/variant/)（非递归可辨识联合库）：

  - 修复缺失 `override` 的警告（感谢 EugeneZelenko，[\#78](https://github.com/boostorg/variant/issues/78)）。

  - 修复 Embarcadero 编译器的问题（感谢 Edward Diener，[\#79](https://github.com/boostorg/variant/issues/79)）。

  - 更新头文件位置，以避免关于使用已弃用头文件的警告（感谢 Andrey Semashev，[\#80](https://github.com/boostorg/variant/issues/80)）。

- [Variant2](/libs/variant2/)（Variant 的现代重实现库）：

  - 在 `visit` 中新增对派生类型的支持。

  - 改进了多个（数百个）备选类型下的编译性能。

  - 新增对 `visit<R>` 的支持。

- [Wave](/libs/wave/)（C/C++ 预处理器实现库）：

  - 实现可变参数宏（variadics）的 C++20 特性，包括 `__VA_OPT__`（[PR#75](https://github.com/boostorg/wave/pull/75)）

  - 实现 `__has_include`（[PR#102](https://github.com/boostorg/wave/pull/102)）

  - 引入新示例 `check_macro_naming`，对 Boost 自身也有用（[PR#97](https://github.com/boostorg/wave/pull/97)）

  - 修复 C++20 中移除 `std::allocator` 成员导致的编译问题（[PR#72](https://github.com/boostorg/wave/pull/72)）

  - 修复 Xpressive 词法分析器与 `token_statistics` 示例（[PR#79](https://github.com/boostorg/wave/pull/79)）

  - 修复 lexertl 词法分析器（[PR#78](https://github.com/boostorg/wave/pull/78)）

  - 确保钩子（hooks）对预定义宏也会运行（[PR#87](https://github.com/boostorg/wave/pull/87)）

  - 各类次要缺陷修复

  - 对 C++98/03 的支持现已弃用，将在 1.77 中移除

- [YAP](/libs/yap/)（表达式模板库）：

  - 修复占位符（placeholders）的编译错误；它们现在可在一般情形下工作，特别是可与 yap::print() 配合工作。

  - 全面 constexpr 化 YAP。

  - 修复 yap::print() 中值类别（value category）的正确打印。

  - 文档澄清。

## 更新的工具（Updated Tools）

- [Boostbook](/tools/boostbook/)（BoostBook 文档格式工具）：

  - 将生成文档的编码从 US-ASCII 更改为 UTF-8。（Glen Fernandes）

## 已测试的编译器（Compilers Tested）

Boost 的主要测试编译器如下：

- Linux：

  - Clang：3.0, 4.0.1, 6.0.1

  - Clang，C++0x：3.0

  - Clang，C++11：3.0, 3.1, 3.2, 3.3, 3.4, 4.0.1, 6.0.1, 7.0.0, 8.0.0

  - Clang，C++14：3.5.0, 3.6.0, 3.7.1, 3.8.0, 3.9.1, 4.0.0, 4.0.1, 5.0.2, 6.0.1, 7.0.0, 8.0.0

  - Clang，C++17：5.0.2, 6.0.1, 7.0.0, 8.0.0

  - GCC：4.4.7, 4.5.3, 4.6.3, 5.4.0, 8.0.1

  - GCC，C++0x：4.4.7

  - GCC，C++11：4.7.3, 4.8.5, 4.9.4, 5.4.0, 6.4.0, 7.1.0, 8.0.1

  - GCC，C++14：5.4.0, 5.5.0, 6.4.0, 7.1.0, 7.3.0, 8.0.1

  - GCC，C++17：7.3.0, 8.0.1

  - Intel，C++14：18.0

- OS X：

  - Apple Clang：9.0.0, 9.1.0, 10.0.0

  - Apple Clang，C++11：9.0.0, 9.1.0, 10.0.0

  - Apple Clang，C++14：9.0.0, 9.1.0, 10.0.0

  - Apple Clang，C++17：9.1.0, 10.0.0

  - Apple Clang，C++1z：9.0.0

  - Apple Clang，C++2a：10.0.0

- Windows：

  - GCC：3.4.5, 4.1.2, 4.2.4, 4.3.3, 4.4.0, 4.5.4

  - GCC，C++0x：4.6.4

  - GCC，C++11：4.7.3, 4.8.1, 4.9.3

  - GCC，C++14：5.1.0, 5.2.0, 5.3.0, 6.1.0, 6.2.0, 6.3.0, 6.4.0

  - GCC，C++17：7.1.0, 7.2.0, 7.3.0

  - Visual C++：7.1, 8.0, 9.0, 10.0, 11.0, 12.0, 14.0, 14.1

- FreeBSD：

  - Clang：4.0.0

  - Clang，C++11：4.0.0

  - Clang，C++14：4.0.0

  - Clang，C++1z：4.0.0

Boost 的其他测试编译器包括：

- Linux：

  - Clang：3.0, 3.8.1, 3.9.1, 4.0.1, 5.0.2, 6.0.1

  - Clang，C++0x：3.0

  - Clang，C++11：3.0, 3.1, 3.2, 3.3, 3.4, 4.0.1, 6.0.1, 7.0.0, 8.0.0

  - Clang，C++14：3.5.0, 3.6.0, 3.7.1, 3.8.0, 3.9.1, 4.0.0, 4.0.1, 5.0.2, 6.0.1, 7.0.0, 8.0.0

  - Clang，C++17：5.0.2, 6.0.1, 7.0.0, 8.0.0

  - GCC：4.4.7, 4.5.3, 4.6.3, 4.9.4, 5.4.0, 5.5.0, 8.0.1

  - GCC，C++0x：4.4.7

  - GCC，C++11：4.7.3, 4.8.5, 4.9.4, 5.4.0, 6.4.0, 7.1.0, 8.0.1

  - GCC，C++14：5.4.0, 5.5.0, 6.3.0, 6.4.0, 7.1.0, 7.3.0, 8.0.1, 8.1.0

  - GCC，C++17：7.3.0, 8.0.1

  - Intel，C++14：18.0

- OS X：

  - Apple Clang：9.0.0, 9.1.0, 10.0.0

  - Apple Clang，C++11：9.0.0, 9.1.0, 10.0.0

  - Apple Clang，C++14：9.0.0, 9.1.0, 10.0.0

  - Apple Clang，C++17：9.1.0, 10.0.0

  - Apple Clang，C++1z：9.0.0

  - Apple Clang，C++2a：10.0.0

- Windows：

  - GCC：3.4.5, 4.1.2, 4.2.4, 4.3.3, 4.4.0, 4.5.4

  - GCC，C++0x：4.6.4

  - GCC，C++11：4.7.3, 4.8.1, 4.9.3

  - GCC，C++14：5.1.0, 5.2.0, 5.3.0, 6.1.0, 6.2.0, 6.3.0, 6.4.0

  - GCC，C++17：7.1.0, 7.2.0, 7.3.0

  - Visual C++：7.1, 8.0, 9.0, 10.0, 11.0, 12.0, 14.0, 14.1

- FreeBSD：

  - Clang：4.0.0

  - Clang，C++11：4.0.0

  - Clang，C++14：4.0.0

  - Clang，C++1z：4.0.0

## 致谢（Acknowledgements）

本次发布由 Marshall Clow、Michael Caisse 与 Glen Fernandes 管理。
