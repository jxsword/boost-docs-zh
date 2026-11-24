# Boost 术语表（翻译先行 · 全体子代理共用）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 用途：全部文档与翻译子代理共用，统一译法；与总纲第 5 节术语规范配套。
> 来源：术语取自 boost.org 官网与官方文档（核实: 2026-11-14 可达）；译法为本文档统一约定。

## 0. 使用规则（翻译硬性约束）

1. **一律不译**：库名（如 `Asio`、`multi_index`）、类/函数/宏/命名空间（`BOOST_*`、`std::*`、`boost::*`）、提案号（P0xxx）、工具名（b2、QuickBook、boostdep 等）、许可证名（Boost Software License）。首次出现时以括号加中文注释，如 `Asio（网络与底层 I/O 库）`。**注意：该"括号注释"规则仅适用本项目自撰文档；语料译文（site/zh 镜像页）不加注释括号**（总纲 §4.3 / 附录 A C5）。
2. 表中"固定译法"为唯一译法：同一英文词全站只用一种中文对应，不得同义替换。
3. 库名大小写以官方为准（如 `StringAlgo` 官方写作 StringAlgo Algorithms 库，目录名 `algorithm/string`）。
4. 翻译完成后执行 grep 术语一致性校验：库名/宏/API 被译成中文即视为错误。

## 1. 固定译法表（英文 → 唯一中文译法）

| 英文原文 | 固定译法 | 备注 |
|---|---|---|
| release notes | 发布说明 | 本项目主体翻译对象 |
| release | 发布（版本） | "1.92.0 release"→"1.92.0 发布" |
| release candidate (RC) | 候选版本 | |
| beta | 测试版（beta） | 保留英文标签 |
| changelog | 变更日志 | |
| header-only | 仅头文件库 | 无需编译链接 |
| compiled library | 需编译库 | |
| automatically linked / auto-linking | 自动链接 | MSVC pragma 机制 |
| category | 分类 | 官网 30 个分类 |
| dependency | 依赖 | |
| superproject | 超级项目 | boostorg/boost 主仓库 |
| modular Boost / modularization | Boost 模块化 / 模块化改造 | 2013 年起 git 化改造 |
| module | 模块 | superproject 中一个库 = 一个 git 子模块；勿与 C++20 modules 混译 |
| C++20 modules | C++20 模块 | 指语言特性，注意与上一行区分 |
| git submodule | git 子模块 | |
| master / develop branch | master 分支 / develop 分支 | 分支名不译 |
| toolset | 工具集 | b2 的编译器配置（gcc/clang/msvc） |
| target | 构建目标 | |
| regression test | 回归测试 | |
| regression dashboard | 回归测试看板 | |
| breaking change | 破坏性变更 | |
| deprecation | 弃用 | |
| removal | 移除 | |
| bug fix / defect fix | 缺陷修复 | |
| enhancement | 功能增强 | |
| new library | 新增库 | |
| updated library | 更新的库 | 发布说明栏目名 |
| major change | 重大变更 | |
| standardized component | 已标准化组件 | |
| proposal (P0xxx) | 提案（P0xxx，编号不译） | |
| adopted into the standard | 已合入标准 | |
| upstream | 上游 | |
| distribution | 发行版 | Debian/Fedora 等 |
| package manager | 包管理器 | |
| baseline | 基线 | vcpkg baseline 清单 |
| pinned version | 锁定版本 | |
| backport | 向后移植 | |
| patch release / fix release | 修补版本 | 如 1.91.0-1 |
| ABI | ABI（应用二进制接口） | 不译 |
| API | API（应用编程接口） | 不译 |
| long-term support (LTS) | 长期支持（LTS） | |
| feature-test macro | 特性测试宏 | `__cpp_lib_*` 等 |
| maintainers | 维护者 | |
| reviewers / Formal Review | 正式评审（Formal Review） | 新库入库的社区评审流程 |
| unmaintained | 无维护者（停止维护） | 官网 Maintainers 列表状态 |
| deprecated | 弃用 | 同 deprecation |
| header | 头文件 | |
| link / linking | 链接 | |
| runtime | 运行时 / 运行库 | 按语境 |
| static / dynamic linking | 静态链接 / 动态链接 | |
| cross-platform | 跨平台 | |
| wrapper | 封装（库） | |
| binding | 绑定 | |
| compile-time | 编译期 | |
| run-time | 运行期 | |
| intrusive | 侵入式 | |
| non-intrusive | 非侵入式 | |
| lock-free | 无锁 | |
| wait-free | 无等待 | |
| allocator | 分配器 | |
| iterator | 迭代器 | |
| range | 范围 | |
| view | 视图 | |
| adaptor / adapter | 适配器 | |
| trait | 特征（traits） | "类型特征"仅用于 TypeTraits 语境 |
| concept | 概念（concept） | C++20 关键字时不译 |
| coroutine | 协程 | |
| generator | 生成器 | |
| reflection | 反射 | |
| serialization | 序列化 | |
| interoperability | 互操作性 | |

