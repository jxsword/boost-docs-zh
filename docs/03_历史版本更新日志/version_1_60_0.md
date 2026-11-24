# Boost 1.60.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_60_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_60_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2015-12-17 15:52 GMT（原文日期行：December 17th, 2015 15:52 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- VMD（可变宏数据库）：可变宏数据（Variadic Macro Data）库，作者 Edward Diener。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Atomic（原子操作库）——ABI 相关变更：强制 `atomic<>` 存储正确对齐，修复在支持大于机器字长原子操作的平台上的潜在问题；可能改变含 `atomic<>` 成员的用户数据结构的二进制布局。
- Container（扩展容器库）——重大新特性：实现多态内存资源（Polymorphic Memory Resources）；`basic_string` 新增 C++11 `back`/`front` 操作。
- Filesystem（可移植文件系统操作库）——重大新特性（对齐 Filesystem 技术规范 TS）：新增 `lexically_normal`、`lexically_relative`、`relative`、`weakly_canonical`；`path` 新增反向迭代器类型与 `rbegin()`/`rend()`、`size()`；编译器支持时按 TS 提供 C++11 `noexcept` 与移动构造/赋值；在 TS 中改名的既有函数同时支持新旧名称。
- Fusion（异构容器与算法库）——标准要求相关：全部容器与生成器支持 C++11 变参模板；因实现限制，编号形式 `fusion::vectorN` 在 C++11 起经由别名模板提供并弃用（部分特化可能编译出错，可通过 `BOOST_FUSION_HAS_VARIADIC_VECTOR` 检查并切换用法）；`fusion::fold` SFINAE 友好。
- Log（日志库）——配置变更：Windows 上配置宏 `BOOST_LOG_USE_WINNT6_API` 不再被库使用，目标 Windows 版本改由 `BOOST_USE_WINAPI_VERSION` 配置。
- Thread（可移植线程库，4.6.0）——实验性新特性：新增 `shared_timed_mutex` 作为 `shared_mutex` 的替代名称，并弃用将 `shared_mutex` 当作定时互斥量的用法；`future::then` 支持更多启动策略（executor、inherit）。
- Predef（编译器/架构/OS 预定义宏库）——新增 SIMD 硬件检测。

另有 22 项常规缺陷修复与改进（Chrono、Context、Core、Flyweight、Geometry、Interprocess、Intrusive、LexicalCast、Locale、Move、MultiIndex、odeint（常微分方程求解库）、Optional、Test 等库），见英文原文存档。
