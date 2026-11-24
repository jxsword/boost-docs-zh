# Version 1.87.0

## Version 1.87.0

December 12th, 2024 00:52 GMT

[Documentation](/doc/libs/1_87_0/)

| Platform | File | SHA256 Hash |
|----|----|----|
| unix | [boost_1_87_0.tar.bz2](https://archives.boost.io/release/1.87.0/source/boost_1_87_0.tar.bz2) | af57be25cb4c4f4b413ed692fe378affb4352ea50fbe294a11ef548f4d527d89 |
|  | [boost_1_87_0.tar.gz](https://archives.boost.io/release/1.87.0/source/boost_1_87_0.tar.gz) | f55c340aa49763b1925ccf02b2e83f35fdcf634c9d5164a2acb87540173c741d |
| windows | [boost_1_87_0.7z](https://archives.boost.io/release/1.87.0/source/boost_1_87_0.7z) | db6b7d77a2286ebe79d4aa7252c08b051d271fd8b013b6b18bc7a966552c1139 |
|  | [boost_1_87_0.zip](https://archives.boost.io/release/1.87.0/source/boost_1_87_0.zip) | f367a218d27b23b568956bacf56d08d2c1d9647211337136be8cac5cb2ff0828 |

Downloads {.download-table}

\* The download links are supported by grants from [The C++ Alliance](https://cppalliance.org/).  
  

### New Libraries

- [Parser](/libs/parser/): Framework for building parsers, from Zach Laine.

### Updated Libraries

- [Asio](/libs/asio/):
  - Added support for using byte spans and sequences of byte spans as buffer sequences. This means that they can be passed directly to I/O operations such as `async_read`.

  - Added support for generic dispositions, which are types that can be used to test whether an asynchronous operation completed without error. This includes `error_code` and `exception_ptr`, but can be extended to user types via specialisation of the `disposition_traits` class template. The standard types `std``::``error_code` and `std``::``exception_ptr` are recognised as dispositions.

  - Added disposition support to the `boost``::``asio``::``use_future` completion token, `boost``::``asio``::``awaitable``<>`-based coroutines, `boost``::``asio``::``spawn``()`, and `boost``::``asio``::``experimental``::``cancellation_condition`.

  - Added the `execution_context``::``service_maker` abstract base class. A `service_maker` is an object that is passed to an execution context's constructor, and allows services to be added at context construction time.

  - Added `boost``::``asio``::``config`, which provides access to configuration parameters that are associated with an execution context. The class is intended for use by asio internals, or by libraries or user-provided abstractions that build on top of asio, and will typically be used to fine tune behaviour, such as enabling or disabling certain optimisations. A concrete configuration source, such as `boost``::``asio``::``config_from_env`, `boost``::``asio``::``config_from_concurrency_hint` and `boost``::``asio``::``config_from_string`, may be passed to the `io_context` or `thread_pool` constructor.

  - Added an initial set of configuration parameters recognised by Asio's `io_context` and `thread_pool` implementations.

  - Removed some previously deprecated facilities.

  - Deprecated `basic_io_object` and `deadline_timer`.

  - Added rvalue-qualified `operator``()` overloads to associating binders.

  - Added support for modular build structure.

  - Fixed `spawn``()` of functions that return move-only types.

  - Fixed `co_composed` to not require concepts support.

  - Fixed the epoll reactor to not try to re-register regular file descriptors after fork.

  - Fixed a leak in `ssl``::``detail``::``engine` move assignment.

  - Fixed compile error when `BOOST_ASIO_DISABLE_SMALL_BLOCK_RECYCLING` is defined.

  - Fixed compile error when using Clang 19.

  - Changed `thread_pool``::``join``()` to ensure that it stops threads that are subsequently added to the pool using `thread_pool``::``attach``()`.

  - Fixed the offsets passed to `io_uring_prep_write_fixed` and `io_uring_prep_read_fixed`, when they are used for stream-oriented operations.

  - Consult the [Revision History](/doc/libs/1_87_0/doc/html/boost_asio/history.html) for further details.

- [Atomic](/libs/atomic/):
  - Fixed initialization of atomic wait state list on memory reallocation. ([\#72](https://github.com/boostorg/atomic/issues/72))

- [Beast](/libs/beast/):
  - API Changes
    - Added `error_code` overload for `basic_fields``::``insert``()`.

    - Added overload for `websocket``::``stream``::``get_status` to query permessage-deflate status.

  - Fixes
    - Fixed use-after-move in calls to `net``::``dispatch` within `http``::``basic_stream`, which caused `bad_executor` exceptions on timeouts.

    - Removed mutating operations in initiating functions.

    - Fixed cancellation handling in `teardown_tcp_op`.

    - Set `state_` in `basic_parser` before calling `on_finish_impl`.

    - Removed static specifier from `clamp` functions.

    - Addressed `-``Wattributes` warnings in tests.

    - Addressed unreachable code warning in tests.

  - Improvements
    - Added forward declaration headers for types in `beast``::``http` namespace

    - Enabled `http``::``parser` to use `basic_fields``::``insert``()` with `error_code` overload

    - Applied `header_limit_` in `http``::``basic_parser` to trailer headers

    - Improved `http``::``basic_parser` to return `http``::``error``::``header_limit` earlier

    - Added support for modular boost build structure

  - Acknowledgements
    - Jackarain, Saleh Hatefinya, René Ferdinand Rivera Morell

- [Charconv](/libs/charconv):
  - Fixed support for PPC64LE architecture using `__ibm128` as long double format

  - Fixed intrinsic usage with Windows ARM64 platform

  - Fixed formatting of fixed with specified precision using `std``::``float128_t` or `__float128`

- [Cobalt](/libs/cobalt):
  - Removed requirement for get_executor to return a const ref

  - Added experimental/composition.

- [Compat](/libs/compat/):
  - Added `to_array``.``hpp` (contributed by Ruben Perez Hidalgo.)

- [Container](/libs/container/):
  - Added `stored_size` option to `static_vector` and `small_vector`.

  - Fixed bugs/issues:
    - [GitHub \#261: *"End iterators are not dereferencable"*](https://github.com/boostorg/container/issues/261).

    - [GitHub \#288: *"Compile error when using flat_map::extract_sequence with small_vector"*](https://github.com/boostorg/container/issues/288).

- [Filesystem](/libs/filesystem/):
  - As was announced in 1.84.0, Windows versions prior to 10 are no longer supported.

  - On Windows, `canonical` is now based on the `GetFinalPathNameByHandleW` WinAPI function. As a side effect, drive letters are converted to upper case, which makes the resulting paths more interoperable. ([\#325](https://github.com/boostorg/filesystem/issues/325))

  - **v4:** `canonical` no longer produces a trailing directory separator in the resulting path, if the input path has one.

  - If a `path` constructor or member function is called with an argument of a user-defined type that is convertible to `path` and one or more `Source` types, the conversion to `path` is now chosen by default. This may resolve argument conversion ambiguities in some cases, but may also result in a less optimal conversion path. If a different conversion path is desired, users are recommended to use explicit type casts. ([\#326](https://github.com/boostorg/filesystem/issues/326))

  - Added a workaround for `dirfd` being a macro on FreeBSD 9 and older. ([\#328](https://github.com/boostorg/filesystem/issues/328))

- [Flyweight](/libs/flyweight/index.html):
  - Added [`concurrent_factory`](/libs/flyweight/doc/tutorial/configuration.html#concurrent_factory), a factory based on a concurrent container from [Boost.Unordered](/libs/unordered/) that provides excellent performance in multithreaded scenarios.

  - Marked as `noexcept` those `boost``::``flyweight` operations previously documented as not throwing (issue [\#15](https://github.com/boostorg/flyweight/issues/15)).

- [Geometry](/libs/geometry/):
  - Improvements
    - Use using instead of typedef in part of the code

    - Modernize meta function with alias in part of the code

    - Add support for modular build structure

    - Complete CMake coverage (added github actions cmake tests)

    - Improve documentation workflow

    - Update Qt end WxWidgets examples

    - Add enumerate to prepare for 17 and 23

  - Breaking changes
    - Remove deprecated rescaling code

  - Solved issues
    - [\#1309](https://github.com/boostorg/geometry/issues/1309) Fix some missing qbk includes

    - [\#1226](https://github.com/boostorg/geometry/issues/1226) [\#1326](https://github.com/boostorg/geometry/issues/1326) Fix extra round on ring

    - [\#1293](https://github.com/boostorg/geometry/issues/1293) [\#1294](https://github.com/boostorg/geometry/issues/1294) [\#1295](https://github.com/boostorg/geometry/issues/1295) Fix traversal through non clustered rings

    - [\#893](https://github.com/boostorg/geometry/issues/893) [\#1299](https://github.com/boostorg/geometry/issues/1299) Fix blocking rings for non union conditions

    - [\#1342](https://github.com/boostorg/geometry/issues/1342) Fix discarding a start turn for combination with touch

    - [\#1288](https://github.com/boostorg/geometry/issues/1288) [\#1345](https://github.com/boostorg/geometry/issues/1345) Fixes in handling (imperfect) touch

    - [\#1279](https://github.com/boostorg/geometry/issues/1279) Fix covered_by incorrect results

    - Various fixes of errors and warnings

- [Iterator](/libs/iterator/):
  - `function_output_iterator` is now compliant with `std``::``output_iterator` concept. ([\#85](https://github.com/boostorg/iterator/issues/85))

- [Interprocess](/libs/interprocess/):
  - Decreased number of Boost dependencies from 11 (in total) to 7.

  - Deprecated `<``boost``/``interprocess``/``containers``/*.hpp>` headers. They were the original source of **Boost.Container** in 2011, but no longer maintained. As a long transition, Boost.Interprocess has maintained those headers for compatibility. They will be removed in a future Boost release.

  - Some workarounds for Cygwin were added. Regression tests now work on Cygwin64.

  - **ABI breaking**: `segment_manager` nows uses a new implementation that supports overaligned types and fixes some existing bugs. You can obtain the pre-Boost 1.87 ABI \#defining `BOOST_INTERPROCESS_SEGMENT_MANAGER_ABI` to `1` before including Boost.Interprocess headers.

  - Fixed bugs:
    - [GitHub \#152 (*"Handle EINTR in shared_memory_object"*)](https://github.com/boostorg/interprocess/issues/152).

    - [GitHub \#173 (*"Managed shared memory segment value not aligned"*)](https://github.com/boostorg/interprocess/issues/173).

    - [GitHub \#192 (*"managed_windows_shared_memory crash on destruction"*)](https://github.com/boostorg/interprocess/issues/192).

    - [GitHub \#199 (*"missing/misused m_is_wide in char_wchar_holder assignment operators"*)](https://github.com/boostorg/interprocess/issues/199).

    - [GitHub \#210 (*"Bug in boost::interprocess::ipcdetail::sync_handles::obtain_mutex"*)](https://github.com/boostorg/interprocess/issues/210).

    - [GitHub \#215 (*"Alignment problem with boost/interprocess/segment_manager on SPARC 32Bit"*)](https://github.com/boostorg/interprocess/issues/215).

    - [GitHub \#217 (*"managed_map_file find_or_construct does not return Cache aligned memory"*)](https://github.com/boostorg/interprocess/issues/217).

    - [GitHub \#230 (*"`interprocess``::``ipcdetail``::``intermodule_singleton` not working on MinGW"*)](https://github.com/boostorg/interprocess/issues/230).

    - [GitHub \#236 (*"` ``Floating`` ``point`` ``inaccuracies`` ``in`` `get_current_process_creation_time` ``lead`` ``to`` `intermodule_singleton\` failures"*)](https://github.com/boostorg/interprocess/issues/236).

- [JSON](/libs/json/):
  - Direct serialization.

  - Add GDB pretty printers for Boost.JSON types.

  - Conversion into structs ignores unknown keys.

  - Exception wrapping behaviour for `value_to` is simplified.

  - Deprecated initilaizer list behavior was removed.

  - Deprecated type aliases were removed.

  - Use correct 64bit full multiplication for MinGW on ARM64.

  - Fix parse_into handling of tuple of the wrong size.

  - Check for input size larger than allowed size of sequence.

  - Fix `value_ref` segfaulting on GCC 14.

- [LexicalCast](/libs/lexical_cast/):
  - Dropped dependency on Boost.Integer, leading to better compile times.

- [Log](/libs/log/):
  - Replaced Boost.Thread synchronization primitives with equivalents from the C++ standard library. This may improve multithreaded performance, but also has user-facing consequences:
    - Boost.Thread thread interruption is no longer supported. Boost.Log no longer has special treatment for the `thread_interrupted` exception that is used by Boost.Thread to implement thread interruption. This exception will be handled like any other exception. In particular, user-specified exception handlers may now be invoked with the `thread_interrupted` pending exception.

    - For timed waiting operations, timeouts are now using std::chrono time units. This means that the `ordering_window` named parameter that is supported by the `bounded_ordering_queue` and `unbounded_ordering_queue` classes now expects an `std``::``chrono``::``duration` value instead of `boost``::``posix_time``::``time_duration` from Boost.DateTime.

    - In case of errors indicated by thread synchronization primitives, `std``::``system_error` exception is thrown instead of Boost.Thread exception types.

  - Added support for C++ standard library lock types to `strictest_lock`.

- [Math](/libs/math/):
  - **Major update.**

  - Many special functions, and distribuitions now support CUDA (NVCC and NVRTC) and SYCL

  - Added mapairy, holtsmark, and saspoint5 distibutions, see [1163](https://github.com/boostorg/math/pull/1163)

  - Added landau distibution, see [1159](https://github.com/boostorg/math/pull/1159)

  - Fixed unexpected exception in beta quantile, see [1169](https://github.com/boostorg/math/issues/1169)

- [Move](/libs/move/index.html):
  - Fixed bugs:
    - [Git Issue \#56: *"Forward declarations of std types cause compilation errors on some platforms"*](https://github.com/boostorg/move/issues/56).

- [Mp11](/libs/mp11/):
  - Added `mp_lambda` (contributed by Joaquin M Lopez Munoz)

- [Multiprecision](/libs/multiprecision/):
  - Make `float128` trivially copyable

  - Make `__float128` a floating point type even in non-GNU modes

- [MySQL](/libs/mysql/):
  - **Breaking changes to experimental APIs**:
    - The thread-safety feature in `connection_pool` has been redesigned to overcome some design flaws found by user experience. The boolean option `thread_safe` has been added to `pool_params` (set to `false` by default). When set, some pool functions change behavior so they can be safely used concurrently. This works by internally creating a strand, dispatching to it when required, and re-wiring cancellation signals. When `pool_params``::``thread_safe` is `false`, the usual Asio executor semantics apply, with no overhead.

    - `pool_executor_params` has been removed, replaced by `pool_params``::``connection_executor` and `pool_params``::``thread_safe`.

    - The built-in timeout functionality in `connection_pool``::``async_get_connection` has been completely removed. This function now supports per-operation cancellation, so the same functionality can be achieved by using `asio``::``cancel_after`.

    - Destroying a `connection_pool` now cancels outstanding async operations, as other Asio I/O objects do. This prevents resource leaks: an outstanding `async_run` operation extends the pool's lifetime until the operation completes, which could cause the pool object to never get destroyed.

    - When an `async_get_connection` operation is cancelled before a connection is available, the operation now consistently fails with `client_errc``::``pool_not_running`, `client_errc``::``no_connection_available` or `client_errc``::``pool_cancelled`, depending on the pool state (previously, it would fail with either `client_errc``::``timeout` or the last error code encountered by the internal `async_connect` operations performed by the pool). This information is now included in the output diagnostics object.

    - `client_errc``::``timeout` and `client_errc``::``cancelled` have been removed.

    - Calling `async_get_connection` on a pool that is not running no longer fails immediately, but waits for `async_run` to be called.

    - `sequence` now returns an owning type. This makes it safe use with `with_params` in deferred async operations. `format_sequence_view` has been renamed to `format_sequence`.

    - `sequence` has been moved to a separate header, `boost``/``mysql``/``sequence``.``hpp`.

  - `any_connection`, client-side SQL formatting (including `format_sql` and `with_params`) and `connection_pool` have been promoted to stable APIs.

  - `any_connection` is now recommended for new code, instead of `connection` and its aliases `tcp_connection`, `tcp_ssl_connection` and `unix_connection`.

  - Added `with_params`, a new `ExecutionRequest` encapsulating a query template string and parameters to expand the query. When executed, it expands the query using client-side SQL formatting and sends it to the server for execution. This is the new recommended way to run simple queries with parameters.

  - Added `with_diagnostics`, an adapter completion token that transforms exceptions thrown by async functions to include `diagnostics` objects, matching how sync throwing functions work.

  - `with_diagnostics``(``asio``::``deferred``)` is now the default completion token for all operations in `any_connection` and `connection_pool`. This causes expressions like `co_await`` ``conn``.``async_connect``(``params``)` to behave identically to `conn``.``connect``(``params``)`. Note that `connection` and its type aliases haven't been updated to match this behavior.

  - Async functions in `connection_pool` now support per-operation cancellation.

  - All async operations now support `asio``::``cancel_after`, `asio``::``cancel_at` and similar completion tokens that require a bound executor to initiations passed to `asio``::``async_initiate`.

  - `connection` and `any_connection` now dispatch immediate completions through the token's immediate executor.

  - Fixed an issue that caused a crash when trying to use an `any_connection` that hasn't been previously connected.

  - Removed an incorrect `noexcept` specifier from a potentially throwing constructor in `field`.

  - Fixed an issue that could cause the write buffer size to exceed the configured buffer size limit.

  - Heavily updated the documentation and examples to be more relevant and reflect the new recommended best practices.

- [Optional](/libs/optional/):
  - **Breaking change.** Dropped support for C++03. C++11 is now the required minimum; at least some C++11 features.

  - Dropped dependency on Boost.Utility.

  - Dropped dependency on Boost.Predef.

  - Dropped dependency on Boost.StaticAssert.

  - Dropped dependency on Boost.Move.

  - A bit faster implementation of some relational operations.

  - **Warning.** In the future releases we intend to introduce the range interface into `optional`, so that `std``::``ranges``::``range``<``optional``<``T``>>` will be `true`. This may affect the overload resolution in programs that make decisions based on predicates such as `std``::``ranges``::``range`.

  - Tags `in_place_init` and `in_place_init_if` become `inline`` ``constexpr` and therewith leave smaller footprint in the executable. This addresses [issue \#103](https://github.com/boostorg/optional/issues/103).

- [PFR](/libs/pfr/):
  - `boost``::``pfr``::``for_each_field_with_name` function was added. Many thanks to [Lena](https://github.com/Baduit) for the [PR#171](https://github.com/boostorg/pfr/pull/171).

  - **Significant** compilation time improvement for structures with big size and small fields count. Many thanks to [Zachary Wassall](https://github.com/runer112) for the [PR#120](https://github.com/boostorg/pfr/pull/120).

  - Fixed `pragma` directives.

  - **Initial support for C++20 Modules**. See the docs for more info.

  - Fix unused variable warnings in core_name14_disabled.hpp. Thanks to [Anarthal (Rubén Pérez)](https://github.com/anarthal) for the [PR#183](https://github.com/boostorg/pfr/pull/183) and [PR#187](https://github.com/boostorg/pfr/pull/187).

  - Default limit for fields count in aggregate in C++17 was raised from 100 to 200.

  - Fixed warning about GCC not being aware of the -Wundefined-var-template.

  - Multiple minor improvement for compilation time.

- [Process](/libs/process):
  - (v2) Implemented cancellation of async_wait on windows.

  - (v2) Added FORCE_DISABLE_CLOSE_RANGE

  - (v2) ext: Multiple ext fixes for BSD & Solaris.

  - (v2) unavailable `ext` functions now compile and give an `operation_not_supported` error (includes IOS)

  - (v2) multiple link fixes

  - (v2) removed filesystem from the linked library - which filsystem library is used only affects header files now

  - (v1) Added deprecation notice for 1.88.

- [SmartPtr](/libs/smart_ptr/):
  - C++03 is no longer supported, a C++11 compiler is required. This includes GCC 4.8 or later, and MSVC 14.0 or later.

  - The functionality enabled by the macros `BOOST_SP_ENABLE_DEBUG_HOOKS`, `BOOST_SP_USE_STD_ALLOCATOR`, `BOOST_SP_USE_QUICK_ALLOCATOR`, `BOOST_AC_USE_SPINLOCK`, `BOOST_AC_USE_PTHREADS`, `BOOST_SP_USE_SPINLOCK`, and `BOOST_SP_USE_PTHREADS` has been deprecated and support for it will be removed in a future release.

- [Stacktrace](/libs/stacktrace/):
  - `Boost``::``stacktrace_from_exception` CMake target was added. Many thanks to [int mian](https://github.com/void-mian) for the [PR#189](https://github.com/boostorg/stacktrace/pull/189).

  - Don't export `boost_stacktrace_impl_return_nullptr` for static build on MSVC. Many thanks to [huangqinjin](https://github.com/huangqinjin) for the [PR#186](https://github.com/boostorg/stacktrace/pull/186).

  - Fixed autolinking with `ole32``.``lib` and `Dbgeng``.``lib` while using clang under Windows OS.

  - Fixed missing namespace in docs. Thanks to [Mats Taraldsvik](https://github.com/meastp) for the [PR#181](https://github.com/boostorg/stacktrace/pull/181).

  - Fixed missing include for `std``::``exception`. Thanks to [Julien Schueller](https://github.com/jschueller) for the [PR#178](https://github.com/boostorg/stacktrace/pull/178).

  - Fixed type conversions errors reported by GCC. Thanks to [agent_J](https://github.com/jplcz) for the [PR#175](https://github.com/boostorg/stacktrace/pull/175).

  - Fixed setting B2 `from_exception` feature from CLI. Thanks to [Dmitry Arkhipov](https://github.com/grisumbras) for the [PR#194](https://github.com/boostorg/stacktrace/pull/194).

- [STLInterfaces](/libs/stl_interfaces/):
  - Correct misdocumented requirements for sequence container `swap`; the expected return type is `void`, not `bool`. ([\#71](https://github.com/boostorg/stl_interfaces/issues/71))

  - Add `[[``no_unique_address``]]` to the data members of the adaptors in `view_adaptor``.``hpp`. ([\#65](https://github.com/boostorg/stl_interfaces/issues/65))

  - Enable deducing `this` for recent versions of Clang and MSVC that support it, but do not advertise that support via `__cpp_explicit_this_parameter`. ([PR#68](https://github.com/boostorg/stl_interfaces/pull/68))

- [Test](/libs/test/):
  - Fixed support for clang tidy with dummy conditions [PR#348](https://github.com/boostorg/test/pull/348)

  - Fixed dynamic linking with clang [PR#431](https://github.com/boostorg/test/pull/431)

- [Unordered](/libs/unordered/):
  - **Major update.**

  - Added concurrent, node-based containers `boost``::``concurrent_node_map` and `boost``::``concurrent_node_set`.

  - Added `insert_and_visit``(``x``,`` ``f1``,`` ``f2``)` and similar operations to concurrent containers, which allow for visitation of an element right after insertion (by contrast, `insert_or_visit``(``x``,`` ``f``)` only visits the element if insertion did *not* take place).

  - Made visitation exclusive-locked within certain `boost``::``concurrent_flat_set` operations to allow for safe mutable modification of elements ([PR#265](https://github.com/boostorg/unordered/pull/265)).

  - In Visual Studio Natvis, supported any container with an allocator that uses fancy pointers. This applies to any fancy pointer type, as long as the proper Natvis customization point "Intrinsic" functions are written for the fancy pointer type.

  - Added GDB pretty-printers for all containers and iterators. For a container with an allocator that uses fancy pointers, these only work if the proper pretty-printer is written for the fancy pointer type itself.

  - Fixed `std``::``initializer_list` assignment issues for open-addressing containers ([PR#277](https://github.com/boostorg/unordered/pull/277)).

  - Allowed non-copyable callables to be passed to the `std``::``initializer_list` overloads of `insert_``{``and``|``or``}``_``[``c``]``visit` for concurrent containers, by internally passing a `std``::``reference_wrapper` of the callable to the iterator-pair overloads.

- [URL](/libs/url/):
  - feat: set_params supports encoding_opts. ([\#856](https://github.com/boostorg/url/issues/856))

  - refactor: no deprecated variant2 alias from API. ([\#857](https://github.com/boostorg/url/issues/857))

  - refactor: query_rule consistent interpretation. ([\#864](https://github.com/boostorg/url/issues/864))

- [UUID](/libs/uuid/):
  - Restored the ability to construct a `constexpr`` ``uuid` that was inadvertently lost in 1.86.

- [Wave](/libs/wave/):
  - Fixed bugs:
    - [GitHub \#220: *"Seg fault under C++20 and empty stringify parameter"*](https://github.com/boostorg/wave/issues/220). Thanks [Lu HongYi](https://github.com/jwnhy/)

    - [GitHub \#222: *"No line directive if first line of included file is blank"*](https://github.com/boostorg/wave/issues/222). Thanks [Nick Nobles](https://github.com/njnobles)

  - Build improvements including modular build support, thanks [René Rivera](https://github.com/grafikrobot)

### Compilers Tested

Boost's primary test compilers are:

- Linux:
  - Clang, C++03: 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang, C++11: 3.4, 11.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang, C++14: 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 5.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang, C++17: 6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - Clang, C++20: 11.0.0, 12.0.0, 13.0.0, 14.0.0, 15.0.0

  - GCC, C++03: 4.6.3, 11, 12

  - GCC, C++11: 4.7.3, 4.8.5, 11, 12

  - GCC, C++14: 5.4.0, 6.4.0, 7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC, C++17: 7.3.0, 8.0.1, 9.1.0, 11, 12

  - GCC, C++20: 8.0.1, 9.1.0, 10, 11, 12

- OS X:
  - Apple Clang, C++03: 11.0.3

  - Apple Clang, C++11: 11.0.3

  - Apple Clang, C++14: 11.0.3

  - Apple Clang, C++17: 11.0.3

  - Apple Clang, C++20: 11.0.3

- Windows:
  - Visual C++: 10.0, 11.0, 12.0, 14.0, 14.1, 14.2, 14.3

### Acknowledgements

Marshall Clow, Glen Fernandes and Ion Gaztañaga managed this release.

Copyright Rene Rivera 2006-2007.
