# Version 1.51.0

## Version 1.51.0

August 20th, 2012 23:00 GMT

[Documentation](/doc/libs/1_51_0/)

| Platform | File |
|----|----|
| unix | [boost_1_51_0.tar.bz2](http://sourceforge.net/projects/boost/files/boost/1.51.0/boost_1_51_0.tar.bz2) |
|  | [boost_1_51_0.tar.gz](http://sourceforge.net/projects/boost/files/boost/1.51.0/boost_1_51_0.tar.gz) |
| windows | [boost_1_51_0.7z](http://sourceforge.net/projects/boost/files/boost/1.51.0/boost_1_51_0.7z) |
|  | [boost_1_51_0.zip](http://sourceforge.net/projects/boost/files/boost/1.51.0/boost_1_51_0.zip) |

Downloads {.download-table}

### Patches

- [Locale Patch](http://cppcms.com/files/locale/boost_locale_utf.patch) - Fixes a bug which causes `boost``::``locale``::``utf``::``utf_traits` to accept some invalid UTF-8 sequences, which is a possible security flaw.

### New Libraries

- [Context](/libs/context/): Context switching library, from Oliver Kowalke.

### Updated Libraries

- [Algorithm](/libs/algorithm/):
  - Fixed `is_sorted_until` ; now matches the c++11 standard behavior on ranges with duplicate values.

  - Added range support for the rest of the search algorithms.

  - `unhex` now uses Boost.Exception to signal bad input.

- [Asio](/libs/asio/):
  - Fixed an incompatibility between `ip``::``tcp``::``iostream` and C++11 ([\#7162](https://svn.boost.org/trac/boost/ticket/7162)).

  - Decorated GCC attribute names with underscores to prevent interaction with user-defined macros ([\#6415](https://svn.boost.org/trac/boost/ticket/6415)).

  - Added missing `#include`` ``<``cctype``>`, needed for some versions of MinGW.

  - Changed to use `gcc`'s atomic builtins on ARM CPUs, when available ([\#7140](https://svn.boost.org/trac/boost/ticket/7140)).

  - Changed strand destruction to be a no-op, to allow strand objects to be destroyed after their associated `io_service` has been destroyed.

  - Added support for some newer versions of glibc which provide the `epoll_create1``()` function but always fail with `ENOSYS` ([\#7012](https://svn.boost.org/trac/boost/ticket/7012)).

  - Changed the SSL implementation to throw an exception if SSL engine initialisation fails ([\#6303](https://svn.boost.org/trac/boost/ticket/6303)).

  - Fixed another regression in `buffered_write_stream` ([\#6310](https://svn.boost.org/trac/boost/ticket/6310)).

  - Implemented various minor performance improvements, primarily targeted at Linux x86 and x86-64 platforms.

- [Config](/libs/config/):
  - Deprecated a whole bunch of macros that were c++11 specific, but not named to show that they were c++11 specific. Made new macros with better names, and paired the old macros with the new ones. Updated the documentation to list the deprecated macros.

- [Chrono](/libs/chrono/):
  - [\#6918](https://svn.boost.org/trac/boost/ticket/6918) Boost Chrono compilation failure on HP uX due to undefined pthread_getcpuclockid.

  - [\#6241](https://svn.boost.org/trac/boost/ticket/6241) boost::chrono compilation problems without std::wstring support.

  - [\#6987](https://svn.boost.org/trac/boost/ticket/6987) Documentation & C++11.

  - [\#7041](https://svn.boost.org/trac/boost/ticket/7041) time_point.hpp depends on Boost.System.

  - [\#7042](https://svn.boost.org/trac/boost/ticket/7042) Avoiding time_point and duration dependency on time.h and CLOCK_REALTIME.

  - [\#7058](https://svn.boost.org/trac/boost/ticket/7058) Make it work when BOOST_NO_EXCEPTIONS is defined.

  - [\#7069](https://svn.boost.org/trac/boost/ticket/7069) Misspellings in clock_string\<thread_clock\>.

  - [\#7081](https://svn.boost.org/trac/boost/ticket/7081) WinError.h capitalization in boost/detail/win/basic_types.hpp.

- [Geometry](/libs/geometry/):
  - points accessed through a pointer (e.g. in a linestring) should now be specialized without the pointer. In previous versions a type `my_point` used like `linestring``<``my_point``*>` had to be specalized like: `template``<>`` ``struct`` ``tag``<``my_point``*>`. Now the library itself removes the pointer before calling the traits class, so now it should be like: `template``<>`` ``struct`` ``tag``<``my_point``>`

  - intersection was sometimes wrong for integer points, fixed

  - documentation, order of parameters in simplify was wrong, fixed

  - [7030](https://svn.boost.org/trac/boost/ticket/7030) spherical distance, fixed (by patch of Karsten Ahnert)

- [Graph](/libs/graph/):
  - Refactored support for internal and bundled properties in Boost.Graph-provided graph types, and cleaned up named parameter functionality:
    - Enabled old-style (non-bundled) internal properties in `compressed_sparse_row_graph`.

    - Bundled properties should work correctly for all graph types and adaptors.

  - Bugs fixed:
    - [\#6993](https://svn.boost.org/trac/boost/ticket/6993): Typo Bundled Properties document

    - [\#7002](https://svn.boost.org/trac/boost/ticket/7002): Problem with initialization of CSR bidirectional graph

    - [\#7023](https://svn.boost.org/trac/boost/ticket/7023): Enclose internal type graphml_reader in anonymous namespace

    - Other bugs and warnings not in Trac

- [Hash](/libs/functional/hash/):
  - Support the standard smart pointers.

  - `hash_value` now implemented using SFINAE to avoid implicit casts to built in types when calling it.

  - Updated to use the new config macros.

- [Lexical cast](/libs/conversion/lexical_cast.htm):
  - Better performance, less memory usage for `boost``::``array``<``character_type``,`` ``N``>` and `std``::``array``<``character_type``,`` ``N``>` conversions.

  - Fixed bug with volatile input parameter [\#7157](https://svn.boost.org/trac/boost/ticket/7157).

- [Math](/libs/math/):
  - Updated to use the new config macros.

- [MSM](/libs/msm/):
  - Support for boost::any <https://www.boost.org/doc/libs/1_51_0/libs/msm/doc/HTML/ch03s03.html#any-event> or kleene <https://www.boost.org/doc/libs/1_51_0/libs/msm/doc/HTML/ch03s04.html#kleene-event> as acceptable events

  - Bugfix: compiler error with fsm internal table and none (compound) event.

  - Bugfix: euml::defer\_ leading to stack overflow.

- [Proto](/libs/proto/):
  - Proto transforms get pseudo-parameter pack expansion support for unpacking expressions. See the [Release Notes](/doc/html/proto/appendices.html#boost_proto.appendices.release_notes.boost_1_51) for more information.

- [Ratio](/libs/ratio/):
  - [\#7075](https://svn.boost.org/trac/boost/ticket/7075) Workaround for error: the type of partial specialization template parameter constant "n1" depends on another template parameter.

- [Regex](/libs/regex/):
  - Updated to use the new config macros.

- [Thread](/libs/thread/):
  - [\#4258](https://svn.boost.org/trac/boost/ticket/4258) Linking with boost thread does not work on mingw/gcc 4.5.

  - [\#4885](https://svn.boost.org/trac/boost/ticket/4885) Access violation in set_tss_data at process exit due to invalid assumption about TlsAlloc.

  - [\#6931](https://svn.boost.org/trac/boost/ticket/6931) mutex waits forwever with Intel Compiler and /debug:parallel

  - [\#7044](https://svn.boost.org/trac/boost/ticket/7044) boost 1.50.0 header missing.

  - [\#7052](https://svn.boost.org/trac/boost/ticket/7052) Thread: BOOST_THREAD_PROVIDES_DEPRECATED_FEATURES_SINCE_V3_0_0 only masks thread::operator==, thread::operator!= forward declarations, not definitions.

  - [\#7066](https://svn.boost.org/trac/boost/ticket/7066) An attempt to fix current_thread_tls_key static initialization order.

  - [\#7074](https://svn.boost.org/trac/boost/ticket/7074) Multiply defined symbol boost::allocator_arg.

  - [\#7078](https://svn.boost.org/trac/boost/ticket/7078) Trivial 64-bit warning fix on Windows for thread attribute stack size

  - [\#7089](https://svn.boost.org/trac/boost/ticket/7089) BOOST_THREAD_WAIT_BUG limits functionality without solving anything

- [Unordered](/libs/unordered/):
  - Fix construction/destruction issue when using a C++11 compiler with a C++03 allocator ([\#7100](https://svn.boost.org/trac/boost/ticket/7100)).

  - Remove a `try``..``catch` to support compiling without exceptions.

  - Adjust SFINAE use to try to supprt g++ 3.4 ([\#7175](https://svn.boost.org/trac/boost/ticket/7175)).

  - Updated to use the new config macros.

- [Wave](/libs/wave/):
  - See the [Changelog](/libs/wave/ChangeLog) for details.

- [xpressive](/libs/xpressive/):
  - Work around buggy wide ctype facet on cygwin and mingw.

  - Work around absence of \_\_isctype on some glibc implementations.

  - `op``::``as` shouldn't assume `string``::``iterator` != `char``*`.

  - Fix assertion in `cpp_regex_traits` on libc++, thanks to John Fletcher.

### Compilers Tested

Boost's primary test compilers are:

- Linux:
  - GCC: 4.2.4, 4.3.4, 4.4.3, 4.5.3, 4.6.2, 4.7

  - GCC, C++11 mode: 4.3.4, 4.4.3, 4.5.3, 4.6.2

  - Intel: 11.1, 12.0, 12.1

  - LLVM Clang 2.8

- OS X:
  - GCC: 4.4

  - GCC, C++11 mode: 4.4

  - Intel: 11.1, 12.0

- Windows:
  - GCC, mingw: 4.4.0, 4.4.7, 4.5.4, 4.6.3

  - Visual C++: 8.0, 9.0, 10.0

- FreeBSD:
  - GCC: 4.2.1, 32 and 64 bit

Boost's additional test compilers include:

- Linux:
  - Clang: from subversion

  - LLVM Clang: 3.0

  - GCC: 4.2.4, 4.3.4, 4.4.4, 4.4.7, 4.5.3, 4.6.2, 4.6.3, 4.7.0, 4.7.1

  - GCC, C++11 mode: 4.3.4, 4.4.4, 4.5.3, 4.6.3

  - pgCC: 11.9

  - Intel: 10.1, 11.1, 12.0, 12.1

  - Visual Age: 10.1

- OS X:
  - Clang: from subversion

  - Clang, C++11 mode: from subversion

  - Intel: 11.1, 12.0

  - GCC: 4.4

  - GCC, C++11 mode: 4.4

- Windows:
  - Visual C++: 8.0, 9.0, 10.0

  - GCC, mingw: 4.4.0, 4.6.3, 4.7.0

- AIX:
  - IBM XL C/C++ Enterprise Edition: V12.1.0.0

- FreeBSD:
  - GCC: 4.2.1, 32 and 64 bit

- Solaris:
  - Sun: 5.10

### Acknowledgements

[Beman Dawes](/users/people/beman_dawes.html), Eric Niebler, [Rene Rivera](/users/people/rene_rivera.html), Daniel James, Vladimir Prus and Marshall Clow managed this release.

Copyright Rene Rivera 2006-2007.
