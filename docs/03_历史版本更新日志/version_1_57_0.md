# Boost 1.57.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_57_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_57_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2014-11-03 21:55 GMT（原文日期行：November 3rd, 2014 21:55 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

本版无新增库。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Asio（网络与底层 I/O 库）——弃用：`asio::strand` 显式标记为弃用，应改用 `asio::io_service::strand`。
- Interprocess（进程间通信库）——移除：自有 `unique_ptr` 被移除，`boost::interprocess::unique_ptr` 现转发到 Move（移动语义辅助库）的通用 `boost::movelib::unique_ptr`（更接近标准 `std::unique_ptr` 且维护更好）。
- Iterator（迭代器构建设施库）——重大变更：库的大部分组件移入 `boost::iterators` 命名空间（为向后兼容仍可从 `boost` 命名空间访问）；迭代器操作符按迭代器类别条件定义；部分内部组件（如 `minimum_category`）公开。
- Any（类型安全的任意类型容器库）——标准要求相关：不再要求 RTTI（使用 TypeIndex（类型信息库）做 RTTI 模拟）。
- LexicalCast（字符串↔数值等类型转换库）——内部重组：库由单一头文件改为多个头文件。
- Flyweight（享元库）——恢复非 explicit 的默认构造函数（1.56 改为 explicit 引入初始化场景的回归）；新增基于 Serialization（序列化框架库）的序列化支持。
- Move（移动语义/emplace 辅助库）——重大新特性：新增 `unique_ptr` 智能指针与 `move_if_noexcept` 工具。
- Thread（可移植线程库）——实验性新特性：泛型锁定算法支持变参模板、新增队列视图（queue views）、`generic_executor_ref`、`make_valid_future`。

另有 25 项常规缺陷修复与改进（CircularBuffer、Config、Container、Coroutine、Geometry、Intrusive、Math、MultiArray、Multiprecision、MultiIndex、Preprocessor、TypeIndex、TypeTraits、Units、Unordered、Utility、uBLAS 等库），见英文原文存档。
