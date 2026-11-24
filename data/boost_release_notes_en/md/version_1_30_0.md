# Version 1.30.0

## Version 1.30.0

March 19th, 2003 12:00 GMT

| Platform | File |
|----|----|
| unix | [boost_1_30_0.tar.bz2](http://sourceforge.net/projects/boost/files/boost/1.30.0/boost_1_30_0.tar.bz2) |
|  | [boost_1_30_0.tar.gz](http://sourceforge.net/projects/boost/files/boost/1.30.0/boost_1_30_0.tar.gz) |
| windows | [boost_1_30_0.zip](http://sourceforge.net/projects/boost/files/boost/1.30.0/boost_1_30_0.zip) |

Downloads {.download-table}

- [Filesystem Library](/libs/filesystem/doc/index.htm) added - Portable paths, iteration over directories, and other useful filesystem operations, from Beman Dawes.

- [Optional Library](/libs/optional/doc/optional.html) added - A discriminated-union wrapper for optional values, from Fernando Cacciola.

- [Interval Library](/libs/numeric/interval/doc/interval.htm) added - Extends the usual arithmetic functions to mathematical intervals, from Guillaume Melquiond, Herve Bronnimann and Sylvain Pion.

- [MPL](/libs/mpl/doc/index.html) added - Template metaprogramming framework of compile-time algorithms, sequences and metafunction classes, from Aleksey Gurtovoy.

- [Spirit Library](/libs/spirit/index.html) added - An LL (unlimited lookahead) parser framework that represents parsers directly as EBNF grammars in inlined C++ source code, complete with semantic actions, ASTs and much more, from Joel de Guzman and team.

- [Smart Pointers Library](/libs/smart_ptr/index.html) - cast functions are now spelled [static_pointer_cast](/libs/smart_ptr/shared_ptr.htm#static_pointer_cast) / [dynamic_pointer_cast](/libs/smart_ptr/shared_ptr.htm#dynamic_pointer_cast); [enable_shared_from_this](/libs/smart_ptr/enable_shared_from_this.html) added; shared_ptr::shared_ptr(), shared_ptr::reset(), weak_ptr::weak_ptr(), weak_ptr::reset() no longer throw; [get_deleter](/libs/smart_ptr/shared_ptr.htm#get_deleter) added; weak_ptr::get() removed; make_shared is now spelled [weak_ptr::lock()](/libs/smart_ptr/weak_ptr.htm#lock) ; [intrusive_ptr documentation](/libs/smart_ptr/intrusive_ptr.html) added; some experimental undocumented shared_ptr features have been removed; a [page describing some smart pointer programming techniques](/libs/smart_ptr/sp_techniques.html) has been added.

- [boost/assert.hpp](/libs/utility/assert.html), [boost/current_function.hpp](/libs/utility/current_function.html), [boost/throw_exception.hpp](/libs/utility/throw_exception.html), [boost/checked_delete.hpp](/libs/utility/checked_delete.html) have been documented.

- [Date-Time Library](/libs/date_time/doc/index.html) - several fixes and small additions including an interface change to partial_date. See the Date-Time Change History for more details.

- [Function Library](/libs/function/index.html) - added support for assignment to zero (to clear) and comparison against zero (to check if empty).

- [Operators Library](/libs/utility/operators.htm#symmetry) - now takes advantage of named return value optimization (NRVO) when available, from Daniel Frey.

- [Regression Tests](/status/compiler_status.html) - Much expanded, plus a very nice [summary page](http://boost.sourceforge.net/regression-logs/) from Rene Rivera.

- [Test Library](/libs/test/index.html) - introduced following new facilities:
  - Automatic registration of unit tests
  - XML log format
  - XML report format
  - BOOST_CHECK_NO_THROW test tool
  - BOOST_BITWISE_CHECK test tool

  For a complete list of changes see the Test Library [release notes](/libs/test/doc/release_notes.html#v1_30_0).

- Many fixes and enhancements to other libraries.

Copyright Rene Rivera 2006-2007.
