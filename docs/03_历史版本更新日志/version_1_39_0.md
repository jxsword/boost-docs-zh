# Boost 1.39.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_39_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_39_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2009-05-02 12:00 GMT（原文日期行：May 2nd, 2009 12:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Signals2（线程安全信号槽库）：托管的信号与槽回调实现（线程安全的第 2 版），作者 Frank Mori Hess。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Hash（哈希函数库）——移除：删除用于哈希容器的弃用头文件，其内容已并入 `<functional/hash.hpp>`（\#2412）。

另有 11 项常规缺陷修复与改进（含 Flyweight 享元库引用计数组件的线程安全死锁修复；Asio、Foreach、Interprocess、Intrusive、ProgramOptions、Proto、PtrContainer、Range、Unordered、Xpressive 等库），见英文原文存档。
