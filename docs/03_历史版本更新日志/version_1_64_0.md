# Boost 1.64.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_64_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_64_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2017-04-19 17:42 GMT（原文日期行：April 19th, 2017 17:42 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Process（进程管理库）：跨平台进程库——创建子进程、设置子进程流、（同步或异步）通过流与子进程通信、（同步或异步）等待进程退出、终止进程，作者 Klemens D. Morgenstern（注：`group.wait()` 不返回的缺陷当时已知）。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Context（执行上下文库）——API 变更：新增 `call/cc` API；`execution-context` API 弃用。
- Fiber（用户态纤程库）——移除：`(un)bounded_channel` 被移除。
- Geometry（几何算法库）——破坏性变更：`ublas_transformer` 更名为 `matrix_transformer`；rtree `index::dynamic_*` 参数的构造函数加 `explicit` 修饰；`strategy::area::huiller` 被 `strategy::area::spherical` 取代。矩阵变换改基于 QVM（二维/三维/四维向量与矩阵库）而非 uBLAS（线性代数库）。
- Regex（正则表达式库）——安全修复：使用 libFuzzer 对库去模糊化（de-fuzz）并修复发现的问题；Oracle C++ 工具集不再限于静态链接。
- Unordered（无序关联容器库）——初始支持 C++17 新成员函数：`unordered_map` 的 `insert_or_assign`/`try_emplace`，全部容器的 `merge`/`extract`。
- Multiprecision（任意精度算术库）——大量精度与舍入修复；错误处理对齐 C99 Annex F。
- TypeTraits（类型特征库）——新增 `make_void` 与 `void_t` 特征。
- SmartPtr（智能指针库）——重写数组的 `allocate_shared`/`make_shared`（更优、更可维护的实现）；新增带移动语义的指针转换函数。

另有 26 项常规缺陷修复与改进（Any、Atomic、Config、Container、Conversion、Core、Coroutine2、DLL、Hash、Interprocess、Intrusive、LexicalCast、Math、MultiIndex、Predef、Test、TypeIndex、Variant 等库），见英文原文存档。
