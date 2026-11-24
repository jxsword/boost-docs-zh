# Version 1.28.0

## Version 1.28.0

May 15th, 2002 12:00 GMT

| Platform | File |
|----|----|
| unix | [boost_1_28_0.tar.bz2](http://sourceforge.net/projects/boost/files/boost/1.28.0/boost_1_28_0.tar.bz2) |
|  | [boost_1_28_0.tar.gz](http://sourceforge.net/projects/boost/files/boost/1.28.0/boost_1_28_0.tar.gz) |
| windows | [boost_1_28_0.zip](http://sourceforge.net/projects/boost/files/boost/1.28.0/boost_1_28_0.zip) |

Downloads {.download-table}

- The Boost mailing lists are now also accessible as [newsgroups](/more/mailing_lists.htm#newsgroup).

- A powerful [mailing list archive](http://aspn.activestate.com/ASPN/Mail/Archives/boost/) has been contributed by the [ActiveState Programmer Network](http://aspn.activestate.com/ASPN).

- [Lambda Library](/libs/lambda/doc/index.html) added, from Jaakko Jarvi and Gary Powell. Define small unnamed function objects at the actual call site: for_each( a.begin(), a.end(), std::cout \<\< \_1 \<\< ' ' );

- [I/O State Saver Library added](/libs/io/doc/ios_state.html) - Save I/O state to prevent jumbled data, from Daryle Walker.

- [Configuration Library](/libs/config/config.htm): User code should not use BOOST_NO_LIMITS.

- [Random Number Library](/libs/random/index.html): Avoid compiler warnings.

- [Smart Pointers Library](/libs/smart_ptr/index.html): Added shared_polymorphic_cast and shared_polymorphic_downcast.

- [Function Library](/libs/function/index.html): Now supports function objects with the unary `&` operator overloaded.

- [Utility Library](/libs/utility/utility.htm): Added `addressof``()` function.

- The usual small fixes and tweaks.

Copyright Rene Rivera 2006-2007.
