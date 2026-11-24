# Boost 1.70.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_70_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_70_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2019-04-12 06:04 GMT（原文日期行：April 12th, 2019 06:04 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Outcome（函数失败报告与处理库）：在不适合直接使用 C++ 异常处理的场景中报告与处理函数失败的一组工具，作者 Niall Douglas。
- Histogram（多维直方图库）：面向 C++14 的快速、可扩展多维直方图库，接口便捷，作者 Hans Dembinski。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Beast（HTTP/WebSocket 网络库）——重大更新：部分 API 有变更。新增 `basic_stream`/`tcp_stream`（异步操作内建超时，超时以 `error::timeout` 完成；支持 `simple`/`unlimited` 及用户自定义 RatePolicy 流量整形策略）、`async_base`/`stable_async_base` 组合操作基类、可移动可赋值的 `ssl_stream`；全部异步操作改用 Asio 的 `async_initiate` 以高效接入协程 TS；定义 `BOOST_BEAST_SEPARATE_COMPILATION` 并包含 `<boost/beast/src.hpp>` 可显著加速编译。
- Asio（网络与底层 I/O 库）——重大新特性：I/O 对象（如 socket）支持自定义 I/O executor；新增带 `initiate` 静态成员函数的 `async_result` 新形式；协程 TS 支持更新并提升到 `asio` 命名空间；新增可拷贝构造的 `DynamicBuffer_v2` 概念、简化自定义异步操作实现的 `async_compose`、`make_strand` 辅助函数。
- DLL（动态库加载库）——新增宏 `BOOST_DLL_USE_STD_FS`，定义为 1 时改用 C++17 的 `std::filesystem::path`、`std::system_error` 与 `std::error_code`；注意异常类型由 `boost::system::system_error` 变为 `std::system_error`，需相应更新 `catch` 语句。动态库加载检测与装饰逻辑大幅重写，新增 `shared_library::decorate()`。
- Test（单元测试框架库）——破坏性变更：`minimal.hpp` 开始显示弃用警告；浮点比较逻辑变更可能导致此前静默未走浮点比较的测试失败；`unit_test_log_formatter` 内部 API 变更。新特性：`BOOST_TEST(3.0001 == 3)` 之类的表达式也走浮点比较、新增 `BOOST_TEST_INFO_SCOPE`、移除对 Timer 的依赖。
- Spirit（解析器/生成器框架库）——X3 移除：sequence into plain 解析改为触发编译期错误（不再静默取最后一个值）；移除从未正常工作的 1.0#INF 解析器；移除未公开的 `make_attribute` 特征（Qi 中并入 `transform_attribute`）。
- 已知问题（Known Issues 栏）：发布后补丁——修复 Beast 组合操作中 executor 被移走后空闲 ping 超时问题（\#1599）。

另有 22 项常规缺陷修复与改进（Context、Coroutine2、DynamicBitset、Fiber、Filesystem、Integer、Log、Math、Mp11、MultiIndex、Multiprecision、PolyCollection、Stacktrace、TypeIndex、TypeTraits、Variant、uBLAS 等库），见英文原文存档。
