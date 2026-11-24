# Boost 1.56.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_56_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_56_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2014-08-07 16:08 GMT（原文日期行：August 7th, 2014 16:08 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Align（内存对齐库）：内存对齐函数、分配器与适配器，作者 Glen Fernandes。
- Type_Index（类型信息库）：运行期/编译期可拷贝类型信息，作者 Antony Polukhin。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Boost 模块化改造（Modularization 栏）：Boost 版本控制迁移至 git 子模块体系（对用户影响不大，目录结构略有变化）；部分库代码拆分为新模块——Assert（可定制断言宏，维护者 Peter Dimov）、Core（供其他库使用的核心工具，低依赖）、Lexical_Cast（通用字面文本转换）、Throw_Exception（统一的库内异常抛出基础设施）、Winapi（不含 `<windows.h>` 的 Windows API 声明，供 Boost 内部使用）；所有头文件路径保持不变。
- Atomic（原子操作库）——ABI 相关变更：库整体重新设计（修复特征测试宏取值、整数溢出处理等缺陷）；`memory_order` 枚举取值变更（具体值不属接口，但若在用户接口中使用可能破坏 ABI）。重大新特性：Windows x64/MSVC 支持 128 位原子操作（假设目标 CPU 有 `cmpxchg16b` 指令）；实验性支持 Windows ARM 与 DEC Alpha。
- Intrusive（侵入式容器库）——源码破坏性变更：移除此前弃用的 `xxx_dont_splay` 函数、splay 容器的 `splay_set_base_hook`/`splay_set_member_hook` 及 `splaytree_algorithms` 函数的 `bool splay = true` 额外参数。
- Math（数学特殊函数与统计分布库）——破坏性变更：部分非核心头文件移入 `libs/math/include_private`（继续使用需将该目录加入编译器 include 路径）；曾返回最大有限值的分布与特殊函数改为按文档抛出 `overflow_error`（涉及 gamma_p_inva、ibeta_inv 等 special functions 与 pareto、beta、binomial 等分布），依赖不抛异常行为的应用可能开始收到异常。
- TR1（2005 年技术报告 1 组件库）——弃用：该库现已弃用。
- Variant（非递归可辨识联合库）——破坏性变更：编译器支持时改用变参模板（二进制更小、编译更快；未使用 `BOOST_VARIANT_ENUM_PARAMS`/`BOOST_VARIANT_ENUM_SHIFTED_PARAMS` 的元编程代码可能失效；可用 `BOOST_VARIANT_DO_NOT_USE_VARIADIC_TEMPLATES` 禁用）。
- Optional（可选值容器库）——破坏性变更：显式禁止将临时对象绑定到 optional 引用；支持 `explicit operator bool`。
- Regex（正则表达式库）——破坏性变更：修正 `basic_regex<>::mark_count()` 使其与既有文档一致，`basic_regex<>::subexpression(n)` 相应调整。
- Interprocess（进程间通信库）——ABI 破坏性变更：消息队列 `BOOST_INTERPROCESS_MSG_QUEUE_CIRCULAR_INDEX` 选项原实现完全失效，为修复必须破坏 ABI；另修复 1.55 引入的 ABI 回归。
- Utility（通用工具库）——弃用：`empty_deleter` 弃用，改用 Core（核心工具集）的 `null_deleter`。

另有 40 项常规缺陷修复与改进（Accumulators、Any、Asio、Assign、CircularBuffer、ConceptCheck、Container、Context、Coroutine、DynamicBitset、Chrono、Flyweight、Fusion、Geometry、Hash、LexicalCast、Log、Move、MPL、MultiArray、MultiIndex、Multiprecision、Odeint、Predef、Preprocessor、ProgramOptions、SmartPtr、Thread、TTI、Unordered、UUID 等库），见英文原文存档。
