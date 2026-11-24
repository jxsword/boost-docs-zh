# Boost 1.83.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_83_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_83_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2023-08-11 16:23 GMT（原文日期行：August 11th, 2023 16:23 GMT）
> 下载：下载文件与 SHA256 清单见原文存档（URL 模式 https://archives.boost.io/release/1.83.0/source/）；原文另注明下载链接由 The C++ Alliance 资助支持。

## 总体注记（General Notes）

本版原文无"总体注记"栏目。

## 已知问题（Known Issues）

以下为库作者提供的补丁，这些补丁发现得过晚，来不及在本发布中修复。

- JSON

  - 在 Windows ARM 平台上编译可能因缺少内建函数（intrinsics）而失败，见 [\#926](https://github.com/boostorg/json/issues/926) 与 [\#927](https://github.com/boostorg/json/issues/927)。[补丁](https://github.com/boostorg/json/commit/c4ce8509d015a0b75cfa9d36609b8409821a9c86.patch)。

- Unordered

  - 修复会销毁不存在元素的错误拷贝赋值运算符（copy assignment operator），见 [\#205](https://github.com/boostorg/unordered/issues/205)。[补丁](/patches/1_83_0/0001-unordered-fix-copy-assign.patch)。

## 新增库（New Libraries）

- [Compat](/libs/compat/)（标准库补丁库）：收录后续 C++ 标准所新增标准组件的 C++11 实现的仓库（repository），由 Peter Dimov 与各位贡献者开发。

## 更新的库（Updated Libraries）

- [Any](/libs/any/)（类型安全的任意类型容器库）：

  - 新增 `boost::anys::unique_any` C++11 类——`boost::any`（或 `std::any`）的替代品，不要求所存类型可拷贝或移动构造。

  - 文档移植为 QuickBook 文档格式，代码中改用 Doxygen 注释。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 修复 `const` 限定类型的 `atomic_ref` 编译问题。注意，即使是 `const` 限定的原子对象也必须位于可读写内存中（[\#62](https://github.com/boostorg/atomic/issues/62)）。

- [Chrono](/libs/chrono/)（时间度量与时钟库）：

  - 移除对已弃用 Boost.Ratio 特性的使用。

- [Compat](/libs/compat/)（标准库补丁库）：

  - 新增 `latch.hpp`，为 `std::latch` 的实现（由 Christian Mazakas 贡献）。

  - 新增 `shared_lock.hpp`，为 `std::shared_lock` 的（部分）实现（由 Christian Mazakas 贡献）。

- [Core](/libs/core/)（核心工具集库）：

  - `boost::core::type_name` 新增对不完整类型（incomplete type）的支持。

  - `boost/core/bit.hpp` 中的位操作函数在较新的 MSVC 版本（VS2019 update 5 及更高）上现为 `constexpr`。

  - 在 `boost/core/bit.hpp` 中新增 `boost::core::byteswap`（C++23 `std::byteswap` 的实现）。

  - 将让出（yield）原语 `sp_thread_pause`、`sp_thread_yield`、`sp_thread_sleep` 从 SmartPtr 的实现细节移至 `boost/core/yield_primitives.hpp`。

- [DLL](/libs/dll/)（动态库加载/插件库）：

  - 修复 glibc 2.36 及更高版本上的测试失败，感谢 [Đoàn Trần Công Danh](https://github.com/sgn) 提交的错误报告 [\#58](https://github.com/boostorg/dll/issues/58)。

- [Filesystem](/libs/filesystem/)（可移植文件系统操作库）：

  - 新增 `directory_entry::refresh` 方法，用于更新由 path 所标识的目录项（directory entry）的内部缓存文件状态。

  - **v4：** 初始化或修改 path 的 `directory_entry` 构造函数与修改器（modifier）现在会自动调用 `refresh`。当查询文件系统获取文件状态失败时（例如文件不存在），可能产生此前以及 **v3** 中不会报告的错误。这一新行为与 std::filesystem 类似。

  - **v4：** 移除了接受 `file_status` 参数的 `directory_entry` 构造函数与方法。建议用户移除这些实参，依赖 `directory_entry` 内部调用 `refresh`。

  - 新增用于检查文件类型的 `directory_entry` 成员方法，与 std::filesystem 类似。

  - 新增更多测试文件状态的方法：`is_block_file`、`is_character_file`、`is_fifo`、`is_socket` 与 `is_reparse_file`。

  - `recursive_directory_iterator` 现在更可能复用在文件系统遍历期间获得的文件类型信息。这可能改善性能（[\#288](https://github.com/boostorg/filesystem/issues/288)）。

  - `boost/filesystem/fstream.hpp` 中定义的文件流在标准库文件流可移动时也可移动（[\#280](https://github.com/boostorg/filesystem/issues/280)）。

  - 新增头文件 `boost/filesystem/cstdio.hpp`，其中包含以 `path` 为第一个实参的可移植 `fopen` 重载。该函数等价于 `std::fopen`，区别在于在 Windows 上路径使用原生宽字符编码。

  - 泛型 `path` 比较运算符现在更加受限，以避免用户代码中包含 `using namespace boost::filesystem;` 指令时出现潜在的歧义（[\#285](https://github.com/boostorg/filesystem/issues/285)）。

  - 修复用户代码中潜在的重载决议歧义：自迭代器构造 `path` 的构造函数可能与接受 `std::initializer_list` 实参的函数重载相互干扰（[\#287](https://github.com/boostorg/filesystem/issues/287)）。

  - 在 Windows 上，针对创建目录迭代器时各种文件系统返回的错误新增了更多变通方案（[\#284](https://github.com/boostorg/filesystem/issues/284)、[\#286](https://github.com/boostorg/filesystem/issues/286)）。

  - 在 Windows 上，放宽查询文件时间所需的访问权限（[\#290](https://github.com/boostorg/filesystem/issues/290)）。

- [Flyweight](/libs/flyweight/index.html)（享元模式库）：

  - 为 `boost::flyweight` 新增智能指针语法（`operator*` 与 `operator->` 解引用到底层值）。

  - 修复 [`simple_locking`](/libs/flyweight/doc/reference/locking.html#simple_locking_synopsis) 所用互斥量不是递归型（recursive）的情形（issue [\#12](https://github.com/boostorg/flyweight/issues/12)）。

- [Geometry](/libs/geometry/)（几何算法库）：

  - 改进（Improvements）：

    - [PR#1140](https://github.com/boostorg/geometry/pull/1140) 移除依赖，并在多处将 boost 替换为 std

    - [PR#1154](https://github.com/boostorg/geometry/pull/1154) 补齐缺失的头文件，使所有头文件均可独立编译，符合 Boost 政策

    - [PR#1157](https://github.com/boostorg/geometry/pull/1157) 在 `calculate_point_order` 中检查 const Ring 概念（concept）

  - 已解决问题（Solved issues）：

    - [\#1100](https://github.com/boostorg/geometry/issues/1100) 修复 union（并集）运算

    - [\#1139](https://github.com/boostorg/geometry/issues/1139) 修复不同几何类型下的处理

    - [\#1158](https://github.com/boostorg/geometry/issues/1158) 修复凸包（convex hull）计算

    - [\#1161](https://github.com/boostorg/geometry/issues/1161) 修复几何对象以极点（pole）为顶点时 within 算法的问题

    - 各类错误与警告的修复

- [Iterator](/libs/iterator/)（迭代器构建设施库）：

  - 新增 `is_iterator` 类型特征（traits），可用于测试某类型是否符合迭代器类型的要求。

  - `filter_iterator` 现支持被适配迭代器与函数对象的移动构造（[PR#79](https://github.com/boostorg/iterator/pull/79)）。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 该库现在只抛出 `system_error`，仅当内存分配失败时抛出 `std::bad_alloc`。

  - 序列化行为现在可通过 `serialize_options` 更改。

  - 上下文相关转换（contextual conversions）。

  - 新增解析器选项，用于更精确的数字解析。

  - 流式 `operator<<` 支持 `parse_options`。

  - 新增解析器选项，允许 JSON 字面量 `Infinity` 与 `NaN`。

  - 新增仅校验数字而不进行解析的解析器模式。

  - 指数大于 `INT_MAX` 的数字现在会被解析器接受并按无穷大处理。

  - 修复应提供强保证（strong guarantee）的 `object` 成员函数。

  - 修复包含 `boost/range.hpp` 时 `end` 调用的歧义。

  - 修复 ASan（AddressSanitizer）失败。

  - 修复 `error::size_mismatch` 的错误消息。

  - 修复转换为含 const 元素的 tuple 的问题。

- [Locale](/libs/locale/index.html)（本地化与 Unicode 文本处理库）：

  - 消息目录（message catalog）文件不再支持按位/二元运算符（左移/右移、按位与/或/异或/非），与 GNU gettext 行为保持一致。

  - Windows 上的 Std 后端在所请求的 locale 不存在时使用 classic locale 而非系统 locale（现与其他操作系统上的行为相同）。

  - `localization_backend_manager::get` 已弃用，请改用 generator。

  - 新增转换器（converter）类，作为 `to_utf`/`from_utf`/`between` 的替代。

  - 修复格式字符串中无效索引导致的未定义行为（UB）。

  - 修复在 Windows 上无 ICU 时 UTF 到 iso-2022-jp 等编码的转换。

  - 复数形式翻译的计数参数改用 `long long`。

  - 修复部分类的可移动性与异常规范（exception specification）。

- [Log](/libs/log/)（日志库）：

  - 修复 `text_file_backend` 中当格式化后的日志记录大小超过 `rotation_size` 限制时可能出现的无限循环（[\#209](https://github.com/boostorg/log/issues/209)）。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - 新增 Daubechies 尺度函数（scaling functions）傅里叶变换的数值求值（[921](https://github.com/boostorg/math/pull/921)）。

  - 为统计分布新增 logcdf 函数（[946](https://github.com/boostorg/math/pull/946)）。

  - 新增对 C++23 `<stdfloat>` 类型的支持（[978](https://github.com/boostorg/math/pull/978)）。

  - 修复多处 `-Wmaybe-uninitialized` 警告。

  - 修复数字不可表示时 `round` 与 `trunc` 函数的问题（[968](https://github.com/boostorg/math/pull/968)）。

  - 修复 F 分布众数（mode）的计算（[976](https://github.com/boostorg/math/pull/976)）。

  - 修复 beta 分布中的溢出（[977](https://github.com/boostorg/math/pull/977)）。

  - 修复超几何分布（hypergeometric distribution）中的溢出（[987](https://github.com/boostorg/math/pull/987)）。

  - 修复非零中心时中位数绝对偏差（median absolute deviation）的计算（[997](https://github.com/boostorg/math/pull/997)）。

- [Mp11](/libs/mp11/)（C++11 元编程库）：

  - 为 `mp_from_sequence`、`mp_iota`、`mp_iota_c` 新增 offset/from 参数。

  - 新增 `mp_value`、`mp_list_v`、`mp_rename_v`、`mp_is_value_list`。

  - 为 `<boost/mp11/list.hpp>` 中的原语新增值列表（value list）支持。

  - 为 `mp_repeat`、`mp_fill`、`mp_at`、`mp_back`、`mp_take`、`mp_pop_back`、`mp_drop`、`mp_insert`、`mp_erase` 新增值列表支持。

- [Multi-index Containers](/libs/multi_index/)（多索引容器库）：

  - 更新非唯一有序索引（non-unique ordered indices）中的范围 `insert`，以保留等价元素的插入顺序（issue [\#68](https://github.com/boostorg/multi_index/issues/68)）。

  - 序列化现在使用 `std::size_t` 而非 `unsigned long` 来保存与加载 `multi_index_container` 的大小（在 LLP64 数据模型中 `unsigned long` 小于 `std::size_t`）。为反映此变更，`multi_index_container` 序列化的[类版本号](/libs/serialization/doc/tutorial.html#versioning)从 3 提升到 4。

- [Multiprecision](/libs/multiprecision/)（任意精度算术库）：

  - 修复有理数适配器（rational adapter）除法的缺陷（[542](https://github.com/boostorg/multiprecision/pull/542)）。

  - 修复多线程环境下全局精度（precision）变更的处理（[552](https://github.com/boostorg/multiprecision/pull/552)）。

  - 修复 `cpp_int::eval_convert_to` 的 `noexcept` 规范（[555](https://github.com/boostorg/multiprecision/pull/555)）。

- [MySQL](/libs/mysql/)（MySQL 客户端库）：

  - **重大更新。**

  - 现已完整支持存储过程，包括产生数据的 `SELECT` 语句以及带 `OUT` 参数的过程。

  - 新增对多查询（multi-query）的支持，允许通过一次调用运行多条以分号分隔的语句。

  - 新增静态类型接口，可使用 [Boost.Describe](/libs/describe/) 结构体与元组（tuple）将查询结果解析到用户提供的类型。

  - 文本查询与预处理语句现在可通过新的 `connection::execute` 与 `connection::start_execution` 函数（及其异步对应版本）执行。这些新函数取代 `connection::query`、`connection::execute_statement`、`connection::start_query` 与 `connection::start_statement_execution`。新函数允许使用诸如静态接口等新特性。

  - 新增分离编译（separate compilation）模式以帮助缩短构建时间。源代码包含于 `boost/mysql/src.hpp`，该头文件必须且只能在一个翻译单元（translation unit）中包含。

  - 预处理语句现在可使用迭代器对指定参数，配合 `statement::bind` 与 `connection::execute` 执行。这使参数数量与类型在编译期未知的用例成为可能。

  - 预处理语句执行现在接受 `bool`、`std::optional` 与 `boost::optional` 类型的参数。

  - 新增错误码，并验证了与 MySQL v8.0.33 和 MariaDB v11.0 的兼容性。

  - 修复 Windows `min()` 与 `max()` 宏导致的潜在问题。

  - 所有断言现均使用 [Boost.Assert](/libs/assert/)。

  - 所有异常现均通过 [Boost.ThrowException](/libs/throw_exception/) 抛出。

  - 立即完成（immediate completion）现在通过 I/O 对象的执行器（executor）正确分发。

- [Ratio](/libs/ratio/)（编译期分数运算库）：

  - 将默认 `BOOST_RATIO_VERSION` 改为 2。

  - 对 `BOOST_RATIO_EXTENSIONS` 的支持现已弃用，并将在 Boost.Ratio 基于标准 `<ratio>` 头文件实现后最终移除。

- [Test](/libs/test/)（单元测试框架库）：

  - 在 CI（持续集成）系统中添加更多较旧平台（例如 GCC 4.6）。

  - 修复 `uintptr_t` 的处理，确保其在 32 位系统上可移植（[353](https://github.com/boostorg/test/pull/353)）。

  - 修复来自 `-Wdeprecated-copy-dtor` 与 `-Wdeprecated-copy-with-user-provided-dtor` 的警告（[375](https://github.com/boostorg/test/pull/375)）。

  - 修复 C++23 `<stdfloat>` 类型下 `check_is_close` 的处理（[382](https://github.com/boostorg/test/pull/382)）。

- [Timer](/libs/timer/)（简易计时器库）：

  - 移除对 Boost.Chrono、Boost.System 等库的依赖。

  - 禁用已弃用的头文件，除非定义了 `BOOST_TIMER_ENABLE_DEPRECATED`。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - **重大更新。**

  - 新增 `boost::concurrent_flat_map`，一个基于开放寻址（open addressing）的快速、线程安全哈希映射。

  - 加速开放寻址容器的遍历。

  - 在开放寻址容器中，`erase(iterator)` 此前不返回任何值，现在返回可转换为指向下一元素迭代器的代理（proxy）对象。这使得典型的 `it = c.erase(it)` 写法成为可能，且当返回的代理未被使用时不会带来任何性能损失。

- [URL](/libs/url/)（URL 解析库）：

  - `parse_query` 不再重新创建 `string_view`（[\#757](https://github.com/boostorg/url/issues/757)）。

  - `url_view`/`string_view` 构造函数要求实参不是 `url_view_base`（[\#756](https://github.com/boostorg/url/issues/756)）。

  - `IP-literal` 可以是 `IPv6addrz`（[\#711](https://github.com/boostorg/url/issues/711)）。

- [UUID](/libs/uuid/)（UUID 生成与解析库）：

  - 改进了 AVX 目标上生成的 x86 代码。移除了在 SSE3 目标上对 `lddqu` 指令的使用——该指令会拖累 Intel NetBurst CPU 的性能，但在 Skylake 及更新的 CPU 上更为高效（[PR#138](https://github.com/boostorg/uuid/pull/138)）。

- [Variant2](/libs/variant2/)（Variant 的现代重实现库）：

  - 新增 `uses_double_storage()`。

## 更新的工具（Updated Tools）

- [Build](/tools/build/)（Boost.Build 构建系统框架）：

  - 包含 [B2 version 4.10.1](/tools/build/doc/html/#_version_4_10_1) 的发布。

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
