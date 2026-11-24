# Boost 1.38.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_38_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_38_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2009-02-08 12:00 GMT（原文日期行：February 8th, 2009 12:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Flyweight（享元模式库）：管理大量高度冗余对象的设计模式实现，作者 Joaquín M López Muñoz。
- ScopeExit（作用域退出执行库）：在作用域退出时执行任意代码，作者 Alexander Nasonov。
- Swap（标准化 swap 实现库）：增强的泛型 swap 函数，作者 Joseph Gauterin。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Regex（正则表达式库）——破坏性变更：Perl 正则语法下现在允许空表达式与空分支（\#1081）；设置新的 `syntax_option_type` no_empty_expressions 可恢复旧行为（禁止空表达式）。
- Xpressive（可内嵌表达式的正则库）——移除：移植至 Proto v4，`boost/xpressive/proto` 下的 Proto v2 已被移除。
- Thread（可移植线程库）——默认行为变更：不再在线程内捕获未处理异常（以便调试器定位未处理异常的成因）；未处理异常仍将导致应用程序终止。
- MultiIndex（多索引容器库）——弃用：部分冗余的 typedef 弃用（详见库发布说明）。
- Hash（哈希函数库）——弃用：`boost/functional/detail/container_fwd.hpp` 移至 `boost/detail/container_fwd.hpp`，原位置弃用。
- 其他变更：本版引入使用 CMake（构建系统）构建 Boost 的实验性支持。

另有 16 项常规缺陷修复与改进（Accumulators、Any、Asio、Config、DateTime、Exception、Filesystem、Graph、Interprocess、Intrusive、LexicalCast、Math、Proto、TR1、TypeTraits、Unordered 等库），见英文原文存档。
