# Boost 1.44.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_44_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_44_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2010-08-13 17:00 GMT（原文日期行：August 13th, 2010 17:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Meta State Machine（有限状态机库，MSM）：高性能、表达力强的 UML2 有限状态机，作者 Christophe Henry。
- Polygon（多边形布尔运算库）：面向整数坐标平面多边形的布尔/裁剪、缩放/偏移等运算，作者 Lucanus Simonson。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Filesystem（可移植文件系统操作库）——破坏性升级预告：本版同时包含 Version 2 与 Version 3；V3 为大版本升级，会破坏部分既有用户代码，故 V2 仍为默认版本，鼓励用户迁移至 V3。
- Iostreams（流/设备抽象框架库）——破坏性变更：`file_descriptor`、`file_descriptor_source`、`file_descriptor_sink` 的构造函数与 `open` 方法变更；定义宏 `BOOST_IOSTREAMS_USE_DEPRECATED` 可继续使用旧方法（\#3323、\#3517、\#4335）。
- System（错误码与 system_error 库）——破坏性变更：为符合 C++0x FCD，`system_category` 与 `generic_category` 改为函数；引用处需加 "()" 使之成为函数调用，否则部分用户代码将编译失败。
- Proto（表达式模板/DSL 构建库）——行为微调（三处）：`proto::and_` 作为 transform 时应用全部变换但仅返回最后一个结果；`proto::as_expr`/`as_child` 不再对已是 Proto 表达式的对象经过域 generator；在可能处改用 `proto::basic_expr` 以缩短编译时间（细节见 Proto 发布说明）。
- Asio（网络与底层 I/O 库）——编译影响：为缩短编译时间做了拆分，部分程序可能需补加头文件（如使用 `boost::array` 但未显式包含 `<boost/array.hpp>` 的程序）。

另有 18 项常规缺陷修复与改进（Accumulators、Config、Foreach、Fusion、Hash、Math、MPL、MultiIndex、Regex、Spirit、Thread、TR1、TypeTraits、uBLAS、Utility、Uuid、Wave、Xpressive 等库），见英文原文存档。
