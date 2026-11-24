# Boost 1.49.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_49_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_49_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2012-02-24 21:20 GMT（原文日期行：February 24th, 2012 21:20 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Heap（优先队列家族库）：优先队列数据结构，作者 Tim Blechmann。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- 安全补丁（Patches 栏）：Locale（本地化与 Unicode 文本处理库）补丁——修复 `boost::locale::utf::utf_traits` 接受部分非法 UTF-8 序列的安全缺陷。
- Unordered（无序关联容器库）——默认行为变更：在无右值引用的编译器上，容器默认不再可移动（原移动模拟引发若干怪异问题，\#6167、\#6311）；定义宏 `BOOST_UNORDERED_USE_MOVE` 可恢复可移动性（元素仍始终使用 Boost.Move）。
- Asio（网络与底层 I/O 库）——重大新特性：新增基于 C++11 时钟类型要求的类模板 `basic_waitable_timer`（可用 C++11 `<chrono>` 时钟或 Boost.Chrono，并提供 high_resolution_timer、steady_timer、system_timer 三个 typedef）；新增用于等待 Windows 内核对象的 `windows::object_handle` 类。

另有 18 项常规缺陷修复与改进（Chrono、Container、Filesystem、Foreach、Geometry、Graph、Icl、Interprocess、Intrusive、LexicalCast、Locale、Move、PropertyTree、Proto、Spirit、Thread、Uuid、xpressive 等库），见英文原文存档。
