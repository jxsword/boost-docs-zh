# Version 1.49.0

## Version 1.49.0

February 24th, 2012 21:20 GMT

[Documentation](/doc/libs/1_49_0/)

| Platform | File |
|----|----|
| unix | [boost_1_49_0.tar.bz2](http://sourceforge.net/projects/boost/files/boost/1.49.0/boost_1_49_0.tar.bz2) |
|  | [boost_1_49_0.tar.gz](http://sourceforge.net/projects/boost/files/boost/1.49.0/boost_1_49_0.tar.gz) |
| windows | [boost_1_49_0.7z](http://sourceforge.net/projects/boost/files/boost/1.49.0/boost_1_49_0.7z) |
|  | [boost_1_49_0.zip](http://sourceforge.net/projects/boost/files/boost/1.49.0/boost_1_49_0.zip) |

Downloads {.download-table}

### Patches

- [Locale Patch](http://cppcms.com/files/locale/boost_locale_utf.patch) - Fixes a bug which causes `boost``::``locale``::``utf``::``utf_traits` to accept some invalid UTF-8 sequences, which is a possible security flaw.

### New Libraries

- [Heap](/libs/heap/index.html): Priority queue data structures, from Tim Blechmann.

### Updated Libraries

- [Asio](/libs/asio):
  - Added a new class template `basic_waitable_timer` based around the C++11 clock type requirements. It may be used with the clocks from the C++11 `<``chrono``>` library facility or, if those are not available, Boost.Chrono. The typedefs `high_resolution_timer`, `steady_timer` and `system_timer` may be used to create timer objects for the standard clock types.

  - Added a new `windows``::``object_handle` class for performing waits on Windows kernel objects. Thanks go to Boris Schaeling for contributing substantially to the development of this feature.

  - On Linux, `connect``()` can return EAGAIN in certain circumstances. Remapped this to another error so that it doesn't look like a non-blocking operation ([\#6048](https://svn.boost.org/trac/boost/ticket/6048)).

  - Fixed a compile error on NetBSD ([\#6098](https://svn.boost.org/trac/boost/ticket/6098)).

  - Fixed deadlock on Mac OS X ([\#6275](https://svn.boost.org/trac/boost/ticket/6275)).

  - Fixed a regression in `buffered_write_stream` ([\#6310](https://svn.boost.org/trac/boost/ticket/6310)).

  - Fixed a non-paged pool "leak" on Windows when an `io_service` is repeatedly run without anything to do ([\#6321](https://svn.boost.org/trac/boost/ticket/6321)).

  - Reverted earlier change to allow some speculative operations to be performed without holding the lock, as it introduced a race condition in some multithreaded scenarios.

  - Fixed a bug where the second buffer in an array of two buffers may be ignored if the first buffer is empty.

- [Chrono](/libs/chrono):
  - Bug Fixes:
    - [\#6092](http://svn.boost.org/trac/boost/ticket/6092) Input from non integral durations makes the compiler fail.

    - [\#6093](http://svn.boost.org/trac/boost/ticket/6093) \[1/3\]second fails as valid duration input.

    - [\#6113](http://svn.boost.org/trac/boost/ticket/6113) duplicate symbol when BOOST_CHRONO_HEADER_ONLY is defined.

    - [\#6243](http://svn.boost.org/trac/boost/ticket/6243) Sandia-pgi-11.9: more than one instance of overloaded function "min" matches.

    - [\#6257](http://svn.boost.org/trac/boost/ticket/6257) process_cpu_clock::now() on linux gives time_points 1/1000 times.

- [Container](/libs/container/):
  - Fixed bugs [\#6499](https://svn.boost.org/trac/boost/ticket/6499), [\#6336](https://svn.boost.org/trac/boost/ticket/6336), [\#6335](https://svn.boost.org/trac/boost/ticket/6335), [\#6287](https://svn.boost.org/trac/boost/ticket/6287), [\#6205](https://svn.boost.org/trac/boost/ticket/6205), [\#4383](https://svn.boost.org/trac/boost/ticket/4383).

  - Added `allocator_traits` support for both C++11 and C++03 compilers through an internal `allocator_traits` clone.

- [Filesystem](/libs/filesystem/):
  - Fix [\#3714](https://svn.boost.org/trac/boost/ticket/3714), Added test cases and fixes for class path errors when assignment or append used self or portion of self as source.

  - Fix [\#4889](https://svn.boost.org/trac/boost/ticket/4889), [\#6320](https://svn.boost.org/trac/boost/ticket/6320), Locale codecvt_facet not thread safe on Windows. Move Windows, Mac OS X, locale and codecvt facet back to namespace scope. POSIX except OS X uses local static initialization (IE lazy) to ensure exceptions are catchable if environmental variables are misconfigured and to avoid use of locale("") if not actually used.

  - Fix [\#5652](https://svn.boost.org/trac/boost/ticket/5652), recursive_directory_iterator fails on cyclic symbolic links. Thanks to Daniel Aarno for the patch.

  - Fix [\#5653](https://svn.boost.org/trac/boost/ticket/5653), recursive_directory_iterator(error_code) can still throw filesystem_error.

  - Fix [\#5900](https://svn.boost.org/trac/boost/ticket/5900), directory_iterator access violation on Windows if error is thrown. Thanks to Andreas Eckleder for the patch.

  - Fix [\#5900](https://svn.boost.org/trac/boost/ticket/5900) comment 2, a bug in director_iterator construction with error_code argument that caused increment to be called without the ec argument being passed.

  - Fix [\#5989](https://svn.boost.org/trac/boost/ticket/5989) by cleaning up test suite path_test.cpp code even though the ticket itself was not a defect, and clarifying docs; iteration over a path yields generic format.

  - Fix [\#5592](https://svn.boost.org/trac/boost/ticket/5592), Change Windows codecvt processing from CP_THREAD_ACP to CP_ACP.

  - Operations function fixes for PGI compiler, thanks to Noel Belcourt.

  - Relax permissions test to reflect reality, particularly on the Sandia test platforms.

- [Foreach](/libs/foreach/):
  - Fix for [\#6131](https://svn.boost.org/trac/boost/ticket/6131)

- [Geometry](/libs/geometry/):
  - Fixed bugs
    - Distance for multi-geometries ignored specified distance strategy.

    - In difference for polygon/multi_polygon (reported 2011/10/24 on GGL-list).

    - Raise exception for calculation of distances of multi-geometrie(s) where one of them is empty

    - Multi DSV did not correctly use settings.

    - Self-intersections could sometimes be missed (introduced in 1.48).

    - Convex hull crashed on empty range (e.g. empty multi point).

  - Solved tickets
    - [\#6028](https://svn.boost.org/trac/boost/ticket/6028) Documentation: closure.

    - [\#6178](https://svn.boost.org/trac/boost/ticket/6178) Missing headerfile.

    - [\#6021](https://svn.boost.org/trac/boost/ticket/6021) convex hull of multipoint.

  - Additional functionality
    - Support for line/polygon intersections and differences

    - Support for convert of segment/box of different point types

    - Support for append for multi point

    - Scalar functions (distance, area, length, perimeter) now throw an empty_input_exception on empty input

  - Documentation
    - Updated support status

  - Internal changes
    - Updates in specializations/not_implemented for distance/convert/assign/area

    - Move of wkt/dsv to io folder, making domains redundant

    - Strategy concepts assigned to zero to avoid clang warnings (patched by Vishnu)

- [Graph](/libs/graph/):
  - Fixed bugs [\#5881](https://svn.boost.org/trac/boost/ticket/5881), [\#6033](https://svn.boost.org/trac/boost/ticket/6033), [\#6061](https://svn.boost.org/trac/boost/ticket/6061), [\#6137](https://svn.boost.org/trac/boost/ticket/6137), [\#6246](https://svn.boost.org/trac/boost/ticket/6246), [\#6239](https://svn.boost.org/trac/boost/ticket/6239), [\#6293](https://svn.boost.org/trac/boost/ticket/6293), [\#6306](https://svn.boost.org/trac/boost/ticket/6306), [\#6313](https://svn.boost.org/trac/boost/ticket/6313) and [\#6371](https://svn.boost.org/trac/boost/ticket/6371), plus others not in Trac.

  - Re-enabled LEDA graph support (thanks to Jens Muller for the patch).

  - Added documentation for `edge_predecessor_recorder`.

- [Icl](/libs/icl/):
  - Fixed tickets [\#6095](https://svn.boost.org/trac/boost/ticket/6095) and [\#6210](https://svn.boost.org/trac/boost/ticket/6210).

  - Added move semantics for constructors, assignment operators and binary operators.

- [Interprocess](/libs/interprocess/):
  - Fixed bugs [\#6531](https://svn.boost.org/trac/boost/ticket/6531), [\#6412](https://svn.boost.org/trac/boost/ticket/6412), [\#6398](https://svn.boost.org/trac/boost/ticket/6398), [\#6340](https://svn.boost.org/trac/boost/ticket/6340), [\#6319](https://svn.boost.org/trac/boost/ticket/6319), [\#6287](https://svn.boost.org/trac/boost/ticket/6287), [\#6265](https://svn.boost.org/trac/boost/ticket/6265), [\#6233](https://svn.boost.org/trac/boost/ticket/6233), [\#6147](https://svn.boost.org/trac/boost/ticket/6147), [\#6134](https://svn.boost.org/trac/boost/ticket/6134), [\#6058](https://svn.boost.org/trac/boost/ticket/6058), [\#6054](https://svn.boost.org/trac/boost/ticket/6054), [\#5772](https://svn.boost.org/trac/boost/ticket/5772), [\#5738](https://svn.boost.org/trac/boost/ticket/5738), [\#5622](https://svn.boost.org/trac/boost/ticket/5622), [\#5552](https://svn.boost.org/trac/boost/ticket/5552), [\#5518](https://svn.boost.org/trac/boost/ticket/5518), [\#4655](https://svn.boost.org/trac/boost/ticket/4655), [\#4452](https://svn.boost.org/trac/boost/ticket/4452), [\#4383](https://svn.boost.org/trac/boost/ticket/4383), [\#4297](https://svn.boost.org/trac/boost/ticket/4297).

  - Fixed timed functions in mutex implementations to fulfill POSIX requirements: *Under no circumstance shall the function fail with a timeout if the mutex can be locked immediately. The validity of the abs_timeout parameter need not be checked if the mutex can be locked immediately.*

- [Intrusive](/libs/intrusive/):
  - Fixed bugs [\#6347](https://svn.boost.org/trac/boost/ticket/6347), [\#6223](https://svn.boost.org/trac/boost/ticket/6223), [\#6153](https://svn.boost.org/trac/boost/ticket/6153).

- [Lexical cast](/libs/conversion/lexical_cast.htm):
  - Fixed bugs and warnings: [\#6127](https://svn.boost.org/trac/boost/ticket/6127), [\#6132](https://svn.boost.org/trac/boost/ticket/6132), [\#6159](https://svn.boost.org/trac/boost/ticket/6159), [\#6182](https://svn.boost.org/trac/boost/ticket/6182), [\#6186](https://svn.boost.org/trac/boost/ticket/6186), [\#6193](https://svn.boost.org/trac/boost/ticket/6193), [\#6264](https://svn.boost.org/trac/boost/ticket/6264), [\#6290](https://svn.boost.org/trac/boost/ticket/6290), [\#6298](https://svn.boost.org/trac/boost/ticket/6298), [\#6400](https://svn.boost.org/trac/boost/ticket/6400).

  - Better performance and less memory usage for boost::container::basic_string conversions.

- [Locale](/libs/locale/):
  - Fixed incorrect use of `MultiByteToWideChar` in detection of invalid input sequences.

- [Move](/libs/move/):
  - Fixed bugs [\#6417](https://svn.boost.org/trac/boost/ticket/6417), [\#6183](https://svn.boost.org/trac/boost/ticket/6183), [\#6185](https://svn.boost.org/trac/boost/ticket/6185), [\#6395](https://svn.boost.org/trac/boost/ticket/6395), [\#6396](https://svn.boost.org/trac/boost/ticket/6396),

- [PropertyTree](/libs/property_tree):
  - Fixes for bugs [\#4840](https://svn.boost.org/trac/boost/ticket/4840), [\#5259](https://svn.boost.org/trac/boost/ticket/5259), [\#5281](https://svn.boost.org/trac/boost/ticket/5281), [\#5944](https://svn.boost.org/trac/boost/ticket/5944), [\#5757](https://svn.boost.org/trac/boost/ticket/5757), [\#5710](https://svn.boost.org/trac/boost/ticket/5710), and [\#5307](https://svn.boost.org/trac/boost/ticket/5307).

- [Proto](/libs/proto):
  - Force some functions to be inline, fixes [\#5735](https://svn.boost.org/trac/boost/ticket/5735).

  - Add user documentation for per-domain `as_expr` and `as_child`; other doc tweaks.

  - Fix some buggy and over-complicated example programs.

  - Add some missing copyright notices.

- [Spirit](/libs/spirit/index.html):
  - Spirit V2.5.2, see the '[What's New](/doc/libs/1_49_0/libs/spirit/doc/html/spirit/what_s_new/spirit_2_5_2.html)' section for details.

- [Thread](/libs/thread):
  - Fixed Bugs:
    - [\#2309](http://svn.boost.org/trac/boost/ticket/2309) Lack of g++ symbol visibility support in Boost.Thread.

    - [\#2639](http://svn.boost.org/trac/boost/ticket/2639) documentation should be extended(defer_lock, try_to_lock, ...).

    - [\#3639](http://svn.boost.org/trac/boost/ticket/3639) Boost.Thread doesn't build with Sun-5.9 on Linux.

    - [\#3762](http://svn.boost.org/trac/boost/ticket/3762) Thread can't be compiled with winscw (Codewarrior by Nokia).

    - [\#3885](http://svn.boost.org/trac/boost/ticket/3885) document about mix usage of boost.thread and native thread api.

    - [\#3975](http://svn.boost.org/trac/boost/ticket/3975) Incorrect precondition for promise::set_wait_callback().

    - [\#4048](http://svn.boost.org/trac/boost/ticket/4048) thread::id formatting involves locale

    - [\#4315](http://svn.boost.org/trac/boost/ticket/4315) gcc 4.4 Warning: inline ... declared as dllimport: attribute ignored.

    - [\#4480](http://svn.boost.org/trac/boost/ticket/4480) OpenVMS patches for compiler issues workarounds.

    - [\#4819](http://svn.boost.org/trac/boost/ticket/4819) boost.thread's documentation misprints.

    - [\#5040](http://svn.boost.org/trac/boost/ticket/5040) future.hpp in boost::thread does not compile with /clr.

    - [\#5423](http://svn.boost.org/trac/boost/ticket/5423) thread issues with C++0x.

    - [\#5502](http://svn.boost.org/trac/boost/ticket/5502) race condition between shared_mutex timed_lock and lock_shared.

    - [\#5594](http://svn.boost.org/trac/boost/ticket/5594) boost::shared_mutex not fully compatible with Windows CE.

    - [\#5617](http://svn.boost.org/trac/boost/ticket/5617) boost::thread::id copy ctor.

    - [\#5739](http://svn.boost.org/trac/boost/ticket/5739) set-but-not-used warnings with gcc-4.6.

    - [\#5826](http://svn.boost.org/trac/boost/ticket/5826) threads.cpp: resource leak on threads creation failure.

    - [\#5839](http://svn.boost.org/trac/boost/ticket/5839) thread.cpp: ThreadProxy leaks on exceptions.

    - [\#5859](http://svn.boost.org/trac/boost/ticket/5859) win32 shared_mutex constructor leaks on exceptions.

    - [\#6100](http://svn.boost.org/trac/boost/ticket/6100) Compute hardware_concurrency() using get_nprocs() on GLIBC systems.

    - [\#6141](http://svn.boost.org/trac/boost/ticket/6141) Compilation error when boost.thread and boost.move are used together.

    - [\#6168](http://svn.boost.org/trac/boost/ticket/6168) recursive_mutex is using wrong config symbol (possible typo).

    - [\#6175](http://svn.boost.org/trac/boost/ticket/6175) Compile error with SunStudio.

    - [\#6200](http://svn.boost.org/trac/boost/ticket/6200) patch to have condition_variable and mutex error better handle EINTR.

    - [\#6207](http://svn.boost.org/trac/boost/ticket/6207) shared_lock swap compiler error on clang 3.0 c++11.

    - [\#6208](http://svn.boost.org/trac/boost/ticket/6208) try_lock_wrapper swap compiler error on clang 3.0 c++11.

- [Unordered](/libs/unordered):
  - On compilers without rvalue references, the containers are no longer movable by default, as move emulation was causing some odd quirks ([\#6167](https://svn.boost.org/trac/boost/ticket/6167), [\#6311](https://svn.boost.org/trac/boost/ticket/6311)). Define `BOOST_UNORDERED_USE_MOVE` to make them movable - Boost.Move is still used for elements regardless.

  - Fix sequence point warning ([\#6370](https://svn.boost.org/trac/boost/ticket/6370)).

  - Better support for C++11 compilers using older standard libraries.

- [Uuid](/libs/uuid/):
  - fixed [\#6258](https://svn.boost.org/trac/boost/ticket/6258)

  - fixed [\#5325](https://svn.boost.org/trac/boost/ticket/5325) (sha1 implementation handles messages as long as the specification)

  - progress on [\#6118](https://svn.boost.org/trac/boost/ticket/6118) (there are fewer warnings)

- [xpressive](/libs/xpressive/):
  - Eliminate some unused variable warnings on gcc.

### Compilers Tested

Boost's primary test compilers are:

- Linux:
  - Intel: 11.1

  - LLVM Clang 2.8

  - GCC: 3.4.6, 4.2.4, 4.3.4, 4.4.3, 4.5.2, 4.6.2

  - GCC, C++0x mode: 4.3.4, 4.4.3, 4.5.2

- OS X:
  - Intel: 11.1

  - GCC: 4.2.1, 4.4.4

  - GCC, C++0x mode: 4.4.4

- Windows:
  - Visual C++ 8.0, 9.0, 10.0

  - GCC, mingw: 4.4.0, 4.4.7, 4.5.4, 4.6.1, 4.7.0

- FreeBSD:
  - GCC 4.2.1, 32 and 64 bit.

- QNX:
  - QCC, C++0x mode: 4.4.2, 4.6.1, 4.6.2

Boost's additional test compilers include:

- Linux:
  - GCC: 4.2.4, 4.3.4, 4.4.4, 4.5.2, 4.6.2

  - GCC, C++0x mode: 4.3.4, 4.4.4, 4.5.2

  - pgCC: 11.9

  - Intel: 10.1, 11.1, 12.0

  - PathScale: 4.0.8

  - Visual Age 10.1

- OS X:
  - Clang from subversion

  - Intel 11.1, 12.0

  - GCC: 4.4.4

  - GCC, C++0x mode: 4.4.4

- Windows:
  - Visual C++ 8.0, 9.0, 10.0

  - Visual C++ with STLport: 9.0

  - Visual C++, Windows Mobile 5, with STLport: 9.0

  - GCC, mingw: 4.4.0, 4.5.2

  - GCC, C++0x mode, mingw: 4.5.2

  - GCC, mingw 64-bit: 4.4.7, 4.5.4, 4.6.1

- AIX:
  - IBM XL C/C++ Enterprise Edition, V11.1.0.0

- FreeBSD:
  - GCC 4.2.1, 32 and 64 bit

- Solaris:
  - Sun 5.10

### Acknowledgements

[Beman Dawes](/users/people/beman_dawes.html), Eric Niebler, [Rene Rivera](/users/people/rene_rivera.html), Daniel James and Vladimir Prus managed this release.

Copyright Rene Rivera 2006-2007.
