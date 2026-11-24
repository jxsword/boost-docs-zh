# Boost 1.52.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_52_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_52_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2012-11-05 16:05 GMT（原文日期行：November 5th, 2012 16:05 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

本版无新增库。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- 安全补丁（Patches 栏）：Locale（本地化与 Unicode 文本处理库）补丁——修复 `boost::locale::utf::utf_traits` 接受部分非法 UTF-8 序列的安全缺陷。
- Interprocess（进程间通信库）——ABI 破坏性变更：`message_queue` 以环形缓冲区索引重新实现（旧行为为有序数组，复制开销大），性能大幅提升；可取消定义宏 `BOOST_INTERPROCESS_MSG_QUEUE_CIRCULAR_INDEX` 恢复旧实现。
- Iterator（迭代器构建设施库）——破坏性变更：因修复 \#5825，function_input_iterator 不再对被包装的无可参函数做多余调用（构造 end 迭代器不再触发调用；解引用并递增 N 次触发 N 次而非 N+1 次），依赖旧行为的用户代码需调整。
- Thread（可移植线程库）——破坏性变更：BOOST_THREAD_VERSION==3（自 1.53 起为默认值）时启用三项变更——unique_future 更名为 future（\#6229）、joinable 的 thread 析构函数应调用 terminate（\#6266）、thread 移动赋值在 joinable 时应调用 terminate（\#6269）；1.50 起弃用的特性仅保留至 1.55。
- Chrono（时间度量与时钟库）——弃用：chrono I/O 自 2.0.0 起完全重构，\_\_duration_short、\_\_duration_long 等旧操作符与 \_\_duration_punct\<\> facet 弃用；BOOST_CHRONO_VERSION==2 时旧接口不可用。
- Ratio（编译期分数运算库）——弃用：`ratio_string<>::short_name` 与 `ratio_string<>::long_name` 弃用，分别改用 `symbol` 与 `prefix`，将于 1.55 移除。
- Utility（通用工具库）——行为变更：`boost::result_of` 在实现提案 n3276 的编译器上改用 `decltype`，并在该模式下做到 SFINAE 友好（n3436）。

另有 18 项常规缺陷修复与改进（Accumulators、Config、Container、DateTime、Foreach、Function、Graph、Hash、LexicalCast、Math、Phoenix、Polygon、Proto、uBLAS、Unordered、Uuid、Wave、xpressive 等库），见英文原文存档。
