# Boost 1.55.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_55_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_55_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2013-11-11 19:50 GMT（原文日期行：November 11th, 2013 19:50 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Predef（编译器/架构/OS 预定义宏库）：从 C/C++/Objective C(+ +) 预定义宏或常见头文件中提取编译器、架构、操作系统、库等版本号信息的库，作者 Rene Rivera。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Config（编译器/平台特性检测库）——破坏性变更：移除对部分老旧编译器的支持，新最低要求为 Digital Mars 8.41、GCC 3.3、Intel 6.0、Visual C++ 7.1（部分 Boost 库可能有更高要求）；Metrowerks CodeWarrior、SunPro 5.7 及更早、Borland C++ Builder 2006 (5.82) 及更早列为下一批移除候选。
- Intrusive（侵入式容器库）——源码破坏性变更：弃用 splay 容器的 `xxx_dont_splay` 函数与 `splay_set_hook`（应改用 `bs_set_hook`），均将在 Boost 1.56 移除。ABI 破坏性变更：修复哈希容器 end 迭代器实现（原指向桶数组末尾之后，与桶数组相邻分配的值会引发严重缺陷，现改为指向桶数组起始）。另实现 SCARY 迭代器并大幅削减模板与调试符号膨胀。
- MultiIndex（多索引容器库）——标准要求相关：大幅提升 C++11 兼容度——`multi_index_container` 高效可移动、支持初始化列表、提供 emplace、支持不可拷贝元素（如 `std::unique_ptr<T>`）、随机访问索引提供 `shrink_to_fit()`；弃用 `member_offset`、`const_mem_fun_explicit`、`mem_fun_explicit`、`composite_key_result_equal_to/less/greater/hash` 等类。
- Graph（图结构与算法库）——不再允许以 `void` 作为捆绑属性类型（此前不可靠，现由静态断言禁止，应改用 `boost::no_property`）；新增 Hawick 回路、边着色、最小费用最大流算法与 `finish_edge` 访问者事件点。
- Visual Studio 2013（VC++ 12）已知缺陷：Serialization（序列化框架库）因缺失 include 无法编译；Unordered/MultiIndex 等库以初始化列表调用重载函数时 VC++ 误报歧义（VC++ 缺陷）；Thread 的 `ex_scoped_thread` 编译失败（\#9333）。
- Log（日志库）——弃用：三个头文件 `boost/log/utility/intrusive_ref_counter.hpp`、`explicit_operator_bool.hpp`、`empty_deleter.hpp` 弃用并将在未来版本移除（内容已移往其他库）。新增 `BOOST_LOG_WITHOUT_DEFAULT_FACTORIES` 配置宏，可显著减小二进制体积。
- LexicalCast（字符串↔数值等类型转换库）——行为变更：`std::bad_alloc` 异常不再被转换为 `boost::bad_lexical_cast`。
- PropertyMap（属性映射概念库）——弃用：将原始指针用作属性映射的做法弃用（在 Visual Studio 上常出问题，Graph 的测试与示例已移除该用法）。
- 发布后补丁（Patches 栏）：Log 的 `dump` 操纵器在启用 AVX2 的 CPU（如 Intel Haswell）上输出不正确，已提供补丁。

另有 38 项常规缺陷修复与改进（Accumulators、Any、Asio、Atomic、Chrono、CircularBuffer、Container、Context、Coroutine、Filesystem、Fusion、Geometry、Hash、Interprocess、Math、Move、MSM（有限状态机库）、Multiprecision、MPI、Phoenix、Polygon、Rational、SmartPtr、Thread、Timer、TypeTraits、Unordered、Utility、Variant、Wave、xpressive 等库），见英文原文存档。
