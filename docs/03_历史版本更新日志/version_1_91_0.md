# Boost 1.91.0 发布说明（中文翻译）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/boost_org_releases_1_91_0.md（原始 URL：https://www.boost.org/releases/1.91.0/，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2026-04-15（发布页原文无 GMT 日期行，取 GitHub tag boost-1.91.0 所指提交时间 2026-04-15 14:33 GMT）

1.91.0-1（修补重发布，GitHub tag boost-1.91.0-1，2026-04-23）无独立发布说明正文，本文件正文为 1.91.0 原版说明。

## 总体注记（General Notes）

- [StaticAssert](/libs/static_assert/)（静态断言库）已合并进 [Config](/libs/config/)（编译器/平台特性检测与配置宏库）。这包括代码、测试与文档。为了向后兼容，StaticAssert 的 git 子模块、CMake 与 b2 目标（target）仍然可用；这些目标只是引入对 Config 的依赖。最终，该子模块与目标将被移除。建议用户更新自己对 StaticAssert 的依赖，以 Config 取代之。无需修改任何 C++ 代码。大多数 Boost 库已相应更新。

## 新增库（New Libraries）

- [Decimal](/libs/decimal)（IEEE 754 十进制浮点数库）：

  - 由 Matt Borland 与 Christopher Kormanyos 实现的 IEEE 754 十进制浮点数（Decimal Floating Point Numbers）。

## 更新的库（Updated Libraries）

- [Any](/libs/any/)（类型安全的任意类型容器库）：

  - 修复 CMake 中对 `import std` 的检测。

  - 简化 `boost::anys::basic_any` 的实现。

- [Asio](/libs/asio/)（网络与底层 I/O 库）

  - 新增经由内联命名空间（inline namespace）的可选二进制版本化，使多个 Asio 版本可在同一进程中共存而不发生符号冲突。

  - 将 Windows 下默认的互斥量实现从 `CRITICAL_SECTION` 改为 `SRWLOCK`。

  - 新增基于 `std::atomic` 的"精简"互斥量（slim mutex）实现，缩小 strand、套接字及其他描述符的状态尺寸。

  - 新增在 Cygwin64 下的编译支持，包括不定义 `__USE_W32_SOCKETS` 的情形。

  - 新增在包含 Asio 头文件之前覆盖 `BOOST_ASIO_DECL` 的能力。

  - 修复 NetBSD 上 `MSG_NOSIGNAL` 的处理。

  - 修复与近期 Boost 版本（不再支持链接 `boost_system`）一同构建的问题。

  - 修复旧版 Android 上与 musl libc 的兼容性。

  - 修复较旧 Apple 平台上对 `std::aligned_alloc` 的检测。

  - 修复 MSVC 下 `serial_port_base::character_size::store` 的警告。

  - 在文档中澄清 `ip::multicast::outbound_interface` 的 IPv4 与 IPv6 语义。

  - 更新 TLS v1.3 上下文初始化，以正确检测 LibreSSL 支持。

  - 修复与近期 OpenSSL 中 `X509` 常量性（constness）相关 API 变更的兼容性。

  - 更多细节请查阅[修订历史（Revision History）](/doc/libs/1_91_0/doc/html/boost_asio/history.html)。

