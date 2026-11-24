# Boost 1.61.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_61_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_61_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2016-05-13 02:58 GMT（原文日期行：May 13th, 2016 02:58 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Compute（并行/GPU 计算库）：并行/GPU 计算库。
- DLL（动态库加载库）：便捷操作 DLL 与 DSO 的库，跨平台支持加载库、导入原生函数与变量、为 C++ 修饰函数与符号创建别名、查询库的节与导出符号、自加载与自查询、按导出符号获取程序/模块位置。
- Hana（现代异构元编程库）：现代化 C++ 元编程库——提供操作异构序列的高层算法、以自然语法书写类型级计算、内省用户自定义类型等工具。
- Metaparse（编译期解析器生成库）：生成编译期解析器、在 C++ 编译过程中解析内嵌 DSL 代码的库；与 Spirit（解析器/生成器框架库）类似，但 Metaparse 构建的解析器在编译期解析。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Context（执行上下文库）——API 变更：`fcontext_t` 不再属于公开 API；移除 WinFiber API 支持；`execution_context` 放宽至 C++11、实现类型安全的数据传递、可在栈顶执行函数、性能提升；移除静态成员函数 `current()`，启用新的调用语义。
- Coroutine2（协程库，栈式）——标准要求变更：放宽至 C++11；性能提升。
- Optional（可选值容器库）——行为变更：`boost::optional` 现针对引用类型特化——optional 引用的 `sizeof` 等于指针大小；修复拷贝相关缺陷；部分编译器上错误引用绑定导致的运行期缺陷转为编译期错误；可交换 optional 引用（同指针浅交换，底层对象不受影响）；支持抽象类型的 optional 引用；完美转发构造函数 SFINAE 友好。
- Log（日志库）——弃用：对 `boost::basic_string_ref` 及其特化的支持弃用（未来版本移除），建议改用 `boost::basic_string_view`。文件收集器支持限制目标目录中存储日志文件的数量。
- Move（移动语义/emplace 辅助库）——实验性新特性：渐近最优的无缓冲归并与排序算法 `adaptive_merge` 与 `adaptive_sort`。
- Math（数学特殊函数与统计分布库）——工具部分新增多项式算术。

另有 18 项常规缺陷修复与改进（Any、Container、Coroutine、Fusion、Geometry、Interprocess、Intrusive、LexicalCast、Multiprecision、Regex、Test、Variant 等库），见英文原文存档。
