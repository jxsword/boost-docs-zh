# Version 1.83.0

## Version 1.83.0

August 11th, 2023 16:23 GMT

[Documentation](/doc/libs/1_83_0/)

| Platform | File | SHA256 Hash |
|----|----|----|
| unix | [boost_1_83_0.tar.bz2](https://archives.boost.io/release/1.83.0/source/boost_1_83_0.tar.bz2) | 6478edfe2f3305127cffe8caf73ea0176c53769f4bf1585be237eb30798c3b8e |
|  | [boost_1_83_0.tar.gz](https://archives.boost.io/release/1.83.0/source/boost_1_83_0.tar.gz) | c0685b68dd44cc46574cce86c4e17c0f611b15e195be9848dfd0769a0a207628 |
| windows | [boost_1_83_0.7z](https://archives.boost.io/release/1.83.0/source/boost_1_83_0.7z) | 22ee9dcf3f1fb58f585772f70c69113a4077b92adeac58b643b3543b78633a16 |
|  | [boost_1_83_0.zip](https://archives.boost.io/release/1.83.0/source/boost_1_83_0.zip) | c86bd9d9eef795b4b0d3802279419fde5221922805b073b9bd822edecb1ca28e |

Downloads {.download-table}

\* The download links are supported by grants from [The C++ Alliance](https://cppalliance.org/).  
  

### Known Issues

These are patches from library authors which were found too late to be fixed in the release.

- JSON
  - Compilation on Windows ARM platforms may fail for missing intrinsics, see [\#926](https://github.com/boostorg/json/issues/926) and [\#927](https://github.com/boostorg/json/issues/927). [Patch](https://github.com/boostorg/json/commit/c4ce8509d015a0b75cfa9d36609b8409821a9c86.patch).

- Unordered
  - Fix erroneous copy assigment operator that would destroy non-existent elements, see [\#205](https://github.com/boostorg/unordered/issues/205). [Patch](/patches/1_83_0/0001-unordered-fix-copy-assign.patch).

### New Libraries

- [Compat](/libs/compat/): A repository of C++11 implementations of standard components added in later C++ standards, from Peter Dimov and contributors.

### Updated Libraries

- [Any](/libs/any/):
  - New `boost``::``anys``::``unique_any` C++11 class - an alternative to `boost``::``any` (or to `std``::``any`) that does not require copy or move construction from the held type.

  - Ported documentation to Quickbook, Doxygen comments now used in code.

- [Atomic](/libs/atomic/):
  - Fixed compilation of `atomic_ref` for `const`-qualified types. Note that even `const`-qualified atomic objects must still reside in read-write memory. ([\#62](https://github.com/boostorg/atomic/issues/62))

- [Chrono](/libs/chrono/):
  - Remove use of deprecated Boost.Ratio features.

- [Compat](/libs/compat/):
  - Added `latch``.``hpp`, an implementation of `std``::``latch` (contributed by Christian Mazakas.)

  - Added `shared_lock``.``hpp`, a (partial) implementation of `std``::``shared_lock` (contributed by Christian Mazakas.)

- [Core](/libs/core/):
  - Added support for incomplete types to `boost``::``core``::``type_name`.

  - Bit manipulation functions in `boost``/``core``/``bit``.``hpp` are now `constexpr` on recent MSVC versions (VS2019 update 5 and later.)

  - Added `boost``::``core``::``byteswap` (an implementation of `std``::``byteswap` from C++23) to `boost``/``core``/``bit``.``hpp`.

  - Moved the yield primitives `sp_thread_pause`, `sp_thread_yield`, `sp_thread_sleep` from SmartPtr implementation details to `boost``/``core``/``yield_primitives``.``hpp`.

- [DLL](/libs/dll/):
  - Fixed tests failures on glibc 2.36+, thanks to [Đoàn Trần Công Danh](https://github.com/sgn) for the bugreport [\#58](https://github.com/boostorg/dll/issues/58).

- [Filesystem](/libs/filesystem/):
  - Added `directory_entry``::``refresh` method that updates internal cached file statuses for the directory entry identified by path.

  - **v4:** `directory_entry` constructors and modifiers that initialize or modify the path now automatically call `refresh`. This may result in errors that were not indicated before and in **v3**, if querying the filesystem for file statuses fails (e.g. if the file does not exist). This new behavior is similar to std::filesystem.

  - **v4:** `directory_entry` constructors and methods taking `file_status` parameters are removed. Users are recommended to remove these arguments and rely on `directory_entry` calling `refresh` internally.

  - Added `directory_entry` member methods for checking the file type of the file, similar to std::filesystem.

  - Added more methods for testing file status: `is_block_file`, `is_character_file`, `is_fifo`, `is_socket` and `is_reparse_file`.

  - `recursive_directory_iterator` is now more likely to reuse information about the file type that is obtained during filesystem iteration. This may improve performance. ([\#288](https://github.com/boostorg/filesystem/issues/288))

  - File streams defined in `boost``/``filesystem``/``fstream``.``hpp` are now movable, if the standard library file streams are. ([\#280](https://github.com/boostorg/filesystem/issues/280))

  - Added a new header `boost``/``filesystem``/``cstdio``.``hpp` with a portable `fopen` overload that takes `path` as the first argument. This function is equivalent to `std``::``fopen`, except that on Windows it uses the native wide character encoding for paths.

  - Generic `path` comparison operators are now more restricted to avoid potential ambiguities when user's code contains a `using`` ``namespace`` ``boost``::``filesystem``;` directive. ([\#285](https://github.com/boostorg/filesystem/issues/285))

  - Fixed potential overload resolution ambiguity in users' code, where `path` constructors from iterators could interfere with function overloads taking a `std``::``initializer_list` argument. ([\#287](https://github.com/boostorg/filesystem/issues/287))

  - On Windows, added more workarounds for errors returned by various filesystems when creating a directory iterator. ([\#284](https://github.com/boostorg/filesystem/issues/284), [\#286](https://github.com/boostorg/filesystem/issues/286))

  - On Windows, relaxed access rights needed for querying file times. ([\#290](https://github.com/boostorg/filesystem/issues/290))

- [Flyweight](/libs/flyweight/index.html):
  - Added smart-pointer syntax to `boost``::``flyweight` (`operator``*` and `operator``->` dereferencing to the underlying value).

  - Fixed a situation where the mutex used by [`simple_locking`](/libs/flyweight/doc/reference/locking.html#simple_locking_synopsis) was not recursive (issue [\#12](https://github.com/boostorg/flyweight/issues/12)).

- [Geometry](/libs/geometry/):
  - Improvements
    - [PR#1140](https://github.com/boostorg/geometry/pull/1140) Drop dependencies and replace boost with std in several places

    - [PR#1154](https://github.com/boostorg/geometry/pull/1154) Add missing headers so that all headers compile independently complying with Boost policy

    - [PR#1157](https://github.com/boostorg/geometry/pull/1157) Check const Ring concept in calculate_point_order

  - Solved issues
    - [\#1100](https://github.com/boostorg/geometry/issues/1100) Fix for union

    - [\#1139](https://github.com/boostorg/geometry/issues/1139) Fix for different geometry types

    - [\#1158](https://github.com/boostorg/geometry/issues/1158) Fix for convex hull

    - [\#1161](https://github.com/boostorg/geometry/issues/1161) Fix within algorithm for geometries having a pole as a vertex

    - Various fixes of errors and warnings

- [Iterator](/libs/iterator/):
  - Added `is_iterator` type trait that allows to test whether the type qualifies as an iterator type.

  - `filter_iterator` now supports move-construction of the adopted iterator and the function object. ([PR#79](https://github.com/boostorg/iterator/pull/79))

- [JSON](/libs/json/):
  - The library now only throws `system_error`, except for when allocation failed, in which case `std``::``bad_alloc` is thrown.

  - Serialization behavior can now be changed by `serialize_options`.

  - Contextual conversions.

  - Parser option for more precise number parsing.

  - Support `parse_options` in stream `operator``<<`.

  - Parser option to allow `Infinity` and `NaN` JSON literals.

  - Parser mode that only validates numbers rather than parsing them.

  - Numbers with exponent larger than `INT_MAX` are accepted by the parser and treated as infinity.

  - Fix `object` member functions that should provide strong guarantee.

  - Fix ambiguity of `end` call when `boost``/``range``.``hpp` is included.

  - Fix ASan failures.

  - Fix error message for `error``::``size_mismatch`.

  - Fix conversion into tuple with const elements.

- [Locale](/libs/locale/index.html):
  - Bitwise/binary operators (left/right shift, binary and/or/xor/not) are no longer supported in message catalog files matching GNU gettext behavior

  - Std backend on Windows uses the classic locale instead of the system locale when the requested locale does not exist (now same as on other OSs)

  - `localization_backend_manager``::``get` is deprecated, use the generator instead

  - New converter classes as alternative to `to_utf`/`from_utf`/`between`

  - Fix UB on invalid index in format strings

  - Fix conversion of UTF to e.g. iso-2022-jp on Windows without ICU

  - Use `long`` ``long` as the count parameter for pluralized translations

  - Fix movability and exception specification for some classes

- [Log](/libs/log/):
  - Fixed a possible infinite loop in `text_file_backend`, when the size of a formatted log record exceeds the `rotation_size` limit. ([\#209](https://github.com/boostorg/log/issues/209))

- [Math](/libs/math/):
  - Added Numerical evaluation of Fourier transform of Daubechies scaling functions [921](https://github.com/boostorg/math/pull/921).

  - Added logcdf function to statistical distributions [946](https://github.com/boostorg/math/pull/946).

  - Added support for C++23's `<``stdfloat``>` types [978](https://github.com/boostorg/math/pull/978).

  - Fixed various `-``Wmaybe``-``uninitialized` warnings

  - Fixed `round` and `trunc` functions for non-representable numbers [968](https://github.com/boostorg/math/pull/968).

  - Fixed calculation of mode for F-distribution [976](https://github.com/boostorg/math/pull/976).

  - Fixed overflow in beta distribution [977](https://github.com/boostorg/math/pull/977).

  - Fixed overflow in hypergeometric distribution [987](https://github.com/boostorg/math/pull/987).

  - Fixed calculation of median absolute deviation with non-zero center [997](https://github.com/boostorg/math/pull/997).

- [Mp11](/libs/mp11/):
  - Added an offset/from parameter to `mp_from_sequence`, `mp_iota`, `mp_iota_c`.

  - Added `mp_value`, `mp_list_v`, `mp_rename_v`, `mp_is_value_list`.

  - Added value list support to the primitives in `<``boost``/``mp11``/``list``.``hpp``>`.

  - Added value list support to `mp_repeat`, `mp_fill`, `mp_at`, `mp_back`, `mp_take`, `mp_pop_back`, `mp_drop`, `mp_insert`, `mp_erase`.

- [Multi-index Containers](/libs/multi_index/):
  - Updated range `insert` in non-unique ordered indices to preserve insertion order of equivalent elements (issue [\#68](https://github.com/boostorg/multi_index/issues/68)).

  - Serialization now uses `std``::``size_t` instead of `unsigned`` ``long` to save and load the size of a `multi_index_container` (`unsigned`` ``long` is smaller than `std``::``size_t` in LLP64 data models). `multi_index_container` serialization [class version](/libs/serialization/doc/tutorial.html#versioning) has been bumped from 3 to 4 to reflect this change.

- [Multiprecision](/libs/multiprecision/):
  - Fixed bug in rational adapter division [542](https://github.com/boostorg/multiprecision/pull/542).

  - Fixed handling of global precsion changes in multi-threaded environments [552](https://github.com/boostorg/multiprecision/pull/552).

  - Fixed `cpp_int``::``eval_convert_to` noexcept specification [555](https://github.com/boostorg/multiprecision/pull/555).

- [MySQL](/libs/mysql/):
  - **Major update.**

  - Stored procedures are now fully supported, including `SELECT` statements producing data and procedures with `OUT` parameters.

  - Added support for multi-queries, which allows running multiple semicolon-separated statements with a single call.

  - A statically-typed interface has been added, which allows parsing query results into user-provided types, using [Boost.Describe](/libs/describe/) structs and tuples.

  - Text queries and prepared statements can now be executed using the new `connection``::``execute` and `connection``::``start_execution` functions (and their async counterparts). These superseed `connection``::``query`, `connection``::``execute_statement`, `connection``::``start_query` and `connection``::``start_statement_execution`. The new functions allow access to new features, like the static interface.

  - A separate compilation mode has been added to help reduce build times. Sources are included in `boost``/``mysql``/``src``.``hpp`, which must be included in exactly one translation unit.

  - Prepared statements can now be executed using an iterator pair to specify parameters, using `statement``::``bind` and `connection``::``execute`. This enables use cases where the number and type of parameters is not known at compile-time.

  - Prepared statement execution now accepts parameters of type `bool`, `std``::``optional` and `boost``::``optional`.

  - Added error codes and verified compatibility with MySQL v8.0.33 and MariaDB v11.0.

  - Fixed potential problems with Windows' `min``()` and `max``()` macros.

  - All assertions now use [Boost.Assert](/libs/assert/).

  - All exceptions are now thrown via [Boost.ThrowException](/libs/throw_exception/).

  - Immediate completions are now correctly dispatched through the I/O object executor.

- [Ratio](/libs/ratio/):
  - Change default `BOOST_RATIO_VERSION` to 2.

  - Support for `BOOST_RATIO_EXTENSIONS` is now deprecated and will eventually be removed when Boost.Ratio is implemented in terms of the standard `<``ratio``>` header.

- [Test](/libs/test/):
  - Added addtional older platforms to CI system (e.g. GCC 4.6)

  - Fixed handling of `uintptr_t` to make sure it is portable on 32-bit systems [353](https://github.com/boostorg/test/pull/353).

  - Fixed warnings from `-``Wdeprecated``-``copy``-``dtor` and `-``Wdeprecated``-``copy``-``with``-``user``-``provided``-``dtor` [375](https://github.com/boostorg/test/pull/375).

  - Fixed handling of `check_is_close` for C++23 `<``stdfloat``>` types [382](https://github.com/boostorg/test/pull/382).

- [Timer](/libs/timer/):
  - Remove dependency on Boost.Chrono, Boost.System, and others.

  - Disable deprecated headers unless `BOOST_TIMER_ENABLE_DEPRECATED` is defined.

- [Unordered](/libs/unordered/):
  - **Major update.**

  - Added `boost``::``concurrent_flat_map`, a fast, thread-safe hashmap based on open addressing.

  - Sped up iteration of open-addressing containers.

  - In open-addressing containers, `erase``(``iterator``)`, which previously returned nothing, now returns a proxy object convertible to an iterator to the next element. This enables the typical `it`` ``=`` ``c``.``erase``(``it``)` idiom without incurring any performance penalty when the returned proxy is not used.

- [URL](/libs/url/):
  - `parse_query` does not recreate `string_view`. ([\#757](https://github.com/boostorg/url/issues/757))

  - `url_view`/`string_view` constructor requires non-`url_view_base`. ([\#756](https://github.com/boostorg/url/issues/756))

  - `IP``-``literal` can be `IPv6addrz`. ([\#711](https://github.com/boostorg/url/issues/711))

- [UUID](/libs/uuid/):
  - Improved generated x86 code for AVX targets. Removed the use of `lddqu` instruction on SSE3 targets, which penalize performance on Intel NetBurst CPUs but is more optimal on Skylake and later CPUs. ([PR#138](https://github.com/boostorg/uuid/pull/138))

- [Variant2](/libs/variant2/):
  - Added `uses_double_storage``()`.

### Updated Tools

- [Build](/tools/build/):
  - Includes release of [B2 version 4.10.1](/tools/build/doc/html/#_version_4_10_1).

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
