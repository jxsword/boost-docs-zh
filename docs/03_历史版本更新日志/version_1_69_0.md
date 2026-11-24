# Boost 1.69.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_69_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_69_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2018-12-12 02:58 GMT（原文日期行：December 12th, 2018 02:58 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- SafeNumerics（溢出安全整数运算库）：面向 C++14 及以上、保证正确的整数运算库，作者 Robert Ramey。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- 构建系统（非 Windows 用户须知）——默认行为变更：b2（Boost 构建工具）支持 visibility，构建共享库时默认使用隐藏符号可见性（共享库更小、加载更快、符号冲突更少）；如需旧行为可用命令行 `./b2 visibility=global` 构建。
- System（错误码库）——转为仅头文件库：仍构建一个兼容用占位库，但不再需要链接它。`error_category` 析构函数改为 `protected` 且不再 `virtual`（潜在破坏性变更，影响面预期有限）；新增 64 位标识符构造函数（使不同 category 对象可相等比较）与 `failed` 虚函数（支持"成功不等于 0"的 category）；弃用的 `boost::system::throws` 对象移除，`boost::throws()` 弃用；`system_error` 的单 `error_code` 构造函数改为 `explicit`，`code()` 改为按值返回。
- 已停用库（Discontinued Libraries）：Signals (v1) 正式移除——1.54 弃用、1.68 预告移除，1.68 为最后提供该库的版本，建议改用 Signals2（线程安全信号槽库）。
- Logic（三态布尔库）——破坏性变更：可用时改用 `explicit operator bool`。
- Integer（整数类型选择库）——弃用：`boost/pending/integer_log2.hpp` 弃用并将在未来版本移除，改用 `boost/integer/integer_log2.hpp`。
- Multiprecision（任意精度算术库）——行为变更：给 `cpp_int` 赋非有限值现在成为运行期错误；新增 `cpp_bin_float_oct`、`cpp_complex_oct` typedef 与 `std::string_view` 支持。
- Test（单元测试框架库）——正式支持仅头文件变体的多翻译单元用法；新增 `BOOST_TEST_CASE_NAME` 手动命名测试用例。
- Stacktrace（堆栈回溯库）——`libbacktrace` 用法大幅改进（内存占用下降、栈捕获快一个数量级、启用 `syminfo` 回退、可用 `BOOST_STACKTRACE_BACKTRACE_INCLUDE_FILE` 指定头文件路径）。

另有 39 项常规缺陷修复与改进（Any、Asio、Assign、Beast、CircularBuffer、ConceptCheck、Context、Core、DLL、DynamicBitset、Fiber、Filesystem、Flyweight、Function、Geometry、GIL、Iostreams、Iterator、LexicalCast、Math、Mp11、MultiArray、MultiIndex、PolyCollection、Pool、Preprocessor、Rational、Spirit、TypeIndex、Utility、Variant、YAP 等库），见英文原文存档。
