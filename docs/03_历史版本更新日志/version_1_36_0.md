# Boost 1.36.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_36_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_36_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2008-08-14 12:00 GMT（原文日期行：August 14th, 2008 12:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Accumulators（增量统计累加器框架库）：增量计算框架与统计累加器集合，作者 Eric Niebler。
- Exception（增强异常库）：在异常对象中携带任意数据、以及跨线程传送异常的库，作者 Emil Dotchevski。
- Units（量纲系统库）：零开销的量纲分析与单位/数量操作及转换，作者 Matthias Schabel 与 Steven Watanabe。
- Unordered（无序关联容器库）：无序关联容器，作者 Daniel James。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Wave（C/C++ 预处理器实现库）——破坏性变更：Wave V2.0 大版本发布，引入破坏性 API 变更，不再能用于 1.36.0 之前的 Boost 版本；主要是 API 与 hook 接口为一致性而精简。
- CircularBuffer（环形缓冲区库）——默认行为变更：默认构造函数不再分配内存，并将缓冲区容量置为 0。
- Asio（网络与底层 I/O 库）——重大新特性：新增串口、UNIX 域套接字、raw socket 与 ICMP 支持；POSIX 流式文件描述符与 Windows 流式/随机访问 HANDLE 封装；以 `null_buffers` 实现 reactor 风格（只报告就绪不执行 I/O）操作；缓冲区序列逐字节遍历迭代器；`read_until()`/`async_read_until()` 支持自定义消息边界判定函数对象等。

另有 13 项常规缺陷修复与改进（Assign、Foreach、Function、Hash、Interprocess、Intrusive、Math、MPI、MultiIndex、PtrContainer、Spirit、Thread、Xpressive 等库，含 win32 条件变量严重缺陷修复），见英文原文存档。
