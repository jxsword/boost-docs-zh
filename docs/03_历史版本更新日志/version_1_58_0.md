# Boost 1.58.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_58_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_58_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2015-04-17 07:53 GMT（原文日期行：April 17th, 2015 07:53 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Endian（字节序处理库）：不论处理器字节序如何，均能正确进行字节序处理与转换的类型与转换函数。
- Sort（排序库）：含 spreadsort——一种快于 O(n*log(n)) 的通用混合基数排序。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Container（扩展容器库）——源码破坏性变更：`scoped_allocator_adaptor` 的 `propagate_on_container_copy_assignment`、`propagate_on_container_move_assignment` 与 `propagate_on_container_swap` 不再是 `boost::integral_constant<bool, true/false>` 类型（依赖重组需要放弃这些类，且与 `std::integral_constant` 的互操作无保证），假定 `boost::true_type`/`boost::false_type` 的代码将无法编译（可用内部 `::value` 常量作替代）。重大新特性：引入实验性 `small_vector` 容器；大规模依赖重组（现仅依赖 Core、Intrusive 等基础工具，预处理代码量明显减少、编译时间改善）。
- Variant（非递归可辨识联合库）——破坏性变更：`boost::get<U>(VariantT)` 与 `boost::polymorphic_get<U>(VariantT)` 默认改用编译期检查的 getter（断言 `U` 是 `VariantT` 可存储的类型之一）；定义 `BOOST_VARIANT_USE_RELAXED_GET_BY_DEFAULT` 可恢复宽松默认行为。
- Functional/Factory——轻微破坏性变更：指示不使用分配器的默认模板参数由 `boost::none_t` 改为 `void`。
- Optional（可选值容器库）——行为变更：`boost::none_t` 不再可从字面量 0 转换（避免 `optional<rational<int>> oi = 0;` 误初始化为空值）；`U` 不可赋值/转换到 `T` 时不再允许 `optional<U>` 赋值给 `optional<T>`。
- 已知问题（Known Issue 栏）：Python（Python 绑定库）针对 3.0–3.3 版本构建失败（2.X 与 3.4+ 不受影响，git 已修复并附补丁）；Fusion（异构容器与算法库）存在非 constexpr 类型回归（\#11211，git 已修复并附补丁）。
- Conversion（类型转换库）——新增 `polymorphic_pointer_downcast` 与 `polymorphic_pointer_cast`；全部函数改用 `boost::throw_exception` 抛异常。
- Flyweight（享元库）——新增 `std::hash` 与 `boost::hash` 支持（可禁用以免与遗留代码冲突）。

另有 30 项常规缺陷修复与改进（Asio、Chrono、Context、DateTime、Function、Fusion、Geometry、Hash、Interprocess、Intrusive、LexicalCast、Log、Math、Move、MultiIndex、Multiprecision、Phoenix、Predef、Random、Thread、TypeErasure、TypeIndex、Units、Unordered 等库），见英文原文存档。
