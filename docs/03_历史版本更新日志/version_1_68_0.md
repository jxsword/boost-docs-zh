# Boost 1.68.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_68_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_68_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2018-08-09 03:46 GMT（原文日期行：August 9th, 2018 03:46 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- YAP（表达式模板库）：面向 C++14 及以上的表达式模板库，作者 Zach Laine。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Windows 用户须知——默认行为变更：Boost.WinAPI（Win32 API 薄封装库）默认目标版本从 Windows Vista 提升为 Windows 7（在可能处生效）；Beast、Chrono、DateTime、Dll、Log、Process、Stacktrace、System、Thread、UUID 等库内部以它为 Windows SDK 抽象层，可用 `BOOST_USE_WINAPI_VERSION` 宏指定目标版本。
- GIL（通用图像库）——标准要求变更：现在要求符合 C++11 的编译器。IO 扩展整体重写为 IO v2（IO v1 移除）；新增顶层总头文件 `boost/gil.hpp` 与 Toolbox 扩展。
- Signals（信号槽库，旧版）——移除预告：Signals 将在下一版本移除（1.54.0 已弃用），应立即迁移到 Signals2（线程安全信号槽库）以避免中断。
- Fiber（用户态纤程库）——NUMA 支持移入附加库 fiber-numa，通过 `numa=on` 属性启用。
- Uuid（UUID 生成与解析库）——破坏性变更：移除为向后兼容保留的 sha1 detail 命名空间头文件重定向。新增 std::hash 支持、随机生成器移动语义。
- Test（单元测试框架库）——破坏性变更：`master_test_suite_t` 对象不再可拷贝。
- Geometry（几何算法库）——面积（area）策略接口变更（潜在破坏性变更）；球形与地理坐标系统新增 Point-Box、Box-Box 距离策略与 nadgrids 网格平移支持。
- Multiprecision（任意精度算术库）——行为变更：转换到无符号整数类型改为截断，与标准定义行为一致。新增复数多精度数支持与 Eigen 互操作性。
- Optional（可选值容器库）——新增 `has_value()`、`map()`、`flat_map()` 成员函数，向 `std::optional` 看齐。

另有 25 项常规缺陷修复与改进（Beast、Context、Coroutine2、Fusion、Graph、LexicalCast、Log、Math、MultiIndex、Predef、ProgramOptions、Rational、System、Spirit、Stacktrace、TypeIndex 等库），见英文原文存档。
