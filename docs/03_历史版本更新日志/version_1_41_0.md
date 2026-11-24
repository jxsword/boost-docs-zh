# Boost 1.41.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_41_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_41_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2009-11-17 17:00 GMT（原文日期行：November 17th, 2009 17:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- PropertyTree（属性树库）：尤其适合存储配置数据的树形数据结构，作者 Marcin Kalicinski 与 Sebastian Redl。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Spirit（解析器/生成器框架库）——破坏性变更：新 Spirit V2.1 的首个官方发布（全新的解析、词法分析与输出生成库），与早期版本不向后兼容（已知问题：`qi::symbol::find` 会匹配以所查字符串开头的前缀符号，下版修复）。
- DateTime（日期时间库）——默认行为变更：时间段的默认输出格式改为 "%-%O:%M:%S%F"（原为 "%-%H:%M:%S%F"）；需保留旧行为须在 time IO facet 构造时显式指定格式字符串（\#1861）。
- Thread（可移植线程库）——重大新特性：新增 futures、promises 与 packaged tasks 支持；`boost::thread_specific_ptr` 在大量线程特定对象时更快；部分设施改为仅头文件库（header-only）。
- Python（Python 互操作库）——重大新特性：支持 Python 3（Haoyu Bai 的 Google Summer of Code 项目，导师 Stefan Seefeld）。
- 构建系统（Boost.CMake）：CMake 构建版本已移出主发布，将独立发布且略滞后于主发布，并具备按需产出修补版本的能力。

另有 11 项常规缺陷修复与改进（Filesystem、Iostreams、Math、MultiIndex、Proto、Regex、System、Unordered、Utility、Wave、Xpressive 等库，及 OS X 32+64 位 fat 构建修复），见英文原文存档。
