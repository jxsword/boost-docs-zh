# Boost 1.54.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_54_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_54_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2013-07-01 17:10 GMT（原文日期行：July 1st, 2013 17:10 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Log（日志库）：日志库，作者 Andrey Semashev。
- TTI（类型特征内省库）：类型特征内省（Type Traits Introspection）库，作者 Edward Diener。
- TypeErasure（运行期多态概念库）：基于概念（concept）的运行期多态。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- 平台/构建要求（News 栏）——不再支持 80386 目标 CPU，x86 32 位最低目标为 i486（SmartPtr 与 Atomic（原子操作库）及其内部使用者此前就未正确支持 80386）；x86 32 位默认按 i686（Pentium Pro）及以后编译，可用 b2/bjam 命令行的 `instruction-set` 属性调整（如 `b2 variant=release architecture=x86 instruction-set=i486 stage`）。
- Signals（信号槽库，旧版）——弃用：不再积极维护，新开发请使用 Signals2（线程安全信号槽库）；既有 Signals 代码仍可工作，Signals2 文档附有移植指南。
- Algorithm（通用算法集合库）——接口变更：`copy_while`/`copy_until` 返回类型改为 `std::pair<InputIterator, OutputIterator>`（使用返回值的代码需在调用后加 `.second`）；新增 `is_permutation`、`equal`、`mismatch` 的 C++14 版本。
- Interprocess（进程间通信库）——ABI 破坏性变更：Windows 上 bootstamp 函数改用 EventLog 服务启动时间作为系统启动时间（原 WMI `LastBootupTime` 因时间同步与休眠而不稳定、实际不可用）；如需 1.54 之前的行为，定义 `BOOST_INTERPROCESS_BOOTSTAMP_IS_LASTBOOTUPTIME`。
- Multiprecision（任意精度算术库）——破坏性变更：`rational_adapter` 更名为 `rational_adaptor`。新增 MPFI 支持、`logged_adaptor`、经 GCC `__float128` 或 Intel `_Quad` 的 128 位浮点支持、cpp_int 用户自定义字面量与 `constexpr` 改进。
- Asio（网络与底层 I/O 库）——重大新特性：新增 `handler_type`/`async_result` 特征类（自定义发起函数返回类型）、`asio::spawn()`（基于 Coroutine（协程库）的栈式协程高层封装，可同步风格写异步逻辑）、`asio::use_future`（从异步操作返回 C++11 `std::future`）、generic 协议类（运行期指定地址族与协议类型）、TLS v1.1/1.2 支持；默认行为变更：`ssl::context` 默认自动禁用 SSL 压缩。
- LexicalCast（字符串↔数值等类型转换库）——行为变更：转换到字符指针现在触发编译期断言（原为运行期检查）；支持 `boost::int128_type`/`boost::uint128_type`。
- Thread（可移植线程库）——C++11 兼容新特性：`call_once` 可传递可移动参数、新增 `future<>.then`（延续）与 synchronized value 类。
- Math（数学特殊函数与统计分布库）——重大重组：纳入整数工具（最大公约数/最小公倍数）、四元数与八元数等类目，新增 Bessel 函数求零点等。

另有 31 项常规缺陷修复与改进（Accumulators、Any、Chrono、CircularBuffer、Container、Context、Coroutine、Geometry、Graph、Intrusive、Iostreams、MSM（有限状态机库）、Move、Polygon、PropertyMap、Range、TypeTraits、uBLAS、Unordered、Utility、Variant、Wave、xpressive 等库），见英文原文存档。
