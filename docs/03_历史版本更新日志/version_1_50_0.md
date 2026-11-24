# Boost 1.50.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_50_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_50_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2012-06-28 12:48 GMT（原文日期行：June 28th, 2012 12:48 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Algorithm（通用算法集合库）：一组实用的泛型算法，含多种搜索算法与 C++11 标准库的大多数新算法，作者 Marshall Clow。
- Functional/OverloadedFunction（函数重载合并库）：将多个不同函数重载为单个函数对象，作者 Lorenzo Caminiti。
- LocalFunction（局部函数库）：在其他函数内部、所需作用域处直接定义局部函数，作者 Lorenzo Caminiti。
- Utility/IdentityType（宏参数类型包裹库）：用圆括号包裹类型，使其总能作为宏参数传递，作者 Lorenzo Caminiti。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- 安全补丁（Patches 栏）：Locale（本地化与 Unicode 文本处理库）补丁——修复 `boost::locale::utf::utf_traits` 接受部分非法 UTF-8 序列的安全缺陷；Unordered（无序关联容器库）补丁——修复 C++11 编译器搭配 C++03 分配器时插入元素误判可隐式转换构造节点导致的缺陷。
- Filesystem（可移植文件系统操作库）——移除：从发行包中移除 Filesystem Version 2，Version 3 成为唯一发行版本，仍在使用 V2 的用户应尽快迁移。
- Thread（可移植线程库）——破坏性变更：joinable 的 thread 析构函数应调用 terminate（\#6266）；thread 移动赋值在 joinable 时应调用 terminate（\#6269）。
- MSM（有限状态机库）——破坏性变更：以 eUML 定义、仅含转换表的前端改用更优语法，属破坏性变更（详见库文档 eUML-composite-table 一节）。
- Locale（本地化与 Unicode 文本处理库）——依赖变更：Boost.System 成为必需依赖。

另有 23 项常规缺陷修复与改进（Accumulators、Array、Asio、Bimap、Chrono、Concept Check、Foreach、Geometry、Graph、Hash、Iostreams、Iterator、MultiArray、LexicalCast、Math、ProgramOptions、PropertyMap、Proto、Ratio、ScopeExit、Unordered、Wave、xpressive 等库），见英文原文存档。