- [Atomic](/libs/atomic/)（原子操作库）：

  - 修复 Apple 编译器在 PowerPC 上编译 `thread_pause` 的问题。（[\#79](https://github.com/boostorg/atomic/issues/79)）

- [Beast](/libs/beast/)（基于 Asio 的 HTTP/WebSocket 库）：

  - 修复 `inflate_with_eb` 中的类型转换警告。

  - 对 chunk 头强制 8KB 合理性上限。

  - 将 OpenSSL 变为测试的可选依赖。

  - 移除对 Boost.StaticAssert 的依赖。

  - 在 HTTP 字段枚举中加入 `HTTP2-Settings`。

- [Charconv](/libs/charconv/)（字符与数值互转库）：

  - 修复绝对值小于 2^64 的负 128 位整数在 `to_chars` 中的溢出。

- [Core](/libs/core/)（核心工具集库）：

  - 头文件 `boost/is_placeholder.hpp` 已从 Bind 移至 Core。（[\#90](https://github.com/boostorg/core/issues/90)）

- [Describe](/libs/describe/)（枚举/结构体成员描述宏库）：

  - 在 C++20 下，当外围类尚不完整（incomplete）时，被描述的嵌套枚举（described nested enums）现在也能工作。（感谢 Julien Blanc。）

  - 将 `enum_to_string` 改为 constexpr。（感谢 Julien Blanc。）

- [DynamicBitset](/libs/dynamic_bitset/)（动态位集库）：

  - 为 `operator-( const bit_iterator_base< Iter > & lhs, const bit_iterator_base< Iter > & rhs )` 补上缺失的 friend 声明。

  - 修复使用原始指针作为迭代器的标准库实现时的编译。

  - 修复 `from_block_range()`，防止其在位集未使用部分置位。

- [Exception](/libs/exception/)（增强异常库）：

  - 新增可定制的序列化 API，内建对 Boost.JSON 与 nlohmann/json 的支持。

- [Filesystem](/libs/filesystem/)（可移植文件系统库）：

  - Boost.Filesystem 现在定义并使用自己的平台宏 `BOOST_FILESYSTEM_POSIX_API` 与 `BOOST_FILESYSTEM_WINDOWS_API`。旧的 `BOOST_POSIX_API` 与 `BOOST_WINDOWS_API` 宏仍由 Boost.System 定义。Boost.Filesystem 会检查这两组宏是否同步，若不同步默认将编译失败。将 `BOOST_FILESYSTEM_ALLOW_SYSTEM_API_MISMATCH` 定义为 1 可把编译错误降级为警告，定义为 2 则可完全禁用该检查。注意，此时 Boost.Filesystem 报告的错误码取值将与其错误类别（error category）不匹配。

  - 在不支持 `openat` 及相关 API 的 POSIX 平台上，修复迭代器遇到悬空符号链接（dangling symlink）且禁用跟随符号链接时，`recursive_directory_iterator` 递增所报告的错误。

  - **对 Cygwin 用户是破坏性变更。** 本库现在把 Cygwin 视为 POSIX 平台。这带来若干面向用户的影响，特别是：

    - `path::value_type` 类型由 `wchar_t` 改为 `char`。与其他 POSIX 平台一样，宽字符路径将使用 `path::imbue` 设置的 locale 转换为窄字符编码。注意，由于 Cygwin 运行在 Windows 之上，它内部还会再做一次字符码转换。务必在 Cygwin 环境中正确配置 locale。

    - 路径语法现遵循 POSIX 约定，不支持 Windows 特有路径（如 UNC 路径、盘符与路径前缀）。

    - API 中某些 Windows 特有的部分将不可访问。由于重解析点（reparse point）是 Windows 独有特性，文件将不再报告 `file_type::reparse_file`。重解析点的处理依赖 Cygwin 运行时行为。

    - Cygwin 有自己的符号链接实现，与原生 Windows 符号链接不兼容。Boost.Filesystem 现在将创建并操作 Cygwin 符号链接。

    - Boost.Filesystem 报告的错误码将使用 POSIX `errno` 取值。

  - 在 DragonFly BSD、NetBSD 与 Solaris 上，Boost.Filesystem 默认路径 locale 现使用 UTF-8 作为路径字符编码。

  - 在 Linux 上，除原先已列入黑名单的文件系统外，`copy_file` 与 `copy` 现对 configfs、securityfs、cgroup 与 cgroup2 文件系统也采用 `read`/`write` 循环实现。

- [JSON](/libs/json/)（JSON 解析与序列化库）：

  - 将从 `std::initializer_list` 构造 `value` 的方式改为使用 `value_from`。

- [LEAF](/libs/leaf/)（轻量级错误处理库）：

  - 新增可定制的序列化 API，内建对 Boost.JSON 与 nlohmann/json 的支持。

  - 新增在 Windows 上跨 DLL 边界使用 LEAF 错误对象的支持（默认关闭）。

  - 改进内部 TLS（线程本地存储）API（如 Win32、嵌入式）。

  - 改进诊断系统与 `on_error` 实现。

  - 实现质量改进（如更精确地使用 `noexcept`）。

  - 移除已弃用的 `verbose_diagnostic_info`（由 `diagnostic_details` 取代）。

- [LexicalCast](/libs/lexical_cast/)（字符串与数值等类型转换库）：

  - 实现了 C++20 模块 `boost.lexical_cast` 的初始版本。

- [Log](/libs/log/)（日志库）：

  - 默认在 Cygwin 上启用构建进程间通信支持。

- [Math](/libs/math/)（数学特殊函数与统计分布库）：

  - 为 `non_central_f_distribution` 新增 `find_non_centrality` 参数求取函数。

  - 为 `non_central_t_distribution` 新增参数求取函数。

  - 新增不完全伽马函数对数 `lgamma_q`。

  - 新增下不完全伽马函数对数 `lgamma_p`。

  - 为 `pchip` 新增 `domain()` 函数。

  - 修复 logistic 分布中损坏的 CUDA 支持。

  - 修复 Windows on ARM64 上错误的浮点特征（traits）。

  - 修复大参数下 `ibeta` 的错误结果。

  - 修复 phi 参数为 N * PI / 2 时 `ellint_2` 的错误结果。

  - 要求用户显式启用 CUDA，而不再依据是否存在 NVCC 来假定。

- [MultiIndex](/libs/multi_index/)（多索引容器库）：

  - **破坏性变更：** 本库接受或提供的所有类型列表（`indexed_by`、`tag` 以及嵌套 typedef `index_specifier_type_list`、`index_type_list`、`iterator_type_list` 与 `const_iterator_type_list`）不再基于 [Boost.MPL](/libs/mpl)，而是改为 [Boost.Mp11 列表](/libs/mp11/doc/html/mp11.html#definitions)。由此，Boost.MultiIndex 不再依赖 Boost.MPL。预计大多数用户代码不会受此变更影响；不过也可以通过全局定义宏 `BOOST_MULTI_INDEX_ENABLE_MPL_SUPPORT` 恢复先前行为。对 Boost.MPL 的旧式支持将来可能被弃用并移除。

  - **破坏性变更：** `composite_key` 及相关类模板（`composite_key_equal_to`、`composite_key_compare`、`composite_key_hash`）改为可变参数（variadic）（此前模板参数个数上限受 `BOOST_MULTI_INDEX_LIMIT_COMPOSITE_KEY_SIZE` 限制）。此变更对用户应当透明，但 `composite_key::key_extractors` 现返回 `std::tuple` 而非 `boost::tuple`（其余受影响的类模板同理）。

  - 移除为支持 C++11 之前编译器而设的内部变通（workaround）与回退实现。

- [MSM](/libs/msm/)（有限状态机库，Meta State Machine）：

  - 新特性（`backmp11` 后端）：

    - 改进层次状态机中 `deferred_events` 属性的支持（[\#173](https://github.com/boostorg/msm/issues/173)）

    - 通过 `deferred_events` 属性支持条件延迟（[\#155](https://github.com/boostorg/msm/issues/155)）

    - 简化仿函数（functor）签名（[\#175](https://github.com/boostorg/msm/issues/175)）

    - 将排队事件与延迟事件合并到单一事件池（[\#168](https://github.com/boostorg/msm/issues/168)）

    - 事件池中事件的小对象优化（[\#172](https://github.com/boostorg/msm/issues/172)）

    - 通过 `flat_fold` 分发策略提升运行时性能（[\#180](https://github.com/boostorg/msm/issues/180)）

    - 进一步优化编译：与 1.90 版相比，编译时间最多加快 25%，内存（RAM）消耗更低

  - 缺陷修复（`backmp11`）：

    - 调用 `on_entry(…​)` 与 `on_exit(…​)` 时 `FSM` 类型不正确（[\#167](https://github.com/boostorg/msm/issues/167)）

    - 完成事件（completion event）触发过于频繁（[\#166](https://github.com/boostorg/msm/issues/166)）

    - 层次状态机中的迁移未被正确选择（favor_compile_time）（[\#200](https://github.com/boostorg/msm/issues/200)）

    - `state_machine` 无法移动（[\#205](https://github.com/boostorg/msm/issues/205)）

  - **破坏性变更（`backmp11`）**：事件池的直接访问由 `public` 改为 `protected`，因为在库代码之外操作它可能导致未定义行为。

- [OpenMethod](/libs/openmethod/)（开放式（多）方法库）：

  - 与 `boost::intrusive_ptr` 互操作。

- [Optional](/libs/optional/)（可选值容器库）：

  - 对具备完整 C++11 支持（含"不受限联合"（unrestricted unions）与引用限定符（ref-qualifier））的编译器，将实现从对齐存储（aligned storage）改为联合存储（union storage）。这使渐进式 `constexpr` 支持成为可能：

    - 在 C++11 下，对满足特定约束的类型，某些构造函数与带 `const` 限定的访问器可在编译期上下文中使用（即成为*核心常量表达式*（core constant expression））。

    - 在 C++14 下，对协作类型，甚至某些修改性操作也成为核心常量表达式（那些不需要把 `optional` 从无值状态变为有值状态的操作）。

    - 在 C++17 下，对协作类型，所有构造函数（包括拷贝与移动）都成为核心常量表达式。

    这解决了 issue [\#132](https://github.com/boostorg/optional/issues/132) 与 [\#143](https://github.com/boostorg/optional/issues/143)。

  - **破坏性变更。** 放弃了定制 `swap` 的机制。几乎没人知道该机制，它也从未被文档化。

  - 做了几处小改动，使接口更接近 `std::optional`：

    - 启用语法 `o = {}`，用于把 optional 对象置为无值状态。

    - 启用语法 `o.value_or({})`，其使用默认构造的 `T`。

    - 构造 `o = u`（其中 `o` 类型为 `optional<T>`，`u` 类型为可转换到 `T` 的 `U`）不再创建临时 `T`。

  - 新增从 `optional<T>&` 到 `optional<T&>` 的转换。这解决了 [\#142](https://github.com/boostorg/optional/issues/142)。

  - `none_t` 现在满足 `std::equality_comparable`，这意味着 `none_t` 与 `optional<T>` 建模概念（concept）`std::equality_comparable_with`（当 `T` 满足 `std::equality_comparable` 时），也就是说，可以对 optional 对象的范围执行 `std::ranges::find(rng, boost::none)`。

  - **警告。** 未来发布中我们打算为 `optional` 引入范围（range）接口，使 `std::ranges::range<optional<T>>` 变为 `true`。这将影响某些情形下的重载决议——那些依据 `std::ranges::range` 这类谓词做决策的程序。例如，以下代码的行为将开始发生变化：

        template <typename T>
        void serialize(T const& v)
        {
          if constexpr (std::ranges::range<T>)
            serialize_as_range(v);
          else if constexpr (custom::is_optional_like<T>)
            serialize_as_optional(v);
          else
            serialize_as_value(v);
        }

- [PFR](/libs/pfr/)（无宏结构体反射库）：

  - 新增基于实验性 C++26 反射（Reflection）的实现。将宏 `BOOST_PFR_USE_CPP26_REFLECTION` 定义为 `1` 即可启用。

  - `boost::pfr::for_each_field*()` 函数现在能很好地配合有状态访问者（visitor）工作。

- [Random](/libs/random/)（随机数生成器与分布库）：

  - 修复 `binomial_distribution` 意外不支持无符号类型的问题。

- [Redis](/libs/redis/)（Redis 客户端库）：

  - 新增对 **Sentinel**（哨兵）部署的内建支持，可通过 `config::sentinel` 配置。本库自动处理主/从发现、错误检测与重连（[PR#345](https://github.com/boostorg/redis/pull/345)、[PR#391](https://github.com/boostorg/redis/pull/391)、[\#237](https://github.com/boostorg/redis/issues/237)）。

  - 新增 **`generic_flat_response`**，是 `flat_response` 的高性能替代品，使用连续内存且在稳态下零分配。非常感谢 Nikolai Vladimirov 提交的 PR（[PR#340](https://github.com/boostorg/redis/pull/340)、[PR#356](https://github.com/boostorg/redis/pull/356)、[PR#358](https://github.com/boostorg/redis/pull/358)、[PR#378](https://github.com/boostorg/redis/pull/378)、[PR#383](https://github.com/boostorg/redis/pull/383)、[\#263](https://github.com/boostorg/redis/issues/263)）。

  - **服务器推送（server push）处理**的总体改进：

    - 新增订阅跟踪支持，在每次重连后恢复生效的订阅。可通过 `request::subscribe`、`request::psubscribe`、`request::unsubscribe` 与 `request::punsubscribe` 使用（[PR#375](https://github.com/boostorg/redis/pull/375)、[\#367](https://github.com/boostorg/redis/issues/367)）。

    - 新增 `push_parser`，一个便于解析 PubSub 相关消息的视图（[PR#390](https://github.com/boostorg/redis/pull/390)、[\#349](https://github.com/boostorg/redis/issues/349)）。

    - **`connection::async_receive`** 与 **`connection::receive`** 现已**弃用**。建议用户改用 `async_receive2`，它支持更快的批量处理（[PR#381](https://github.com/boostorg/redis/pull/381)、[PR#340](https://github.com/boostorg/redis/pull/340)、[\#331](https://github.com/boostorg/redis/issues/331)）。

    - **`consume_one`** 现已**弃用**。建议用户改用 `generic_flat_response::clear`。详情参见 PubSub 示例。

    - 改进了文档与示例。

  - **`config::username`**、**`config::password`**、**`config::client_name`** 与 **`config::database_index`** 现已**弃用**。建议用户改用 `config::setup`。新增 `request::hello` 与 `request::hello_setname` 以简化 setup 请求的构造（[PR#392](https://github.com/boostorg/redis/pull/392)）。

  - 调整了日志消息级别使其更贴切：配置与网络错误用 `level::error`，成功的连接尝试用 `level::info`，详细输出用 `level::debug`（[PR#389](https://github.com/boostorg/redis/pull/389)、[\#395](https://github.com/boostorg/redis/issues/395)）。

  - 新增 `request::append()` 用于拼接请求对象（[PR#342](https://github.com/boostorg/redis/pull/342)、[\#341](https://github.com/boostorg/redis/issues/341)）。

  - 修复向 `request::push_range` 传入含 `std::tuple` 元素的范围时生成无效命令的问题（[PR#363](https://github.com/boostorg/redis/pull/363)、[\#360](https://github.com/boostorg/redis/issues/360)）。

  - 从公共头文件中移除 `<ostream>`，使其更轻量（[PR#364](https://github.com/boostorg/redis/pull/364)、[\#361](https://github.com/boostorg/redis/issues/361)）。

- [Stacktrace](/libs/stacktrace/)（堆栈回溯库）：

  - 移除针对可能不兼容运行时的编译期检查。由此不再有误报，`from_exception` 功能开箱即用。少数不兼容/泄漏运行时的情形现在在运行期报告。

  - 在 Cygwin 上禁用 `from_exception`（[PR#219](https://github.com/boostorg/stacktrace/pull/219)）。非常感谢 David McFarland 提交的 PR！

  - 移除 `has_addr2line` 与 C 标准库的链接，以简化使用非系统默认 `libstdc.so` 的构建。

- [System](/libs/system/)（错误码与 system_error 库）：

  - `operator|(result<T&>, U)` 的返回类型改为非引用。

  - `r & f` 现在支持成员指针（通过 `boost::compat::invoke` 实现）。

  - 现在会安装 CMake 配置文件，尽管本库是仅头文件库。这避免破坏包含 `find_package(Boost COMPONENTS system …​)` 的第三方 `CMakeLists.txt` 文件。

  - 在 C++20 及更高标准下，`error_code` 的 `constexpr` 程度进一步提高。

  - 为 `result` 新增 `unsafe_value`。

  - `result<>::operator*` 与 `result<>::operator->` 现在在 `!has_value()` 时抛出异常，而不再将其作为前置条件。旧行为现在由 `unsafe_value()` 表达。

  - 新增 `boost/system/unwrap_and_invoke.hpp`。

- [Test](/libs/test/)（单元测试框架库）：

  - 新增 friend 运算符，使 `std::optional` 在 GCC \< 10 下能正确比较。

- [TypeIndex](/libs/type_index/)（运行时类型索引库）：

  - 从 C++20 起优化 CTTI（译注：编译期类型标识）类型比较。

  - 在 C++14 及更现代的标准下，`ctti_type_index::name()` 现默认返回美化（pretty）值。缩小了库二进制体积。

- [Unordered](/libs/unordered/)（无序关联容器（哈希实现）库）：

  - 修复并发容器中范围插入的返回值（[PR#344](https://github.com/boostorg/unordered/pull/344)）。

- [UUID](/libs/uuid/)（UUID 生成与解析库）：

  - 在 `boost/uuid/uuid_io.hpp` 中新增 `from_chars`。

  - 为 `string_generator` 新增 `noexcept` 的 `operator()` 重载。

  - `string_generator` 现在除 `char` 与 `wchar_t` 外还支持 Unicode 字符类型。

  - 大多数 `uuid` 访问器、操作以及 `to_chars` 现在在可能时为 `constexpr`（C++14 及更高标准、较新编译器）。

  - 新增 `to_chars` 的 SIMD 实现，UUID 格式化性能最多可提升 5.5 倍。（Andrey Semashev）

  - 新增 `from_chars` 的 SIMD 实现，UUID 解析性能最多可提升 13 倍。（Andrey Semashev）

  - 在 `boost/uuid/uuid_io.hpp` 中新增 `uuid_from_string`。

  - 新增专用异常类 `invalid_uuid`，派生自 `std::runtime_error` 以保持向后兼容。

- [URL](/libs/url/)（URL 解析库）：

  - 新特性：

    - 所有解析函数在 C++20 下现为 `constexpr`，支持编译期 URL 解析与校验（[PR#976](https://github.com/boostorg/url/pull/976)）。

    - 为查询容器新增 `get_or`，键不存在时返回默认值（[PR#953](https://github.com/boostorg/url/pull/953)）。

    - 新增独立的 `decode` 与 `decoded_size` 自由函数（[PR#952](https://github.com/boostorg/url/pull/952)）。

    - 为 `grammar::range` 新增用户提供 `RangeRule` 的支持，允许自定义文法规则（[PR#950](https://github.com/boostorg/url/pull/950)）。

    - 为所有视图类型特化 `std::ranges::enable_borrowed_range`（[PR#966](https://github.com/boostorg/url/pull/966)）。

    - 为 `token_rule_t` 新增 EBO（空基类优化）与默认构造（[PR#964](https://github.com/boostorg/url/pull/964)）。

    - 为 segment（段）新增 natvis 可视化器（[PR#962](https://github.com/boostorg/url/pull/962)）。

  - 性能：

    - 内部 URL 偏移量由 `size_t` 改为 `uint32_t`，减小 64 位平台上的对象大小（[PR#969](https://github.com/boostorg/url/pull/969)）。

  - 修复：

    - `normalize_path` 中由点段消除（dot-dot cancellation）引起的歧义（[PR#986](https://github.com/boostorg/url/pull/986)）。

    - `parse_query` 对空 `string_view` 输入的防护（[PR#949](https://github.com/boostorg/url/pull/949)）。

    - `params_iter_impl::decrement()` 对含 `=` 值的解码大小（[PR#978](https://github.com/boostorg/url/pull/978)）。

    - `decode_view::remove_prefix`/`remove_suffix` 断言（[PR#978](https://github.com/boostorg/url/pull/978)）。

    - `pct_string_view::operator*()` 的 `decode_view` 完整性（[PR#963](https://github.com/boostorg/url/pull/963)）。

    - 示例 router 现为仅移动（move-only）（[PR#959](https://github.com/boostorg/url/pull/959)）。

    - GCC 在 `tuple_rule` 中误报的 `-Wmaybe-uninitialized`（[PR#981](https://github.com/boostorg/url/pull/981)）。

    - Laurel Lye Systems Engineering 的安全评审：三轮评估、21 项确认修复，新增公共接口边界测试与模糊（fuzz）测试（[PR#982](https://github.com/boostorg/url/pull/982)、[PR#988](https://github.com/boostorg/url/pull/988)）。

  - 文档：

    - 新增设计依据（design rationale）页面（[PR#987](https://github.com/boostorg/url/pull/987)）。

    - 文档化 plus scheme 约定（[PR#970](https://github.com/boostorg/url/pull/970)）。

    - 移除旧版 QuickBook（QuickBook 文档格式）文档。

- [Variant2](/libs/variant2/)（Variant 的现代重实现库）：

  - 放宽 `holds_alternative<T>` 与 `get<T>` 的要求：不再要求 `T` 在备选类型列表中恰好出现一次，现在只要求至少出现一次。

## 更新的工具（Updated Tools）

原文本版无"更新的工具（Updated Tools）"章节。

## 已测试的编译器（Compilers Tested）

Boost 的主要测试编译器如下：

- Linux：

  - Clang，C++03：3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++11：3.4, 11.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++14：3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 5.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++17：6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang，C++20：11.0.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - GCC，C++03：4.6.3, 11, 12

  - GCC，C++11：4.7.3, 4.8.5, 11, 12

  - GCC，C++14：5.4.0, 6.4.0, 7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC，C++17：7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC，C++20：8.0.1, 9.1.0, 10, 11, 12

- OS X：

  - Apple Clang，C++03：11.0.3

  - Apple Clang，C++11：11.0.3

  - Apple Clang，C++14：11.0.3

  - Apple Clang，C++17：11.0.3

  - Apple Clang，C++20：11.0.3

- Windows：

  - Visual C++：10.0, 11.0, 12.0, 14.0, 14.1, 14.2, 14.3

## 致谢（Acknowledgements）

本次发布由 Marshall Clow、Glen Fernandes 与 Ion Gaztañaga 管理。
