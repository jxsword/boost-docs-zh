# Boost 1.80.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_80_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_80_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2022-08-10 21:25 GMT（原文日期行：August 10th, 2022 21:25 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.80.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 已知问题（Known Issues）

以下补丁由库作者提供，因发现时间过晚而未能纳入本次发布修复。

- Config（编译器/平台特性检测与配置宏库）

  - 新增对 libcpp15 的支持，该版本标准库已移除 `std::unary_function` 与 `std::binary_function`。[补丁](/patches/1_80_0/0005-config-libcpp15.patch)。

- Filesystem（可移植文件系统操作库）

  - 在 Windows 10 之前的系统上，针对网络共享的目录迭代器可能无法构造，参见 [PR#246](https://github.com/boostorg/filesystem/pull/246) 与 [\#245](https://github.com/boostorg/filesystem/issues/245)。[补丁](/patches/1_80_0/0001-filesystem-win-fix-dir-it-net-share.patch)。

  - 在 Windows 上，`weakly_canonical` 无法处理以 "\\?\ 前缀开头的路径（译注：原文该处引号残缺），参见 [\#247](https://github.com/boostorg/filesystem/issues/247)。[补丁](/patches/1_80_0/0002-filesystem-fix-weakly-canonical-long-paths.patch)。

  - 在不支持 `*at` API 的 POSIX 系统上，因缺少一个头文件包含而导致编译失败，参见 [\#250](https://github.com/boostorg/filesystem/issues/250)。[补丁](/patches/1_80_0/0004-filesystem-posix-fix-no-at-apis-missing-include.patch)。

- Unordered（无序关联容器（哈希实现）库）

  - 容器在被移动后不处于有效状态，参见 [\#139](https://github.com/boostorg/unordered/issues/139)。[补丁](/patches/1_80_0/0003-unordered-valid-after-move.patch)。

  - 修复 MSVC /RTCc 构建下的运行期失败。[补丁](/patches/1_80_0/0006-unordered-msvc-rtcc.patch)。

## 新增库（New Libraries）

本版无新增库。

## 更新的库（Updated Libraries）

- [Asio](/libs/asio/)（网络与底层 I/O 库）：

  - 为所有异步操作添加了推导尾置返回类型（deduced trailing return type），以支持 C++11 下新形式的 `async_result`。

  - 将 `append`、`prepend`、`as_tuple` 与 `deferred` 移入 `boost::asio` 命名空间，并使其兼容 C++11。

  - 使 `experimental::parallel_group` 兼容 C++11。

  - 为连续容器（如 `std::span`）新增了 `buffer()` 重载。

  - 使基于 `awaitable<>` 的协程能够直接 `co_await` 以函数对象形式打包的操作。

  - 将 `spawn()` 改为基于完成标记（completion token）的异步操作，并新增对取消（cancellation）的支持。`basic_yield_context` 标记现在支持仅可移动（move-only）与可变参数的结果类型。在以 C++11 及更高标准为目标时，`spawn()` 与 `basic_yield_context` 直接基于 Boost.Context（执行上下文库）实现。

  - 新增 `is_async_operation` 特征（traits）与 `async_operation` 概念（concept）。

  - 新增 `completion_signature_of` 特征。

  - 为 POSIX 描述符、串口、管道、Windows `object_handle`、Windows 流句柄与 Windows 随机访问句柄新增了转换移动构造/赋值。

  - 为管道、Windows 流句柄与 Windows 随机访问句柄新增 `release()` 成员函数。

  - 依据文档所载的 `Endpoint` 类型要求，支持其 `data()` 成员函数返回 `void` 指针的 `Endpoint` 实现。

  - 从 `experimental::promise` 中移除了 `all()` 与 `race()`，因为 `experimental::parallel_group` 已覆盖该功能。

  - 为同步与异步操作产生的异常和错误码添加了源位置（source location）信息。

  - 修复与 OpenSSL 3.0.4 及更高版本的兼容性。

  - 修复与 `-masm=intel` 的兼容性。

  - 明确说明：就同一套接字上的某些其他同步操作而言，套接字 `shutdown()` 调用是线程安全的。

  - 优化了仅执行器（executor）类型不同的 I/O 对象的移动构造。

  - 修复 clang/libc++ 下对 `std::invoke_result` 的检测。

  - 修复 `experimental::parallel_group` 的发起（initiation）错误地移动（move）而非转发（forward）实参的问题。

  - 修复 `post()`、`dispatch()` 与 `defer()` 实现中的一处顺序（sequencing）问题。

  - 修复 `awaitable<>` 实现，使被等待的发起函数抛出的异常能经由当前完成处理程序（completion handler）传播。

  - 修复 gcc 7 下对 `std::aligned_alloc` 的检测。

  - 更改实现，在新编译器上避免使用即将弃用的 `std::aligned_storage`。

  - 修复较旧 Apple 平台上对 `std::aligned_alloc` 的检测。

  - 移除了 `experimental::coro` 实现中有误的断言。

  - 在使用 Intel C++ 构建时，增加了对 Qt 所定义宏的防御。

  - 在 Windows 上更改了 `select_reactor` 的实现，确保其中断器（interrupter）套接字重建失败所产生的任何异常都能经由 `io_context::run()` 向外传播。

  - 修复了多种编译器警告。

  - 更新了全部组合操作（composed operations）示例与 C++11 超时示例，改用新形式的 `async_result`。

  - 新增面向 C++20 的组合操作与协程示例。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_80_0/doc/html/boost_asio/history.html)。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 改进了在 ARM、AArch32 与 AArch64 目标平台上字节序检查的可移植性。（[\#59](https://github.com/boostorg/atomic/issues/59)）

  - 修复在 C++17 模式下使用 MSVC 14.0（Visual Studio 2015）的编译问题。（[\#61](https://github.com/boostorg/atomic/issues/61)）

- [Filesystem](/libs/filesystem/)：

  - 在 Windows 上，为查询文件属性新增了一个回退实现，用于文件因 `ERROR_ACCESS_DENIED` 错误而无法打开的情形。这可能使 `status` 与 `symlink_status` 对非重解析点（reparse point）或符号链接的系统文件和目录也能成功。（[\#234](https://github.com/boostorg/filesystem/issues/234)）

  - 在 Windows 上，为查询文件属性时产生 `ERROR_INVALID_PARAMETER` 错误的 FAT/exFAT 文件系统增加了变通方案。此问题影响 `status` 与 `symlink_status`（会报告文件不存在）、无法构造的目录迭代器，以及其他依赖这些操作的功能。（[\#236](https://github.com/boostorg/filesystem/issues/236)、[\#237](https://github.com/boostorg/filesystem/issues/237)）

  - 解决了 [RTEMS](https://www.rtems.org/)（嵌入式实时操作系统）上的一处编译问题。（[PR#240](https://github.com/boostorg/filesystem/pull/240)）

  - 在 Linux 上，修正了当 `copy_file_range` 在运行期以 `ENOSYS` 失败时切换到 `sendfile` 版 `copy_file` 实现的逻辑。原先的 `sendfile` 回退实现会跳过文件系统类型检查，在某些文件系统上可能失败。

  - 在支持 POSIX.1-2008 所定义的 `openat` 及相关 API 的 POSIX 系统上，以及 Windows Vista 及更高版本上，改进了上一发布中针对 [CVE-2022-21658](https://www.cve.org/CVERecord?id=CVE-2022-21658) 的 `remove_all` 防护。此前的修复在某些[条件下](https://github.com/boostorg/filesystem/issues/224#issuecomment-1183738097)仍可能误删非预期文件。其他系统仍然易受攻击。

- [GIL](/libs/gil/)（通用图像库）：**注意：** 我们计划在 Boost 1.80 之后的一到两个发布内，以破坏性变更方式将要求的最低 C++ 语言标准切换为 C++17（[\#676](https://github.com/boostorg/gil/issues/676)）

  - 新增：

    - GSoC 2020（Google Summer of Code，谷歌编程之夏）：新增 Perona-Malik 各向异性扩散算法（[PR#500](https://github.com/boostorg/gil/pull/500)）

    - GSoC 2020：新增直方图类及相关功能（[PR#499](https://github.com/boostorg/gil/pull/499)）

    - GSoC 2020：新增直方图均衡化功能（[PR#514](https://github.com/boostorg/gil/pull/514)）

    - GSoC 2020：新增直方图匹配算法（[PR#515](https://github.com/boostorg/gil/pull/515)）

    - GSoC 2020：新增水平（`hstack`）或垂直（`vstack`）堆叠图像的能力（[PR#506](https://github.com/boostorg/gil/pull/506)）

    - GSoC 2020：新增自适应直方图均衡化算法（[PR#516](https://github.com/boostorg/gil/pull/516)）

    - GSoC 2020：新增标准霍夫变换（Hough Transform）与圆光栅化（[PR#512](https://github.com/boostorg/gil/pull/512)）

    - GSoC 2020：新增用于直线光栅化的 Bresenham 算法（[PR#512](https://github.com/boostorg/gil/pull/512)）

    - GSoC 2021：新增绕图像中心以任意角度旋转图像的功能（[PR#565](https://github.com/boostorg/gil/pull/565)）

    - GSoC 2021：基于 Jerry Van Aken 的论文《An Efficient Ellipse-Drawing Algorithm》新增椭圆光栅化支持（[PR#585](https://github.com/boostorg/gil/pull/585)）

    - 新增从兼容视图构造 `image` 的构造函数（[PR#520](https://github.com/boostorg/gil/pull/520)）

    - 为仿射变换 `matrix3x2` 新增求逆函数（[PR#527](https://github.com/boostorg/gil/pull/527)）

    - 新增标准形态学变换（[PR#541](https://github.com/boostorg/gil/pull/541)）

    - 为 `any_image` 新增 `for_each_pixel` 重载（[PR#648](https://github.com/boostorg/gil/pull/648)）

    - 为 `image` 类新增 C++17 多态内存资源（polymorphic memory resource）类型别名（[PR#529](https://github.com/boostorg/gil/pull/529)）

  - 变更：

    - **破坏性变更：** 要求的最低 C++ 版本从 C++11 提升至 C++14。目前 GIL 的大部分代码仍可用 C++11 编译器编译，但不保证一直如此；自本发布起，任何不支持至少 C++14 的编译器均视为不受支持。

    - **破坏性变更：** `any_color_converted_view()` 已弃用，将在下一个发布中移除。请改用提供相同功能的 `color_converted_view()`。

    - **破坏性变更：** 用于 `any_image` 的 `apply_operation` 已弃用，将在下一个发布中移除。请改用提供相同功能的 `variant2::visit`。（[PR#656](https://github.com/boostorg/gil/pull/656)）

    - 将数值（numeric）扩展移入核心库（[PR#573](https://github.com/boostorg/gil/pull/573)）

    - 新增对 C++17 `<filesystem>` 的支持（[PR#636](https://github.com/boostorg/gil/pull/636)）。系统会自动检测 `std::filesystem` 的可用性，除非定义了强制优先使用 Boost.Filesystem 的 `BOOST_GIL_IO_USE_BOOST_FILESYSTEM` 宏。

    - 将 `pixel_multiply_t` 重命名为 `pixel_multiplies_t`，将 `pixel_divide_t` 重命名为 `pixel_divides_t`（[PR#655](https://github.com/boostorg/gil/pull/655)）

    - 将 `io/dynamic_io_new.hpp` 重命名为 `io/detail/dynamic.hpp`（[PR#653](https://github.com/boostorg/gil/pull/653)）

    - 将函数 `construct_matched` 移入 `boost::gil::detail` 命名空间，因为它仅被其他实现细节使用（[PR#653](https://github.com/boostorg/gil/pull/653)）

    - 使 `packed_pixel` 可平凡复制（trivially copyable）与可平凡赋值（[PR#679](https://github.com/boostorg/gil/pull/679)）

    - 以 C99 定宽整数类型取代已弃用的 libtiff v4.3 类型别名（[PR#685](https://github.com/boostorg/gil/pull/685)）

  - 移除：

    - **破坏性变更：** 移除对 GCC 5 的支持（[PR#572](https://github.com/boostorg/gil/pull/572)）

    - 移除 deprecated.hpp（[PR#627](https://github.com/boostorg/gil/pull/627)）

  - 修复：

    - 修复 RGB 到 HSL 的转换（[PR#505](https://github.com/boostorg/gil/pull/505)）

    - 修复 RGB 到有符号 CMYK 的转换（[PR#522](https://github.com/boostorg/gil/pull/522)）

    - 移除 hsv.hpp 中不必要的数值转换（[PR#530](https://github.com/boostorg/gil/pull/530)）

    - 修复 `homogeneous_color_base` 在像素元素为引用时的默认构造函数（[PR#542](https://github.com/boostorg/gil/pull/542)）

    - 修复 `subchroma_image_view` 返回局部临时对象引用的问题（[PR#556](https://github.com/boostorg/gil/pull/556)）

    - 补充 diffusion.hpp 中缺失的头文件保护（include guard）（[PR#568](https://github.com/boostorg/gil/pull/568)）

    - 修复 `any_image_view<>::const_t`（[PR#526](https://github.com/boostorg/gil/pull/526)）

    - 修复 I/O 扩展中与 C++20 不兼容之处（[PR#617](https://github.com/boostorg/gil/pull/617)）

    - 确保全部示例可无错构建（[PR#628](https://github.com/boostorg/gil/pull/628)）

    - 修复对 `float32_t` 通道模型图像的 `convolve_2d`（[PR#577](https://github.com/boostorg/gil/pull/577)）

    - 修复对非一维可迭代视图的 `for_each_pixel`（[PR#621](https://github.com/boostorg/gil/pull/621)）

    - 修复：PNG I/O 中的 `is_equal_to_sixteen` 原为小于（less-than）比较（[PR#650](https://github.com/boostorg/gil/pull/650)）

    - 重新允许带两个分量的 `devicen_t`（[PR#654](https://github.com/boostorg/gil/pull/654)）。该支持在 Boost 1.72 中被意外移除。

    - 修复 `image` 类在维度为空时的内存泄漏（[PR#649](https://github.com/boostorg/gil/pull/649)）

  - 致谢：

    - Cypre55, Samuel Debionne, Mike-Devel, Edward Diener, Peter Dimov, Omar Emara, Dhruva Gole, Nicolas Herry, Eugene K, Avinal Kumar, Gaurav Kumar, Marco Langer, Pranam Lashkari, Mateusz Łoskot, Giovanni Mascellani, Debabrata Mandal, Gopi Krishna Menon, René Ferdinand Rivera Morell, Felix Morgner, Harshit Pant, Paul92, André Schröder, Scramjet911, Siddharth, Dirk Stolle, Prathamesh Tagore, theroyn, Olzhas Zhumabek

- [Graph](/libs/atomic/)（图结构与算法库）（译注：原文该条目链接误指向 /libs/atomic/）：

  - 缺陷修复：

    - 修复 `stoer_wagner_min_cut` 中每个最小割（mincut）阶段结束时顶点未被合并的缺陷（[\#286](https://github.com/boostorg/graph/issues/286)）

    - 修复 `strong_components` 返回类型的转换警告（[\#293](https://github.com/boostorg/graph/issues/293)）

    - 修复 `boykov_kolmogorov_max_flow` 命名参数重载的编译失败（[\#232](https://github.com/boostorg/graph/issues/232)）

  - 代码总体改进：

    - 移除 `astar_search_no_init_tree` 中对 `combine` 的冗余调用（[\#260](https://github.com/boostorg/graph/issues/260)）

    - 移除 `d_ary_heap_indirect<>::child` 中冗余的 `child_idx` 实参（[\#261](https://github.com/boostorg/graph/issues/261)）

    - 改进遍历类别（traversal categories）的文档（[\#303](https://github.com/boostorg/graph/issues/303)）

  - 致谢：

    - Viktor Pti, Sebastian Brockmeyer, Etienne dg

- [Histogram](/libs/histogram/)（多维直方图库）：

  - 修复在某些条件下对轴大小为零（物理或逻辑）的直方图进行迭代时 `indexed` 段错误（segfault）的问题。

  - 移除先前已弃用的 API：

    - 类 `accumulators::thread_safe`：请改用 `accumulators::count<T, true>`

    - 方法 `accumulators::sum::large` 与 `accumulators::sum::small`：请改用 `accumulators::sum::large_part` 与 `accumulators::sum::small_part`

    - 类型别名 `algorithm::reduce_option`：请改用 `algorithm::reduce_command`

    - 模板函数 `axis::traits::static_options`：请改用 `axis::traits::get_options`

    - 模板函数 `axis::traits::static_is_inclusive`：请改用 `axis::traits::is_inclusive`

    - 类型别名 `indexed::range_iterator`：请改用 `indexed::iterator`

    - 类型别名 `indexed::accessor::reference`：请改用 `indexed::accessor::const_reference`

- [Iterator](/libs/iterator/)（迭代器构建设施库）：

  - 对 C++11 及更高标准，新增对写入 `function_output_iterator` 的值进行完美转发（perfect forwarding）的支持。（[PR#73](https://github.com/boostorg/iterator/pull/73)）

  - 新增防护：防止将解引用另一个 `function_output_iterator` 得到的结果写入 `function_output_iterator`。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 新增非 const 的 `value::at` 重载。

  - 新增手动选择平台字节序的能力。

  - 新增 `string::subview()` 重载。

  - 修复 `array::erase(it)` 中的段错误。

  - 修复 libc++ 上 `serialize` 性能低下的问题。

  - 修复 GCC 8 上到 `std::string_view` 的歧义转换问题。

  - 修复大端平台上的解析。

  - 修复对尾随逗号之后注释的处理。

- [LEAF](/libs/leaf/)（轻量级错误处理库）：

  - API 破坏性变更：`throw leaf::exception(....)` 现改为 `leaf::throw_exception(....)`。

  - 修复一个罕见构建配置（启用异常处理、禁用诊断）支持中的缺陷。

  - 全库以 `nullptr` 取代 `0`。

  - 修复 pedantic（严谨模式）警告。

- [Locale](/libs/locale/)（本地化与 Unicode 文本处理库）：

  - 弃用对 C++03 及更早标准的支持，下一个发布将要求 C++11。

  - 提供 `-sICU_LINK_LOCALE` 作为与 Boost.Regex（正则表达式库）不兼容的 `-sICU_LINK` 的临时替代。`-sICU_LINK_LOCALE` 与 `-sICU_LINK` 均已弃用，将来会被与 Boost.Regex 兼容的 `ICU_*_NAME` 选项取代。

  - 修复 ICU `collator`（排序器）实现在变换空字符串时的未定义行为/断言失败。

  - 修复与共享库中类可见性相关的一些问题（仅 Unix）。

  - 修复与 C++20 模式的兼容性。

  - 修复与 `BOOST_USE_WINDOWS_H` 的兼容性。

  - 修复因缺少头文件包含导致的构建失败。

  - 处理或抑制了大量警告，使构建日志更整洁。

- [Log](/libs/log/)（日志库）：

  - 缺陷修复：

    - 修复基于 UDP 套接字的 `syslog_backend` 在 syslog 服务器使用 IPv6 地址时绑定错误本地地址的问题。（[\#181](https://github.com/boostorg/log/issues/181)）

    - 为 gcc 11.2 的 libstdc++ 中的一个[缺陷](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105857)增加了变通方案。当在格式化流上使用 `max_size_decor` 时，`std::codecvt::do_length` 会错误访问输入缓冲区并导致缓冲区溢出。

  - 更多细节请参见[变更日志（changelog）](/libs/log/doc/html/log/changelog.html)。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - **弃用 C++11 支持**：自 2023 年起，我们将要求 C++14 作为最低标准。这意味着最低要求为 GCC-5 或 MSVC-14.1。

  - 新增 `constexpr` fma（融合乘加）支持，参见 [734](https://github.com/boostorg/math/pull/734)。

  - 新增对 Chatterjee 相关系数的支持，参见 [770](https://github.com/boostorg/math/pull/770)。

  - 为所有分布新增对其概率密度函数（PDF）对数的支持。

  - 改进在无异常或 RTTI（运行时类型信息）支持下的构建支持。

  - 修复 1F1（超几何函数）若干边界情形的小缺陷，参见 [778](https://github.com/boostorg/math/pull/778)。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - **将 C++11 支持标记为弃用**：自 2023 年起，我们将转向要求 C++14 作为最低标准级别。届时将不再支持 GCC 5 之前版本与 MSVC 14.1 之前版本。

  - 修复 `boost/cstdfloat.hpp` 与本库之间的冲突。

  - 清理了大量 gcc 与 clang 警告。

  - 修复复合类型（complex、interval、rational）的输入流在流中存在尾随分隔符且无空白字符时的问题。

  - 修复输入为 1、2 或 3 时 `constexpr` 整数平方根的问题。

  - 为 float128.hpp 补充缺失的 `<memory>` `#include`。

  - 修正类 `number` 的双实参构造函数，避免某些情形下的歧义。

  - 修正 gmp.hpp 中除以零的行为，并使其更为一致。

- [Multi-index Containers](/libs/multi_index/)（多索引容器库）：

  - 维护性工作。

- [Nowide](/libs/nowide/)（Windows 下 UTF-8 标准 I/O 适配库）：

  - 大幅提升文件批量（Bulk）I/O 的性能。

  - `basic_filebuf`：修复 `fflush` 失败时 `sync` 返回值错误的问题。

  - `basic_filebuf`：修复一个边界情形下可能出现的未定义行为——实际未写入任何内容但缓冲区处于"写入"模式时。

  - `basic_filebuf`：限制字符回退（即 `pbackfail`），仅允许回退已缓冲的字符（可能仅 1 个字符）。

- [Optional](/libs/optional/)（可选值容器库）：

  - 新增 `std::hash<boost::optional<T>>` 特化。对自行定义了此类特化的程序而言，这是一项破坏性变更。更多细节参见[规格说明（specs）](/libs/optional/doc/html/boost_optional/reference/header__boost_optional_optional_hpp_/detailed_semantics___std__hash_specializations.html#reference_std_hash_spec)。

- [STLInterfaces](/libs/stl_interfaces/)（迭代器/范围定制点 CRTP 基类库）：

  - 修复 [\#53](https://github.com/boostorg/stl_interfaces/issues/53)："missing 'typename' prior to dependent type name 'C::const_iterator'"（依赖类型名 'C::const_iterator' 前缺少 'typename'）问题。

  - 修复 [\#54](https://github.com/boostorg/stl_interfaces/issues/54)："Concept check fails on .data() of a view on contiguous iterator_interface instantiations"（对连续迭代器 iterator_interface 实例化之上的视图调用 .data() 时概念检查失败）问题。

  - 新增内容，使编写与标准库中的视图和视图适配器行为一致且可互操作的视图与视图适配器更加容易：

    - 为 C++23 之前的代码新增 C++23 `std::bind_back()` 与 `std::range_adaptor_closure` 的等效实现。

    - 依照 [P2387](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p2387r3.html) 中的示例，新增模板 `closure` 与 `adaptor`，使编写视图适配器更加容易。

- [System](/libs/system/)（错误码与 system_error 库）：

  - 当 `error_code` 被转换为 `std::error_code` 之后再转换回 `error_code` 时，现在会尽可能地恢复原始值。

  - 重构了从 `error_category` 到 `std::error_category` 的转换，以避免在内存泄漏检查工具中显现的一次性分配。

  - 新增一个允许替换 `error_code` 源位置的构造函数，以及相应的 `assign`。

  - 为 `result` 新增转换构造函数。

- [Unordered](/libs/unordered/)：重大更新：

  - [重构](/libs/unordered/doc/html/unordered.html#buckets_fast_closed_addressing_implementation)内部实现，速度大幅提升。

  - 允许 `final` 的 `Hasher` 与 `KeyEqual` 对象。

  - 更新文档，新增基准测试图表与关于新内部数据结构的说明。

- [Utility](/libs/utility/)（通用工具库）：

  - 在 `string_view`/`string_ref` 中，修复 `max_size` 返回错误值的问题。（[\#91](https://github.com/boostorg/utility/issues/91)）

  - 从 `string_view::compare` 中移除 `noexcept` 限定符，因为它在某些输入实参下可能抛出异常。（[\#94](https://github.com/boostorg/utility/issues/94)）

  - 在 `string_view`/`string_ref` 中，新增以无实参方式调用 `substr` 的支持。（[\#96](https://github.com/boostorg/utility/issues/96)）

  - 新增 C++23 引入的 `string_view::contains` 方法。（[\#93](https://github.com/boostorg/utility/issues/93)）

  - 在 `string_view` 的 `remove_prefix`/`remove_suffix` 方法中新增断言，以强制执行"前缀/后缀长度不得超过 string view 大小"这一前置条件。此前（未载入文档的）静默截断前缀/后缀长度的行为已弃用，将在未来发布中移除。（[\#92](https://github.com/boostorg/utility/issues/92)）

- [Wave](/libs/wave/)（C/C++ 预处理器实现库）：修复的缺陷：

  - [\#24](https://github.com/boostorg/wave/issues/24)：条件段（conditional section）之后行号错误。

  - [\#160](https://github.com/boostorg/wave/issues/160)：在 msvc /permissive- 模式下有一个测试以错误 C2660 与错误 C2440 失败。

  - [\#161](https://github.com/boostorg/wave/issues/161)：`BOOST_WAVE_THROW_NAME_CTX` 不会触发上下文回调，且总是抛出异常。

  - [\#162](https://github.com/boostorg/wave/issues/162)：当预处理翻译单元中包含 Boost 头文件时，Wave 在 boost/integer.hpp(99) 处失败。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)（b2 构建系统框架）：

  - 包含 [B2 version 4.9.2](/tools/build/doc/html/#_version_4_9_2) 的发布。

## 已测试的编译器（Compilers Tested）

Boost 的主要测试编译器如下（译注：原文该句重复出现两次，此处仅译一次）：

- Linux：

  - Clang：3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 12.0.0, 13.0.0, 14.0.0

  - Clang，C++11：3.4, 11.0.0, 13.0.0, 14.0.0

  - Clang，C++14：3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 5.0, 12.0.0, 13.0.0, 14.0.0

  - Clang，C++17：6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0, 12.0.0, 13.0.0, 14.0.0

  - Clang，C++20：11.0.0, 12.0.0, 13.0.0, 14.0.0

  - GCC：4.6.3, 11, 12

  - GCC，C++11：4.7.3, 4.8.5, 11, 12

  - GCC，C++14：5.4.0, 6.4.0, 7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC，C++17：7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC，C++20：8.0.1, 9.1.0, 10, 11, 12

- OS X：

  - Apple Clang：11.0.3

  - Apple Clang，C++11：11.0.3

  - Apple Clang，C++14：11.0.3

  - Apple Clang，C++17：11.0.3

  - Apple Clang，C++20：11.0.3

- Windows：

  - Visual C++：10.0, 11.0, 12.0, 14.0, 14.1, 14.2, 14.3

## 致谢（Acknowledgements）

本次发布由 Marshall Clow、Michael Caisse 与 Glen Fernandes 管理。
