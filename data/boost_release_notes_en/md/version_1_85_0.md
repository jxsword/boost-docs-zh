# Version 1.85.0

## Version 1.85.0

April 15th, 2024 17:38 GMT

[Documentation](/doc/libs/1_85_0/)

| Platform | File | SHA256 Hash |
|----|----|----|
| unix | [boost_1_85_0.tar.bz2](https://archives.boost.io/release/1.85.0/source/boost_1_85_0.tar.bz2) | 7009fe1faa1697476bdc7027703a2badb84e849b7b0baad5086b087b971f8617 |
|  | [boost_1_85_0.tar.gz](https://archives.boost.io/release/1.85.0/source/boost_1_85_0.tar.gz) | be0d91732d5b0cc6fbb275c7939974457e79b54d6f07ce2e3dfdd68bef883b0b |
| windows | [boost_1_85_0.7z](https://archives.boost.io/release/1.85.0/source/boost_1_85_0.7z) | 16d16b9658753117c1434e5450c5eac194957f4b6d0b390b9d07900d37c115a4 |
|  | [boost_1_85_0.zip](https://archives.boost.io/release/1.85.0/source/boost_1_85_0.zip) | e712fe7eb1b9ec37ac25102525412fb4d74e638996443944025791f48f29408a |

Downloads {.download-table}

\* The download links are supported by grants from [The C++ Alliance](https://cppalliance.org/).  
  

### Known Issues

These are patches from library authors which were found too late to be fixed in the release.

- Container
  - flat_map/multimap containers can crash or return invalid results in some compilers due to UB in the library, see [\#273](https://github.com/boostorg/container/issues/273). [Patch](/patches/1_85_0/0001-container-fix-flat_map.patch).

### New Libraries

- [Charconv](/libs/charconv/): A high quality implementation of `<``charconv``>` in C++11, from Matt Borland.

- [Scope](/libs/scope/): A collection of scope guard utilities and a `unique_resource` wrapper, from Andrey Semashev.

### Updated Libraries

- [Asio](/libs/asio/):
  - Fixed the `async_result` primary template's concept checking to correctly handle lvalue-qualified completion signatures.

  - Fixed some compile errors that could arise when using the `bind_allocator`, `bind_executor`, `bind_immediate_executor` and `bind_cancellation_slot` completion token adapters to adapt each other.

  - Changed the `experimental``::``ranged_parallel_group` operation so that it moves the `completion_order` vector when invoking the completion handler.

  - Fixed some warnings about deprecated implicit copy constructors on `ip``::``basic_resolver_query`, `io_context``::``strand`, and `coroutine`.

  - Updated the version specification used to initialise Winsock.

  - Fixed `co_spawn` to correctly propagate exceptions resulting from cancellation to the completion handler.

  - Added calls to `std``::``launder` to fix undefined behaviour in `awaitable``<>` internal storage.

  - Added missing handling of the `file_base``::``append` flag in the Windows implementation of file support.

  - Updated the socket and descriptor implementations to add more cases where they will fall back to `fcntl` if a call to `ioctl` fails.

  - Fixed the `boost/asio/experimental/parallel_group.hpp` header so that it is self-contained.

  - Fixed a compile error that occurred when channels and `experimental``::``coro` were both used in the same translation unit.

  - Added missing CancellationSlot type requirements to documentation.

  - Fixed the documentation hyperlinks for the deduced return types of asynchronous operations' initiating functions.

  - Other minor documentation updates.

- [Atomic](/libs/atomic/):
  - Added support for `pause` instruction on RISC-V. ([PR#65](https://github.com/boostorg/atomic/pull/65))

- [Beast](/libs/beast/):
  - API Changes
    - The status code list has been updated to conform with the IANA registry.

  - Fixes
    - Unreachable code warning in `buffers_cat``.``hpp`.

    - Connection error handling in `websocker_server_awaitable` example.

    - Concurrent calls to `async_write` in advanced server examples.

    - zlib name conflicts with minizip.

    - host string should be updated after `SSL_set_tlsext_host_name``()`.

  - Improvements
    - `asio``::``associator` is specialized for `bind_wrapper` and `bind_front_wrapper`.

    - Add non-allocating overload for error category message function.

  - Documentation
    - Specifies when calling `http``::``message``::``prepare_payload``()` is optional.

    - Operations affected by `basic_stream``::``expires_after``()`.

    - `teardown``()` and `async_teardown``()` are customization points.

    - Moving or copying `http``::``serializer` after first usage is undefined behaviour.

    - `websocket``::``permessage_deflate` should be configured before performing the WebSocket handshake.

    - `bytes_transferred` in http reads operations reports the number of bytes consumed by the HTTP parser.

  - Acknowledgements
    - Emile Cormier, JohannesWilde, yhzx233

- [Bimap](/libs/bimap/):
  - Fixed heterogeneous lookup for side collections ([PR#42](https://github.com/boostorg/bimap/pull/42)).

- [Bind](/libs/bind/):
  - C++03 is no longer supported; a C++11 compiler is required. (This includes GCC 4.7 or later, and MSVC 12.0 (VS 2013) or later.)

- [Conversion](/libs/conversion/):
  - Removed outdated mentions of `boost``::``lexical_cast` that is not part of the library any more. Thanks to [Danil Sidoruk](https://github.com/eoan-ermine) for the PR [PR#28](https://github.com/boostorg/conversion/pull/28)!

- [Core](/libs/core/):
  - Added a new `boost``/``core``/``functor``.``hpp` header with a `functor` class template for wrapping a raw function into a function object class.

  - Changed `null_deleter`, `fclose_deleter` and checked deleter definitions so that they don't bring namespace `boost` into argument-dependent lookup. Users may need to either explicitly qualify the namespace of the called function or add a `using`-declaration.

- [Filesystem](/libs/filesystem/):
  - `path``::``generic_path` and `path``::``generic_string` methods now remove duplicate directory separators in the returned paths.

  - **v4:** `path``::``generic_path`, `path``::``generic_string`, `path``::``make_preferred` and `path``::``lexically_normal` avoid converting between backslashes and forward slashes in path root names. For example, on Windows, `path``(``"\\\\\\\\?\\\\c:\\\\foo"``).``generic_string``()` now returns "\\?\c:/foo" instead of "//?/c:/foo". Similarly, `path``(``"\\\\\\\\host/share/foo/.."``).``lexically_normal``()` now returns "\\host\share".

  - **v4:** `equivalent` now indicates error if either one of the paths doesn't exist.

  - **v4:** `absolute` now returns a path with a trailing directory separator when the input path has an empty `relative_path``()`. ([\#301](https://github.com/boostorg/filesystem/issues/301))

  - Added a `unique_path` overload taking a single `error_code``&`` ``ec` argument. The overload generates a unique path using the default path model.

  - `weakly_canonical` now produces an absolute path if the input path is relative and contains no elements that exist in the filesystem. ([\#300](https://github.com/boostorg/filesystem/issues/300))

  - Added a new `copy_options``::``ignore_attribute_errors` option for `copy_file` and `copy` operations. The new option allows to ignore possible errors while copying file attributes. ([\#179](https://github.com/boostorg/filesystem/issues/179))

  - On Linux, `copy_file` backends based on `sendfile` and `copy_file_range` system calls will attempt to preallocate storage for the target file. This may reduce filesystem fragmentation and provide early error indication if there is not enough free space. Not all filesystems support this feature; file copying proceeds if storage preallocation is not supported.

  - On POSIX systems that support [`fdopendir`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fdopendir.html), `openat` and related APIs defined in POSIX.1-2008, as well as on Windows, `recursive_directory_iterator` now uses file descriptors/handles instead of paths to query the file statuses and open nested directories during iteration. This makes directory iteration more resilient to concurrent modifications of the filesystem.

  - Removed APIs that were previously declared deprecated. In particular, `path` and `recursive_directory_iterator` member functions, `is_regular`, `copy_directory`, `symbolic_link_exists`, `complete`, `copy_option`, `symlink_option`, as well as `boost``/``filesystem``/``convenience``.``hpp` and `boost``/``filesystem``/``path_traits``.``hpp` headers were removed. Possible replacements for the removed components are mentioned in the documentation.

  - Support for `path` construction, assignment and appending from container types (e.g. `std``::``vector``<``char``>`) is now disabled by default. Users can still enable this functionality by defining `BOOST_FILESYSTEM_DEPRECATED`. This functionality remains deprecated and will be completely removed in a future release.

- [Function](/libs/function/):
  - C++03 is no longer supported; a C++11 compiler is required. (This includes GCC 4.7 or later, and MSVC 12.0 (VS 2013) or later.)

- [Geometry](/libs/geometry/):
  - Improvements
    - [PR#1247](https://github.com/boostorg/geometry/pull/1247) Use if constexpr macro instead of condition macro

    - [PR#1242](https://github.com/boostorg/geometry/pull/1242) Pass strategy to sort by side

    - [PR#1234](https://github.com/boostorg/geometry/pull/1234) Add cmake files for clang/mac/darwin/arm64

  - Solved issues
    - [\#1231](https://github.com/boostorg/geometry/issues/1231), [\#1244](https://github.com/boostorg/geometry/issues/1244) Fix invalid set operations for CCW polygons

    - [\#1259](https://github.com/boostorg/geometry/issues/1259) Fix compilation error with CUDA NVCC compiler

    - [\#1250](https://github.com/boostorg/geometry/issues/1250) Fix buffer of linestring returning incorrect inner polygon

    - [\#1230](https://github.com/boostorg/geometry/issues/1230) Fix union operation perturbing a point and returning wrong result

    - [\#1229](https://github.com/boostorg/geometry/issues/1229) Fix union producing self intersections

    - [PR#1248](https://github.com/boostorg/geometry/pull/1248) Fix buffer issue by setting turns in closed clusters as non traversable

    - [PR#1246](https://github.com/boostorg/geometry/pull/1246) Fix compilation of converter and is_base_of

    - Various fixes of errors and warnings

- [Iterator](/libs/iterator/):
  - Support for C++03 is deprecated and will be removed in a future release.

- [JSON](/libs/json/):
  - Boost.Endian is now used to deal with endianness.

  - Aliases to Boost.System and Boost.Container components are deprecated and **will be completely removed in 1.87.0**.

  - Conversion of described classes supports private members.

  - Rvalue reference overload for `visit`.

  - Add conversion support for path-like types.

  - Parsing into described classes correctly considers inherited members.

  - Conversion of self-referential sequences is disabled.

  - Fixed reference handling in visit.

- [LEAF](/libs/leaf/):
  - New API for transporting of error objects and exceptions between threads: `try_capture_all`.

  - `result``<``T``>` able to transport exceptions captured via `try_capture_all`.

  - `result``<``T``>` transporting dynamically captured error objects with improved efficiency.

  - Old `make_shared_context`/`capture` APIs are deprecated, will be removed in the next release.

  - Removed support for transporting of dynamicaly captured error objects in exceptions.

- [LexicalCast](/libs/lexical_cast/):
  - Significant rewrite of the internal logic to separate optimized and C++ Standard Library IO-based streams:
    - C++ Standard Library based streams now constructed in less cases leading to **better performance**;

    - less template instantiations and simpler code;

    - always use `std``::``char_traits` (do not use custom traits from input/output types as it leads to linktime or runtime errors);

    - fixed missuse of forward declared boost::array (thanks to [13steinj](https://github.com/13steinj) for the report [\#64](https://github.com/boostorg/lexical_cast/issues/64)!);

    - support for `volatile` input types was dropped, following the C++ Standard Library trend.

  - Optimized conversions from std::basic_string_view and boost::basic_string_view [\#30](https://github.com/boostorg/lexical_cast/issues/30).

  - Dropped dependency on Boost.NumericConversion and Boost.MPL. Fixed some cases of converting floting point types to arithmetics.

  - The library now compiles and works fine with `-``fno``-``sanitize``-``recover``=``integer` [\#45](https://github.com/boostorg/lexical_cast/issues/45).

- [Locale](/libs/locale/):
  - Fix linker issues due to missing typeinfo for `char8_t` in C++20 mode

  - Fix IConv compile flags when using ICU that has a bundled IConv

  - `collator` now throws on construction, if at all, as documented

  - `collator` no longer derives from `std``::``collator` to avoid possible type confusing when it isn't available for the current backend [PR#216](https://github.com/boostorg/locale/pull/216)

  - Throw an exception when a faulty IConv library is detected (e.g. on some MacOS versions) instead of looping indefinitely [PR#218](https://github.com/boostorg/locale/pull/218)

  - Reduce resolution of `date_time` to seconds as milliseconds where not easily available causing confusion [\#221](https://github.com/boostorg/locale/issues/221)

- [Math](/libs/math/):
  - Added a new collection of optimization algorithms:
    - Differential Evolution [PR#1062](https://github.com/boostorg/math/pull/1062)

    - JSO [PR#1065](https://github.com/boostorg/math/pull/1065)

    - Random Search [PR#1071](https://github.com/boostorg/math/pull/1071)

    - CMA-ES [PR#1074](https://github.com/boostorg/math/pull/1074)

  - Fix Divide by 0 warning in NCF survival function

  - Fix constexpr depth limits of ccmath::floor/ceil fail for large arguments

  - Improve accuracy of quartic_roots

  - Fix cstdfloat numeric limits detection macro for libstdc++14

  - Fix for MSVC UCRT defining \_Complex_I in complex.h when using C++14 [PR#1060](https://github.com/boostorg/math/pull/1060)

  - Improve cstdfloat iostream [PR#1066](https://github.com/boostorg/math/pull/1066)

  - Fix redefnition of Boost.Config macros when using standalone mode in a non-standalone environment

  - Significant improvements to code coverage with associated bug fixes

- [MSM](/libs/msm/):
  - **Major Update**. Backend update (back11). Requires C++ 11. The documentation now uses it as default.

  - **Big new feature**. New front-end (PlantUML). Requires C++ 20

  - Various Bugfixes (compiler errors and warnings, priority of deferred events)

- [Multi-index Containers](/libs/multi_index/):
  - Fixed documentation errors.

- [Multiprecision](/libs/multiprecision/):
  - Fix deprecation warnings from C++23 \<limits\> [PR#575](https://github.com/boostorg/multiprecision/pull/575)

  - Fix cpp_bin_float for small bit counts [PR#577](https://github.com/boostorg/multiprecision/pull/577)

  - Fix -Wpessimizing-move [PR#580](https://github.com/boostorg/multiprecision/pull/580)

  - Add covecov runs

  - Reduce truncation in cpp_dec_float multiplication [PR#585](https://github.com/boostorg/multiprecision/pull/585)

  - Fix complex_adaptor to match precision requirements [PR#597](https://github.com/boostorg/multiprecision/pull/597)

  - Fix for breaking changes in tommath [PR#603](https://github.com/boostorg/multiprecision/pull/603)

  - Fix for types that can be converted to number participting in arithmetic operator overloads [\#608](https://github.com/boostorg/multiprecision/issues/608)

- [MySQL](/libs/mysql/):
  - **Breaking change**: Boost.MySQL now requires linking to the new **Boost.Charconv** compiled library. This addresses a locale-dependency problem, increases efficiency, and powers the new client-side SQL formatting feature.

  - Added experimental support for **connection pools**, which allows re-using sessions and provides built-in reconnection and error handling.

  - Added experimental support for **type-erased connections** (`any_connection` class). `any_connection` is not a template and features simpler connection establishment and reconnection semantics.

  - Added experimental support for **client-side SQL formatting functions** (`format_sql` and `format_sql_to`). These allow securely composing queries client-side, which enables patterns like batch inserts, dynamic filters or PATCH-like updates.

  - Fixed a performance issue affecting `close_statement` and `async_close_statement` that could cause significant delays in application code.

  - Added support for building with `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT`.

  - The deprecated execution interface (`connection``::``query`, `connection``::``start_query`, `connection``::``execute_statement`, `connection``::``start_statement_execution` and their async counterparts) now triggers warnings, as it's scheduled for removal in Boost 1.86.

  - Fixed a bug that caused some error messages to be truncated.

  - Warning cleanup. Builds are now clean from warnings when building with `-``Wall` and `-``Wextra`.

  - All `field_view` constructors are now stable.

  - The library internals have been rewritten using a sans-io approach to reduce complexity.

- [Odeint](/libs/numeric/odeint/):
  - **Breaking change**: The library now explicitly requires C++14 instead of implicitly by including Boost.Math

  - Fix compatibility with Thrust 1.10.0

  - Removed C++03 Boost components:
    - Array

    - Bind

    - Function

    - Static_assert

- [PFR](/libs/pfr/):
  - `boost``::``pfr``::``get_name` now can work with local types on some compilers. Thanks to [Bela Schaum](https://github.com/schaumb) for the PR [PR#152](https://github.com/boostorg/pfr/pull/152)!

  - Removed unused implementation details. Thanks to [Denis Mikhailov](https://github.com/denzor200) for the PR [PR#154](https://github.com/boostorg/pfr/pull/154).

  - Allow throwing exceptions from `boost``::``pfr``::``structure_to_tuple`. Thanks to [Denis Mikhailov](https://github.com/denzor200) for the bug report [\#155](https://github.com/boostorg/pfr/issues/155).

  - Field reflection trick is now described in the docs. Thanks to all the discussion participans in [\#150](https://github.com/boostorg/pfr/issues/150)!

- [Random](/libs/random/):
  - Added splitmix64 PRNG [PR#89](https://github.com/boostorg/random/pull/89)

- [System](/libs/system/):
  - C++03 is no longer supported; a C++11 compiler is required. (This includes GCC 4.8 or later, and MSVC 14.0 (VS 2015) or later.)

  - The deprecated header `boost``/``system``/``cygwin_error``.``hpp` has been removed.

  - The original and obsolete (32 bit) MinGW is no longer supported. MinGW-w64 (both 64 and 32 bit) is still supported.

  - `operator``&` now works for `result``<``void``>` (by way of taking a nullary function.)

  - Added `operator``|=` for `result`.

- [Stacktrace](/libs/stacktrace/):
  - **Big new feature: stacktrace from arbitrary exception**. On some POSIX platforms `std``::``stacktrace``::``from_current_exception``()` now returns the stacktrace of the current exception object as if the stacktrace was captures at the point of throwing the exception. Many thanks to Andrei Nekrashevich for prototyping the idea in `libsfe`.

  - Fixed memory consumption on Windows with `boost_stacktrace_windbg`. Thanks to [ycyclop](https://github.com/ycyclop) for reporting the issue [\#111](https://github.com/boostorg/stacktrace/issues/111), to [Thiago A. Correa](https://github.com/correa) for providing more information, to [Andrei Karpovskii](https://github.com/akarpovskii) for providing a possible fix.

  - Fixed library build with non hidden visibility. Thanks to [Jan Bouwer](https://github.com/JBouwer) for the report and information on how to fix it.

  - Added a separate section on async signal safety to the docs. Many thanks to [tworonix](https://github.com/tworonix) for highlighting the problem in [\#131](https://github.com/boostorg/stacktrace/issues/131) and to [itrofimow](https://github.com/itrofimow) for information on the problem.

- [STLInterfaces](/libs/stl_interfaces/):
  - Change the behavior of `iterator_interface` for input iterators in C++20 and later, to more closely follow the C++20 concepts.

  - Remove hidden friends from `iterator_interface` to fix errors about concepts being redefined with different constraints.

  - Add a new `v3` inline namespace, containing a new iterator_interface based on deducing this instead of CRTP (C++23 and later).

  - Add an rvalue-qualified overload of `closure``::``operator``()`, to prevent dangling temporaries.

- [Test](/libs/test/):
  - Respect library-spcific \_NO_LIB macros [PR#406](https://github.com/boostorg/test/pull/406)

  - Supress MSVC C4702 from \_\_builtin_unreachable() on intentionally unreachable code

  - Fix boost::function streaming error [PR#411](https://github.com/boostorg/test/pull/411)

- [Unordered](/libs/unordered/):
  - Optimized `emplace``()` for a `value_type` or `init_type` (if applicable) argument to bypass creating an intermediate object. The argument is already the same type as the would-be intermediate object.

  - Optimized `emplace``()` for `k``,``v` arguments on map containers to delay constructing the object until it is certain that an element should be inserted. This optimization happens when the map’s `key_type` is move constructible or when the `k` argument is a `key_type`.

  - Fixed support for allocators with explicit copy constructors ([PR#234](https://github.com/boostorg/unordered/pull/234)).

  - Fixed bug in the `const` version of `unordered_multimap``::``find``(``k``,`` ``hash``,`` ``eq``)` ([PR#238](https://github.com/boostorg/unordered/pull/238)).

- [Variant](/libs/variant/):
  - Removed more of the pre-C++11 macro and workarounds.

- [Wave](/libs/wave/): Fixed bugs:
  - [\#200](https://github.com/boostorg/wave/issues/200): Emitted pragmas lack terminating newline

  - [\#202](https://github.com/boostorg/wave/issues/202): YYMARKER not updated when fill called on BOOST_WAVE_BSIZE boundary

### Updated Tools

- [Build](/tools/build/):
  - Includes release of [B2 version 5.1.0](/tools/build/doc/html/#_version_5_1_0).

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

Marshall Clow and Glen Fernandes managed this release.

Copyright Rene Rivera 2006-2007.
