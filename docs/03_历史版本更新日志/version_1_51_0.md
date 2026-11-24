# Boost 1.51.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_51_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_51_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2012-08-20 23:00 GMT（原文日期行：August 20th, 2012 23:00 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Context（执行上下文库）：上下文切换库，作者 Oliver Kowalke。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- 安全补丁（Patches 栏）：Locale（本地化与 Unicode 文本处理库）补丁——修复 `boost::locale::utf::utf_traits` 接受部分非法 UTF-8 序列的安全缺陷。
- Config（编译器/平台特性检测与配置宏库）——弃用：弃用一批表明 C++11 特性但命名未体现 C++11 的宏，提供命名更规范的新宏并与旧宏一一配对，弃用清单已列入文档。
- Geometry（几何算法库）——破坏性变更：经指针访问的点类型（如 `linestring<my_point*>` 中的 `my_point`）其 traits 特化方式变更：旧版须写 `template<> struct tag<my_point*>`，现由库自行去除指针，应写 `template<> struct tag<my_point>`。

另有 15 项常规缺陷修复与改进（Algorithm、Asio、Chrono、Graph、Hash、LexicalCast、Math、MSM、Proto、Ratio、Regex、Thread、Unordered、Wave、xpressive 等库），见英文原文存档。
