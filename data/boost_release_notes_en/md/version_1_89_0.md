# Version 1.89.0

## Version 1.89.0

August 14th, 2025 02:16 GMT

[Documentation](/doc/libs/1_89_0/)

| Platform | File | SHA256 Hash |
|----|----|----|
| unix | [boost_1_89_0.tar.bz2](https://archives.boost.io/release/1.89.0/source/boost_1_89_0.tar.bz2) | 85a33fa22621b4f314f8e85e1a5e2a9363d22e4f4992925d4bb3bc631b5a0c7a |
|  | [boost_1_89_0.tar.gz](https://archives.boost.io/release/1.89.0/source/boost_1_89_0.tar.gz) | 9de758db755e8330a01d995b0a24d09798048400ac25c03fc5ea9be364b13c93 |
| windows | [boost_1_89_0.7z](https://archives.boost.io/release/1.89.0/source/boost_1_89_0.7z) | d8b0c1d593d68fe359616aa2fae4b3e258ca1f90ed57eb46c5494c29cdd1d49d |
|  | [boost_1_89_0.zip](https://archives.boost.io/release/1.89.0/source/boost_1_89_0.zip) | 77bee48e32cabab96a3fd2589ec3ab9a17798d330220fdd8bde6ff5611b4ccde |

Downloads {.download-table}

\* The download links are supported by grants from [The C++ Alliance](https://cppalliance.org/).  
  

### New Libraries

- [Bloom](/libs/bloom/): Bloom filters, from Joaquín M López Muñoz.

### Updated Libraries

- [Any](/libs/any/):
  - **Initial support for C++20 Modules**. See the docs for more info.

- [Asio](/libs/asio/):
  - Added allocator constructors to `execution_context`, `io_context` and `thread_pool`, with the supplied allocator being used for allocating objects associated with the execution context.

  - Added a new configuration parameter "timer" / "heap_reserve" that may be used to reserve space in the vector used for a timer queue's heap.

  - Added a new configuration parameter "resolver" / "threads" that specifies the number of internal threads used by `async_resolve` to emulate asynchronous address resolution.

  - Removed `deadline_timer`, `basic_deadline_timer` and `time_traits` from the convenience header `boost/asio.hpp`.

  - Ensured that the Windows named pipes created by `connect_pipe` use unique names that do not conflict if Asio is used in multiple, independent plug-in DLLs.

  - Changed `BOOST_ASIO_CONCURRENCY_HINT_SAFE` to be consistent with the `io_context` default constructor.

  - Fixed the documentation for `BOOST_ASIO_CONCURRENCY_HINT_UNSAFE_IO` to reflect that registration locking is still enabled.

  - Added separate `b2` and `cmake` build targets for optional dependencies.

  - Added the `[[``noreturn``]]` attribute to `boost``::``asio``::``detail``::``throw_exception`.

  - Fixed `co_spawn` to adhere to the asynchronous operation requirement for non-reentrant invocation of the completion handler.

  - Added a documentation note on `basic_signal_set` async signal safety.

  - Fixed various minor compilation errors on different platforms.

  - Consult the [Revision History](/doc/libs/1_89_0/doc/html/boost_asio/history.html) for further details.

- [Atomic](/libs/atomic/):
  - Added TSAN instrumentation in asm-based x86, AArch32, AArch64 and PPC backends. This silences TSAN false errors for code using Boost.Atomic for thread synchronization.

  - Following the announcement in Boost 1.84, removed support for Windows versions older than Windows 10.
    - A note to MinGW-w64 users. Since Windows SDK headers on MinGW-w64 define `_WIN32_WINNT` to an older Windows version by default, you may need to define `_WIN32_WINNT``=``0x0A00` or `BOOST_USE_WINAPI_VERSION``=``0x0A00` when compiling Boost.Atomic and the code that uses Boost.Atomic.

  - Support for Windows CE is deprecated and will be removed in a future release.

  - Added support for timed waiting operations.

  - Exposed `thread_pause` operation, which can be used as a backoff measure in spin loops. Added support for PowerPC and improved support for AArch64 in `thread_pause`.

  - Removed `BOOST_ATOMIC_NO_ATOMIC_FLAG_INIT` macro definition. Since the library now requires C++11, `BOOST_ATOMIC_FLAG_INIT` is always supported.

  - Enabled bitwise operations for atomic enumerations. This can be useful when enumerations are used to implement bit masks.

- [Beast](/libs/beast/):
  - Fixes
    - Conditionally defined `immediate_executor_type` in `async_base`.

    - Added missing `cstdint` header to `detail``/``cpu_info``.``hpp`.

    - Fixed `std``::``is_trivial` deprecation warnings.

    - `handshake_timeout` now applies to closing handshakes during reads.

  - Improvements
    - Replaced `detail``/``work_guard``.``hpp` with `net``::``executor_work_guard`.

    - Fixed portability issues for building tests in MinGW.

  - Documentation
    - Removed moved sections from documentation.

    - Removed superfluous log messages from tests.

  - Acknowledgements
    - yliu1021

- [Charconv](/libs/charconv):
  - Fixed a performance degradation with `from_chars` for integer types

  - Fixed rounding and trailing decimal place bugs with `to_chars` for specified precisions with floating point types

- [Cobalt](/libs/cobalt/):
  - Move assign fixed for generator & promise.

  - Fixed internal exceptions

  - Added IO library. Cobalt.io provides a large subset of asio as a compiled library.

- [Compat](/libs/compat/):
  - Added `move_only_function``.``hpp`.

- [ContainerHash](/libs/container_hash/):
  - Added the `hash_is_avalanching` trait class.

- [Conversion](/libs/conversion/):
  - Added an ability to use `polymorphic_downcast` and `polymorphic_cast` in constexpr (requires C++20).

- [Core](/libs/core/):
  - Fixed `bit_ceil` to return 1 for input 0 as per specification. ([PR#199](https://github.com/boostorg/core/pull/199))

  - Added support for `std``::``format` to `boost``::``core``::``string_view`. ([\#190](https://github.com/boostorg/core/issues/190))

- [Detail](/libs/detail/):
  - Operators generated by `BOOST_BITMASK` now use underlying type of the enum to implement bitwise operators. The operators are marked `noexcept` and `constexpr`, when possible.

  - The function `bitmask_set` generated by `BOOST_BITMASK` is marked deprecated. In a future release, `BOOST_BITMASK` will stop producing this function. Users are recommended to use double negation (`!!``mask`) to test if the value is zero. This affects e.g. enums defined in Boost.Filesystem.

- [DLL](/libs/dll/):
  - Fixed compiling and exporting on Cygwin. Many thanks to [Luohao Wang](https://github.com/Luohaothu) for the PR!

  - Fixed building on FreeBSD. Thanks to [ash](https://github.com/agokhale) for the bug report!

  - Added `BOOST_DLL_USE_STD_FS` CMake option to match the preprocessor option. Thanks to [Yury Bura](https://github.com/yurybura) for the PR!

- [Filesystem](/libs/filesystem/):
  - Corrected ASAN warnings about comparing pointers to potentially unrelated objects in `path``::``append`. ([\#335](https://github.com/boostorg/filesystem/issues/335))

- [Geometry](/libs/geometry/):
  - Major improvements
    - [PR#1369](https://github.com/boostorg/geometry/pull/1369) Rewrite of traversal

    - [PR#1402](https://github.com/boostorg/geometry/pull/1402) Add geometry polyhedral surface

  - Improvements
    - [PR#1404](https://github.com/boostorg/geometry/pull/1404) Performance improvements in buffer

    - [PR#1405](https://github.com/boostorg/geometry/pull/1405) Avoid static variables and functions in header files

  - Breaking changes
    - [PR#1401](https://github.com/boostorg/geometry/pull/1401) Remove deprecated headers

  - Solved issues
    - [\#1221](https://github.com/boostorg/geometry/issues/1221) Difference with rectilinear multipolygon with integer coordinates produces invalid polygon with disconnected interior

    - [\#1295](https://github.com/boostorg/geometry/issues/1295) Wrong result in intersection (result polygon is equal to the biggest of the input polygons)

    - [\#1349](https://github.com/boostorg/geometry/issues/1349) Difference of polygons giving wrong result

    - [\#1382](https://github.com/boostorg/geometry/issues/1382) Buffer operation creates self-intersection

    - Various fixes of errors and warnings

- [Hash2](/libs/hash2/):
  - Added Blake2 algorithm (`blake2s_256`, `blake2b_512`).

  - Added XXH3 algorithm (`xxh3_128`).

- [Iterator](/libs/iterator/):
  - Fixed `filter_iterator` copy/converting constructor, which could previously produce an invalid iterator. ([\#92](https://github.com/boostorg/iterator/issues/92))

  - Removed usage of `is_trivial` in `iterator_facade` as it is deprecated in C++26. ([\#93](https://github.com/boostorg/iterator/issues/93))

  - `iterator_facade``::``operator``[]` now always returns a proxy rather than conditionally returning a value or a proxy. This allows users to bind a reference to the result of the operator, regardless of whether the value type is trivially-copyable. ([\#61](https://github.com/boostorg/iterator/issues/61))

  - The proxy returned by `iterator_facade``::``operator``[]` now supports forwarding dereferencing operators to the referenced value. This allows `it``[``n``]->``foo``()` and `(*``it``[``n``]).``foo``()` expressions to compile.

  - The proxy returned by `iterator_facade``::``operator``[]` now implementes perfect forwarding in its assignment operator.

- [JSON](/libs/json/):
  - Revamped documentation.

  - Optionals that are ranges are categorised as optionals.

  - Described class support is enabled for types with bases.

- [Log](/libs/log/):
  - Added support for `BOOST_LOG_WITHOUT_ASIO` configuration macro, which can be used to remove the dependency on Boost.Asio and disable the related functionality.

  - Use locale-independent formatting of the file counter in `text_file_backend` when composing log file names. This fixes failures in the subsequent parsing of the file names in `file_collector``::``scan_for_files`. ([PR#246](https://github.com/boostorg/log/pull/246))

  - Added a new `wrap_filter` utility that simplifies injecting user-defined function objects in filtering expressions. ([\#195](https://github.com/boostorg/log/issues/195))

- [Math](/libs/math/):
  - Add explicit C++14 `<``type_traits``>` and `constexpr` requirement to builds

  - Collected fixes for GPU support on a variety of platforms

  - Fix lower incomplete gamma function with x = 0

  - Fix the external archive error in the jSO algorithm

  - Fix numeric underflow in ibeta

  - Fix inverse ibeta for large values of a and b

  - Fix variadic functions to make them safe with C++26

- [MQTT5](/libs/mqtt5/):
  - Fixed incorrect parsing of URI paths in the list of brokers ([\#31](https://github.com/boostorg/mqtt5/issues/31)).

  - Default Maximum Packet Size now explicitly set in the `CONNECT` packet. ([\#33](https://github.com/boostorg/mqtt5/issues/33)).

  - Fixed high CPU usage with large Maximum Packet Size values ([\#33](https://github.com/boostorg/mqtt5/issues/33)).

- [Multiprecision](/libs/multiprecision/):
  - **Major update.**

  - Adds a new backend type: `cpp_double_fp_backend`

  - Fixes a namespace collision with Boost.Serialization

- [MySQL](/libs/mysql/):
  - The `caching_sha2_password` authentication plugin can now be used without TLS. This is the default in MySQL 8 and above. Plaintext connections that attempt to use this plugin no longer fail with `client_errc``::``auth_plugin_requires_ssl` ([\#313](https://github.com/boostorg/mysql/issues/313)).

  - Fixed a problem causing `client_errc``::``incomplete_message` to be returned during connection establishment when the target database does not exist and the `caching_sha2_password` is used. The appropriate server-generated diagnostic is now returned. See issues [\#468](https://github.com/boostorg/mysql/issues/468) and [\#488](https://github.com/boostorg/mysql/issues/488).

  - The handshake algorithm is now more resilient to protocol violations ([\#469](https://github.com/boostorg/mysql/issues/469)).

  - Fixed a build failure with gcc-15 due to a missing include ([PR#475](https://github.com/boostorg/mysql/pull/475)). Thanks [hhoffstaette](https://github.com/hhoffstaette) for the PR.

  - Added [benchmarks against the official drivers](https://www.boost.org/doc/libs/master/libs/mysql/doc/html/mysql/benchmarks.html).

  - Optimized `metadata` representation to be faster to construct and take less memory ([\#461](https://github.com/boostorg/mysql/issues/461)).

- [PFR](/libs/pfr/):
  - Rewrite C++20 module following the new recommended Boost practice. See the docs for more info.

  - Fixed C++26 compilation on modern clang compilers. Thanks to [Valery Mironov](https://github.com/MBkkt) for the report!

  - Support types that use 'Arrays of Length Zero' compiler extension.

  - Fixed typos. Thanks to [Egor](https://github.com/TryKuhn) for highlighting the issues!

  - Return `std``::``array``<``std``::``string_view``,`` ``0``>` type for `boost``::``pfr``::``names_as_array``(``empty_struct``{})` to allow compilation of `for`` ``(``std``::``string_view`` ``name`` ``:`` ``boost``::``pfr``::``names_as_array``(``empty_struct``{}))`. Many thanks to [sabudilovskiy](https://github.com/sabudilovskiy) for the bug report!

- [process](/libs/process/):
  - Added `v1``.``hpp` to emulate v1 `process``.``hpp` include.

  - Fix to windows path escaping

  - Fixed exit-code issue wehre terminate & async_wait lead to a loss of the exit-code value.

- [Random](/libs/random/):
  - Fix NAN being generated by `beta_distribution`

  - Improve the performance of `beta_distribution``::``operator``()`

- [System](/libs/system/):
  - The stub compiled library has been removed; System has been header-only since release 1.69.

  - This may affect `CMakeLists.txt` files containing `find_package(Boost COMPONENTS system ...)`. The easiest fix is to just remove `system` from the list of components as it's no longer required. If compatibility with Boost releases earlier than 1.69 is to be preserved, one can use `find_package(Boost COMPONENTS ... OPTIONAL_COMPONENTS system)`.

- [TypeIndex](/libs/type_index/):
  - **Initial support for C++20 Modules**. See the docs for more info.

- [Unordered](/libs/unordered/):
  - Deprecated `boost``::``unordered``::``hash_is_avalanching` is now a using-declaration of `boost``::``hash_is_avalanching` in `<``boost``/``container_hash``/``hash_is_avalanching``.``hpp``>`. Use that header directly instead. `<``boost``/``unordered``/``hash_traits``.``hpp``>` will be removed in the future.

  - Added `pull``(``const_iterator``)` to open-addressing containers. This operation allows for efficient removal and retrieval of an element via move construction.

- [Histogram](/libs/histogram/):
  - Update CMake minimum version and Python detection in CMake

  - Improve documentation
    - Add example on how to make an axis which accepts multiple value types that are not implicitly convertible

    - Show how to use `histogram``::``fill` with a multidimensional histogram efficiently when data per dimension is already available as contiguous data

  - Don't use deprecated form of user-defined literal operator

  - Add support for modular build structure with b2

  - Fixed warnings in MSVC about narrowed types

  - Added collector accumulator, which stores all values in a bin

  - Internal changes to tests and classes in detail namespace

### Updated Tools

- [Build](/tools/build/):
  - Includes release of [B2 version 5.3.2](/tools/build/doc/html/#_version_5_3_2).

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
