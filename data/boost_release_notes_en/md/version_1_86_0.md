# Version 1.86.0

## Version 1.86.0

August 14th, 2024 16:07 GMT

[Documentation](/doc/libs/1_86_0/)

| Platform | File | SHA256 Hash |
|----|----|----|
| unix | [boost_1_86_0.tar.bz2](https://archives.boost.io/release/1.86.0/source/boost_1_86_0.tar.bz2) | 1bed88e40401b2cb7a1f76d4bab499e352fa4d0c5f31c0dbae64e24d34d7513b |
|  | [boost_1_86_0.tar.gz](https://archives.boost.io/release/1.86.0/source/boost_1_86_0.tar.gz) | 2575e74ffc3ef1cd0babac2c1ee8bdb5782a0ee672b1912da40e5b4b591ca01f |
| windows | [boost_1_86_0.7z](https://archives.boost.io/release/1.86.0/source/boost_1_86_0.7z) | 413ee9d5754d0ac5994a3bf70c3b5606b10f33824fdd56cf04d425f2fc6bb8ce |
|  | [boost_1_86_0.zip](https://archives.boost.io/release/1.86.0/source/boost_1_86_0.zip) | cd20a5694e753683e1dc2ee10e2d1bb11704e65893ebcc6ced234ba68e5d8646 |

Downloads {.download-table}

\* The download links are supported by grants from [The C++ Alliance](https://cppalliance.org/).  
  

### New Libraries

- No new libraries.

### Updated Libraries

- [Asio](/libs/asio/):
  - Changed the `default_completion_token` trait's primary template to select `deferred` as the default completion token. As a result, most asynchronous operations' initiating functions will return a deferred asynchronous operation by default.

  - Added the `is_completion_condition` trait and added missing default completion tokens to overloads of `async_read`, `async_read_at`, `async_write`, and `async_write_at`.

  - Added the `is_connect_condition` trait and used it disambiguate overloads of `async_connect` when the completion token is defaulted.

  - Extended the completion token adapters `as_tuple`, `bind_allocator`, `bind_cancellation_slot`, `bind_executor`, `bind_immediate_executor`, and `redirect_error` to allow them to be used as partial completion token adapters.

  - Added the `cancel_after` and `cancel_at` completion token adapters.

  - Changed all completion token adapters to ensure they correctly propagate the asynchronous operation's I/O executor during adaptation.

  - Moved `co_composed` out of the `experimental` namespace.

  - Added `composed`, which creates an initiation function object from a stateful implementation. It is similar to `co_composed`, but for regular function objects rather than C++20 coroutines.

  - Changed the `detached` completion token to work with asynchronous operations that have multiple completion signatures.

  - Changed `async_initiate` to allow an empty variadic list of completion signatures, which would indicate that an asynchronous operation never completes.

  - Added overloads of `async_initiate` that automatically deduce the type of the completion token.

  - Added `async_immediate` which implements a trivial asynchronous operation that completes immediately, using an associated immediate executor if available.

  - Enabled SFINAE-based partial specialisation of the `associator` trait.

  - A number of bug fixes, compiler/platform compatibility improvements, and minor optimisations.

  - Various updates to documentation and examples.

  - Consult the [Revision History](/doc/libs/1_86_0/doc/html/boost_asio/history.html) for further details.

- [Atomic](/libs/atomic/):
  - Use [`futex``(``2``)`](https://man.openbsd.org/OpenBSD-6.2/futex.2) system call on OpenBSD since recent OpenBSD versions have removed support for `syscall``(``2``)`.

- [Beast](/libs/beast/):
  - API Changes
    - Added HTTP status code 418 `I``'``m`` ``a`` ``teapot`.

  - Fixes
    - Narrowing conversion in `read_size_hint_db``()`.

    - Overloads that are ambiguous when using default completion tokens.

    - Misplaced static_assert in `http``::``basic_fields` move-assignment operator.

    - Underflow of `bytes_transferred` in WebSocket partial write operations.

    - `websocket``::``stream``::``read_size_hint``()` does not exceed `read_message_max`.

    - Various warnings in tests.

    - Error handling in SSL shutdown operations in examples.

    - Annotate fallthrough case in zlib.

    - Handling of expired timers in `basic_stream``::``ops``::``transfer_op`.

    - Ambiguity in `test``::``basic_stream` constructor overloads.

    - Partial parsing of the final chunk in `http``::``parser`.

  - Improvements
    - Graceful shutdown in `server_flex_awaitable` example.

    - Simplified awaitable examples.

    - Added fuzzing targets.

    - Remove superfluous uses of `std``::``bind` in some examples.

    - `ssl_stream` does not use `flat_stream`.

  - Documentation
    - `ssl_stream` and `flat_stream` marked as deprecated.

    - `net``::``ssl``::``stream` is canonical in snippets and examples.

    - Added `SSL``/``TLS`` ``Shutdown`` ``Procedure` section.

  - Acknowledgements
    - tyler92, Ruslan Zakirov, Orgad Shaneh, Alexander Kernozhitsky

- [Charconv](/libs/charconv):
  - Fixed support for PPC64LE architecture.

  - Fixed support for platforms like Alpine linux that provide the `<``quadmath``.``h``>` header but not the compiled library.

  - Fixed first character pattern matching in `from_chars` for integer types.

  - Fixed overflow detection for integers with base greater than 10.

  - Added native support for `std``::``float16_t` and `std``::``bfloat16_t` instead of using interchange formats.

- [Cobalt](/libs/cobalt):
  - Added support for asio::cancel_after

  - Made `asio``::``deferred` co_await-able, because it's asio's default token

  - Added `noop` utility

  - Added experimental support for stackful coroutines/fibers

  - Fixed movability of channel & coroutine types

- [Compat](/libs/compat/):
  - Added `bind_front``.``hpp`, `bind_back``.``hpp`, `invoke``.``hpp`, `mem_fn``.``hpp`, `integer_sequence``.``hpp` and `type_traits``.``hpp`.

  - Added `function_ref``.``hpp`.

- [Container](/libs/container/):
  - Fixed bugs/issues:
    - [GitHub \#285: *"devector\<\>::push_front asserts after clear()"*](https://github.com/boostorg/container/issues/285).

    - [GitHub \#280: *"Several containers don't support non-movable types when move assigning"*](https://github.com/boostorg/container/issues/280).

    - [GitHub \#279: *"small_vector cannot go back to use stack space"*](https://github.com/boostorg/container/issues/279).

    - [GitHub \#277: *"Remove dep on boost::static_assert"*](https://github.com/boostorg/container/issues/277).

    - [GitHub \#275: *"Compilation fails if custom key comparison is used"*](https://github.com/boostorg/container/issues/275).

    - [GitHub \#273: *"flat_map/vector crashes on appends (memory corruption)"*](https://github.com/boostorg/container/issues/273).

    - [GitHub \#269: *"flat_multimap::emplace not sorting elements under GCC"*](https://github.com/boostorg/container/issues/269).

    - [GitHub \#266: *"small_vector\<T\> is misaligned on the stack in 32 bits"*](https://github.com/boostorg/container/issues/266).

    - [GitHub \#259: *"Global variables"*](https://github.com/boostorg/container/issues/259).

    - [GitHub \#245: *"flat_tree::insert ordered range doesn't assert sorting"*](https://github.com/boostorg/container/issues/245).

    - [GitHub \#241: *"flat_map should support same interface as std::map"*](https://github.com/boostorg/container/issues/241).

- [Core](/libs/core/):
  - Added a `boost``/``core``/``pointer_in_range``.``hpp` header with a `pointer_in_range` function template to check if a pointer is within a given range (Glen Fernandes).

  - Fixed `type_name` for abstract classes. ([\#172](https://github.com/boostorg/core/issues/172))

  - Fixed `boost``/``core``/``type_name``.``hpp` compilation error with MSVC with disabled native `wchar_t` type. ([\#173](https://github.com/boostorg/core/issues/173))

  - Added a workaround for an MSVC [bug](https://developercommunity.visualstudio.com/t/Compiler-bug:-Incorrect-C2247-and-C2248/10690025) causing `empty_value` compilation errors when it is used with a nested class. ([PR#175](https://github.com/boostorg/core/pull/175))

- [CRC](/libs/crc/):
  - C++03 is no longer supported; a C++11 compiler is required. (This includes GCC 4.6 or later, and MSVC 10.0 (VS 2010) or later.)

  - Removed dependencies on Array, Config, Integer, and TypeTraits. The library is now standalone.

- [Filesystem](/libs/filesystem/):
  - `is_empty` operation is now better protected against concurrent filesystem modifications.

  - On POSIX systems, `is_empty` now indicates error if invoked on a file other than a regular file or a directory.

  - On Windows, fixed `file_size` and `is_empty` operating on symlinks rather than the files the symlinks refer to. ([\#313](https://github.com/boostorg/filesystem/issues/313))

  - `directory_entry``::``refresh` no longer throws an exception if the file referenced by the entry doesn't exist. This makes `directory_entry``::``status` and `directory_entry``::``symlink_status`, as well as methods based on them, behave similarly to the equivalent standalone operations. The fact that the file does not exist is still indicated via the `error_code` returned by the corresponding `directory_entry``::``refresh` overload, or can be seen by testing if the file type returned by `directory_entry``::``status` or `directory_entry``::``symlink_status` calls is `file_type``::``file_not_found`. ([\#314](https://github.com/boostorg/filesystem/issues/314))

  - Fixed `weakly_canonical` testing path elements for existence relative to the current path instead of the base path specified in the call, if the input path was a relative path.

  - On Windows, fixed `weakly_canonical` producing incorrect result path when the input path started with "..". ([\#311](https://github.com/boostorg/filesystem/issues/311))

- [Format](/libs/format/):
  - C++03 is no longer supported; a C++11 compiler is required. (This includes GCC 4.7 or later, and MSVC 12.0 (VS 2013) or later.)

- [Function](/libs/function/):
  - Removed dependency on Boost.TypeTraits.

  - Brought back the `argN_type` typedefs that were accidentally lost in 1.85.

- [GIL](/libs/gil/):
  - Added
    - Added `tell``()` and `error``()` functions to `istream_device` and `ostream_device` classes ([PR#747](https://github.com/boostorg/gil/pull/747)).

  - Changed
    - Don't ignore custom color converter in `color_converted_view` function ([PR#726](https://github.com/boostorg/gil/pull/726)).

    - Added workaround for conflict with `min``()` and `max``()` macros on WinAPI ([PR#745](https://github.com/boostorg/gil/pull/745)).

    - The use of `boost``::``filesystem` in GIL is now configurable in CMake via option `BOOST_GIL_USE_BOOST_FILESYSTEM` ([PR#743](https://github.com/boostorg/gil/pull/743)).

  - Fixed
    - Fixed convolution in `convolve_2d` ([PR#723](https://github.com/boostorg/gil/pull/723))

    - Normalize Gaussian 2D kernel to avoid darkening ([PR#725](https://github.com/boostorg/gil/pull/725))

    - Wrong buffer size in path string conversion functions for `std``::``wstring` is fixed, avoiding buffer overflows when using I/O-related functions with `std``::``wstring` paths ([PR#746](https://github.com/boostorg/gil/pull/746)).

  - Acknowledgements
    - Christoph Gringmuth, Christopher Kormanyos, nicolacandussi, Dirk Stolle, Olzhas Zhumabek

- [Graph](/libs/graph/):
  - *Major* update: C++14 is the new minimum standard; this was partly dictated by dependencies (at least to C++11) and partly by choice. If you require support for an older standard, please contact the maintainer.

  - Remove direct dependency on Boost.Regex.

  - Fix several compilation errors caused by not explicitly including common headers.

  - `isomorphism`: Fix docs, ignore `vertex_max_invariant` parameter in favour of cheaply calculating upper exclusive bound, fix bug with Associative Property Map, improve space efficiency from linear in the size of the maximum invariant to linear in the size of g1.

  - `boykov_kolmogorov_max_flow`: Fix named parameter overload.

  - `adj_list_edge_iterator`: Fix maybe-uninitialized warnings.

  - `hawick_circuits`: Add a parameter to optionally limit the depth of the search, causing a potentially suboptimal answer to be returned early.

  - `disjoint_sets`: Improve performance of `link_sets` by removing redundant lookup of set representatives.

  - `maximum_adjacency_search`: Refactor and more tests.

  - `property`: Use `BOOST_ATTRIBUTE_NO_UNIQUE_ADDRESS` to remove wasted space.

  - `labeled_graph`: Fix `remove_labeled_vertex` so that it actually removes the label too.

  - `r_c_shortest_paths`: Fix bug that the single-solution variant did not always return the shortest path.

  - `read_graphviz`: Fix stack overflow (oss-fuzz issue 66719) and non-keyword subgraph parsing.

  - Many miscellaneous improvements: broken links, typos, etc.

- [Interprocess](/libs/interprocess/):
  - Fixed bugs:
    - [GitHub \#191 (*"vectorstream: support file sizes larger than INT_MAX "*)](https://github.com/boostorg/interprocess/pull/191).

    - [GitHub \#198 (*"Minor fixes for documentation of offset_ptr"*)](https://github.com/boostorg/interprocess/pull/198).

    - [GitHub \#202 (*"Allow to map message_queue in anonymous memory"*)](https://github.com/boostorg/interprocess/pull/202).

    - [GitHub \#207 (*"cmake: link system libraries"*)](https://github.com/boostorg/interprocess/pull/207).

    - [GitHub \#214 (*"Doc: Fix github links"*)](https://github.com/boostorg/interprocess/pull/214).

- [Intrusive](/libs/intrusive/):
  - Fixed bug [GitHub \#86: *Invalid UTF-8 character in comment*](https://github.com/boostorg/intrusive/issues/86)

- [JSON](/libs/json/):
  - Support for GCC versions older than version 5.0 is deprecated and **will stop in Boost 1.88.0**.

  - `source_location` parameter was added to throwing accessor functions.

  - Parse option to tolerate invalid UTF-16 surrogate pairs, and produce [WTF-8](https://simonsapin.github.io/wtf-8/).

  - Added accessor functions that return `system``::``result`.

  - Handle missing error case in direct parsing.

- [LexicalCast](/libs/lexical_cast/):
  - Fixed conversion of `std``::``basic_string_view` and `boost``::``basic_string_view` containing one or more `\``0` characters. Issue was introduced in 1.85.0.

- [leaf](/libs/leaf/):
  - More optimal verbose_diagnostic_info implementation.

  - Bug fixes.

  - Added \[\[nodiscard\]\] to class result\<\>.

- [Locale](/libs/locale/):
  - Add support for custom allocators in `conv``::``utf_to_utf`

  - Don't build examples by default

- [Log](/libs/log/):
  - Added a workaround for `windres``.``exe` issue, when it is used in CMake to compile event log resource files on MinGW-w64. ([PR#231](https://github.com/boostorg/log/pull/231))

- [Math](/libs/math/):
  - Correct Bessel function results at infinity, see [1143](https://github.com/boostorg/math/issues/1143).

  - Improve Non Central T numerical stability, see [scipy20693](https://github.com/scipy/scipy/issues/20693).

  - Correct `float_next`/`float_prior` behaviour at infinity.

  - Prevent spurious underflow in non-central beta, see [scipy20693](https://github.com/scipy/scipy/issues/20693).

  - Add improvement to Heuman Lambda precision.

  - Improve Skew Normal root finding, see [1120](https://github.com/boostorg/math/issues/1120).

  - Lots of minor fixes and improved code coverage.

- [Multiprecision](/libs/multiprecision/):
  - Make sure `eval_convert_to``()` does not terminate with super large numbers, see [618](https://github.com/boostorg/multiprecision/pull/618).

  - Fix `sinc` implementation to match behavior of Boost.Math.

  - Fix divide-by-zero in cpp_int modulus operations.

  - Fix underflow behavior consistency for integers greater than 128-bits, see [626](https://github.com/boostorg/multiprecision/issues/626).

- [MySQL](/libs/mysql/):
  - The long-deprecated functions `query`, `start_query`, `execute_statement` and `start_statement_execution` (and their async equivalents) have been removed.

  - Breaking changes to experimental APIs:
    - The `identifier` class (client-side SQL formatting) has been removed. Use the new format specifiers feature, instead.

    - The required interface for custom formatters has been changed to accomodate the new format specifiers API.

    - `any_connection``::``async_connect` now requires that its `connect_params` argument be kept alive until the operation completes. The overload taking a `const`` ``connect_params``*` has been removed.

    - `character_set``::``name` is now a `const`` ``char``*` instead of a `string_view`, as MySQL character set names can't contain NULL characters.

    - `any_connection` internal buffer is now limited to 64MB. If you need to read or write rows bigger than that, increase `any_connection_params``::``max_buffer_size`. `connection` and their helper typedefs are not limited.

    - Renamed `any_connection_params``::``initial_read_buffer_size` to `initial_buffer_size`.

    - Renamed `pool_params``::``initial_read_buffer_size` to `initial_buffer_size`.

  - New experimental API: **pipelines**. Pipelines can increase efficiency by coalescing several requests in a single network packet. Pipelines can be used to run text queries, prepare, execute and close statements, reset session state and set the connection's character set.

  - Client-side SQL formatting now supports ranges out of the box. Formatting can be further customized using the new `sequence` function. Use cases like batch inserts and batch lookups can be significantly simplified using this functionality.

  - Client-side SQL formatting now supports format specifiers which modify how values are formatted. `{:``i``}` formats a string as a dynamic SQL identifiers, and `{:``r``}` outputs a raw unescaped

  - The static interface (`static_results` and `static_execution_state`) now supports Boost.Pfr types using `pfr_by_name` and `pfr_by_position`. Added `underlying_row_t` to support such types.

  - `date` and `datetime` can now be constructed from and converted to C++20 `std``::``chrono``::``local_time`.

  - Added `any_connection_params``::``max_buffer_size`, which allows to set a limit to the connection's internal buffer.

  - Added `is_fatal_error`, which allows users can now distinguish between fatal (which require closing and re-opening the connection) and non-fatal error codes.

  - Added `formattable_ref`, a type-erased reference type that can refer to any type satisfying the `Formattable` concept.

  - Fixed an ODR violation under MSVC which could cause crashes in release builds when using Boost.MySQL with other code also using `asio``::``coroutine` in different translation units.

- [Odeint](/libs/numeric/odeint/):
  - Added CMake Option `BOOST_NUMERIC_ODEINT_NO_ADAPTORS` to reduce dependencies, see [82](https://github.com/boostorg/odeint/issues/82)

  - Fixed CMake detection of MPI.

- [Process](/libs/process/):
  - Moved the old boost.process to v1 subfolder and inline namespace. deprecated process/\*.hpp v1 headers

  - Turned v2 into a compile library.

  - Fixed usage on alpine linux / musl

- [Stacktrace](/libs/stacktrace/):
  - **Big new feature: stacktrace from arbitrary exception for Windows**. `std``::``stacktrace``::``from_current_exception``()` now works on Windows platform. Many thanks to [huangqinjin](https://github.com/huangqinjin) for the implementation [PR#159](https://github.com/boostorg/stacktrace/pull/159) Now on POSIX and Windows the `from_current_exception``()`` ` function returns the stacktrace of the current exception object as if the stacktrace was captured at the point of throwing the exception.

  - Fixed inclusion of rarely used Windows SDK headers which can cause conflict with other code using Windows SDK. Thanks to [Marat Abrarov](https://github.com/mabrarov) for fixing the issue [PR#157](https://github.com/boostorg/stacktrace/pull/157).

  - Build option `boost``.``stacktrace``.``from_exception` now properly works on MacOS. Thanks to [Peter Dimov](https://github.com/pdimov) for the fix [PR#166](https://github.com/boostorg/stacktrace/pull/166).

  - Fixed a typo in assert expression. Thanks to [Kilian Henneberger](https://github.com/Ukilele) for the bug report [\#164](https://github.com/boostorg/stacktrace/issues/164).

  - Fixed shadowing warnings. Thanks to [Nigel Stewart](https://github.com/nigels-com) for the bug report [\#141](https://github.com/boostorg/stacktrace/issues/141).

  - Added `dladdr` minimal support for AIX. Many thanks to Clément Chigot for the implementation [PR#114](https://github.com/boostorg/stacktrace/pull/114).

  - Added `Boost``::``stacktrace` CMake alias that refers to the best supported implementation of Boost.Stacktrace on the platform. Thanks to [Alex](https://github.com/leha-bot) for the feature [PR#167](https://github.com/boostorg/stacktrace/pull/167).

  - Significant improvement of CMake: multiple fixes, added many new tests, improved CI. Many thanks to [Peter Dimov](https://github.com/pdimov) for all the improvements.

  - Fix addr2line work when the process is looked up via `PATH`. Thanks to [Schreischildkroete](https://github.com/Schreischildkroete) for the bug report and to [Jens Richter](https://github.com/j-jr-richter) for fix [\#72](https://github.com/boostorg/stacktrace/issues/72).

- [Test](/libs/test/):
  - Fix `-``Wundef` in configuration step.

  - Fix unreachable return compilation error on MSVC.

- [Unordered](/libs/unordered/):
  - Added container `pmr` aliases when header `<``memory_resource``>` is available. The alias `boost``::``unordered``::``pmr``::[``container``]` refers to `boost``::``unordered``::[``container``]` with a `std``::``pmr``::``polymorphic_allocator` allocator type.

  - Equipped open-addressing and concurrent containers to internally calculate and provide statistical metrics affected by the quality of the hash function. This functionality is enabled by the global macro `BOOST_UNORDERED_ENABLE_STATS`.

  - Avalanching hash functions must now be marked via an `is_avalanching` typedef with an embedded `value` constant set to `true` (typically, defining `is_avalanching` as `std``::``true_type`). `using`` ``is_avalanching`` ``=`` ``void` is deprecated but allowed for backwards compatibility.

  - Added Visual Studio Natvis framework custom visualizations for containers and iterators. This works for all containers with an allocator using raw pointers. In this release, containers and iterators are not supported if their allocator uses fancy pointers. This may be addressed in later releases.

- [UUID](/libs/uuid/):
  - *Major* update.

  - C++03 is no longer supported, a C++11 compiler is required. (This includes GCC 4.8 or later, MSVC 14.0 (VS 2015) or later, and MinGW-w64.)

  - Decreased number of Boost dependencies from 39 (in total) to just 5.

  - Updated to reflect the newer [RFC 9562](https://datatracker.ietf.org/doc/rfc9562/).

  - Added generators for time-based UUIDs.

  - *Many* other improvements, see the [revision history](/libs/uuid/doc/html/uuid.html#changes).

- [Wave](/libs/wave/):
  - Replaced one use of vsprintf with the more secure vsnprintf

  - Fixed bug:
    - [\#197](https://github.com/boostorg/wave/issues/197): Improper signed overflow handling (UB and a missing division check)

- [WinAPI](/libs/winapi/):
  - Added `BOOST_USE_WINAPI_VERSION` CMake option, which allows users to specify the Windows version for Boost to target.

### Updated Tools

- [BoostBook](/tools/boostbook/):
  - DTD updated: `constructor`, `copy``-``assignment` and `destructor` elements are now allowed inside `method``-``group` elements.

  - Many fixes and improvements in Doxygen-generated documentation:
    - Fixed duplicate equal signs in Doxygen-generated enum value initializers.

    - Disabled alphabetical sorting of function arguments. The sorting can be re-enabled by setting the new `boost``.``sort``.``params` XSL parameter to 1.

    - Added support for custom class member grouping. See Doxygen tags `@``name` and `@``{`/`@``}`.

    - Added support for Doxygen references to classes, methods, enums, variables, etc. (see `@``ref` tag).

    - Added support for `@``remark` and `@``important` tags.

    - Added support for `@``parblock` tags, which can be used to place multiple paragraphs under a tag that expects a single paragraph as an argument (e.g. `@``returns`).

    - Template parameter defaults that refer to implementation details are now concealed, similar to function parameter defaults.

    - Improved presentation of unnamed enums. Instead of showing a synthesized name such as `@``0`, the name is either omitted or is `[``unnamed``]`, if the name is necessary to introduce a link to the enum documentation.

    - Changed the "See Also" (`@``sa`) blocks to be displayed inline, similar to "Returns".

    - Fixed presentation of multiple exception specifications (`@``throws`).

    - Added support for free form description of throwing behavior. If the exception type after the `@``throws` tag is "~" then the exception type is omitted from the output, and the following description is displayed directly in the "Throws" section.

    - Removed redundant spaces in return types and template parameters.

- [Build](/tools/build/):
  - Includes release of [B2 version 5.2.1](/tools/build/doc/html/#_version_5_2_1).

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
