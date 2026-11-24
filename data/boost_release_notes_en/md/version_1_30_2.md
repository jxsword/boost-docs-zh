# Version 1.30.2

## Version 1.30.2

August 19th, 2003 12:00 GMT

| Platform | File |
|----|----|
| unix | [boost_1_30_2.tar.bz2](http://sourceforge.net/projects/boost/files/boost/1.30.2/boost_1_30_2.tar.bz2) |
|  | [boost_1_30_2.tar.gz](http://sourceforge.net/projects/boost/files/boost/1.30.2/boost_1_30_2.tar.gz) |
| windows | [boost_1_30_2.zip](http://sourceforge.net/projects/boost/files/boost/1.30.2/boost_1_30_2.zip) |

Downloads {.download-table}

- [Boost Consulting](http://www.boost-consulting.com) is now hosting Boost CVS mirrors - see our [download page](/more/getting_started.html#CVS).

- Backported changes to the [config system](/libs/config/config.htm), to better handle new compiler releases.

- Bugs in regression reporting in subproject tests were fixed.

- Tests are now run in the context of the user's PATH environment settings

- msvc-stlport and intel-win32-stlport toolsets now build static libraries with multithreading enabled, to be compatible with the STLPort builds.

- intel-win32 toolset now handles `wchar_t` correctly when intel is installed over msvc6.

- Backported fixes from the main trunk which prevent errors building the [Boost.Test](/libs/test/doc/index.html) library in its default configuration.

- Backported portability improvements for [checked_delete](/libs/utility/checked_delete.html).

- Locale support for metrowerks (requiring a statically-linked runtime) is more uniformly handled.

- Backported [conversion/lexical_cast](/libs/conversion/lexical_cast.htm)'s `wchar_t` fixes from the main trunk.

- intel-linux-tools: added `rt` to FINDLIBS in order to make the `clock_gettime``()` function available (backport of a patch in CVS HEAD).

- [regression/compiler_status.cpp](/tools/regression/index.htm): backported fixes in error log links generation.

Copyright Rene Rivera 2006-2007.
