# Boost 1.72.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_72_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_72_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2019-12-11 18:06 GMT（原文日期行：December 11th, 2019 18:06 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

本版无新增库。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Filesystem（可移植文件系统操作库）——库首次要求编译/链接：`filesystem_error` 异常现改为在 Filesystem 的需编译库中实现，用户可能需要在项目中链接 Boost.Filesystem 库。弃用：`operations.hpp` 对新头文件 `exception.hpp`、`file_status.hpp`、`directory.hpp` 的隐式包含（除非定义 `BOOST_FILESYSTEM_NO_DEPRECATED`），未来版本将移除。新增 `directory_options` 枚举（对应 C++20 同名枚举），`symlink_option` 弃用；`recursive_directory_iterator` 的 `level()`、`no_push_pending()`、`no_push_request()`、`no_push()` 弃用，应改用标准对应方法 `depth()`、`recursion_pending()`、`disable_recursion_pending()`。默认行为变更：出错时 `recursive_directory_iterator` 按要求重置到结束状态；新增 `directory_options::pop_on_error` 与 `directory_options::skip_dangling_symlinks` 选项。
- Context（执行上下文库）——移除：`execution_context` 被移除；新增 s390x 架构支持。
- Functional/Factory——移除：`factory`/`value_factory` 由 Glen Fernandes 重写，同时移除两项特性：通过 `BOOST_FUNCTIONAL_VALUE_FACTORY_MAX_ARITY` 提升的 C++03 参数数量上限，以及通过 `BOOST_FUNCTIONAL_FACTORY_SUPPORT_NONE_T` 以 `boost::none_t` 代替 `void` 的用法。
- Math（数学特殊函数与统计分布库）——弃用：头文件 `boost/math/tools/univariate_statistics.hpp` 与 `boost/math/tools/bivariate_statistics.hpp` 弃用，改用 `boost/math/statistics/` 下的对应头文件。新增统计子节（单样本 t 检验、Anderson-Darling 正态性检验、Ljung-Box 自相关检验、随机序列游程检验、经验 CDF 分布等）。
- Preprocessor（预处理器元编程库）——支持 C++20 的 `__VA_OPT__` 构造（`BOOST_PP_VARIADIC_HAS_OPT`、`BOOST_PP_CHECK_EMPTY`、`BOOST_PP_VA_OPT`）。
- 已知问题（Known Issues 栏）：发布后补丁——回退 Coroutine（协程库）不再依赖 Range 的变更。

另有 20 项常规缺陷修复与改进（Asio、Atomic、Beast、CircularBuffer、Endian、GIL、Histogram、Log、MPI、Multiprecision、Outcome、SmartPtr、Test、VMD 等库），见英文原文存档。
