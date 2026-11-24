# Boost 1.42.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_42_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_42_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2010-02-02 14:00 GMT（原文日期行：February 2nd, 2010 14:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Uuid（UUID 生成与解析库）：通用唯一标识符，作者 Andy Tompkins。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Graph（图结构与算法库）——移除：删除 `compressed_sparse_row_graph` 的旧接口，新接口成为默认。
- PropertyMap（属性映射概念库）——移除：删除 boost/ 目录直下自 1.40 起弃用的旧头文件，改由 `boost/property_map/` 下头文件提供。
- Integer（整数类型选择库）——API 变更：`boost::static_signed_min` 等的参数类型与结果类型改为 typedef（此前硬编码为 `unsigned long` 与 `int`），新代码应使用所提供的 typedef，旧代码请尽快更新。
- ProgramOptions（命令行/配置文件选项解析库）——默认行为变更：不再从字符串值中剥离引号（\#850）。

另有 9 项常规缺陷修复与改进（Asio、CircularBuffer、Fusion、Iostreams、Proto、Regex、Spirit、Unordered、Xpressive 等库），见英文原文存档。
