# Boost 1.48.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_48_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_48_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2011-11-15 15:47 GMT（原文日期行：November 15th, 2011 15:47 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Container（扩展容器库）：标准库容器及扩展容器，作者 Ion Gaztañaga。
- Locale（本地化与 Unicode 文本处理库）：为 C++ 提供本地化与 Unicode 处理工具，作者 Artyom Beilis。
- Move（移动语义辅助库）：面向 C++03 与 C++11 编译器的可移植移动语义，作者 Ion Gaztañaga。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- 安全补丁（Patches 栏）：Locale 补丁——修复 `boost::locale::utf::utf_traits` 接受部分非法 UTF-8 序列的安全缺陷。
- Proto（表达式模板/DSL 构建库）——破坏性变更：在支持右值引用的编译器上以右值引用减少运算符重载数量；在 Proto 表达式上定义了额外运算符重载的用户代码可能因此产生歧义，解决办法是用 grammar 禁用 Proto 中与用户自定义运算符冲突的重载。
- Unordered（无序关联容器库）——破坏性变更：改进 C++11 标准支持，equality 与 emplace 行为有破坏性变更（细节见库变更日志）。
- MSM（有限状态机库）——破坏性变更：新增内部转换表特性导致一处小破坏——子机中以 internal_transition_table 声明的内部表的守卫/动作的 "Fsm" 模板参数现在是最内层包含该转换的状态机（子机本身），而非高层状态机。

另有 15 项常规缺陷修复与改进（Asio、Chrono、Config、Fusion、Geometry、Graph、Interprocess、Intrusive、LexicalCast、Math、Numeric.Conversion、Regex、Spirit、TypeTraits、Wave 等库），见英文原文存档。
