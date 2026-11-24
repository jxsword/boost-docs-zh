# Version 1.50.0

## Version 1.50.0

June 28th, 2012 12:48 GMT

[Documentation](/doc/libs/1_50_0/)

| Platform | File |
|----|----|
| unix | [boost_1_50_0.tar.bz2](http://sourceforge.net/projects/boost/files/boost/1.50.0/boost_1_50_0.tar.bz2) |
|  | [boost_1_50_0.tar.gz](http://sourceforge.net/projects/boost/files/boost/1.50.0/boost_1_50_0.tar.gz) |
| windows | [boost_1_50_0.7z](http://sourceforge.net/projects/boost/files/boost/1.50.0/boost_1_50_0.7z) |
|  | [boost_1_50_0.zip](http://sourceforge.net/projects/boost/files/boost/1.50.0/boost_1_50_0.zip) |

Downloads {.download-table}

### Patches

- [Boost.Unordered patch](/patches/1_50_0/001-unordered.patch) - Fixes a bug when compiled using a C++11 compiler, but with a C++03 allocator. When inserting elements, `allocator_traits` detects that the node can be constructed using an accidental implicit conversion which causes several problems.

- [Locale Patch](http://cppcms.com/files/locale/boost_locale_utf.patch) - Fixes a bug which causes `boost``::``locale``::``utf``::``utf_traits` to accept some invalid UTF-8 sequences, which is a possible security flaw.

### New Libraries

- [Algorithm](/libs/algorithm/): A collection of useful generic algorithms, from Marshall Clow. This includes several different searching algorithms, as well as most of the new algorithms from the C++11 standard library

- [Functional/OverloadedFunction](/libs/functional/overloaded_function/): Overload different functions into a single function object, from Lorenzo Caminiti.

- [LocalFunction](/libs/local_function/): Program functions locally, within other functions, directly within the scope where they are needed, from Lorenzo Caminiti.

- [Utility/IdentityType](/libs/utility/identity_type/): Wrap types within round parenthesis so they can always be passed as macro parameters, from Lorenzo Caminiti.

### Updated Libraries

- [Accumulators](/libs/accumulators/):
  - add missing `#include`` ``<``boost``/``throw_exception``.``hpp``>`, fixes [\#6702](https://svn.boost.org/trac/boost/ticket/6702).

  - work around for msvc which allows ctor templates to be copy ctors, fixes [\#6535](https://svn.boost.org/trac/boost/ticket/6535).

  - shorten filenames to meet boost guidelines, fixes [\#6196](https://svn.boost.org/trac/boost/ticket/6196).

- [Array](/libs/array/):
  - add support for Boost.Hash [\#6791](https://svn.boost.org/trac/boost/ticket/6791).

- [Asio](/libs/asio/):
  - Changed the `epoll_reactor` backend to do lazy registration for `EPOLLOUT` events.

  - Fixed the `epoll_reactor` handling of out-of-band data, which was broken by an incomplete fix in the last release.

  - Changed Asio's SSL wrapper to respect OpenSSL's `OPENSSL_NO_ENGINE` feature test `#define` ([\#6432](https://svn.boost.org/trac/boost/ticket/6432)).

  - Fixed `windows``::``object_handle` so that it works with Windows compilers that support C++11 move semantics (such as `g++`).

  - Improved the performance of strand rescheduling.

  - Added support for `g++` 4.7 when compiling in C++11 mode ([\#6620](https://svn.boost.org/trac/boost/ticket/6620)).

  - Fixed a problem where `signal_set` handlers were not being delivered when the `io_service` was constructed with a `concurrency_hint` of 1 ([\#6657](https://svn.boost.org/trac/boost/ticket/6657)).

- [Bimap](/libs/bimap/):
  - Remove spurious dependency on Boost.Serialization, fixes [\#3868](https://svn.boost.org/trac/boost/ticket/3868).

  - Solve unused constructor parameter warning, fixes [\#5749](https://svn.boost.org/trac/boost/ticket/5749).

  - Add key_type and mapped_type (leaving data_type for backward compatibility) typedefs to map views, fixes [\#6031](https://svn.boost.org/trac/boost/ticket/6031).

- [Chrono](/libs/chrono/):
  - Fixed Bugs:
    - [\#6361](https://svn.boost.org/trac/boost/ticket/6361) integer overflow in boost::chrono::process_real_cpu_clock::now() under Windows 32bits.

    - [\#6628](https://svn.boost.org/trac/boost/ticket/6628) compiler warning in process_cpu_clocks.hpp.

    - [\#6666](https://svn.boost.org/trac/boost/ticket/6666) thread_clock.hpp needs pthread.h.

- [Concept Check](/libs/concept_check/):
  - Fixed:
    - [\#6738](https://svn.boost.org/trac/boost/ticket/6738) Shadowed variable warning.

- [Filesystem](/libs/filesystem/):
  - Remove Filesystem Version 2 from the distribution. Version 3 is now the only distributed version. Those still using V2 are urged to migrate to V3 as soon as possible.

  - Add constexpr value_type preferred_separator to class path.

  - Fix [\#5118](https://svn.boost.org/trac/boost/ticket/5118), `replace_extension` doesn't work as specified in documentation. The documentation, implementation, and test cases have all had fixes applied. The documentation had failed to mention that any existing extension is removed. The behavior for simple cases has been reverted to the Version 2 behavior, but with corrections so that complex replacements now work. Two test cases from [\#5118](https://svn.boost.org/trac/boost/ticket/5118) have been added.

  - Fix [\#3737](https://svn.boost.org/trac/boost/ticket/3737), Boost.Filesystem does not compile on Windows Mobile. On Windows, `<``sys``/``stat``.``h``>` is no longer included.

  - Fix [\#4065](https://svn.boost.org/trac/boost/ticket/4065), Boost Filesystem lexicographic path comparison inconsistent. This required multiple source code bug fixes and code cleanup, correcting problems not related to lexicographical issues.

  - Add class path member function compare for consistency with std::string.

  - Tighten `BOOST_FILESYSTEM_DYN_LINK` and `BOOST_FILESYSTEM_STATIC_LINK` logic in `filesystem``/``config``.``hpp` so that one or the other is always defined, and both being defined is a `#error`.

  - Fix [\#6690](https://svn.boost.org/trac/boost/ticket/6690) and [\#6737](https://svn.boost.org/trac/boost/ticket/6737), resolving static linking related problems with VC++ 8 through 11. Note that this fix may reintroduce codecvt thread safety problems [\#4889](https://svn.boost.org/trac/boost/ticket/4889), [\#6320](https://svn.boost.org/trac/boost/ticket/6320), for these compilers if static linking is used.

  - Add `path``::``operator``+=` and concat functions to tack on things like suffixes or numbers. Suggested by Ed Smith-Rowland and others.

  - Fix [\#6809](https://svn.boost.org/trac/boost/ticket/6809), Implementation of `filesystem``::``rename``()` method for MS Windows is wrong, by adding `MOVEFILE_COPY_ALLOWED` to deal with renames across drives, volumes, file systems. Fix has no effect on non-Windows systems.

  - Fix [\#6819](https://svn.boost.org/trac/boost/ticket/6819), A path operand with a source that was a one character array was treated as empty, even if it wasn't empty. Such arrays can occur in unions or in code using C variable length array idioms.

  - Fix [\#6932](https://svn.boost.org/trac/boost/ticket/6932), create_directories throws exception even if `error_code` is specified.

- [Foreach](/libs/foreach/):
  - Revert fix for [\#6131](https://svn.boost.org/trac/boost/ticket/6131) which caused more harm than good.

- [Geometry](/libs/geometry/):
  - Fixed Bugs:
    - the return type of comparable projected point strategy for integer points was wrong (integer), fixed

    - several robustness issues in intersection of segments and polygons, fixed

    - invalid intersection output is filtered out

    - disjoint for multi_polygon's might incorrectly return true, fixed

  - Solved tickets
    - [6585](https://svn.boost.org/trac/boost/ticket/6585) patch for alternative syntax multipoint, applied

    - [6584](https://svn.boost.org/trac/boost/ticket/6584) patch for bug in distance, applied

    - [5730](https://svn.boost.org/trac/boost/ticket/5730) same issue as 6584, fixed

    - [6166](https://svn.boost.org/trac/boost/ticket/6166) patch for missing transformation, applied

    - [6696](https://svn.boost.org/trac/boost/ticket/6696) invalid intersection output, was (by chance) already fixed in Trunk before reported

  - Additional functionality
    - added algorithm "touches" (OGC SF compliant) for \*polygon/\*polygon

- [Graph](/libs/graph/):
  - Fixed Bugs:
    - [\#4622](https://svn.boost.org/trac/boost/ticket/4622) clear_vertex on a vertex with a self-loop can cause a segmentation fault.

    - [\#6033](https://svn.boost.org/trac/boost/ticket/6033) Lowpoint map calculated by biconnected_components(...) is sometimes wrong.

    - [\#6242](https://svn.boost.org/trac/boost/ticket/6242) isomorphism doesn't reset mapping.

    - [\#6435](https://svn.boost.org/trac/boost/ticket/6435) cube_topology documentation should say 3D, not 2D.

    - [\#6520](https://svn.boost.org/trac/boost/ticket/6520) small_world_1_70_6_0p02.png is broken in documentation of graph_parallel.

    - [\#6564](https://svn.boost.org/trac/boost/ticket/6564) BGL copy constructor for subgraph does not track local vertices/edges.

    - [\#6573](https://svn.boost.org/trac/boost/ticket/6573) BGL: boost::isomorphism routine fails with large graphs.

    - [\#6583](https://svn.boost.org/trac/boost/ticket/6583) Dijkstra Visitor Concept docs probably show wrong type for variable.

    - [\#6647](https://svn.boost.org/trac/boost/ticket/6647) BGL strong_components do not compile on MSVC 8.

    - [\#6656](https://svn.boost.org/trac/boost/ticket/6656) Dependent type in subgraph used without typename.

    - [\#6707](https://svn.boost.org/trac/boost/ticket/6707) is_straight_line_drawing.hpp missing \#include \<map\>.

    - [\#6708](https://svn.boost.org/trac/boost/ticket/6708) Make bool boost::intersects() in is_straight_line_drawing.hpp inline?

    - [\#6739](https://svn.boost.org/trac/boost/ticket/6739) Cannot use write_graphviz_dp with a constified subgraph.

    - [\#6858](https://svn.boost.org/trac/boost/ticket/6858) boost::get() calls wrongly resolved by g++.

    - [\#6892](https://svn.boost.org/trac/boost/ticket/6892) VertexIndexGraph concept not required for bron_kerbosch_all_cliques().

    - Other bugs and warnings not in Trac.

- [Hash](/libs/functional/hash/):
  - Support `std``::``array` and `std``::``tuple` when available ([\#6806](https://svn.boost.org/trac/boost/ticket/6806)).

  - Avoid gcc's `-``Wfloat``-``equal` warning ([\#6771](https://svn.boost.org/trac/boost/ticket/6771)).

  - Add deprecation warning to the long deprecated `boost``/``functional``/``detail``/``container_fwd``.``hpp`.

- [Iostreams](/libs/iostreams/):
  - Improved gzip support ([\#5908](https://svn.boost.org/trac/boost/ticket/5908)).

  - Update tests for latest Boost.Filesystem and Boost.Test.

  - Fix some documentation errors ([\#6530](https://svn.boost.org/trac/boost/ticket/6530), [\#6650](https://svn.boost.org/trac/boost/ticket/6650)).

- [Iterator](/libs/iterator/):
  - Fixed:
    - [\#5127](https://svn.boost.org/trac/boost/ticket/5127) Incorrect result_of usage in transform_iterator

    - [\#5697](https://svn.boost.org/trac/boost/ticket/5697) iterator_facade::operator-\> is broken for proxy references

- [MultiArray](/libs/multi_array/):
  - Concepts bug fix and Workaround for Visual Studio 2010 ([\#4874](https://svn.boost.org/trac/boost/ticket/4874))

  - Fix to assert.cpp test case ([Patch](https://svn.boost.org/trac/boost/changeset/78498))

- [Lexical cast](/libs/conversion/lexical_cast.htm):
  - `boost``::``bad_lexical_cast` exception is now globaly visible and can be catched even if code is compiled with -fvisibility=hidden

  - Now it is possible to compile and use library with disabled exceptions [\#5800](https://svn.boost.org/trac/boost/ticket/5800)

  - Better performance, less memory usage and bugfixes for `boost``::``iterator_range``<``character_type``*>` conversions

  - Fixed bugs and warnings: [\#6645](https://svn.boost.org/trac/boost/ticket/6645), [\#6562](https://svn.boost.org/trac/boost/ticket/6562), [\#6812](https://svn.boost.org/trac/boost/ticket/6812), [\#6852](https://svn.boost.org/trac/boost/ticket/6852), [\#6717](https://svn.boost.org/trac/boost/ticket/6717), [\#6770](https://svn.boost.org/trac/boost/ticket/6670), [\#6504](https://svn.boost.org/trac/boost/ticket/6504).

- [Locale](/libs/locale/):
  - Fixed build issues with STLPort library

  - Boost.System is now required depenency

  - Fixed bugs [\#6635](https://svn.boost.org/trac/boost/ticket/6635), [\#6833](https://svn.boost.org/trac/boost/ticket/6833)

- [Math](/libs/math/):
  - Promoted math constants to be 1st class citizens, including convenient access to the most widely used built-in float, double, long double via three namespaces.

  - Added the Owen's T function and Skew Normal distribution written by Benjamin Sobotta.

  - Added Hankel functions.

  - Corrected issue [\#6627 nonfinite_num_put formatting of 0.0 is incorrect](https://svn.boost.org/trac/boost/ticket/6627) based on a patch submitted by K R Walker.

  - Changed constant initialization mechanism so that it is thread safe even for user-defined types, also so that user defined types get the full precision of the constant, even when `long`` ``double` does not. So for example 128-bit rational approximations will work with UDT's and do the right thing, even though `long`` ``double` may be only 64 or 80 bits.

  - Fixed issue in `bessel_jy` which causes Y\[sub 8.5\](4\[pi\]) to yield a NaN.

- [MSM](/libs/msm/):
  - eUML : better syntax for front-ends defined with eUML as transition table only. Caution: Breaking Change\!<https://www.boost.org/doc/libs/1_50_0/libs/msm/doc/HTML/ch03s04.html#eUML-composite-table>

  - Bugfix: graph building was only working if initial_state defined as a sequence.

  - Bugfix: flags defined for a Terminate or Interrupt state do not break the blocking function of these states any more.

  - Bugfix: multiple deferred events from several regions were not working in every case.

  - Bugfix: visitor was passed by value to submachines.

  - Bugfix: no_transition was not called for submachines who send an event to themselves.

  - Fixed warnings with gcc.

- [Program Options](/libs/program_options/):
  - Improved error reporting ([Patch from Leo Goodstadt](https://svn.boost.org/trac/boost/changeset/77827)).

  - Support for customizing name of option's value in help messages ([\#4781](https://svn.boost.org/trac/boost/ticket/4781))

  - Fixed compilation with gcc 4.7 ([\#6790](https://svn.boost.org/trac/boost/ticket/6790)).

- [PropertyMap](/libs/property_map/):
  - Fixed Bugs:
    - [\#6539](https://svn.boost.org/trac/boost/ticket/6539) the return type of get() is not documented correctly.

    - [\#6721](https://svn.boost.org/trac/boost/ticket/6721) property_map_traits documentation does not mention reference.

- [Proto](/libs/proto/):
  - Use `decltype`-based `result_of` if and only if the compiler implements N3276.

  - For C++11, force parameter to `mpl``::``eval_if_c` and `mpl``::``if_c` to be `bool`.

  - Disable `'__forceinline not inlined'` warning on msvc.

- [Ratio](/libs/ratio/):
  - Fixed Bugs:
    - [\#6498](https://svn.boost.org/trac/boost/ticket/6498) boost::ratio won't compile with default settings.

- [ScopeExit](/libs/scope_exit/):
  - New Features:
    - Use variadic macros to specify captures as commas-separated lists (but kept preprocessor sequence syntax for backward compatibility).

    - Capture the object in scope using `this_`.

    - Support empty captures using `void`.

    - Implicit lambda-like captures using `BOOST_SCOPE_EXIT_ALL` on compilers that support C++11 lambda functions.

- [Thread](/libs/thread/):
  - New Features:
    - [\#1850](https://svn.boost.org/trac/boost/ticket/1850) Request for unlock_guard to compliment lock_guard.

    - [\#2637](https://svn.boost.org/trac/boost/ticket/2637) Request for shared_mutex duration timed_lock and timed_lock_shared.

    - [\#2741](https://svn.boost.org/trac/boost/ticket/2741) Proposal to manage portable and non portable thread attributes.

    - [\#3567](https://svn.boost.org/trac/boost/ticket/3567) Request for shared_lock_guard.

    - [\#6194](https://svn.boost.org/trac/boost/ticket/6194) Adapt to Boost.Move.

    - [\#6195](https://svn.boost.org/trac/boost/ticket/6195) c++11 compliance: Provide the standard time related interface using Boost.Chrono.

    - [\#6217](https://svn.boost.org/trac/boost/ticket/6217) Enhance Boost.Thread shared mutex interface following Howard Hinnant proposal.

    - [\#6224](https://svn.boost.org/trac/boost/ticket/6224) c++11 compliance: Add the use of standard noexcept on compilers supporting them.

    - [\#6226](https://svn.boost.org/trac/boost/ticket/6226) c++11 compliance: Add explicit bool conversion from locks.

    - [\#6228](https://svn.boost.org/trac/boost/ticket/6228) Add promise constructor with allocator following the standard c++11.

    - [\#6230](https://svn.boost.org/trac/boost/ticket/6230) c++11 compliance: Follows the exception reporting mechanism as defined in the c++11.

    - [\#6266](https://svn.boost.org/trac/boost/ticket/6266) Breaking change: thread destructor should call terminate if joinable.

    - [\#6269](https://svn.boost.org/trac/boost/ticket/6269) Breaking change: thread move assignment should call terminate if joinable.

    - [\#6272](https://svn.boost.org/trac/boost/ticket/6272) c++11 compliance: Add thread::id hash specialization.

    - [\#6273](https://svn.boost.org/trac/boost/ticket/6273) c++11 compliance: Add cv_status enum class and use it on the conditions wait functions.

    - [\#6231](https://svn.boost.org/trac/boost/ticket/6231) Add BasicLockable requirements in the documentation to follow c++11.

    - [\#6342](https://svn.boost.org/trac/boost/ticket/6342) c++11 compliance: Adapt the one_flag to the c++11 interface.

    - [\#6671](https://svn.boost.org/trac/boost/ticket/6671) upgrade_lock: missing mutex and release functions.

    - [\#6672](https://svn.boost.org/trac/boost/ticket/6672) upgrade_lock:: missing constructors from time related types.

    - [\#6675](https://svn.boost.org/trac/boost/ticket/6675) upgrade_lock:: missing non-member swap.

    - Added missing packaged_task::result_type and packaged_task:: constructor with allocator.

    - Added packaged_task::reset()

  - Fixed Bugs:
    - [\#2575](https://svn.boost.org/trac/boost/ticket/2575) Bug- Boost 1.36.0 on Itanium platform.

    - [\#4345](https://svn.boost.org/trac/boost/ticket/4345) thread::id and joining problem with cascade of threads.

    - [\#4921](https://svn.boost.org/trac/boost/ticket/4921) BOOST_THREAD_USE_DLL and BOOST_THREAD_USE_LIB are crucial and need to be documented.

    - [\#5013](https://svn.boost.org/trac/boost/ticket/5013) documentation: boost::thread: pthreas_exit causes terminate().

    - [\#5173](https://svn.boost.org/trac/boost/ticket/5173) boost::this_thread::get_id is very slow.

    - [\#5351](https://svn.boost.org/trac/boost/ticket/5351) interrupt a future get boost::unknown_exception.

    - [\#5516](https://svn.boost.org/trac/boost/ticket/5516) Upgrade lock is not acquired when previous upgrade lock releases if another read lock is present.

    - [\#5990](https://svn.boost.org/trac/boost/ticket/5990) shared_future\<T\>::get() has wrong return type.

    - [\#6174](https://svn.boost.org/trac/boost/ticket/6174) packaged_task doesn't correctly handle moving results.

    - [\#6222](https://svn.boost.org/trac/boost/ticket/6222) Compile error with SunStudio: unique_future move.

    - [\#6673](https://svn.boost.org/trac/boost/ticket/6673) shared_lock: move assign doesn't works with c++11.

    - [\#6674](https://svn.boost.org/trac/boost/ticket/6674) shared_mutex: try_lock_upgrade_until doesn't works.

    - Fix issue signaled on the ML with task_object(task_object const&) in presence of task_object(task_object&&)

- [Unordered](/libs/unordered/):
  - Fix equality for `unordered_multiset` and `unordered_multimap`.

  - Implement `reserve` ([\#6857](https://svn.boost.org/trac/boost/ticket/6857)).

  - Avoid gcc's `-``Wfloat``-``equal` and `-``Wshadow` warnings ([\#6190](https://svn.boost.org/trac/boost/ticket/6190), [\#6771](https://svn.boost.org/trac/boost/ticket/6771)).

  - Fix namespace issue with bcp ([\#6905](https://svn.boost.org/trac/boost/ticket/6905)).

  - Fix Sun workarounds ([\#6784](https://svn.boost.org/trac/boost/ticket/6784)).

  - Some internal changes to bucket allocation.

  - See the [change log](/doc/html/unordered/changes.html#unordered.changes.boost_1_50_0) for full details.

- [Wave](/libs/wave/index.html):
  - Wave V2.3.2, see the [Changelog](/libs/wave/ChangeLog) for details.

- [xpressive](/libs/xpressive/):
  - Remove very ugly `lexical_cast` hack with a slightly less ugly one.

  - Replace MPL assert with static assert since it's problematic in C++11, fixes [\#6846](https://svn.boost.org/trac/boost/ticket/6846).

### Compilers Tested

Boost's primary test compilers are:

- Linux:
  - Intel: 11.1

  - LLVM Clang 2.8

  - GCC: 4.2.4, 4.3.4, 4.4.3, 4.5.3, 4.6.2

  - GCC, C++0x mode: 4.3.4, 4.4.3, 4.5.3, 4.6.2

- OS X:
  - Intel: 11.1

  - GCC: 4.4.4

  - GCC, C++0x mode: 4.4.4

- Windows:
  - Visual C++ 8.0, 9.0, 10.0

  - GCC, mingw: 4.4.0, 4.4.7, 4.5.4, 4.6.1, 4.7.0

- FreeBSD:
  - GCC 4.2.1, 32 and 64 bit

- QNX:
  - QCC, C++0x mode: 4.4.0, 4.4.7, 4.5.4, 4.6.3, 4.7.0

Boost's additional test compilers include:

- Linux:
  - Clang from subversion

  - GCC: 4.2.4, 4.3.4, 4.4.4, 4.5.3, 4.6.2

  - GCC, C++0x mode: 4.3.4, 4.4.4, 4.5.3, 4.6.2

  - pgCC: 11.9

  - Intel: 10.1, 11.1, 12.0, 12.1

  - Visual Age 10.1

- OS X:
  - Clang from subversion

  - Intel 11.1, 12.0

  - GCC: 4.4.4

  - GCC, C++0x mode: 4.4.4

- Windows:
  - Visual C++ 8.0, 10.0

  - Visual C++ with STLport: 9.0

  - Visual C++, Windows Mobile 5, with STLport: 9.0

  - GCC, mingw: 4.4.0, 4.4.7, 4.5.2, 4.5.4, 4.6.4, 4.7.0

  - GCC, C++0x mode, mingw: 4.5.2

- AIX:
  - IBM XL C/C++ Enterprise Edition, V12.1.0.0

- FreeBSD:
  - GCC 4.2.1, 32 and 64 bit

- Solaris:
  - Sun 5.10

### Acknowledgements

[Beman Dawes](/users/people/beman_dawes.html), Eric Niebler, [Rene Rivera](/users/people/rene_rivera.html), Daniel James, Vladimir Prus and Marshall Clow managed this release.

Copyright Rene Rivera 2006-2007.
