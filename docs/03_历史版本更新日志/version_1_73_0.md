# Boost 1.73.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_73_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_73_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2020-04-28 03:57 GMT（原文日期行：April 28th, 2020 03:57 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.73.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 已知问题（Known Issues）

以下补丁由库作者提供，但因发现太晚而未能在此发布中修复。请谨慎使用，因为它们未经正常的测试流程。

- Outcome `status_code_domain` 断言移除

  - [Outcome 补丁](/patches/1_73_0/0001-outcome-assert.patch)

- Beast 与协程

  - [Beast 补丁](/patches/1_73_0/0002-beast-coroutines.patch)

## 新增库（New Libraries）

- [Nowide](/libs/nowide/)（Windows 下 UTF-8 标准 I/O 适配库）：Windows 上提供 UTF-8 API 的标准库函数，由 Artyom Beilis 开发。

- [StaticString](/libs/static_string/)（编译期固定容量、内嵌连续存储的动态可调字符串库）：容量在编译期固定、内嵌连续存储、可动态调整大小的字符字符串，由 Vinnie Falco 与 Krystian Stasiowski 开发。

## 更新的库（Updated Libraries）

- [Align](/libs/align/)（对齐工具库）：

  - 更新 `aligned_alloc` 以支持较旧的 mingw32。

- [Any](/libs/any/)（类型安全的任意类型容器库）：

  - 通过不包含 `<algorithm>` 加快编译。

  - 维护性工作，包括 CI 加固。

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 修复与 C++20 概念（concept）语法的兼容性。

  - 将 POSIX 描述符类的移动构造函数标记为 `noexcept`。

  - 新增 `ssl::host_name_verification` 类，它是 `ssl::rfc2818_verification` 的直接替代品。`ssl::rfc2818_verification` 类已被标记为弃用。由于此变更，SSL 支持现在依赖于 OpenSSL 1.0.2 中引入的函数。

  - 新增 `ssl::context` 构造函数，可接管原生句柄的所有权。

  - 将 `gcc` 的 C++ 语言版本检测改为使用 `__cplusplus` 宏。

  - 修复端点异步解析操作中的工作计数问题。

  - 修复 `strand<>` 的转换构造函数与赋值运算符。

  - 确保解析器（resolver）在 fork 之后正确重启。

  - 修复与当前 NetBSD 发行版的兼容性。

  - 移除部分 `async_read` 重载中多余的处理程序要求检查。

  - 将 `ssl::context` 类改为传播 `add_certificate_authority` 函数产生的非 EOF 错误。

  - 修复 Windows 特有的 `thread_pool` 析构挂起问题（当线程池关联有 I/O 对象时发生）。

  - 将 `select` 反应器（reactor）改为在出错时重建"自管道技巧"（self pipe trick）套接字。这解决了某些 Windows 版本上系统休眠后这些套接字断开的问题。

  - 修复因 C++98 缺乏引用折叠而导致的缓冲流编译错误。

  - 将 `priority_scheduler` 示例改为演示 `shutdown()` 与 `destroy()` 的调用。

  - 移除一些不必要的空指针检查。

  - 将 Windows 平台检测改为把 TV 类应用（TV titles）识别为 Windows 应用。

  - 添加了一些 emscripten 兼容性补丁。

  - 修复 `use_awaitable_t::as_default_on` 函数中的编译错误。

  - 将所有 boost.bind 占位符的使用改为使用 `boost::placeholders` 命名空间。

  - 修复 `async_compose` 实现中因重载选择不当导致的潜在编译错误。

  - 抑制一些非虚析构函数警告。

  - 各类文档修复与改进。

