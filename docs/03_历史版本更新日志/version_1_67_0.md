# Boost 1.67.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_67_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_67_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2018-04-14 20:37 GMT（原文日期行：April 14th, 2018 20:37 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Contract（契约式编程库）：C++ 契约式编程库，支持全部契约特性——子契约、类不变式、后置条件（含 old 值与返回值）、前置条件、可自定义断言失败动作（如 terminate 或抛异常）、断言的可选编译与检查等，作者 Lorenzo Caminiti。
- HOF（高阶函数库）：C++ 高阶函数（higher-order functions）库，作者 Paul Fultz II。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Atomic（原子操作库）——破坏性变更：1.66 新增的 `(op)_and_test` 操作语义反转，现在操作结果非零时返回 `true`（与 Boost.Atomic 其他 test 方法及 C++ 标准库一致）；定义 `BOOST_ATOMIC_DETAIL_HIGHLIGHT_OP_AND_TEST` 可对每次使用发警告以定位需更新的代码。C++2a 更新：支持作用域枚举的 C++11 编译器上 `memory_order` 变为作用域枚举（可用 `memory_order::acquire` 等短名，旧常量保留兼容，对应 P0439R0）；实验性支持浮点类型原子操作（对应 P0020R6，可用 `BOOST_ATOMIC_FLOAT/DOUBLE/LONG_DOUBLE_LOCK_FREE` 宏检测无锁属性）。
- Multiprecision（任意精度算术库）——破坏性变更：多精度整数向更窄类型转换时，若值过大（或为负）超出目标类型范围，结果为目标类型的最大（或最小）值（此为既定设计，此前执行不严格）；如确需低 N 位，须先按位掩码。
- Spirit（解析器/生成器框架库）——X3 破坏性变更：移除 `with_context`。
- ContainerHash（哈希库）——自 functional 模块拆出以打破依赖环；头文件移至新位置（旧包含路径仍可用）；新增对 `std::string_view`、`std::optional`、`std::variant`、`std::error_code` 等的支持。
- Python（Python 绑定库）——库名加入所用 Python 版本后缀（如 `boost_python27`、`boost_numpy27`），配合 Boost.Build 修复可在单次构建中为多个 Python 版本构建变体。
- Geometry（几何算法库）——面积（area）策略接口变更（潜在破坏性变更）；rtree 默认分配器改为 `boost::container::new_allocator`；新增 `densify()` 算法与球形/地理 Point-Box、Box-Box 距离策略。
- Locale（本地化与 Unicode 文本处理库）——接口新增 `unique_ptr` 支持（保留 C++03 `auto_ptr` 兼容）；可用 `BOOST_LOCALE_HIDE_AUTO_PTR` 移除 `auto_ptr` 接口以支持 C++17。

另有 32 项常规缺陷修复与改进（Asio、Beast、Context、Core、Coroutine2、DateTime、DLL、Fiber、Filesystem、Fusion、Log、Math、MultiIndex、Optional、Phoenix、PolyCollection、Stacktrace、Test、TypeIndex、TypeTraits、Units、Uuid、Variant 等库），见英文原文存档。
