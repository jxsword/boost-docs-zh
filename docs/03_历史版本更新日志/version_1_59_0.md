# Boost 1.59.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_59_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_59_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2015-08-13 15:23 GMT（原文日期行：August 13th, 2015 15:23 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Convert（可扩展类型转换框架库）：可扩展、可配置的类型转换框架，作者 Vladimir Batov。
- Coroutine2（协程库，栈式）：C++14 协程库，作者 Oliver Kowalke。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- PropertyTree（属性树库）——破坏性变更：全新支持完整 Unicode 的 JSON 解析器；新解析器不支持 JSON 文件中的注释与字符串拼接（旧解析器的非标准扩展），依赖这些特性的代码可能失效。
- Log（日志库）——破坏性变更：底层类型信息管理改用 Boost.TypeIndex（类型信息库）——`invalid_type` 异常现携带 `typeindex::type_index` 描述问题类型（原为 `type_info_wrapper`）；`attribute_value::get_type()` 返回 `typeindex::type_index`，自定义属性值实现需相应修改；`type_info_wrapper` 弃用并将在未来版本移除；移除此前已弃用的三个头文件（`intrusive_ref_counter.hpp`、`explicit_operator_bool.hpp`、`empty_deleter.hpp`）；支持符号可见性的系统（如 Linux）上构建时隐藏全部内部符号。
- Geometry（几何算法库）——破坏性变更：buffer 的 side strategy 现返回 `error_code` 而非 bool，自定义 side strategy 需适配。重大新特性：新增 `relate()`/`relation()` 算法、`is_empty` 算法、rtree `const_iterator` 与 Boost.Range 支持、几何模型支持 C++11 `std::initializer_list`。
- Test（单元测试框架库，v3）——重大新特性：`BOOST_TEST` 泛型断言、数据驱动测试用例、测试单元属性（逻辑分组、依赖、启用/禁用）、CLI 新增 `colour_output`/`list_content` 与扩展过滤（取反、标签）；文档用 QuickBook 重写。
- 已知问题（Known Issue 栏）：Log 存在回归导致部分日志语句无法编译（\#11549），已在 git 修复。
- Intrusive（侵入式容器库）——重大新特性：实现 map/multimap 风格接口；重构哈希容器以减少模板实例化。
- MultiIndex（多索引容器库）——重大新特性：新增 ranked indices（排序索引）。

另有 17 项常规缺陷修复与改进（Container、Context、Coroutine、Fusion、Interprocess、LexicalCast、Move、Predef、ProgramOptions、TypeIndex、Variant 等库），见英文原文存档。