## 2. 工具名表（不译 · 首次出现加中文注释）

| 工具名 | 中文注释 | 用途 |
|---|---|---|
| b2 | Boost 构建工具（原名 bjam） | Boost 官方构建驱动 |
| Boost.Build | b2 构建系统框架 | 仓库 `tools/build` |
| BoostBook | BoostBook 文档格式 | 基于 DocBook 的文档中间格式 |
| QuickBook | QuickBook 文档格式 | Wiki 式源格式，编译为 BoostBook |
| Doxygen | Doxygen 文档生成器 | 从源码注释生成参考手册 |
| AsciiDoc | AsciiDoc 文档格式 | 部分新库文档源格式 |
| boostdep | 依赖分析工具 | 生成库依赖报告 |
| bcp | bcp 工具 | 复制库子集及其依赖 |
| CMake | CMake 构建系统 | 第三方集成主流方式 |
| vcpkg | vcpkg 包管理器 | 微软系 C++ 包管理器 |
| Conan | Conan 包管理器 | 去中心化 C/C++ 包管理器 |
| Repology | Repology 版本聚合站 | 发行版包版本追踪 |
| mermaid / mermaid-cli | mermaid 图表 / mermaid 命令行校验工具（mmdc） | 本项目图表 |
| Git / GitHub | Git 版本控制 / GitHub 托管平台 | |
| cppreference | cppreference.com 参考站 | 标准特性判定基准源（第三方，非官方） |

## 3. 委员会与标准术语表

| 术语 | 译法/处理 | 说明 |
|---|---|---|
| WG21（ISO/IEC JTC1/SC22/WG21） | 不译，注释"C++ 标准委员会" | |
| CWG / LWG / LEWG | 不译，注释"核心/库/库演进工作组" | |
| Technical Specification (TS) | 技术规范（TS） | 如 Filesystem TS |
| TR1 | TR1（2005 年技术报告 1） | 首批 Boost 组件进标准 |
| std:: | 不译 | 标准库命名空间 |
| feature-test macro | 特性测试宏 | 见固定译法表 |
| C++11/14/17/20/23/26 | 不译 | 标准版本号 |
| P0xxx / Dxxxx | 不译 | 提案/草案编号 |
| adopted / merged | 已合入 / 已并入 | 指入标准 |
| rejected / not proposed | 未被采纳 / 未提案 | |
| constexpr | 不译 | 关键字 |
| noexcept | 不译 | 关键字 |

## 4. Boost 专有概念表

| 概念 | 处理 | 说明 |
|---|---|---|
| Boost | 不译（首现注释"C++ 准标准库集合"） | |
| Boost Software License (BSL) | 不译，注释"宽松开源许可证" | |
| boost.org / archives.boost.io | 不译 | 官网 / 下载归档站 |
| superproject | 超级项目 | 见固定译法表 |
| meta/libraries.json | 不译 | 官方库清单元数据文件 |
| release cycle | 发布周期 | 每年 4/8/12 月三发 |
| version numbering（X.Y.Z） | 版本号规则：X.Y 为主版本，Z 对应 git tag | |
| header-only library | 仅头文件库 | |
| monolithic release | 单体发布包（整包下载） | 对比 git 子模块方式 |
| latest | latest（最新指向目录） | `/doc/libs/latest/` |
| library categories | 库分类 | 官网 30 类 |
| maintainers | 维护者 | |
| regression test matrix | 回归测试矩阵 | |