- [Assert](/libs/assert/)（可定制断言宏库）：

  - 新增 `source_location`。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 实现 C++20 的 `atomic_ref`。参见[文档](/doc/html/atomic/interface.html#atomic.interface.interface_atomic_ref)，特别是[注意事项](/doc/html/atomic/interface.html#atomic.interface.interface_atomic_ref.caveats)章节。

  - 实现 C++20 引入的 `atomic_flag::test` 操作。

  - `atomic<T>` 现在会考虑 `T` 的对齐要求；当这些要求高于 `atomic` 内部存储的对齐要求时会产生影响。

  - 新增静态断言，强制约束与 `atomic` 和 `atomic_ref` 一起使用的值类型 `T` 的要求。这应能禁止无效类型被用作原子类型。

  - 改进了内部锁池实现。锁池更大，且锁的选择会考虑原子对象的对齐，这应能减少线程竞争的可能性。

  - 修复 x86 上对 8 位与 16 位参数执行 `bit_test_and_*` 操作时生成的错误代码。其他架构不受影响。

  - 修复当 `value_type` 的对齐要求低于 `atomic` 内部存储的对齐要求时，`compare_exchange_*` 操作中可能出现的非对齐内存访问。

  - `boost/atomic/atomic.hpp` 不再包含 `boost/atomic/atomic_flag.hpp` 与 `boost/atomic/fences.hpp`，仅定义 `boost::atomic` 类模板及相关 typedef。请显式包含其他头文件，或使用 `boost/atomic.hpp` 以包含 Boost.Atomic 的全部内容。

  - `atomic<T>::storage()` 访问器及相关的 `atomic<T>::storage_type` 类型已弃用。建议用户分别改用 `atomic<T>::value()` 与 `atomic<T>::value_type`。过渡期间，用户可定义 `BOOST_ATOMIC_SILENCE_STORAGE_DEPRECATION` 来禁用弃用警告。被弃用的部分将在未来发布中移除。

  - 移除对 `BOOST_ATOMIC_DETAIL_HIGHLIGHT_OP_AND_TEST` 的支持。该宏曾作为迁移助手，用于向 Boost.Atomic 1.67 中更新的 `*_and_test` 操作返回值过渡，而 1.67 比 1.73 早两年发布。

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 这是一次维护性更新。

  - Beast 动态缓冲区中嵌套的 `mutable_data_type` 已弃用。

  - 我们很想知道您或您的公司如何使用 Beast，欢迎在[使用 Beast 的公司与个人](https://github.com/boostorg/beast/wiki/Companies-and-Individuals-Using-Beast)（Companies and Individuals Using Beast）列表中添加条目。

  - 完整变更列表请参见完整的[发布说明](/libs/beast/doc/html/beast/release_notes.html)。

- [Context](/libs/context/)（执行上下文库）：

  - [\#133](https://github.com/boostorg/context/issues/133)：IBM Z：修复 fcontext 例程

  - [\#132](https://github.com/boostorg/context/issues/132)：mips64/n64：.align 3

  - [\#131](https://github.com/boostorg/context/issues/131)：使用 OSPLAT MIPS32/MIPS64 设置不同的 ABI（应用二进制接口）

  - [\#129](https://github.com/boostorg/context/issues/129)：修复 RISC-V 汇编中的非 PIC 问题

- [Conversion](/libs/conversion/)（类型转换库）：

  - 新增面向引用的 `boost::polymorphic_downcast`（感谢 Julien Delacroix 提供补丁）。

  - 大幅更新文档。

- [date_time](/libs/date_time/)（日期时间库）：

  - [\#123](https://github.com/boostorg/date_time/issues/123)：支持 C++14 及以上标准中的 constexpr

  - [\#134](https://github.com/boostorg/date_time/issues/134)：将 date_time 全部改为内联。用户不再需要为任何函数链接该库。库本身为保持构建兼容性而保留。

  - [\#132](https://github.com/boostorg/date_time/issues/132)：弃用对旧式 I/O 及 `USE_DATE_TIME_PRE_1_33_FACET_IO` 宏的支持

  - 各类文档更新与缺陷修复。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 修复 `boost::dll::smart_library` 中名称还原（demangling）的问题并添加测试（感谢 Ramil Gauss，[\#35](https://github.com/boostorg/dll/issues/35)）。

  - 使 UB 消毒器（sanitizer）对 `boost::dll::load_mode::type` 不再报错 [\#30](https://github.com/boostorg/dll/issues/30)。

  - 停止依赖 MPL，改进编译时间（感谢 Nikita Kniazev，[\#34](https://github.com/boostorg/dll/issues/34)）。

  - 修复 Windows 上 Clang 与 ICC 的问题，并为这些平台提供 CI 支持（感谢 Nikita Kniazev，[\#33](https://github.com/boostorg/dll/issues/33)）。

  - 维护性工作，包括 CI 加固与测试改进。

- [Dynamic Bitset](/libs/dynamic_bitset/)（动态位集库）：

  - 修复最大块限制定义中的可移植性问题。

- [Flyweight](/libs/flyweight/index.html)（享元模式容器库）：

  - 维护性工作。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 功能增强：

    - [PR#650](https://github.com/boostorg/geometry/pull/650) 补充 `intersection()` 缺失的输入组合，并引入元组化输出（tupled-output）。

    - [PR#671](https://github.com/boostorg/geometry/pull/671) 新增 `d3::point_xyz` 几何模型（感谢 Digvijay Janartha）。

  - 已解决问题：

    - [\#657](https://github.com/boostorg/geometry/issues/657) `EPSG:3785` 的错误定义。

  - 缺陷修复：

    - [PR#639](https://github.com/boostorg/geometry/pull/639) R-tree 异常安全性改进。

    - [PR#668](https://github.com/boostorg/geometry/pull/668) 修复近距离点的 Andoyer 反算公式。

    - [PR#687](https://github.com/boostorg/geometry/pull/687) 修复 distance 算法中的悬空引用。

  - 弃用：

    - [\#590](https://github.com/boostorg/geometry/issues/590) 对 C++03 的支持已弃用，自 Boost 1.75 起 Geometry 将要求 C++14。

- [GIL](/libs/gil/)（通用图像库）：

  - 新增：

    - 为 `image` 类新增移动构造函数与移动赋值运算符（[PR#457](https://github.com/boostorg/gil/pull/457)）。

    - `any_image_view` 类新增成员函数 `size()`（[PR#456](https://github.com/boostorg/gil/pull/456)）。

  - 变更：

    - 以 Boost.LightweightTest 取代 Boost.Test，作为 GIL 使用的唯一测试框架（[PR#459](https://github.com/boostorg/gil/pull/459) 与 [PR#464](https://github.com/boostorg/gil/pull/464)）。这也重组了 `test/extension/io/` 子树及相关 `Jamfile` 中的目标。

    - 移除了剩余的 Boost.MPL 使用（[PR#459](https://github.com/boostorg/gil/pull/459)）。

    - 将所有宏改用 `BOOST_GIL_` 前缀重命名（[PR#411](https://github.com/boostorg/gil/pull/411)）。

    - 将所有 CMake 配置选项改用 `BOOST_GIL_` 前缀重命名（[PR#419](https://github.com/boostorg/gil/pull/419)）。

  - 变更：

    - 移除未被使用且可能未完成的 `extension/dynamic_image/reduce.hpp`（[PR#466](https://github.com/boostorg/gil/pull/466)）。它是 Lubomir Bourdev 与 Jaakko Jarvi 在论文 [Efficient Run-Time Dispatching in Generic Programming with Minimal Code Bloat](http://lubomir.org/academic/MinimizingCodeBloat.pdf) 中所述技术的一次实现尝试。

    - 移除对 Boost.MPL、Boost.System 与 Boost.Test 的直接依赖。

    - 开始移除用于 I/O 扩展测试编译期配置的公开宏，如 `BOOST_GIL_IO_TEST_ALLOW_READING_IMAGES` 与 `BOOST_GIL_IO_TEST_ALLOW_WRITING_IMAGES`。取而代之，若某测试目标被构建，它将无条件构建其全部测试用例。

  - 修复：

    - 避免 I/O 扩展对象析构期间的 `longjmp` 交互（[PR#433](https://github.com/boostorg/gil/pull/433)）。

    - 修复 `image` 类构造函数中缺失的对齐默认值（[PR#429](https://github.com/boostorg/gil/pull/429)）。

    - 修复读取损坏 PNG 文件时的段错误（[PR#414](https://github.com/boostorg/gil/pull/414)）。

    - 修复 I/O 扩展旧版 IOv1 接口中返回值的非法初始化（[PR#409](https://github.com/boostorg/gil/pull/409)）。

  - 致谢：

    - Samuel Debionne、Thiago Henrique Hüpner、Pranam Lashkari、Mateusz Loskot、Debabrata Mandal、Olzhas Zhumabek

- [Histogram](/libs/histogram/)（多维直方图库）：

  - 新特性：

    - 为 `reduce` 算法新增 `crop` 命令

    - `reduce` 中的 `slice` 命令现在可用于 `category` 轴

    - 新增 `count` 累加器（accumulator），可用于为每个单元（cell）添加任意元数据

    - `sum` 算法新增一个参数，可选择仅对内部 bin 求和

  - 若干边界情形缺陷修复

  - 增强文档：

    - 如何在外部 API 中将 Boost.Histogram 用作后端

    - 更多关于如何将 Boost.Histogram 与自定义累加器及 Boost.Accumulators 一起使用的内容

    - 更多关于如何使用 `reduce` 的内容

    - 更新的基准测试

  - [完整变更日志见此](/libs/histogram/doc/html/histogram/history.html)

- [icl](/libs/icl/)（区间容器库（Interval Container Library））：

  - [PR#23](https://github.com/boostorg/icl/pull/23)：移除对 date_time 需编译库的引用。

  - [PR#17](https://github.com/boostorg/icl/pull/17)：修复 `lower` 与 `upper` 小于等于判断的前向声明。

  - 各类缺陷修复。

- [IO](/libs/io/)（I/O 工具库（流状态保存器等））：

  - 将所有 IOS 状态保存器类改为不可复制。（Glen Fernandes）

  - 读取带引号字符串时，正确处理首次从输入流读取时发生的错误。（Glen Fernandes）

  - 实现基于分隔符连接的 `ostream_joiner`。（Glen Fernandes）

  - 将 `ostream_string` 从 Utility 库迁移至 IO 库，作为 `ostream_put`。

  - 在带引号输出中正确处理流的宽度（width）与填充（fill）。（Glen Fernandes）

  - 优化带引号输出，使其直接写入流缓冲区。（Glen Fernandes）

  - Glen Fernandes 成为 IO 库的维护者。

- [LexicalCast](/libs/lexical_cast/)（字符串↔数值等类型转换库）：

  - 维护性工作，包括 CI 加固与针对有缺陷标准库的更好变通方案（感谢 Nikita Kniazev，[\#31](https://github.com/boostorg/lexical_cast/issues/31)、[\#32](https://github.com/boostorg/lexical_cast/issues/32)）。

- [Log](/libs/log/)（日志库）：

  - 新特性：

    - 当日志核心中未注册任何 sink 时，简单日志（trivial logging）所用的默认 sink 现在会在每条日志记录后自动刷新输出（[\#103](https://github.com/boostorg/log/issues/103)）。

    - 当未注册任何 sink 时，`core::flush` 现在会对简单日志所用的默认 sink 执行刷新。

  - 缺陷修复：

    - 为某些 syslog API 实现（如 glibc）添加变通方案：这些实现不会在 `openlog` 调用中保存应用标识字符串，从而可能在每次 `syslog` 调用时访问已释放的内存，导致未定义行为（[\#97](https://github.com/boostorg/log/issues/97)）。

    - 修复指定月内日期（如 `rotation_at_time_point(boost::gregorian::greg_day(1))`）的日志文件轮转可能被静默忽略而不执行的问题（[\#98](https://github.com/boostorg/log/issues/98)）。

    - 修复在尚未写入任何日志记录且已设置目标文件名模式时，`text_file_backend::rotate_file` 可能抛出异常的问题。

    - 将库的多个组件移植到 `std::allocator_traits`，以改进与 C++20 分配器的兼容性。

    - 修复在 MSYS2 Cygwin 环境中构建时的编译错误（[\#102](https://github.com/boostorg/log/issues/102)）。

  - 更多细节参见[变更日志](/libs/log/doc/html/log/changelog.html)。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - 重要：对 C++03 的支持现已弃用，将于 2021 年 3 月起移除。

  - 新增三次 Hermite 插值（Cubic Hermite Interpolation）。

  - 新增改进 Akima 插值（Modified Akima Interpolation）。

  - 新增 PCHIP 插值（PCHIP Interpolation）。

  - 新增五次 Hermite 插值（Quintic Hermite Interpolation）。

  - 为众多分布新增熵（entropy）。

  - 允许两端点相等的平凡求积情形，此外允许积分限互换。

  - 修复 exp_sinh 求积，使其能在非原生区间上处理复数类型。

  - 修复 factorial.hpp 中的各类编译器警告。

  - 在限时 pFq 计算中使用 std::chrono 而非 boost::chrono。

  - 移除大部分旧的 boost::mpl 依赖，以改进 constexpr 支持。

- [Mp11](/libs/mp11/)（C++11 元编程库）：

  - 新增 `mp_unique_if`（由 Kris Jusiak 贡献）

  - 新增 `mp_flatten`

  - 新增 `mp_rotate_left`、`mp_rotate_right`（由 Duncan Barber 贡献）

  - 新增 `mp_compose`

  - 新增 `mp_power_set`

  - 新增 `mp_partial_sum`

  - 新增 `mp_iterate`

- [Multi-index Containers](/libs/multi_index/)（多索引容器库）：

  - `multi_index_container` 现已满足 [AllocatorAware（分配器感知容器）](https://en.cppreference.com/w/cpp/named_req/AllocatorAwareContainer)要求。

  - 内部 `KeyFromValue`、`Compare`、`Hash` 与 `Pred` 对象的交换现在会依据 **\[swappable.requirements\]** 中的标准规范，在 `std::swap` 与 ADL 候选之间选择适当的 `swap` 函数（issue [\#29](https://github.com/boostorg/multi_index/issues/29)）。

  - 提供了部分内部拷贝构造函数与赋值运算符，其默认隐式定义自 C++11 起已被弃用（**\[depr.impldec\]**），某些编译器会对此发出警告。

  - 维护性工作。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - 重要：将 C++03 支持标记为弃用，计划于 2021 年移除。

  - 对 cpp_int 的大幅更新，加入更快的 Karatsuba 与 Coomba 乘法例程。

  - 修复 gmp_rational 向 `long double` 与 `__float128` 的转换，修复 \#178。

  - 修正 libtommath 支持，使其与最新 libtom 发行版配合工作。

  - 修正与最新 Intel C++ 编译器的一些不兼容之处。

  - 修正最新 MSVC 版本的 `constexpr` 算术支持。

- [Outcome](/libs/outcome/)（轻量级错误处理（result/outcome）库）：

  - 功能增强：

    - clang 编译的基于 Outcome 的代码性能已大幅提升。Outcome 状态位域（status bitfield）的先前实现会干扰 clang 的优化器，导致低质量代码生成。与大多数代码生成问题不同，这一问题在真实代码的实证基准中显而易见，如 [P1886 **Error speed benchmarking**](https://wg21.link/P1886)（错误处理速度基准测试）所示。

    - [`better_optimisation`](https://github.com/ned14/outcome/tree/better_optimisation)（Outcome v2.2.0 未来分支）的安全部分已被合并至 Outcome v2.1.3，其中包含新的状态位域实现。它似乎不再干扰 clang 的优化器，且 clang 9 生成的代码在各种预设用例中通常优于 GCC 9 的代码。

    - 可安装性现在按提交进行 CI 测试。由于独立 Outcome 的可安装性（例如 `make install`）损坏的频率比理想情况高得多，现在每次提交都会在 CI 上测试可安装性。

  - 缺陷修复：

    - [\#214](https://github.com/ned14/outcome/issues/214) 较新的支持概念（Concepts）实现的编译器对早期检查 `T` 与 `E` 的可析构性不满，因此移除了模板约束，改为回退到在类型实例化序列中较晚运行的静态断言。

    - [\#220](https://github.com/ned14/outcome/issues/220) 针对 Experimental Outcome 某些用例中未定义行为消毒器（sanitiser）的误报失败实施了变通处理，以避免出现失败消息。

- [PolyCollection](/libs/poly_collection/)（多态集合库）：

  - 抑制 `boost::poly_collection::for_each` 中潜在的冗余移动警告。

  - 修复一个缺陷：在具有不传播且不相等分配器的集合之间进行分配器扩展移动构造与移动赋值时，元素被复制而非移动。

  - 对于 GCC 4.8 附带的旧版 libstdc++-v3（Clang 也可使用），分配器扩展移动构造不再退化为分配器扩展拷贝构造。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 新增关于 PDB 分发的文档（[\#55](https://github.com/boostorg/stacktrace/issues/55)、[\#47](https://github.com/boostorg/stacktrace/issues/47)）（感谢 emptyVoid 与 Roger Orr 提供信息，感谢 zlojvavan 测试）。

  - 修复 msvc-9 构建

  - 维护性工作，包括测试修复（[\#86](https://github.com/boostorg/stacktrace/issues/86)）、拼写错误修复（[\#84](https://github.com/boostorg/stacktrace/issues/84)）、CI 改进与加固、inspect 工具修复。

- [Test](/libs/test/)（单元测试框架库）：

  - Boost.test v3.13，更多细节参见[变更日志](/libs/test/doc/html/boost_test/change_log.html)。

  - 新特性：现在可以在单个 `BOOST_TEST` 表达式中组合容差指示、用户消息与集合比较修饰符。更多细节参见变更日志。

  - 缺陷修复与拉取请求：

    - GitHub Issues：[\#173](https://github.com/boostorg/test/issues/173)、[\#179](https://github.com/boostorg/test/issues/179)、[\#220](https://github.com/boostorg/test/issues/220)、[\#221](https://github.com/boostorg/test/issues/221)、[\#235](https://github.com/boostorg/test/issues/235)、[\#237](https://github.com/boostorg/test/issues/237)、[\#241](https://github.com/boostorg/test/issues/241)、[\#245](https://github.com/boostorg/test/issues/245)、[\#246](https://github.com/boostorg/test/issues/246)、[\#251](https://github.com/boostorg/test/issues/251)、[\#253](https://github.com/boostorg/test/issues/253)、[\#254](https://github.com/boostorg/test/issues/254)、[\#263](https://github.com/boostorg/test/issues/263)

    - Trac 工单：[\#11107](https://svn.boost.org/trac/boost/ticket/11107)

    - GitHub Pull Requests：[PR#41](https://github.com/boostorg/test/pull/41)、[PR#114](https://github.com/boostorg/test/pull/114)、[PR#187](https://github.com/boostorg/test/pull/187)、[PR#239](https://github.com/boostorg/test/pull/239)、[PR#247](https://github.com/boostorg/test/pull/247)、[PR#252](https://github.com/boostorg/test/pull/252)、[PR#259](https://github.com/boostorg/test/pull/259)、[PR#265](https://github.com/boostorg/test/pull/265)

- [ThrowException](/libs/throw_exception/)（统一异常抛出设施库）：

  - 新增接受 `boost::source_location` 对象的 `throw_exception` 重载。

  - 注意：在禁用异常的情况下使用 `BOOST_THROW_EXCEPTION` 的项目需要为该新重载添加定义。

- [TTI](/libs/tti/)（类型内省库（Type Traits Introspection））：

  - 新增对函数模板的内省支持，适用于较新的 gcc 与 vc++ 编译器版本以及所有版本的 clang。14.0 之前的旧版 vc++ 与 4.8 之前的 gcc 可能失败。

  - 新增针对 struct/class、enum 与 union 类型成员的特定内省，可用于比通用"type"内省更细粒度的内省。

- [TypeIndex](/libs/type_index/)（运行时类型索引库）：

  - 维护性工作，包括与 inspect 工具的 CI 集成。

- [Utility](/libs/utility/)（通用工具库）：

  - `ostream_string` 设施已从 Utility 库迁移至 IO 库，作为 `ostream_put`。

- [Variant](/libs/variant/)（非递归可辨识联合库）：

  - 移除未使用的包含（感谢 Nikita Kniazev，[\#74](https://github.com/boostorg/variant/issues/74)）。

  - 修复"以零作为空指针常量"警告（感谢 Bart Siwek，[\#77](https://github.com/boostorg/variant/issues/77)）。

  - 维护性工作，包括拼写错误修复。

- [Variant2](/libs/variant2/)（Variant 的现代重实现库）：

  - 新增对 `std::hash`、`boost::hash` 的支持。

  - 当 `T...` 中所有类型均为平凡（trivial）类型时，`variant<T...>` 现在也是平凡类型。这使其能通过寄存器传入与传出函数，从而提升性能。

- [WinAPI](/libs/winapi/)（Win32 API 薄封装库）：

  - `boost/detail/winapi` 中的头文件已弃用，将在未来发布中移除。

  - Boost.WinAPI 头文件不再包含 `winerror.h`。如需 Windows 错误码，请包含 `boost/winapi/error_codes.hpp`（[\#81](https://github.com/boostorg/winapi/issues/81)）。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)（b2 构建系统框架）：

  - 包含 B2 的 [4.2.0](https://github.com/boostorg/build/releases/tag/4.2.0) 发布。

  - 警告：自 4.0.0 版本起，B2 需要具备完整 C++11 能力的编译器进行引导（bootstrap）。这只在构建 B2 自身时需要，构建供您使用的 Boost 并不需要。

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
