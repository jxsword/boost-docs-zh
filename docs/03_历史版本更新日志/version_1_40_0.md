# Boost 1.40.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_40_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_40_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2009-08-27 17:00 GMT（原文日期行：August 27th, 2009 17:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

本版无新增库。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Boost.CMake——构建系统重大变化：主发布压缩包中的 CMake 构建已损坏（BROKEN），Boost.CMake 自本版起单独分发（可用版本见 Boost.CMake wiki）。
- Serialization（序列化框架库）——移除：删除弃用头文件 `boost/static_warning.hpp`、`boost/state_saver.hpp`、`boost/smart_cast.hpp`、`boost/pfto.hpp`，请改用 `boost/serialization/` 目录下的等价头文件（\#3062）；内部接口应以 `detail::archive_serializer_map` 取代 `detail::archive_pointer_iserializer`。
- Proto（表达式模板/DSL 构建库）——行为变更：PrimitiveTransforms 更严格遵循 ResultOf 协议（部分无效代码可能因此失效）。
- Graph（图结构与算法库）——重大新特性：合入 Parallel Boost Graph Library，为分布式内存计算机（如集群）提供全套图算法与数据结构。
- PropertyMap（属性映射概念库）——弃用预告：属性映射代码移入 `boost/property_map/` 目录，旧文件暂时转发，boost/ 目录直下的旧文件将于 1.42.0 移除。
- 构建系统：Unix 类环境下库的默认命名改为符合系统约定（不再含各种修饰名）；修复 Cygwin 命名；gcc 64 位编译不再要求显式指定目标架构。

另有 14 项常规缺陷修复与改进（Accumulators、Asio、CircularBuffer、Foreach、Function、Fusion、Hash、Interprocess、Intrusive、MPL、ProgramOptions、Random、Unordered、Xpressive 等库），见英文原文存档。
