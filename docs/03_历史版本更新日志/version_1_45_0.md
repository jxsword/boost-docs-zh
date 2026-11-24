# Boost 1.45.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_45_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_45_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2010-11-19 16:00 GMT（原文日期行：November 19th, 2010 16:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

本版无新增库。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Asio（网络与底层 I/O 库）——弃用：分离编译头 `<boost/asio/impl/src.cpp>` 弃用，改用 `<boost/asio/impl/src.hpp>`（\#4560）。
- Interprocess（进程间通信库）——重大新特性与平台行为变化：支持标准右值引用移动语义（GCC 4.5 与 VC10 实测）；进程间命名资源可详细指定权限；`mapped_region::flush` 仅发起磁盘刷新、不保证返回时已完成（可移植性限制）；FreeBSD 与 MacOS 改用 POSIX 信号量实现命名信号量与互斥量。

另有 15 项常规缺陷修复与改进（Config、Flyweight、Foreach、Fusion、Graph、Math、MSM、MultiArray、Proto、Spirit、TypeTraits、uBLAS、Unordered、Wave、Xpressive 等库），见英文原文存档。
