# Version 1.88.0

## Version 1.88.0

April 10th, 2025 20:39 GMT

[Documentation](/doc/libs/1_88_0/)

| Platform | File | SHA256 Hash |
|----|----|----|
| unix | [boost_1_88_0.tar.bz2](https://archives.boost.io/release/1.88.0/source/boost_1_88_0.tar.bz2) | 46d9d2c06637b219270877c9e16155cbd015b6dc84349af064c088e9b5b12f7b |
|  | [boost_1_88_0.tar.gz](https://archives.boost.io/release/1.88.0/source/boost_1_88_0.tar.gz) | 3621533e820dcab1e8012afd583c0c73cf0f77694952b81352bf38c1488f9cb4 |
| windows | [boost_1_88_0.7z](https://archives.boost.io/release/1.88.0/source/boost_1_88_0.7z) | e84a33716a31c1c8cb00783a411630d41c008e9364002dc0fe55aea4f54f4726 |
|  | [boost_1_88_0.zip](https://archives.boost.io/release/1.88.0/source/boost_1_88_0.zip) | 8ee21476f1aca1978339f0f4a218b9b8a6746eec83070f32630f97b09c7e91b7 |

Downloads {.download-table}

\* The download links are supported by grants from [The C++ Alliance](https://cppalliance.org/).  
  

### New Libraries

- [Hash2](/libs/hash2/): An extensible hashing framework, from Peter Dimov and Christian Mazakas.

- [MQTT5](/libs/mqtt5/): MQTT5 client library built on top of Boost.Asio, from Ivica Siladić, Bruno Iljazović, and Korina Šimičević.

### Updated Libraries

- [Array](/libs/array/):
  - Converted documentation to AsciiDoc (Christian Mazakas).

  - Added `noexcept` and `constexpr` as appropriate.

  - Marked obsolete functions as deprecated.

  - Removed obsolete compiler workarounds.

  - Changed `array``<``T``,`` ``0``>::``begin``()`, `cbegin``()`, `end``()`, `cend``()` to return `nullptr`, enabling `constexpr`. This matches the behavior of `std``::``array`.

  - Removed local `hash_value` overload; `boost``::``hash` supports array-like types natively.

  - `array``<``T``,`` ``0``>` can now be initialized with `=`` ``{{}}`.

  - Added `operator``<=>`.

  - Added `to_array`.

- [Asio](/libs/asio/):
  - Added `noexcept` qualifiers to various `local``::``basic_endpoint` member functions, to make it consistent with `ip``::``basic_endpoint`.

  - Fixed the `boost``::``asio``::``config` class's handling of integer values.

  - Fixed a use-after-move error in `experimental``::``ranged_parallel_group`.

  - Fixed an incorrect default template argument in the implementation of `experimental``::``promise`.

  - Fixed the `io_uring` implementation so that it does not attempt to re-register internal descriptors with the reactor after a fork, if they were not previously registered.

  - Fixed an uninitialised member in the `thread_pool` default constructor.

  - Fixed an ambiguous overload issue that occurred when passing a `std``::``span` to the `boost``::``asio``::``buffer` function.

  - Removed some spurious macro definitions that were left after the removal of deprecated buffer functionality.

  - Added documentation to clarify the use of `file_base``::``flags` when opening a file.

  - Added overview documentation on the available runtime configuration options.

  - Updated the overview documentation to reflect the use of `deferred` as the default completion token.

  - Updated the `async_result` documentation to reflect the current type requirements placed on specialisations of the trait.

- [Assert](/libs/assert/):
  - When `BOOST_ASSERT_HANDLER_IS_NORETURN` is defined, `boost``::``assertion_failed` and `boost``::``assertion_failed_msg` are declared as `BOOST_NORETURN`.

- [Beast](/libs/beast/):
  - Fixes
    - Fixed out-of-bounds access in `iequals` function.

  - Improvements
    - Updated SSL examples to verify peer certificate hostname.

    - Refactored CMakeLists.

    - Removed Boost.Scope dependency from examples.

    - Peer pings in WebSocket now count as activity.

  - Documentation
    - Added new examples for Unix domain sockets.

    - Added SSL/TLS Certificate section to documentation.

    - Improved documentation of `websocket``::``stream``::``async_close`.

  - Acknowledgements
    - Morten M. Neergaard

- [Conversion](/libs/conversion/):
  - Use modern C++ in the samples and in the library code.

- [DLL](/libs/dll/):
  - Added constructor from `native_handle_t` to the `boost``::``dll``::``shared_library`. Many thanks to [Tiago Matos](https://github.com/tgmatos) for the [PR#82](https://github.com/boostorg/dll/pull/82).

  - Dropped multiple dependencies on other Boost libraries including Spirit, SmartPtr, Move, TypeTraits, and Function. DLL became more lightweight for compilation.

  - `std``::``error_code``&` in API is used instead of the `boost``::``system``::``error_code``&`. This is not a breaking change as `boost``::``system``::``error_code` is convertible to `std``::``error_code``&`.

  - `boost``::``dll``:``import_``*` functions now return `std``::``shared_ptr` rather than `boost``::``shared_ptr`. Define `BOOST_DLL_USE_BOOST_SHARED_PTR` to restore the old behavior, however note that the macro will be removed in one of the upcomming Boost releases.

  - Use modern C++ in the samples and in the library code.

  - `boost``::``dll``::``library_info` now always throws in case of a broken binary. Updated the docs and added some tests.

  - Documented in FAQ why `RTLD_NODELETE` is missing and why there is no `.``release``()` method. Provided suggestions on possible workarounds.

  - Updated the information on building and using the library. CMake targets now link with `-``ldl` if it is required by the platform.

  - Fixed `detail``::``path_from_handle` implementation for long paths on Windows OS.

  - Highlighted in the docs that `boost``/``dll``/``smart_``*` parts of the library are experimental and incomplete.

  - Fixed multiple mangling issues in `boost``/``dll``/``smart_``*` parts of the library.

- [Geometry](/libs/geometry/):
  - Improvements
    - [PR#1370](https://github.com/boostorg/geometry/pull/1370) Relax half period check in spheroidal normalization

    - [PR#1368](https://github.com/boostorg/geometry/pull/1368) Pass umbrella strategies in rtree spatial predicates

    - [PR#1367](https://github.com/boostorg/geometry/pull/1367) Improvements in traversal

    - [PR#1361](https://github.com/boostorg/geometry/pull/1361) Test set operations on random grids with integer coordinates

    - Several test cases has been added

    - Use using instead of typedef in part of the code

  - Solved issues
    - [PR#1364](https://github.com/boostorg/geometry/pull/1364) Fix several strategies (add getters, fix compilation error and warning)

    - [\#629](https://github.com/boostorg/geometry/issues/629) Avoid warnings for coordinate conversions and unused parameters

    - Various fixes of errors and warnings

- [Graph](/libs/geometry/):
  - Bug fixes
    - Replace implementation of `maximum_weighted_matching`, resolves multiple issues.

    - Ensure `named_graph` is initialized before use.

    - Replace custom geometry code in `is_straight_line_drawing` with Boost.Geometry, fixes incorrect results for very small angles.

    - Fix incorrect callbacks to `finish_edge` in `undirected_dfs`.

  - Performance improvements
    - `adjacency_list`: Remove unnecessary calls to `resize`/`reserve` from within `add_vertex` for `vector`-based storage! A quick benchmark indicates a 10% improvement to graph construction time.

    - `lengauer_tarjan_dominator_tree`: Replace `std``::``deque` with `std``::``vector`, obtaining a ~40% improvement for large graphs.

  - General Improvements
    - Replace the use of several Boost utilities with C++14 language features.

    - Modernize examples with C++14 language features.

    - Various fixes to documentation and build system.

    - `vertex_by_property` no longer requires a mutable graph.

    - Fix compilation issue with `cycle_canceling` and Clang 19.

- [Iterator](/libs/iterator/):
  - Dropped support for C++03 and ancient compilers, updated code base to use C++11 and MP11, reduced usage of MPL. ([PR#82](https://github.com/boostorg/iterator/pull/82))

  - Added `min_category` trait, which is a variadic equivalent of `minimum_category` that doesn't depend on MPL. `minimum_category` is deprecated and will be removed in a future release.

  - Extracted `enable_if_convertible` trait to a separate header `enable_if_convertible``.``hpp`. The trait was previously defined in `iterator_adaptor``.``hpp`, and the header still provides `enable_if_convertible` when included. This dependency is provided for backward compatibility and will be removed in a future release. Users are advised to add includes of `enable_if_convertible``.``hpp`, as needed.

  - Added `*``_t` variants of various iterator traits that produce types.

  - `filter_iterator` and `transform_iterator` now use empty base optimization (EBO) to reduce size of the iterator when the adopted function object is stateless.

  - `zip_iterator` now natively supports `boost``::``tuple`, `std``::``tuple` and `std``::``pair` for iterator tuples and doesn't need including Fusion support headers.

  - `function_output_iterator` no longer allows default construction when the wrapped function is a function pointer. Such construction would previously create an iterator with an uninitialized function pointer value, and such an iterator would be unusable.

  - `generator_iterator``.``hpp` and `shared_container_iterator``.``hpp` headers were moved under the `boost``/``iterator` directory. The previous headers in `boost` are still retained for backward compatibility, but will be removed in a future release. Users are advised to update their includes.

  - `shared_container_iterator` now uses `std``::``shared_ptr` to reference the container internally. The support for `boost``::``shared_ptr` is still retained, but it will incur performance overhead on the iterator construction, as `boost``::``shared_ptr` is now wrapped in a `std``::``shared_ptr` internally. It is recommended to use `std``::``shared_ptr` to reference the container.

- [Locale](/libs/locale/):
  - Raised required ICU version to at least 4.8.1

  - Dropped support for ICU 50.1

  - Fixed parsing of integers with input strings in floating point format ([PR#241](https://github.com/boostorg/locale/pull/241))

  - Support parsing and formatting of `uint64_t` values with the ICU backend ([PR#246](https://github.com/boostorg/locale/pull/246))

  - Support `char8_t` on more platforms

- [Lockfree](/libs/lockfree/):
  - Added new spsc_value, a lockfree single-producer single-consumer value based on a triple-buffer

- [Log](/libs/log/):
  - Disabled usage of `std``::``codecvt``<``char16_t``>` and `std``::``codecvt``<``char32_t``>` locale facets in C++20 and later modes as they were deprecated in C++20. This means character code conversions to/from `char16_t` and `char32_t` is no longer available in C++20 and later.

  - Fixed building issues when using CMake and MinGW-w64. ([PR#241](https://github.com/boostorg/log/pull/241))

  - Fixed incorrect file counter used by `text_file_backend` when the backend was configured to append to an existing file and the actively written file name pattern didn't have a counter placeholder but the target file name pattern did, and the log files were written directly into the target storage. ([\#245](https://github.com/boostorg/log/issues/245))

- [Mp11](/libs/mp11/):
  - Fixed `mp_from_sequence` for non-integral values (accidentally broken in 1.83.0 due to offset support)

- [MySQL](/libs/mysql/):
  - `connection_pool` now resizes correctly even in the presence of many connections with session establishment in-progress. The old algorithm could lead to the pool not being resized as expected under certain conditions ([\#395](https://github.com/boostorg/mysql/issues/395)).

  - Added `any_connection``::``connection_id`. This function retrieves the connection's ID, which can subsequently be used in `KILL` SQL statements to cancel queries. This function is equivalent to `mysql_thread_id` in the official C API ([\#408](https://github.com/boostorg/mysql/issues/408))

  - Attempting to start an async operation on a `connection` or `any_connection` while another operation is in-progress no longer triggers undefined behavior. It now fails with `client_errc``::``operation_in_progress` ([\#405](https://github.com/boostorg/mysql/issues/405)).

  - Attempting to start an operation while a `connection` or `any_connection` are engaged in a multi-function operation no longer yields potentially dangerous packet mismatches. It instead fails with `client_errc``::``engaged_in_multi_function` ([\#448](https://github.com/boostorg/mysql/issues/448)).

  - Improved diagnostics when attempting to use a connection without a established session. Operations now fail with `client_errc``::``not_connected` ([\#450](https://github.com/boostorg/mysql/issues/450)).

  - Fixed a race condition in `connection` and `any_connection` regarding per-operation cancellation. In previous versions, if a cancellation signal was emitted after an intermediate async operation had completed, but before its handler had been called, the signal was ignored. This is no longer the case ([\#199](https://github.com/boostorg/mysql/issues/199)).

  - `field`'s constructor and assignment from `std``::``string_view` are now available in C++17, rather than C++20. These functions were guarded by standard feature-test macros, only available in C++20. These have been replaced by their Boost.Config equivalents.

  - Added an HTTP server example that uses C++20 coroutines.

  - Added a doc page on interfacing sync and async code. This replaces the synchronous connection pool snippet, which contained a race condition.

  - Improved some of the other examples and doc pages.

- [Nowide](/libs/nowide/):
  - Make `getenv` thread-safe ([PR#191](https://github.com/boostorg/nowide/pull/191))

- [PolyCollection](/libs/poly_collection/):
  - Added `boost``::``variant_collection`, a closed polymorphic collection similar in behavior to `std``::``vector``<``std``::``variant``<...>>`.

- [SmartPtr](/libs/smart_ptr/):
  - Fix `operator``<<` for wide streams (accidentally broken in 1.87.0)

- [Stacktrace](/libs/stacktrace/):
  - Use `GetModuleNames` to determine the full module path for MSVC implementation. Many thanks to [Daniel Krügler](https://github.com/Dani-Hub) for the [PR#198](https://github.com/boostorg/stacktrace/pull/198).

  - Print relative addresses to allow their decoding later without knowing the base address. The logic could be disabled by defining `BOOST_STACKTRACE_DISABLE_OFFSET_ADDR_BASE`. Many thanks to [Maciej Czarnecki](https://github.com/McCzarny) for the [PR#200](https://github.com/boostorg/stacktrace/pull/200).

  - Expose all the stacktrace libraries as b2 features for better control over the build and explicit information on what libraries are built. See "Configuration and Build" section for more info. Many thanks to [Uilian Ries](https://github.com/uilianries) for initial implementation of the feature in [PR#202](https://github.com/boostorg/stacktrace/pull/202).

  - Fixed `stacktrace_from_exception` builds with MinGW. Thanks to [crhilton](https://github.com/crhilton) for the fix.

- [TypeIndex](/libs/type_index/):
  - Fixed an UB that was introduced in Boost.TypeIndex 1.84 and prevented the library from building on clang-20.

- [Unordered](/libs/unordered/):
  - Migrated the documentation to a multipage format using Antora.

- [Variant2](/libs/variant2/):
  - Use the smallest appropriate unsigned type for the index.

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
