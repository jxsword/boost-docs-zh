# Boost 1.47.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_47_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_47_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2011-07-11 22:19 GMT（原文日期行：July 11th, 2011 22:19 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Chrono（时间度量与时钟库）：实用的时间工具，作者 Vicente J. Botet Escribá。
- Geometry（几何算法库）：几何库，作者 Barend Gehrels、Bruno Lalande 与 Mateusz Loskot。
- Phoenix（Lambda 表达式库）：在实际调用点定义小型匿名函数对象等，作者 Joel de Guzman、Dan Marsden 与 Thomas Heller。
- Ratio（编译期分数运算库）：编译期有理数算术，作者 Vicente J. Botet Escribá。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- 构建系统（Build System）：Boost.Build 可执行文件的官方名称改为 b2（Boost 构建工具，原名 bjam）；bootstrap 脚本会创建名为 bjam 的副本，以避免第三方构建脚本失效。
- Graph（图结构与算法库）——移除：删除弃用函数 `kolmogorov_max_flow`，请改用 `boykov_kolmogorov_max_flow`。
- Random（随机数生成器与分布库）——大版本对齐 C++11 标准，含多处破坏性/行为变更：大量重命名（如 uniform_int→uniform_int_distribution、mersenne_twister→mersenne_twister_engine，旧名提供包装）；geometric_distribution 与 lognormal_distribution 参数语义改变（boost::random:: 下的新行为）；播种算法改变，用非 Boost.Random 生成器播种将无法编译；特性移入 `boost::random` 命名空间；variate_generator 成为简单透传包装；has_fixed_range 恒为 false；部分 result_type 由有符号改为无符号；gamma_distribution 流式格式因新增参数而与旧版本不兼容。
- Asio（网络与底层 I/O 库）——重大新特性：信号处理、异步程序调试辅助、socket iostream 超时、组合连接操作、重写的 SSL 实现、C++0x 移动语义支持、与 POSIX `fork()` 兼容等。

另有 21 项常规缺陷修复与改进（Accumulators、Config、DateTime、DynamicBitset、Foreach、Function、FunctionTypes、Iostreams、Iterator、LexicalCast、Logic、Math、MSM、MultiIndex、Proto、Range、Spirit、Tokenizer、Utility、Uuid、Wave 等库），见英文原文存档。
