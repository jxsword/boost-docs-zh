# Version 1.79.0

## Version 1.79.0

April 13th, 2022 14:22 GMT

[Documentation](/doc/libs/1_79_0/)

| Platform | File | SHA256 Hash |
|----|----|----|
| unix | [boost_1_79_0.tar.bz2](https://archives.boost.io/release/1.79.0/source/boost_1_79_0.tar.bz2) | 475d589d51a7f8b3ba2ba4eda022b170e562ca3b760ee922c146b6c65856ef39 |
|  | [boost_1_79_0.tar.gz](https://archives.boost.io/release/1.79.0/source/boost_1_79_0.tar.gz) | 273f1be93238a068aba4f9735a4a2b003019af067b9c183ed227780b8f36062c |
| windows | [boost_1_79_0.7z](https://archives.boost.io/release/1.79.0/source/boost_1_79_0.7z) | 6c97cf4f4a0eb00ed776c88065ab3f59e183fa5e65f6464ff94f92328352d9d6 |
|  | [boost_1_79_0.zip](https://archives.boost.io/release/1.79.0/source/boost_1_79_0.zip) | 3634f9a85759311f321e587eace21799c0d0c946ff933e477a2f98885c54bbff |

Downloads {.download-table}

\* The download links are supported by grants from [The C++ Alliance](https://cppalliance.org/).  
  

### Known Issues

These are patches from library authors which were found too late to be fixed in the release.

- Boost.JSON `array``::``erase` can segfault, see [\#692](https://github.com/boostorg/json/issues/692). [Patch](/patches/1_79_0/0001-json-array-erase-relocate.patch).

### New Libraries

- No new libraries.

### Updated Libraries

- [Asio](/libs/asio/):
  - Added `bind_allocator`.

  - Added `file_base``::``sync_all_on_write` flag.

  - Added missing implementation of `basic_file``::``release``()`.

  - Added per-operation cancellation support to signal sets.

  - Exposed `recycling_allocator` as part of the public interface.

  - Added the `nodiscard` attribute to a number of functions.

  - Added OpenSSL 3.0 compatibility.

  - Added support for adopting an existing `SSL``*` into an `ssl``::``stream``<>`.

  - Enabled `executor_work_guard``<>` in all build configurations.

  - Enabled movable socket iostreams when using clang.

  - Fixed `bind_cancellation_slot` and `bind_executor` compatibility with legacy completion tokens.

  - Fixed `associator` specialisations for `experimental``::``append` and `experimental``::``prepend`.

  - Fixed `associated_allocator` primary template.

  - Fixed `io_uring` implementations of `async_receive_from` for sockets and `write_some_at` for files.

  - Fixed `io_uring` feature detection.

  - Fixed `experimental``::``coro`'s per-operation cancellation.

  - Fixed memory management in `experimental``::``promise`'s type-erased completion handlers.

  - Fixed move `operator``=` implementation for `ssl``::``stream`.

  - Fixed `any_io_executor` implementation to work when both `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT` and `BOOST_ASIO_SEPARATE_COMPILATION` are defined.

  - Fixed implementation of `basic_socket``::``at_mark``()` when using the `sockatmark``()` system call.

  - Changed the recycling allocator to use the default alignment as the minimum alignment for allocations.

  - Added a workaround for apparent coroutine codegen bug with Apple's clang.

  - On Windows, changed the file support to open files using the same sharing mode as `fopen``()`.

  - On Linux, fixed UNIX domain sockets implementation to correctly handle `EAGAIN`.

  - Fixed implementation of `experimental``::``basic_channel``::``reset``()` and `experimental``::``basic_concurrent_channel``::``reset``()`.

  - Fixed potential undefined behaviour in the `experimental``::``promise`.

  - Changed the `co_spawn` implementation to dispatch cancellation signals through the executor in some circumstances.

  - Fixed various header inclusion issues.

  - Fixed various warnings.

  - A number of documentation enhancements, including:
    - Added an overview of Asio's asynchronous model.

    - Reworked reference and requirements documentation in terms of asynchronous model.

    - Updated documentation for `dispatch``()`, `post``()`, and `defer``()`.

    - Documented per-operation cancellation for serial ports.

    - Clarified the non-concurrency guarantees made for allocators.

    - Reverted the `io_context` reference documentation to use `executor_work_guard`.

    - Added more detailed reference documentation to `make_strand``()`, `make_work_guard``()`, `ip``::``address_v4`, `ip``::``address_v6`, `experimental``::``basic_channel`, and `experimental``::``basic_concurrent_channel`.

    - Re-arranged and extended the Overview documentation to cover recently added features.

  - Added a C++11 example showing file descriptor passing over local sockets.

  - Added C++14 examples of wrapping callback-based APIs in asynchronous operations.

  - Consult the [Revision History](/doc/libs/1_79_0/doc/html/boost_asio/history.html) for further details.

- [Assert](/libs/assert/):
  - `source_location``().``file_name``()` and `source_location``().``function_name``()` now return `""` instead of `"(unknown)"`.

  - Added a `source_location` constructor from `std``::``source_location`.

  - Changed `BOOST_CURRENT_LOCATION` to more closely match the behavior of `std``::``source_location``::``current``()`, such as being usable at top level or as a default function argument.

- [Atomic](/libs/atomic/):
  - Fixed compilation for Universal Windows Platform (UWP). ([\#54](https://github.com/boostorg/atomic/issues/54))

  - Added `BOOST_ATOMIC_NO_DARWIN_ULOCK` configuration macro. The macro affects compilation on Darwin systems and disables `ulock`-based implementation of waiting and notifying operations. This may be useful to comply with Apple App Store requirements. ([\#55](https://github.com/boostorg/atomic/issues/55))

- [Beast](/libs/beast/):
  - Added missing include for file_body test.

  - Fixed WebSocket handshake response on failure.

  - Fixed open append mode for `file_posix` and `file_win32`.

  - Fixed file open with append/append_existing flag on Windows

  - Fixed clang-cl UTF8 path handling for `file_win32` and `file_stdio`.

  - Added ARM64 builds to drone CI.

  - Fixed async_base documentation link.

  - Added tests for file open in append/append_existing mode.

  - Updated CI to include gcc 11, clang 12, msvc 14.3.

  - Added individual tests to CMake workflow.

  - We'd love to know how you or your company use Beast, consider adding an entry to the [Companies and Individuals Using Beast](https://github.com/boostorg/beast/wiki/Companies-and-Individuals-Using-Beast) list.

  - See the full [Release Notes](/libs/beast/doc/html/beast/release_notes.html) for a complete list of changes.

- [Core](/libs/core/):
  - Made `boost``::``pointer_traits` SFINAE friendly, addressing LWG3545. (Glen Fernandes)

  - Added `boost``::``allocator_traits` that uses the individual allocator access traits. This implementation supports C++03 and above. (Glen Fernandes)

  - Updated the allocator access traits to support most of the C++11 allocator model in C++03. (Glen Fernandes)

  - `boost``/``iterator``.``hpp` is deprecated and will be removed in a future release. The header defines `boost``::``iterator` template, which is equivalent to `std``::``iterator` in `<``iterator``>` header. However, since `std``::``iterator` is itself deprecated in C++17, users are advised to remove `boost``::``iterator` or `std``::``iterator` use from their code.

  - Added `boost``::``core``::``verbose_terminate_handler`, a utility function intended to be passed to `std``::``set_terminate` that prints information about the uncaught exception to `stderr`.

- [Describe](/libs/describe/):
  - Enabled unions in `BOOST_DESCRIBE_STRUCT` and updated examples to check `std``::``is_union``<``T``>`.

  - Added example of defining a `fmtlib` class formatter.

  - Added example of defining a `fmtlib` enum formatter.

  - Added example of printing pointers to members.

- [Filesystem](/libs/filesystem/):
  - **v3:** `path``::``replace_extension` now works in terms of **v3** definition of `path``::``extension` rather than **v4**.

  - Fixed compilation of path appending and concatenation operators with arguments of types convertible to `path` or compatible string type. ([\#223](https://github.com/boostorg/filesystem/issues/223))

  - On POSIX systems that support `fdopendir` and `O_NOFOLLOW` and on Windows, `remove_all` is now protected against [CVE-2022-21658](https://www.cve.org/CVERecord?id=CVE-2022-21658). The vulnerability is a race condition that allows a third party process to replace a directory that is being concurrently processed by `remove_all` with a directory symlink and cause `remove_all` to follow the symlink and remove files in the linked directory instead of removing the symlink itself. ([\#224](https://github.com/boostorg/filesystem/issues/224))

  - On Windows, in `remove` and `remove_all` implementation, use POSIX semantics for file removal, when supported by the OS (Windows 10 1709 and later). When POSIX semantics is supported, the file name is removed from the filesystem namespace as soon as the file is marked for deletion, even if it is still open and in use. With legacy Windows semantics, the file name remains present in the the filesystem namespace until the last file handle to the file is closed, which allows the file marked for deletion to be opened and prevents creating new files with the same name. ([\#216](https://github.com/boostorg/filesystem/issues/216))

  - On Windows, `remove` and `remove_all` now support deleting read-only directories. Support for removing read-only non-directory files was added previously.

  - On Windows, `directory_iterator` internal implementation has been reworked to better utilize modern Windows APIs, which may improve performance while handling symlinks.

  - On Windows, initialize internal WinAPI function pointers early, if possible, to allow Boost.Filesystem operations to be invoked in global constructors. This is only supported on MSVC, GCC, Clang and compatible compilers.

  - On Windows, `resize_file` should no longer fail with an error if the file to be resized is opened.

  - Disabled use of the `statx` syscall on Android prior to 11.0 (API version 30). The syscall is blacklisted by seccomp and causes process termination in runtime. ([\#229](https://github.com/boostorg/filesystem/issues/229))

  - **Deprecated:** `boost``/``filesystem``/``string_file``.``hpp` header is deprecated and will be removed in a future release. The header is no longer included by `boost``/``filesystem``.``hpp` by default. Users are advised to implement the functionality themselves or migrate to other implementations.

  - **Deprecated:** Windows CE support is deprecated and will be removed in a future release. Windows CE has been untested for many years and is likely non-functional.

- [Geometry](/libs/geometry/):
  - Major change
    - [PR#977](https://github.com/boostorg/geometry/pull/977) Rescaling is turned off by default. This avoids many related bugs in set operations and buffer.

  - Improvements
    - [PR#923](https://github.com/boostorg/geometry/pull/923) Added algorithm closest_points for cartesian point/geometry.

    - [PR#939](https://github.com/boostorg/geometry/pull/939) Added algorithm closest_points for other coordinate systems and geometry combinations excl. boxes.

    - [PR#961](https://github.com/boostorg/geometry/pull/961) Added Web Mercator projection.

    - [PR#966](https://github.com/boostorg/geometry/pull/966) More efficient cartesian distance strategy used in simplify.

  - Solved issues
    - [\#956](https://github.com/boostorg/geometry/issues/956) Result of simplify algorithm with incorrect closure.

    - [\#962](https://github.com/boostorg/geometry/issues/962) Runtime error in R-tree deserialization due to load factor.

    - [\#971](https://github.com/boostorg/geometry/issues/971) R-tree insertion time impacted by use of long double on ARM platforms.

  - Bugfixes
    - [PR#936](https://github.com/boostorg/geometry/pull/936) Envelope of polygon containing pole.

    - [PR#948](https://github.com/boostorg/geometry/pull/948) Spherical and geographic envelope for near meridian segments.

    - [PR#974](https://github.com/boostorg/geometry/pull/974) Spheroidal normalization utilities for NaN coordinates.

    - Various fixes in set operations and buffer.

- [Integer](/libs/integer/):
  - Optimized `integer_log2` implementation to use bit operations internally. This allows to employ bit instructions available on most modern CPUs. ([\#31](https://github.com/boostorg/integer/issues/31))

- [IO](/libs/io/):
  - Added `boost``::``io``::``basic_nullbuf`, a null stream buffer, and `boost``::``basic_onullstream`, a null output stream (Glen Fernandes).

- [Iterator](/libs/iterator/):
  - In `counting_iterator`, added support for built-in 128-bit integer types supported by gcc and clang and compatible compilers on some target platforms.

  - Silenced gcc warnings about deprecated implicit copy assignment operator in `counting_iterator`.

- [JSON](/libs/json/):
  - Standalone mode of the library is removed. Users who wish to continue using standalone JSON can switch to [the C++ Alliance fork](https://github.com/CPPAlliance/standalone-json.git).

  - Add `std``::``error_code` overloads.

  - Add `boost``::``source_location` to `error_codes`.

  - Add support for JSON Pointer.

  - Naturally grow string during serialization.

- [LEAF](/libs/leaf/):
  - Support for FreeRTOS and other embedded platforms

  - Improved diagnostic information

  - Improved configuration macros

  - BOOST_LEAF_CHECK using statement expressions under \_\_GNUC\_\_

  - Fixed symbol demangling bug

- [Log](/libs/log/):
  - General changes:
    - In `text_file_backend`, added support for appending to a previously written log file, when file rotation is used and log file names use file counters.

    - **Breaking change:** The `file_collector` interface has changed:
      - `scan_for_files` method returns a `scan_result` structure that contains information collected during the scan;

      - `is_in_storage` method added for testing if a path refers to a file within the target storage directory.

    - Added a new `invoke_manip` stream manipulator that can be used for injecting user's function into a stream output expression.

  - Bug fixes:
    - Fixed file counter being set to zero if the user calls `text_file_backend``::``scan_for_files` multiple times, and the second and the following calls don't find any new files. ([\#179](https://github.com/boostorg/log/issues/179))

  - See [changelog](/libs/log/doc/html/log/changelog.html) for more details.

- [Multi-index Containers](/libs/multi_index/):
  - Improved the efficiency of `count` operations in ranked indices from `O``(``log``(``n``)`` ``+`` ``count``)` to `O``(``log``(``n``))`. Contributed by Damian Sawicki.

  - Maintenance work.

- [Nowide](/libs/nowide/):
  - Fix compilation issues on some platforms (e.g. GCC 11 on MinGW-w64 and Cygwin)

  - Fix missing include when using `BOOST_USE_WINDOWS_H` and `WIN32_LEAN_AND_MEAN`

  - Add sanity check when using `boost``::``nowide``::``stat` with `boost``::``nowide``::``stat_t`

- [Optional](/libs/optional/):
  - Fixed [issue \#98](https://github.com/boostorg/optional/issues/98).

  - Fixed [issue \#92](https://github.com/boostorg/optional/issues/92).

  - Added support for `BOOST_NO_IOSTREAM`.

  - Now aligned storage uses `unsigned`` ``char` rather than `char` to avoid UB.

  - Now using cv-unqualified `value_type` with placement `new` to avoid UB.

- [Predef](/libs/predef/):
  - Version 1.14.0

  - Add detection of LoongArch (from Zhang Na).

- [QVM](/libs/qvm/):
  - Added constexpr under C++17

  - Improved single header distribution

- [Smart Pointers](/libs/smart_ptr/):
  - Added `boost``::``get_allocator_pointer` to obtain the Allocator pointer from the result of `boost``::``allocate_unique` (Glen Fernandes).

- [System](/libs/system/):
  - Added a `boost``::``source_location` parameter to `throw_exception_from_error`.

  - Added `throw_exception_from_error` overloads for `errc``::``errc_t`, `std``::``error_code`, `std``::``errc`, `std``::``exception_ptr`.

  - `result``<``T``>::``value` now automatically supplies `BOOST_CURRENT_LOCATION` to `throw_exception_from_error` via a default argument.

  - Added an `errc``::``make_error_code` overload taking a source location.

- [ThrowException](/libs/throw_exception/):
  - Added `boost``::``throw_with_location`, a more lightweight alternative of `BOOST_THROW_EXCEPTION` for programs that do not use Boost.Exception.

- [Unordered](/libs/unordered/):
  - All containers have been updated to support heterogeneous `count`, `equal_range` and `find`.

  - All containers now implement the member function `contains`.

  - `erase_if` has been implemented for all containers.

  - All containers have been updated to support heterogeneous `erase` and `extract`.

  - Changed behavior of `reserve` to eagerly allocate.

  - Various warning fixes in the test suite.

  - Update code to internally use `boost``::``allocator_traits`.

  - Switch to Fibonacci hashing.

  - Update documentation to be written in AsciiDoc instead of QuickBook.

- [Variant2](/libs/variant2/):
  - Added `operator``<<` for `monostate`.

- [Wave](/libs/wave/):
  - C++11 now required for building Wave itself

  - Fixed bugs:
    - [\#135](https://github.com/boostorg/wave/issues/135): Comma operators in array subscripts are deprecated in C++20

    - [\#137](https://github.com/boostorg/wave/issues/137): Simple unknown directive =\> found_unknown_directive is not called, stripped of pound.

    - [\#138](https://github.com/boostorg/wave/issues/138): Empty ifdef block does not emit line directive for missing whitespace

    - [\#143](https://github.com/boostorg/wave/issues/143): Parsing \_\_has_include() fails with trailing tokens

    - [\#145](https://github.com/boostorg/wave/issues/145): Sanitizer complains about reset_version()

    - [\#147](https://github.com/boostorg/wave/issues/147): bitwise operations between different enumeration types are deprecated

### Updated Tools

- [Build](/tools/build/):
  - Includes release of [B2 version 4.8.2](/tools/build/doc/html/#_version_4_8_2).

### Compilers Tested

Boost's primary test compilers are:

- Linux:
  - Clang: 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 12.0.0

  - Clang, C++11: 3.4, 11.0.0

  - Clang, C++14: 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 5.0, 12.0.0

  - Clang, C++17: 6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0, 12.0.0

  - Clang, C++20: 11.0.0, 12.0.0, 13.0.0

  - GCC: 4.6.3, 11

  - GCC, C++11: 4.7.3, 4.8.5, 11

  - GCC, C++14: 5.4.0, 6.4.0, 7.3.0, 8.0.1, 9.1.0, 11

  - GCC, C++17: 7.3.0, 8.0.1, 9.1.0, 11

  - GCC, C++20: 8.0.1, 9.1.0, 10, 11

- OS X:
  - Apple Clang: 11.0.3

  - Apple Clang, C++11: 11.0.3

  - Apple Clang, C++14: 11.0.3

  - Apple Clang, C++17: 11.0.3

  - Apple Clang, C++20: 11.0.3

- Windows:
  - Visual C++: 10.0, 11.0, 12.0, 14.0, 14.1, 14.2

### Acknowledgements

Marshall Clow, Michael Caisse and Glen Fernandes managed this release.

Copyright Rene Rivera 2006-2007.