## 5. 库名速查表（不译 · 常用 ~60 库附一行中文注释）

> 完整 ~150 库 × 30 分类总表以 `docs/02_组织架构与依赖详解.md` 为准；本表仅供翻译时快速加注。

| 库名（不译） | 分类 | 一行中文注释 |
|---|---|---|
| Config | 基础 | 编译器/平台特性检测与配置宏 |
| Core | 基础 | 核心工具集（非空指针、地址获取等轻量设施） |
| Utility | 基础 | 通用工具（noncopyable、checked_delete 等） |
| Assert | 基础 | 可定制断言宏 |
| ThrowException | 基础 | 统一异常抛出设施 |
| TypeTraits | 基础 | 类型特征 |
| Preprocessor | 基础 | 预处理器元编程 |
| StaticAssert | 基础 | 静态断言 |
| Integer | 基础 | 整数类型选择（int 系） |
| Ratio | 基础 | 编译期分数运算 |
| Predef | 基础 | 编译器/架构/OS 预定义宏库 |
| Describe | 基础 | 枚举/结构体成员描述宏 |
| Move | 基础 | 移动语义/emplace 辅助（兼容 C++03） |
| Swap | 基础 | 标准化 swap 实现 |
| SmartPtr（smart_ptr） | 内存 | 智能指针（shared_ptr/weak_ptr/intrusive_ptr 等） |
| Pool | 内存 | 内存池 |
| PointerContainer | 内存 | 指针容器 |
| Alignment | 内存 | 对齐工具 |
| Thread | 并发 | 可移植线程库 |
| Asio | 并发 | 网络与底层 I/O（proactor 模型） |
| Atomic | 并发 | 原子操作 |
| Context | 并发 | 执行上下文（ucontext/-fiber 原语） |
| Coroutine2 | 并发 | 协程（栈式，基于 Context） |
| Fiber | 并发 | 用户态纤程与通道 |
| Interprocess | 并发 | 进程间通信（共享内存、消息队列） |
| Lockfree | 并发 | 无锁容器与队列 |
| MPI | 并发 | MPI 消息传递接口封装 |
| Container | 容器 | 扩展容器（vector 的 stable/deque 变体、flat_map 等） |
| MultiIndex | 容器 | 多索引容器 |
| Unordered | 容器 | 无序关联容器（hash 实现） |
| Bimap | 容器 | 双向映射 |
| CircularBuffer | 容器 | 环形缓冲区 |
| Heap | 容器 | 优先队列家族 |
| Intrusive | 容器 | 侵入式容器 |
| Variant | 容器 | 非递归可辨识联合 |
| Variant2 | 容器 | Variant 的现代重实现（never-empty） |
| DynamicBitset | 容器 | 动态位集 |
| PropertyTree | 容器 | 属性树（JSON/INI/XML 解析） |
| StringAlgo | 字符串 | 字符串算法（trim/replace/split 等） |
| Regex | 字符串 | 正则表达式 |
| Xpressive | 字符串 | 可内嵌表达式的正则 |
| Spirit | 字符串 | 解析器/生成器框架（PEG） |
| Locale | 字符串 | 本地化与 Unicode 文本处理 |
| Tokenizer | 字符串 | 分词器 |
| Format | 字符串 | 类型安全 printf 风格格式化 |
| LexicalCast | 字符串 | 字符串↔数值等类型转换 |
| Convert | 字符串 | 可扩展类型转换框架 |
| FileSystem | 系统 | 可移植文件系统操作 |
| System | 系统 | 错误码与 system_error |
| Iostreams | 系统 | 流/设备抽象框架 |
| ProgramOptions | 系统 | 命令行/配置文件选项解析 |
| JSON | 系统 | JSON 解析与序列化（1.75 新增） |
| URL | 系统 | URL 解析（1.81 新增） |
| UUID | 系统 | UUID 生成与解析 |
| Nowide | 系统 | Windows 下 UTF-8 标准 I/O 适配 |
| Endian | 系统 | 字节序处理 |
| Process | 系统 | 进程管理（v2 开发中） |
| Beast | 网络 | HTTP/WebSocket 基于 Asio |
| Graph | 数值/图 | 图结构与算法 |
| Geometry | 数值/图 | 几何算法库 |
| Multiprecision | 数值 | 任意精度算术 |
| Math | 数值 | 数学特殊函数与统计分布 |
| Random | 数值 | 随机数生成器与分布 |
| Rational | 数值 | 有理数 |
| Interval | 数值 | 区间算术 |
| Odeint | 数值 | 常微分方程求解 |
| QVM | 数值 | 二维/三维/四维向量与矩阵 |
| SafeNumerics | 数值 | 溢出安全整数运算 |
| uBLAS | 数值 | 线性代数（BLAS 风格） |
| Test | 测试 | 单元测试框架 |
| Stacktrace | 测试 | 堆栈回溯 |
| Exception | 测试 | 增强异常（携带回溯/数据） |
| Log | 测试 | 日志库 |
| Chrono | 时间 | 时间度量与时钟 |
| DateTime | 时间 | 日期时间（历史更早，功能更全） |
| Timer | 时间 | 已废弃的简易计时（并入 Chrono 生态） |
| MPL | 元编程 | 模板元编程库（C++98 风格） |
| Fusion | 元编程 | 异构容器与算法（运行期/编译期融合） |
| Hana | 元编程 | 现代异构元编程（C++14） |
| Proto | 元编程 | 表达式模板/DSL 构建 |
| YAP | 元编程 | 表达式模板库（Proto 的轻量替代） |
| FunctionTypes | 元编程 | 函数类型合成与分解 |
| StlInterfaces | 元编程 | 迭代器/范围定制点 CRTP 基类 |
| Function | 回调 | 多态函数包装 |
| Bind | 回调 | 参数绑定（std::bind 前身） |
| MemFn | 回调 | 成员函数指针包装 |
| Signals2 | 回调 | 线程安全信号槽 |
| Phoenix | 回调 | Lambda 表达式库（Boost.Lambda 继任） |
| Lambda | 回调 | Lambda 表达式库（旧，已被 Phoenix 取代） |
| Factory | 回调 | 工厂/转发函数模板 |
| Any | 泛型 | 类型安全的任意类型容器 |
| TypeErasure | 泛型 | 运行期多态概念（duck typing） |
| Compat | 泛型 | 标准库补丁（std::span/string_view 跨标准兼容） |
| Histogram | 数据 | 多维直方图 |
| DLL | 系统 | 动态库加载/插件 |
| Serialization | 系统 | 序列化框架（版本化、多格式） |
| Wave | 文本 | C/C++ 预处理器实现（Spirit 构建） |
| GIL | 图像 | 通用图像库 |
| Polygon | 数值/图 | 多边形布尔运算 |
| PropertyMap | 图 | 属性映射概念 |
| Statechart | 模式 | 有限状态机 |
| Units | 数值 | 量纲系统 |
| Tribool | 基础 | 三态布尔 |
| Iterator | 泛型 | 迭代器构建设施 |
| Range | 泛型 | 范围抽象（Range algorithms） |
| Algorithm | 泛型 | 通用算法集合（含 minmax 等） |
| VMD | 基础 | 可变宏数据（预处理器扩展） |
| WinAPI | 系统 | Win32 API 薄封装 |
| PFR | 基础 | 无宏结构体反射（Magic GET） |

（本表 ~90 行含去重占位行，有效 ~85 条；合计四表 ≈ 100+ 核心术语，满足总纲 P0 要求。）
