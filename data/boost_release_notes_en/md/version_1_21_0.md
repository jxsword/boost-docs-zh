# Version 1.21.0

## Version 1.21.0

March 9th, 2001 12:00 GMT

- [Iterator Adaptor Library](/libs/utility/iterator_adaptors.htm) added. Adapt a base type into a standard conforming iterator, and more, from Dave Abrahams, Jeremy Siek, and John Potter.

- [Pool Library](/libs/pool/doc/index.html) added. Memory pool management from Steve Cleary.

- [Test Library](/libs/test/doc/index.html) added. Support for program testing and execution from Beman Dawes.

- [Generic Programming Techniques](/more/generic_programming.html) page added, contributed by Dave Abrahams.

- [Graph Library](/libs/graph/doc/table_of_contents.html): Updated use of iterator adaptors. Changed `operator`` ``==` for `adjacency_list``::``edge_descriptor` to improve semantics for multigraphs. Moved `adjacency_iterator_generator` from namespace `detail` to `boost` and added [documentation](/libs/graph/doc/adjacency_iterator.html). Renamed `dynamic_components``()` to [`incremental_components``()`](/libs/graph/doc/incremental_components.html), better matching graph literature terminology. Cleaned up interface of [`connected_components``()`](/libs/graph/doc/connected_components.html) and created separate [`strong_components``()`](/libs/graph/doc/strong_components.html) function using Tarjan's more efficient algorithm. Fixed documentation figures for [`adjacency_list`](/libs/graph/doc/adjacency_list.html) and [`adjacency_matrix`](/libs/graph/doc/adjacency_matrix.html). Added docs for [`cuthill_mckee_ordering``()`](/libs/graph/doc/cuthill_mckee_ordering.html) algorithm.

- [Python Library](/libs/python/doc/index.html) upgraded. Better compatibility with Python 2.0, NULL pointers and smart-pointers get converted to/from python None, massive documentation review/revision.

- [Regular Expression Library](/libs/regex/index.html): Minor fixes for Unicode platforms.

- [Type Traits Library](/libs/type_traits/index.html) upgraded: Major revision.

Copyright Rene Rivera 2006-2007.
