# Boost 1.65.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_65_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_65_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2017-08-21 20:50 GMT（原文日期行：August 21st, 2017 20:50 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- PolyCollection（多态对象容器库）：多态对象的快速容器，作者 Joaquín M López Muñoz。
- Stacktrace（堆栈回溯库）：收集、存储、拷贝与打印堆栈回溯，作者 Antony Polukhin（注：该库在 MinGW 下存在问题，可能产生空回溯）。

## 移除库（Removed Libraries）

- TR1（2005 年技术报告 1 组件库）正式移除。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- SmartPtr（智能指针库）——重大新特性：新增 `atomic_shared_ptr`（基于 `shared_ptr` 的线程安全原子指针操作）与 `local_shared_ptr`（引用计数以非原子操作更新的变体）。
- Unordered（无序关联容器库）——数据结构统一：`unordered_set`/`unordered_multiset`、`unordered_map`/`unordered_multimap` 改用相同数据结构（C++17 节点合并与提取所需）；为长期弃用的函数补充弃用属性。
- Test（单元测试框架库，v3.6）——破坏性变更：logger API 有变更；弃用 `BOOST_GLOBAL_FIXTURE`，改用 `BOOST_TEST_GLOBAL_FIXTURE`（全局 fixture）与 `BOOST_TEST_GLOBAL_CONFIGURATION`（编译期全局配置）。新增 `BOOST_TEST` 直接比较 C 数组等特性。
- Python（Python 绑定库）——移除：`boost::python::numeric` API 被移除（由 `boost::python::numpy` 取代）；`eval()`/`exec()`/`exec_statement()` 支持 `char const*` 参数。
- ProgramOptions（命令行/配置文件选项解析库）——默认行为变更：隐式值选项重新支持从下一个 token 取值（恢复 1.59 之前的行为，替代 1.59 起仅用同 token 隐式值的做法）；支持将值存入 `boost::optional`。
- Context（执行上下文库）——`call/cc` 支持 ucontext-API（swapcontext）、Windows-Fiber-API 与按需增长栈；Coroutine2 同步获得 ucontext-API 与 Windows-Fiber-API 支持。
- Fiber（用户态纤程库）——支持 Intel TSX 硬件事务内存、NUMA、ucontext-API、Windows-Fiber-API 与按需增长栈。
- Asio（网络与底层 I/O 库）——使用标准原子操作要求 g++ ≥ 4.7（修复 g++ 4.6 链接错误）；修复 Linux epoll 后端竞态条件。

### 1.65.1 修补版（2017-09-07）

- Config（编译器/平台特性检测库）：CUDA 版本宏变更；更新已知最新 MSVC 版本（MSVC 14.11 支持结构化绑定）。
- Context / Fiber：修复 `resume_with` 所执行函数未返回 continuation 的问题（对应 1.65.0 已知问题补丁）。
- Thread（可移植线程库）：修复 Windows 下 `boost::condition_variable` 缺陷（\#130，对应 1.65.0 已知问题补丁）。
- SmartPtr：修复 Visual C++ 版本检查与 NVCC（宿主编译器为 clang）编译问题。
- Stacktrace：支持 FreeBSD 及其他未定义 `_GNU_SOURCE` 但提供 `_Unwind_Backtrace` 的系统；修复 MinGW 构建问题。

另有 23 项常规缺陷修复与改进（Asio、Core、DLL、Fusion、Geometry、Hash、Log、Phoenix、Predef、TypeIndex、Typeof、Utility、Variant 等库），见英文原文存档。
