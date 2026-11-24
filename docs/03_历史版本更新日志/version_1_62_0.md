# Boost 1.62.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_62_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_62_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2016-09-28 15:17 GMT（原文日期行：September 28th, 2016 15:17 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Fiber（用户态纤程库）：用户态线程/纤程（fiber）框架，作者 Oliver Kowalke。
- QVM（向量与矩阵运算库）：处理静态尺寸四元数、向量与矩阵的泛型库，侧重图形、视频游戏与仿真应用所需的 2/3/4 维运算，作者 Emil Dotchevski。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Coroutine（协程库，旧版）——弃用：由 Coroutine2（协程库，栈式）取代。
- CircularBuffer（环形缓冲区库）——默认行为变更：debug 模式下不再默认使用调试实现（其线程安全保证与常规实现不同）；`BOOST_CB_DISABLE_DEBUG` 宏不再使用，改为定义 `BOOST_CB_ENABLE_DEBUG=1` 启用调试支持。
- Container（扩展容器库）——重大新特性：实现 C++17 的 `insert_or_assign`/`try_emplace`（map/flat_map）与 `extract`/`insert(node)`（map/multimap/set/multiset）；修订全部容器默认与移动构造函数的 `noexcept` 表达式。
- Variant（非递归可辨识联合库）——移除：弃用 `BOOST_VARIANT_NO_REFERENCE_SUPPORT` 宏并移除对不支持 SFINAE 编译器的支持。
- Geometry（几何算法库）——命名空间 `concept` 更名为 `concepts`，避免与最新编译器冲突；球形与地理坐标系统的集合/关系运算改用新的球形相交策略（此前一律用笛卡尔策略）。
- Test（单元测试框架库，v3.3）——重大新特性：新增 JUNIT 日志器（输出 JUnit/xUnit 兼容流）、多日志器支持（各自日志级别与输出流）与 `--logger` 命令行开关；数据集驱动测试用例获得唯一名称。
- Log（日志库）——重大新特性：新增本机进程间日志工具（资源名封装、进程间消息队列、sink 后端）与限制输出长度的 `max_size_decor` 字符装饰器。
- TypeIndex（类型信息库）——`ctti_type_index` 在 C++14 下支持 `constexpr`，可在编译期取得类型名的 `const char*`（编译期检查命名空间、按字典序排序类型等）。
- Regex（正则表达式库）——安全修复：修复解析特定非法正则时的缓冲区越界。

另有 23 项常规缺陷修复与改进（Atomic、Chrono、Context、DLL、Functional/Forward、Interprocess、Intrusive、LexicalCast、Math、Optional、Phoenix、Thread、Unordered 等库），见英文原文存档。
