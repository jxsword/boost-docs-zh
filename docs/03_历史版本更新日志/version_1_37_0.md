# Boost 1.37.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_37_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_37_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2008-11-03 12:00 GMT（原文日期行：November 3rd, 2008 12:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Proto（表达式模板/DSL 构建库）：面向领域特定嵌入式语言的表达式模板库与编译器构建工具包，作者 Eric Niebler。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Asio（网络与底层 I/O 库）——重大新特性：同步 read、write、accept、connect 操作现已线程安全（即允许对单个 socket 并发执行同步操作，需 OS 支持）；新增 `windows::overlapped_ptr` 类以配合任意重叠 I/O 函数（如 TransmitFile）；Linux 新版本上改用 eventfd 描述符（替代管道）中断阻塞中的 select/epoll 反应器。
- Unordered（无序关联容器库）——更名：按提案 n2691，带 hint 的 `emplace` 重载更名为 `emplace_hint`。

另有 8 项常规缺陷修复与改进（CircularBuffer、DynamicBitset、Exception、Hash、Interprocess、Intrusive、Math 特殊函数、TypeTraits 等库），见英文原文存档。
