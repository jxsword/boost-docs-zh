# Boost 1.63.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_63_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_63_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2016-12-26 23:43 GMT（原文日期行：December 26th, 2016 23:43 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

本版无新增库。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Fiber（用户态纤程库）——弃用：`unbounded_channel` 与 `bounded_channel` 标记为弃用，由新类 `buffered_channel`/`unbuffered_channel` 取代，性能提升。
- Log（日志库）——移除：此前已弃用的 `type_info_wrapper` 被移除。新增 `get_current_file_name` 方法访问文本文件 sink 后端当前日志文件名。
- Test（单元测试框架库，v3.4）——破坏性变更：测试用例名称中出现的冒号替换为下划线。`BOOST_TEST` 的 `per_element`/`lexicographic` 修饰符现也可用于字符串比较。
- Python（Python 绑定库）——重大新特性：新增（基础）C++11 支持（`std::shared_ptr`、`std::unique_ptr`）；引入包装 NumPy 的扩展 API；清理过时内容。
- TypeIndex（类型信息库）——新增 `runtime_cast`（`dynamic_cast` 的模拟实现）。
- Fusion（异构容器与算法库）——`BOOST_FUSION_ADAPT*`/`BOOST_FUSION_DEFINE*` 允许空结构体并支持移动构造与赋值；新增 `std::array` 适配器。
- Metaparse——`BOOST_METAPARSE_STRING` 最大字符串长度提升至 2048，可通过库自带脚本进一步扩展，且可在编译单元内修改长度限制。
- 发布后补丁（Post-release Patches 栏）：Atomic（原子操作库）——在 32 位 x86 上使用 gcc 4.7 之前版本时，64 位原子操作可能生成错误代码，已通过提交修复。

另有 20 项常规缺陷修复与改进（Container、Context、Geometry、Hash、Interprocess、Intrusive、LexicalCast、Move、Optional、Phoenix、Units、Unordered 等库），见英文原文存档。
