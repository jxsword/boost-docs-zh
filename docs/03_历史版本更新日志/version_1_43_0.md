# Boost 1.43.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_43_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_43_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2010-05-06 12:00 GMT（原文日期行：May 6th, 2010 12:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Functional/factory（工厂函数对象库）：动态构造与按值构造的函数对象，作者 Tobias Schwinger。
- Functional/forward（转发适配器库）：解决转发问题的函数对象适配器，作者 Tobias Schwinger。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Range（范围抽象库）——重大更新：合入刚通过正式评审（Formal Review）的 Boost.RangeEx 的全部特性（作者 Neil Groves），包括：全套 STL 迭代器算法的范围版本；可与范围算法组合、表达力空前的范围适配器（range adaptors）；新函数 irange、istream_range、join、combine。
- Random（随机数生成器与分布库）——首次要求编译：`random_device` 的实现移入需编译库（compiled library），并新增 Windows 支持。
- MultiIndex（多索引容器库）——序列化兼容性：经用户提供的 `save_construct_data`/`load_construct_data` 设施正确支持非默认可构造值的序列化；`multi_index_container` 的序列化类版本号由 1 升至 2。
- Asio（网络与底层 I/O 库）——弃用：resolver 实现不再要求 `InternetProtocol::resolver_query` 与 `InternetProtocol::resolver_iterator` typedef（二者不属于已文档化的要求），`ip::tcp`、`ip::udp`、`ip::icmp` 中的对应 typedef 弃用。
- Unordered（无序关联容器库）——更名：`erase_return_void` 更名为 `quick_erase`（\#3966）。
- 构建系统：Windows 上 gcc（mingw 与 cygwin）的 DLL 与导入库命名改为符合环境默认约定（此前与其他 Windows 编译器相同）。

另有 10 项常规缺陷修复与改进（Accumulators、Array、Fusion、Iostreams、Proto、Spirit、Thread、Uuid、Wave、Xpressive 等库；Asio 另有多项性能与平台适配改进），见英文原文存档。
