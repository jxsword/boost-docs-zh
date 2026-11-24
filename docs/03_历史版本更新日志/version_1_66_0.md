# Boost 1.66.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_66_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_66_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2017-12-18 13:58 GMT（原文日期行：December 18th, 2017 13:58 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Beast（HTTP/WebSocket 网络库）：仅用 C++11 与 Boost.Asio 实现的可移植 HTTP、WebSocket 与网络操作库，作者 Vinnie Falco。
- CallableTraits（可调用类型操作库）：FunctionTypes 的精神后继，仅头文件 C++11 库，可在编译期检查与操纵所有"可调用"类型，额外支持 C++17 特性，作者 Barrett Adair。
- Mp11（C++11 元编程库）：C++11 元编程库，作者 Peter Dimov。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Asio（网络与底层 I/O 库）——接口调整以对齐 Networking TS（N4656）：服务（service）模板参数及对应类默认禁用（如 `basic_socket<Protocol>` 取代 `basic_socket<Protocol, SocketService>`），定义 `BOOST_ASIO_ENABLE_OLD_SERVICES` 可恢复旧接口；移除此前已弃用的函数；新增自定义 handler tracking、`io_context` 级禁锁"并发提示"特殊值、`ssl::stream` 首参完美转发、释放底层原生 socket 所有权（IOCP 后端需 Windows 8.1+）等。
- Atomic（原子操作库）——新增整数类型扩展原子操作实验集：`fetch_negate`、`fetch_complement`、`opaque_<op>`、`<op>_and_test`、`bit_test_and_set/reset/complement`。注意：`<op>_and_test` 的语义将在 Boost 1.67 反转，使用这些函数的代码需要更新。按 C++17（P0558R1）不再提供指向非对象类型的指针的算术操作；新增 `atomic<T>::value_type` 与 `atomic<T>::difference_type` 成员 typedef。
- MultiIndex（多索引容器库）——行为变更（技术上向后不兼容）：`modify`/`modify_key` 更稳健，修改器抛异常或回滚函数未正确恢复元素时，被修改元素将被擦除（旧版本会保持容器不变）。
- Optional（可选值容器库）——新编译器上对标量 `T` 变为 trivially-copyable（存储由 `aligned_storage` 改为直接 `T`，要求编译器支持 defaulted 函数）。
- Iterator（迭代器构建设施库）——`next()`/`prior()` 现支持仅通过特化 `std::iterator_traits` 定义嵌套类型的用户迭代器（需编译器支持 C++17 兼容的 `std::iterator_traits`）。
- Utility（通用工具库）——`boost/next_prior.hpp` 移至 Boost.Iterator（用户代码无需改动）。
- PolyCollection（多态对象容器库）——向后移植至 GCC 4.8–4.9 与 Clang 3.3–3.6（受旧版 libstdc++ 限制：状态化分配器不受支持、分配器扩展移动构造退化为拷贝构造、元素拷贝抛异常时拷贝构造会崩溃）。
- Regex（正则表达式库）——安全修复：通过去模糊化（de-fuzzing）发现的大量安全问题小修复。
- Uuid（UUID 生成与解析库）——`name_generator` 重构为可配置哈希提供者概念并提供 RFC-4122 的可选 MD5 实现；新增 `boost::uuids::ns` 中的 RFC-4122 命名空间；detail 头文件移入 detail 子目录（可能产生构建警告）。

另有 20 项常规缺陷修复与改进（DateTime、Fiber、Format、Fusion、Geometry、Log、Math、Predef、Stacktrace、Thread、Variant 等库），见英文原文存档。
