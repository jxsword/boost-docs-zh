# Version 1.71.0

## Version 1.71.0

August 19th, 2019 15:31 GMT

[Documentation](/doc/libs/1_71_0/)

| Platform | File | SHA256 Hash |
|----|----|----|
| unix | [boost_1_71_0.tar.bz2](https://archives.boost.io/release/1.71.0/source/boost_1_71_0.tar.bz2) | d73a8da01e8bf8c7eda40b4c84915071a8c8a0df4a6734537ddde4a8580524ee |
|  | [boost_1_71_0.tar.gz](https://archives.boost.io/release/1.71.0/source/boost_1_71_0.tar.gz) | 96b34f7468f26a141f6020efb813f1a2f3dfb9797ecf76a7d7cbd843cc95f5bd |
| windows | [boost_1_71_0.7z](https://archives.boost.io/release/1.71.0/source/boost_1_71_0.7z) | 1b3949ffddf56129141032542523920034f2e69775fb9332a52ba37c548dbf35 |
|  | [boost_1_71_0.zip](https://archives.boost.io/release/1.71.0/source/boost_1_71_0.zip) | 85a94ac71c28e59cf97a96714e4c58a18550c227ac8b0388c260d6c717e47a69 |

Downloads {.download-table}

\* The download links are supported by grants from [The C++ Alliance](https://cppalliance.org/).  
  

### New Libraries

- [Variant2](/libs/variant2/): A never-valueless, strong guarantee implementation of `std``::``variant`, from Peter Dimov.

### Updated Libraries

- [Align](/libs/align/):
  - Support for any integral type in the integral versions of `align_up` and `align_down`.

  - Revised the implementation of `aligned_allocator` to no longer require a specialization for `void`.

  - Define `propagate_on_container_move_assignment` and `is_always_equal` in `aligned_allocator`.

- [Asio](/libs/asio/):
  - Improved performance slightly by eliminating a redundant move construction when completed handlers are dispatched.

  - Eliminated a compiler warning by annotating a `case` fall-through in the free function `connect``()` implementation.

  - Fixed the `is_``*``_buffer_sequence` detection traits for user-defined sequence types.

  - Fixed some Windows-specific warnings about an incompatible pointer cast when obtaining the `CancelIoEx` entry point.

  - Changed to automatically set the defaults when opening a serial port on Windows.

  - Changed the serial port `get_option``()` member function to be const.

  - Fixed a name hiding issue with the WinRT stream-oriented socket backend's `shutdown` function.

  - Applied a minor fix to the documentation for `is_dynamic_buffer`.

  - Added some support for Haiku OS.

  - Added wolfSSL compatability.

  - Changed to require C++17 or later for coroutines TS support with clang.

  - Fixed a doxygen generation problem in the tutorial.

  - Ensured example programs are correctly incorporated into the documentation.

- [Any](/libs/any/):
  - Static initialization of the default constructed `boost``::``any` is now possible.

  - Fixed performance regression in assignment on a compilers without move-semantics.

  - Maintenance work.

- [Beast](/libs/beast/):
  - This version consists mostly of bug fixes and performance improvements.

  - Substantial work included for the split compilation mode, to reduce compile time when defining `BOOST_BEAST_SEPARATE_COMPILATION`.

  - We'd love to know how you or your company use Beast, consider adding an item to the [Companies and Individuals Using Beast](https://github.com/boostorg/beast/wiki/Companies-and-Individuals-Using-Beast) list.

  - See the full [Release Notes](/libs/beast/doc/html/beast/release_notes.html) for a complete list of changes.

- [Circular Buffer](/libs/circular_buffer/):
  - Correct doxygen generated reference to no longer show internal members. (Glen Fernandes)

  - Eliminate ubsan warning on `add` and `sub`. (Glen Fernandes)

  - Fix incorrect check in `is_uninitialized`. (Niklas Fejes)

- [Container](/libs/container/):
  - Fixed bugs:
    - [GitHub \#47: *"added alignment specification for small_vector"*](https://github.com/boostorg/container/pull/47).

    - [GitHub \#88: *"Implement C++17 MoveAssignable requirements for self-move assignments"*](https://github.com/boostorg/container/issues/88).

    - [GitHub \#107: *"Alignment ignored in resource_adaptor"*](https://github.com/boostorg/container/issues/107).

    - [GitHub \#109: *"Get rid of integer overflow in copy_move_algo.hpp (-fsanitize=integer)"*](https://github.com/boostorg/container/pull/109).

    - [GitHub \#110: *"Avoid gcc 9 deprecated copy warnings in new_allocator.hpp"*](https://github.com/boostorg/container/pull/110).

    - [GitHub \#112: *"vector::resize() compilation error with msvc-10..12: data is not a member of boost::detail::aligned_storage"*](https://github.com/boostorg/container/issues/112).

    - [GitHub \#114: *"Fix small_vector noexcept specification"*](https://github.com/boostorg/container/issues/114).

    - [GitHub \#116: *"MSVC + boost 1.70 compilation error when windows.h is already included (detail/thread_mutex.hpp)"*](https://github.com/boostorg/container/issues/116).

    - [GitHub \#117: *"flat_map/map::insert_or_assign with hint has wrong return types"*](https://github.com/boostorg/container/issues/117).

    - [GitHub \#118: *"Non-unique inplace_set_difference used in in flat_tree_merge_unique and iterator invalidation in insert_unique"*](https://github.com/boostorg/container/issues/118).

    - [GitHub \#122: *"Fix has_trivial_destructor_after_move"*](https://github.com/boostorg/container/issues/122).

    - [GitHub \#123: *"With heterogeneous lookup, `equal_range` can result in a range with length greater than 1"*](https://github.com/boostorg/container/issues/123).

  - `deque` can now have options, using `deque_options`. The block size/bytes can be be specified.

  - `static_vector` can now have options, using `static_vector_options`. Alignment and throwing behaviour can be be specified.

  - `small_vector` can now have options, using `small_vector_options`. Alignment and growth factor can be be specified.

- [Context](/libs/context/):
  - Add support for RISC-V LP64D

  - [\#72](https://github.com/boostorg/context/issues/72): Fix ABI violation on ppc64 ELFv2

  - [\#99](https://github.com/boostorg/context/issues/99): cleanup of stack if creating ucontext fails

- [Conversion](/libs/conversion/):
  - Maintenance work.

- [Core](/libs/core/):
  - Added functions `alloc_construct`, `alloc_construct_n`, `alloc_destroy`, and `alloc_destroy_n` in `<``boost``/``core``/``alloc_construct``.``hpp``>` for allocator aware and exception safe construction and destruction of objects and arrays. (Glen Fernandes)

  - Added constexpr functions `first_scalar` in `<``boost``/``core``/``first_scalar``.``hpp``>` for obtaining a pointer to the first scalar element of an array. Given a pointer of type `T``*` they return a pointer of type `remove_all_extents_t``<``T``>*`. (Glen Fernandes)

  - Added class template `noinit_adaptor` in `<``boost``/``core``/``noinit_adaptor``.``hpp``>` which is an allocator adaptor that converts any allocator into one whose `construct``(``ptr``)` performs default initialization via placement new, and whose `destroy``(``ptr``)` invokes the `value_type` destructor directly. (Glen Fernandes)

  - Added class template `default_allocator` in `<``boost``/``core``/``default_allocator``.``hpp``>`, which can serve as a minimal default allocator that has interface similar to C++20 `std``::``allocator`, supports configurations with disabled exceptions and does not have `std` as an associated namespace. The allocator uses `operator`` ``new` and `operator`` ``delete` for allocation. (Glen Fernandes)

  - In `<``boost``/``core``/``uncaught_exceptions``.``hpp``>` header, added workarounds for better compatibility with QNX SDP 7.0 when libc++/libc++abi libraries are used. (Andrey Semashev, [\#59](https://github.com/boostorg/core/issues/59))

  - The `<``boost``/``detail``/``sp_typeinfo``.``hpp``>` header is now marked as deprecated and will be removed in a future release. `<``boost``/``core``/``typeinfo``.``hpp``>` should be used instead. (Peter Dimov)

- [Dynamic Bitset](/libs/dynamic_bitset/):
  - Enabled hardware-assisted popcount on MSVC ([PR#38](https://github.com/boostorg/dynamic_bitset/pull/38)).

  - Added support for boost::hash and std::hash ([PR#45](https://github.com/boostorg/dynamic_bitset/pull/45)).

  - Support copy-initialization with default constructor ([PR#48](https://github.com/boostorg/dynamic_bitset/pull/48)).

- [Endian](/libs/endian/):
  - Clarified requirements on the value type template parameter

  - Added support for `float` and `double`

  - Added `endian_load`, `endian_store`

  - Updated `endian_reverse` to correctly support all non-`bool` integral types

  - Moved deprecated names to the deprecated header `endian``.``hpp`

- [Fiber](/libs/fiber/):
  - documentation for shared_work updated

- [Filesystem](/libs/filesystem/):
  - Fixed incorrect `error_code` returned from directory iterator increment when `readdir_r` is used.

  - For `path`, fixed rvalue-aware `operator``/` return type to return an rvalue instead of rvalue reference. This fixes leaving a dangling reference in the user's code if the result of `operator``/` is bound to a const reference. ([\#110](https://github.com/boostorg/filesystem/issues/110))

  - Fixes for better compatibility with Windows CE. ([PR#24](https://github.com/boostorg/filesystem/pull/24))

  - Added minimal support for CMake. ([PR#106](https://github.com/boostorg/filesystem/pull/106))

- [Flyweight](/libs/flyweight/index.html):
  - Maintenance work.

- [Histogram](/libs/histogram/index.html):
  - New features:
    - Support for thread-safe storages and new thread-safe accumulators

    - Support for compiling without exceptions/RTTI (increases performance by 10-20 %) (with Glen Fernandes)

    - Performance improvements for 1D and 2D histograms

    - boost::histogram::indexed now returns forward iterator range instead of input iterator range

    - boost::histogram::indexed_range::accessor is now non-copyable and acts like reference to cell value, making more algorithms from the C++ stdlib work

    - boost::histogram::algorithm::reduce with new slice option and option fusion

    - boost::histogram::algorithm::project accepts runtime indices for static histograms

  - Bug Fixes:
    - boost::histogram::algorithm::reduce also works on histograms that have some axis types without reduction support

    - boost::histogram::axis::traits::update now works correctly for boost::histogram::axis::variant

  - Other:
    - 100 % test coverage

    - Reduced internal Boost dependencies

    - Improved documentation and examples

    - Guaranteed no-throw moves for all builtin axis types

    - Compile cleanly at higher warning levels

  - See [changelog](/libs/histogram/doc/html/histogram/history.html) for more details.

- [IoStreams](/libs/iostreams/):
  - Fixed processing of multi-stream files ([PR#87](https://github.com/boostorg/iostreams/pull/87)).

  - Added support for multi-threaded LZMA ([PR#95](https://github.com/boostorg/iostreams/pull/95)).

- [Interprocess](/libs/interprocess/):
  - [GitHub \#85 (*"warning: Implicit conversion loses integer precision"*)](https://github.com/boostorg/interprocess/pull/85).

  - [GitHub \#86 (*"warning: Possible misuse of comma operator"*)](https://github.com/boostorg/interprocess/pull/86).

- [Intrusive](/libs/intrusive/):
  - [GitHub \#42: *Documentation does not describe treap priority_of_value changes*](https://github.com/boostorg/intrusive/pull/42)

  - [GitHub \#43: *Fix tests with BOOST_INTRUSIVE_VARIADIC_TEMPLATES enabled*](https://github.com/boostorg/intrusive/pull/43)

  - [GitHub \#45: *Disable variadic templates for MSVC-12 to avoid ICEs*](https://github.com/boostorg/intrusive/pull/45)

- [LexicalCast](/libs/lexical_cast/):
  - Added tests for `boost``::``filesystem``::``path` conversions [\#25](https://github.com/boostorg/lexical_cast/issues/25).

  - Maintenance work, including [\#28](https://github.com/boostorg/lexical_cast/issues/28).

- [Log](/libs/log/):
  - New features:
    - Improved support for C++17 `std``::``string_view` in `basic_formatting_ostream`. The string view can now participate in character code conversion on output.

    - Added `auto_newline` formatter and stream manipulator. It can be used to ensure that formatted output always ends with a newline while avoiding duplicate newlines.

    - In the output stream, text file and text multi-file sink backends added support for configuring behavior with regard to appending a trailing newline to every formatted log record. Use `auto_newline_mode` named parameter of the backend constructor or call the `set_auto_newline_mode` method on the sink backend.

    - **Note:** The default behavior with regard to trailing newlines added by sink backends has changed slightly compared to the previous Boost.Log releases. The backends will now only add a trailing newline if there isn't one in the formatted log message string already. In previous releases a newline was added unconditionally.

    - Added support for passing arbitrary function objects in the `filter` and `format` named parameters to sink constructors and convenience functions for initializing sinks. For example, it is now possible to specify C++11 lambda functions directly in these parameters. ([\#63](https://github.com/boostorg/log/issues/63))

    - In the default filter and formatter factories used in filter and formatter parsers, added support for severity level attribute values of type `boost``::``log``::``trivial``::``severity_level`. For filters, the support is limited to attributes with "Severity" name.

  - Bug fixes:
    - Fixed incorrect parsing of components of the rotated file names while scanning for files in the text file sink backend. If the file name pattern ended with a placeholder (for example, a file counter), the `scan_for_files` method would not find files matching that pattern in the target storage, leaving them unmanaged. In particular, such files would not be deleted to free target storage. ([\#78](https://github.com/boostorg/log/issues/78))

    - Updated `basic_formatting_ostream` and `basic_record_ostream` to make it possible to overload stream output operators for pointers to user-defined types. User-defined `operator``<<` overloads taking `std``::``basic_ostream` and a pointer argument should now be picked up by the compiler when the pointer is being written to one of Boost.Log streams. ([\#84](https://github.com/boostorg/log/issues/84))

  - See [changelog](/libs/log/doc/html/log/changelog.html) for more details.

- [Math](/libs/math/):
  - New features:
    - Catmull-Rom interpolator now works in C++11

    - Cardinal quadratic B-spline interpolation

    - Domain of elliptic integrals extended

    - sin_pi and cos_pi performance improvements

    - Forward-mode automatic differentiation

    - Vector valued barycentric rational interpolation

    - Ooura's method for evaluation of Fourier integrals

  - Bug fixes:
    - Multiple compatibility issues with Multiprecision fixed

    - Lambert-W fixed on a rare architecture

- [Metaparse](/libs/metaparse/):
  - New features:
    - In C++11 variadic template support for the following: `sequence`, `one_of_c`, `one_of`, `repeated_one_of`, `repeated_one_of1`, `one_char_except_c`, `one_char_except`.

  - Bug fixes:
    - `BOOST_METAPARSE_STRING` does not use out of range character values as template arguments.

    - `any_of_c``<>` does not create empty array in C++14.

- [Move](/libs/move/):
  - [Git Issue \#26: *"Invalid iterator increment/decrement in the last iteration of adaptive_sort_combine_blocks"*](https://github.com/boostorg/move/issues/26).

- [Multi Array](/libs/multi_array/):
  - Simplify allocator support by using new `alloc_construct_n` and `alloc_destroy_n` facilities from Core. (Glen Fernandes)

- [Multi-index Containers](/libs/multi_index/):
  - Added [variants of `const_mem_fun` and `mem_fun`](/libs/multi_index/doc/tutorial/key_extraction.html#x_mem_fun) for differently qualified member functions (issue [\#24](https://github.com/boostorg/multi_index/issues/24)).

  - Terse [`key`](/libs/multi_index/doc/reference/key_extraction.html#key) specification syntax now correctly handles `noexcept`-specified member functions (issue [\#24](https://github.com/boostorg/multi_index/issues/24)).

- [Outcome](/libs/outcome/):
  - Enhancements:
    - [\#184](https://github.com/ned14/outcome/issues/184) As per request from Boost release managers, relocated `version``.``hpp` and `revision``.``hpp` into detail, and added the Boost licence boilerplate to the top of every source file which was missing one (I think). Also took the opportunity to run the licence restamping script over all Outcome, so copyright dates are now up to date.

    - [\#185](https://github.com/ned14/outcome/issues/185) Add FAQ item explaining issue \#185, and why we will do nothing to fix it right now.

    - [\#189](https://github.com/ned14/outcome/issues/189) Refactored the `OUTCOME_TRY` implementation to use more clarified customisation points capable of accepting very foreign inputs. Removed the `std``::``experimental``::``expected``<``T``,`` ``E``>` specialisations, as those are no longer necessary. Fixed the documentation for the customisation points which previously claimed that they are ADL discovered, which they are not. Added a recipe describing how to add in support for foreign input types.

    - [\#183](https://github.com/ned14/outcome/issues/183) Added a separate `motivation``/``plug_error_code` specifically for Boost.

  - Bug fixes:
    - `OUTCOME_VERSION_MINOR` hadn't been updated to 1.

    - [\#181](https://github.com/ned14/outcome/issues/181) Fix issue \#181 where Outcome didn't actually implement the strong swap guarantee, despite being documented as doing so.

    - [\#190](https://github.com/ned14/outcome/issues/190) Fix issue \#190 in Boost edition where unit test suite was not runnable from the Boost release distro.

    - [\#182](https://github.com/ned14/outcome/issues/182) Fix issue \#182 where `trait``::``is_exception_ptr_available``<``T``>` was always true, thus causing much weirdness, like not printing diagnostics and trying to feed everything to `make_exception_ptr``()`.

    - [\#192](https://github.com/ned14/outcome/issues/192) Fix issue \#192 where the `std``::``basic_outcome_failure_exception_from_error``()` was being defined twice for translation units which combine standalone and Boost Outcome's.

- [Parameter](/libs/parameter/doc/html/index.html):
  - Upgraded keyword generation macro `BOOST_PARAMETER_TEMPLATE_KEYWORD` ([PR#15](https://github.com/boostorg/parameter/pull/15)).

  - Moved keyword generation macro `BOOST_PARAMETER_NESTED_KEYWORD` from [Accumulators](/libs/accumulators/doc/html/index.html) to this library ([PR#28](https://github.com/boostorg/parameter/pull/28)).

  - Added support for `std``::``reference_wrapper` and `std``::``ref``()` ([PR#16](https://github.com/boostorg/parameter/pull/16)).

  - Moved `boost``::``parameter``::``required`, `boost``::``parameter``::``optional`, and `boost``::``parameter``::``deduced` metafunction definitions to their own header files in directory boost/parameter ([PR#18](https://github.com/boostorg/parameter/pull/18)).

  - Added support for Boost.[Parameter](/libs/parameter/doc/html/index.html)-enabled function call operators ([PR#20](https://github.com/boostorg/parameter/pull/20)).

  - Added support for parameter category qualifiers "forward", "consume", and "move_from" (current qualifiers are "in", "out", and "in_out") ([PR#21](https://github.com/boostorg/parameter/pull/21)) ([PR#23](https://github.com/boostorg/parameter/pull/23)) based on <http://www.modernescpp.com/index.php/c-core-guidelines-how-to-pass-function-parameters>. Added new usage syntax `BOOST_PARAMETER_NAME``((``object``-``name``),`` ``namespace``-``name``)`` ``qualifier``(``tag``-``name``))` and `BOOST_PARAMETER_NAME``(``qualifier``(``name``))`. (Existing code that uses qualifiers directly and correctly with `BOOST_PARAMETER_FUNCTION` and other code generation macros should remain unaffected for now, so no breaking changes.) The reason for the change in usage is to enable applying of parameter category constraints to Boost.[Parameter](/libs/parameter/doc/html/index.html)-enabled functions and constructors invoked through argument composition. (Otherwise, it is currently possible to use argument composition to bypass parameter category constraints applied in `BOOST_PARAMETER_FUNCTION` et. al.)

  - Added support for perfect forwarding ([PR#23](https://github.com/boostorg/parameter/pull/23)) ([PR#26](https://github.com/boostorg/parameter/pull/26)), so that `parameter``::``parameters``::``operator``()` can accept non-`const` rvalues. As a positive side effect, Boost.[Parameter](/libs/parameter/doc/html/index.html)-enabled functions and constructors are no longer bound by `BOOST_PARAMETER_MAX_ARITY` on compilers that support perfect forwarding. User code can now check for this support by detecting the configuration macro `BOOST_PARAMETER_HAS_PERFECT_FORWARDING`, or manually turn off this support by defining the configuration macro `BOOST_PARAMETER_DISABLE_PERFECT_FORWARDING`.

  - Added metafunctions `boost``::``parameter``::``is_argument_pack` ([PR#27](https://github.com/boostorg/parameter/pull/27)), `boost``::``parameter``::``are_tagged_arguments` ([PR#52](https://github.com/boostorg/parameter/pull/52)), and `boost``::``parameter``::``result_of``::``compose` ([PR#75](https://github.com/boostorg/parameter/pull/75)).

  - Added variadic function template `boost``::``parameter``::``compose``()` which takes in named arguments and returns them in an argument pack ([PR#52](https://github.com/boostorg/parameter/pull/52)). For compilers that do not support perfect forwarding, the configuration macro `BOOST_PARAMETER_COMPOSE_MAX_ARITY` determines the maximum number of arguments that `boost``::``parameter``::``compose``()` can take in ([PR#61](https://github.com/boostorg/parameter/pull/61)).

  - Added code generation macros `BOOST_PARAMETER_BASIC_FUNCTION_CALL_OPERATOR`, `BOOST_PARAMETER_BASIC_CONST_FUNCTION_CALL_OPERATOR`, `BOOST_PARAMETER_NO_SPEC_FUNCTION`, `BOOST_PARAMETER_NO_SPEC_MEMBER_FUNCTION`, `BOOST_PARAMETER_NO_SPEC_CONST_MEMBER_FUNCTION`, `BOOST_PARAMETER_NO_SPEC_FUNCTION_CALL_OPERATOR`, `BOOST_PARAMETER_NO_SPEC_CONST_FUNCTION_CALL_OPERATOR`, `BOOST_PARAMETER_NO_SPEC_CONSTRUCTOR`, and `BOOST_PARAMETER_NO_SPEC_NO_BASE_CONSTRUCTOR` ([PR#52](https://github.com/boostorg/parameter/pull/52)).

  - Added support for Boost.[MP11](/libs/mp11/doc/html/mp11.html) ([PR#47](https://github.com/boostorg/parameter/pull/47)) ([PR#66](https://github.com/boostorg/parameter/pull/66)) ([PR#70](https://github.com/boostorg/parameter/pull/70)). User code can now check for this support by detecting the configuration macro `BOOST_PARAMETER_CAN_USE_MP11`, or manually turn off this support by defining the configuration macro `BOOST_PARAMETER_DISABLE_MP11_USAGE`.

  - Improved support for parameter-dependent return types via SFINAE ([PR#73](https://github.com/boostorg/parameter/pull/73)).

- [PtrContainer](/libs/ptr_container/):
  - Fix a ptr_vector regression introduced in 1.66.0 ([PR#24](https://github.com/boostorg/ptr_container/pull/24)).

- [PolyCollection](/libs/poly_collection/):
  - Maintenance work.

- [SmartPtr](/libs/smart_ptr/):
  - Added aliasing constructors to `weak_ptr`

  - Added `weak_ptr``<``T``>::``empty``()`

  - Added `enable_shared_from`, `shared_from`, and `weak_from`

- [Stacktrace](/libs/stacktrace/):
  - Fixed output of `name``()`, `source_location``()` and `source_line``()` for the default constructed `frame` with thread sanitizer builds in C++98 mode.

  - Fixed output of long strings from `name``()` and `source_location``()` on MSVC [\#78](https://github.com/boostorg/stacktrace/issues/78).

  - Maintenance work.

- [Test](/libs/test/):
  - Boost.test v3.11 see the [Changes log](libs/test/doc/html/boost_test/change_log.html) for more details.

  - Breaking changes:
    - Boost.Test shows deprecation warnings if some very old headers as deprecated. If you encounter such warnings, please follow the indications: those headers will be removed in a future release.

  - New feature:
    - Now `BOOST_TEST` can be used to compare abstract types

  - Bug fixes and pull requests:
    - GitHub Issues: [\#209](https://github.com/boostorg/test/issues/209), [\#218](https://github.com/boostorg/test/issues/218)

    - GitHub Pull Requests: [PR#219](https://github.com/boostorg/test/pull/219), [PR#224](https://github.com/boostorg/test/pull/224)

- [Utility](/libs/utility/):
  - Implemented function template `ostream_string` in `<``boost``/``utility``/``ostream_string``.``hpp``>` to optimally write any kind of string content to an output stream. It satisfies the requirements of \[ostream.formatted.reqmts\]. (Glen Fernandes)

  - Optimized the stream output operators of `basic_string_view` and `basic_string_ref` to write directly to the `rdbuf` stream buffer. (Glen Fernandes)

- [Uuid](/libs/uuid/):
  - **Breaking change:** MD5 name-based uuid generation was corrected to be identical on all endian systems. Define `BOOST_UUID_COMPAT_PRE_1_71_MD5` to keep the result in a format compatible with 1.66 through 1.70. This does not affect the default name-based uuid generation which is based on SHA1. ([PR#109](https://github.com/boostorg/uuid/pull/109))

- [Variant](/libs/variant/):
  - Fixed compilation of `boost``::``apply_visitor` with variants passed by non const reference in [PR#68](https://github.com/boostorg/variant/pull/68). Many thanks to Ed Catmur for providing the fix.

  - Added support for std::hash ([PR#49](https://github.com/boostorg/variant/pull/49)). Macro `BOOST_VARIANT_DO_NOT_SPECIALIZE_STD_HASH` could be defined to avoid those specializations.

  - Added micro optimizations for binary size and performance by Nikita Kniazev in [PR#63](https://github.com/boostorg/variant/pull/63) and [PR#66](https://github.com/boostorg/variant/pull/66).

  - Maintenance work, including [PR#64](https://github.com/boostorg/variant/pull/64) by Nikita Kniazev and [PR#67](https://github.com/boostorg/variant/pull/67) by Hans Dembinski.

- [YAP](/libs/yap/):
  - Added an example showing how to make self-evaluating YAP expressions (that is, expressions that don't need an explicit call to `evaluate``()` or `transform``()`).

### Compilers Tested

Boost's primary test compilers are:

- Linux:
  - Clang: 3.0, 4.0.1, 6.0.1

  - Clang, C++0x: 3.0

  - Clang, C++11: 3.0, 3.1, 3.2, 3.3, 3.4, 4.0.1, 6.0.1, 7.0.0, 8.0.0

  - Clang, C++14: 3.5.0, 3.6.0, 3.7.1, 3.8.0, 3.9.1, 4.0.0, 4.0.1, 5.0.2, 6.0.1, 7.0.0, 8.0.0

  - Clang, C++17: 5.0.2, 6.0.1, 7.0.0, 8.0.0

  - GCC: 4.4.7, 4.5.3, 4.6.3, 5.4.0, 8.0.1

  - GCC, C++0x: 4.4.7

  - GCC, C++11: 4.7.3, 4.8.5, 4.9.4, 5.4.0, 6.4.0, 7.1.0, 8.0.1

  - GCC, C++14: 5.4.0, 5.5.0, 6.4.0, 7.1.0, 7.3.0, 8.0.1

  - GCC, C++17: 7.3.0, 8.0.1

  - Intel, C++14: 18.0

- OS X:
  - Apple Clang: 9.0.0, 9.1.0, 10.0.0

  - Apple Clang, C++11: 9.0.0, 9.1.0, 10.0.0

  - Apple Clang, C++14: 9.0.0, 9.1.0, 10.0.0

  - Apple Clang, C++17: 9.1.0, 10.0.0

  - Apple Clang, C++1z: 9.0.0

  - Apple Clang, C++2a: 10.0.0

- Windows:
  - GCC: 3.4.5, 4.1.2, 4.2.4, 4.3.3, 4.4.0, 4.5.4

  - GCC, C++0x: 4.6.4

  - GCC, C++11: 4.7.3, 4.8.1, 4.9.3

  - GCC, C++14: 5.1.0, 5.2.0, 5.3.0, 6.1.0, 6.2.0, 6.3.0, 6.4.0

  - GCC, C++17: 7.1.0, 7.2.0, 7.3.0

  - Visual C++: 7.1, 8.0, 9.0, 10.0, 11.0, 12.0, 14.0, 14.1

- FreeBSD:
  - Clang: 4.0.0

  - Clang, C++11: 4.0.0

  - Clang, C++14: 4.0.0

  - Clang, C++1z: 4.0.0

Boost's additional test compilers include:

- Linux:
  - Clang: 3.0, 3.8.1, 3.9.1, 4.0.1, 5.0.2, 6.0.1

  - Clang, C++0x: 3.0

  - Clang, C++11: 3.0, 3.1, 3.2, 3.3, 3.4, 4.0.1, 6.0.1, 7.0.0, 8.0.0

  - Clang, C++14: 3.5.0, 3.6.0, 3.7.1, 3.8.0, 3.9.1, 4.0.0, 4.0.1, 5.0.2, 6.0.1, 7.0.0, 8.0.0

  - Clang, C++17: 5.0.2, 6.0.1, 7.0.0, 8.0.0

  - GCC: 4.4.7, 4.5.3, 4.6.3, 4.9.4, 5.4.0, 5.5.0, 8.0.1

  - GCC, C++0x: 4.4.7

  - GCC, C++11: 4.7.3, 4.8.5, 4.9.4, 5.4.0, 6.4.0, 7.1.0, 8.0.1

  - GCC, C++14: 5.4.0, 5.5.0, 6.3.0, 6.4.0, 7.1.0, 7.3.0, 8.0.1, 8.1.0

  - GCC, C++17: 7.3.0, 8.0.1

  - Intel, C++14: 18.0

- OS X:
  - Apple Clang: 9.0.0, 9.1.0, 10.0.0

  - Apple Clang, C++11: 9.0.0, 9.1.0, 10.0.0

  - Apple Clang, C++14: 9.0.0, 9.1.0, 10.0.0

  - Apple Clang, C++17: 9.1.0, 10.0.0

  - Apple Clang, C++1z: 9.0.0

  - Apple Clang, C++2a: 10.0.0

- Windows:
  - GCC: 3.4.5, 4.1.2, 4.2.4, 4.3.3, 4.4.0, 4.5.4

  - GCC, C++0x: 4.6.4

  - GCC, C++11: 4.7.3, 4.8.1, 4.9.3

  - GCC, C++14: 5.1.0, 5.2.0, 5.3.0, 6.1.0, 6.2.0, 6.3.0, 6.4.0

  - GCC, C++17: 7.1.0, 7.2.0, 7.3.0

  - Visual C++: 7.1, 8.0, 9.0, 10.0, 11.0, 12.0, 14.0, 14.1

- FreeBSD:
  - Clang: 4.0.0

  - Clang, C++11: 4.0.0

  - Clang, C++14: 4.0.0

  - Clang, C++1z: 4.0.0

### Acknowledgements

Marshall Clow and Michael Caisse managed this release.

Copyright Rene Rivera 2006-2007.
