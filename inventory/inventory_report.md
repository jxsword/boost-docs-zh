# Boost 1.92.0 corpus inventory report (S1)

> meta: generated 2026-11-14; baseline Boost 1.92.0 (frozen 2026-11-14)
> corpus: boost_1_92_0.7z from archives.boost.io (144,300,348 bytes,
> downloaded 2026-11-14 via proxy with resume; extracted read-only at
> data/boost_1_92_0; tools pipeline/inventory.py + inventory_run.py)

## 1. totals

| metric | value |
|---|---|
| html files | 25,622 |
| html bytes | 388,711,470 (370.7 MiB) |
| translatable english words | 5,684,492 |
| unique segment keys | 269,218 |
| unique segment words | 2,968,750 |
| common keys (pages>=3) | 17,104 (words 114,114) |
| common hit rate (unique-word basis) | 3.8% |
| LLM segments (pages<3) | 252,114 (words 2,871,548) |
| LLM batches (50 seg/batch) | 5,043 |

## 2. form distribution

| form | files | words |
|---|---|---|
| quickbook_boostbook | 18,378 | 3,823,723 |
| doxygen | 2,047 | 455,782 |
| handwritten_html | 1,849 | 480,184 |
| antora_like | 1,694 | 492,073 |
| antora | 1,199 | 187,897 |
| docca_asciidoctor | 455 | 244,833 |

## 3. encoding distribution

| encoding | files |
|---|---|
| utf-8 | 24,996 |
| nonutf8 | 612 |
| utf-8-sig | 14 |

non-utf8 files: 612 (details in manifest encoding column)
- more/index.htm (nonutf8:iso-8859-1)
- libs/any/index.html (nonutf8:unknown)
- libs/assert/index.html (nonutf8:unknown)
- libs/assign/index.html (nonutf8:iso-8859-1)
- libs/bind/index.html (nonutf8:unknown)
- libs/bloom/index.html (nonutf8:iso-8859-1)
- libs/circular_buffer/index.html (nonutf8:iso-8859-1)
- libs/cobalt/index.html (nonutf8:unknown)
- libs/concept_check/index.html (nonutf8:unknown)
- libs/contract/index.html (nonutf8:unknown)
- libs/date_time/index.html (nonutf8:unknown)
- libs/dynamic_bitset/index.html (nonutf8:unknown)
- libs/flyweight/index.html (nonutf8:iso-8859-1)
- libs/function/index.html (nonutf8:unknown)
- libs/fusion/index.html (nonutf8:unknown)
- libs/hash2/index.html (nonutf8:unknown)
- libs/icl/index.html (nonutf8:iso-8859-1)
- libs/iostreams/index.html (nonutf8:unknown)
- libs/lambda/index.html (nonutf8:unknown)
- libs/local_function/index.html (nonutf8:unknown)
- libs/metaparse/index.html (nonutf8:unknown)
- libs/mp11/index.html (nonutf8:unknown)
- libs/mpl/index.html (nonutf8:unknown)
- libs/multi_array/index.html (nonutf8:unknown)
- libs/multi_index/index.html (nonutf8:iso-8859-1)
- libs/numeric/index.html (nonutf8:unknown)
- libs/phoenix/index.html (nonutf8:unknown)
- libs/pool/index.html (nonutf8:unknown)
- libs/preprocessor/index.html (nonutf8:unknown)
- libs/program_options/index.html (nonutf8:unknown)
- libs/ptr_container/index.html (nonutf8:iso-8859-1)
- libs/python/index.html (nonutf8:unknown)
- libs/scope_exit/index.html (nonutf8:unknown)
- libs/signals2/index.html (nonutf8:unknown)
- libs/spirit/index.html (nonutf8:unknown)
- libs/tokenizer/index.html (nonutf8:unknown)
- libs/tuple/index.html (nonutf8:unknown)
- libs/assign/doc/index.html (nonutf8:iso-8859-1)
- libs/bloom/doc/index.html (nonutf8:iso-8859-1)
- libs/date_time/doc/index.html (nonutf8:unknown)
- ... 572 more in manifest

## 4. per-library detail (top 80 by words)

| lib | files | words | llm segs | common words | batches |
|---|---|---|---|---|---|
| (book:doxygen) | 3,400 | 574,514 | 16,345 | 14,950 | 327 |
| asio | 4,822 | 549,787 | 19,904 | 22,363 | 399 |
| math | 519 | 344,465 | 15,787 | 3,615 | 316 |
| graph | 212 | 205,598 | 4,035 | 2,253 | 81 |
| beast | 1,508 | 196,622 | 7,527 | 8,785 | 151 |
| gil | 853 | 179,092 | 22,054 | 4,170 | 442 |
| hana | 737 | 157,613 | 8,303 | 4,200 | 167 |
| url | 1,042 | 140,506 | 3,454 | 7,101 | 70 |
| spirit | 358 | 136,476 | 4,732 | 2,558 | 95 |
| log | 710 | 132,774 | 4,881 | 1,876 | 98 |
| mysql | 1,014 | 132,415 | 5,792 | 3,513 | 116 |
| locale | 287 | 89,189 | 10,979 | 2,144 | 220 |
| multiprecision | 161 | 85,590 | 3,807 | 1,912 | 77 |
| geometry | 451 | 84,895 | 4,719 | 1,544 | 95 |
| openmethod | 701 | 82,484 | 1,473 | 2,500 | 30 |
| test | 440 | 78,549 | 3,586 | 1,474 | 72 |
| outcome | 549 | 70,533 | 2,487 | 1,889 | 50 |
| json | 430 | 69,888 | 2,277 | 1,759 | 46 |
| unordered | 55 | 69,568 | 832 | 5,841 | 17 |
| contract | 133 | 60,900 | 1,865 | 849 | 38 |
| icl | 489 | 60,491 | 1,853 | 441 | 38 |
| preprocessor | 525 | 59,239 | 3,703 | 1,222 | 75 |
| (book:boost) | 459 | 56,383 | 1,764 | 540 | 36 |
| vmd | 182 | 50,038 | 2,207 | 430 | 45 |
| thread | 15 | 49,070 | 2,409 | 193 | 49 |
| tool:build | 1 | 48,068 | 2,432 | 29 | 49 |
| sort | 276 | 48,011 | 3,804 | 1,297 | 77 |
| polygon | 41 | 47,996 | 1,650 | 1,335 | 33 |
| msm | 160 | 47,421 | 2,198 | 563 | 44 |
| fusion | 306 | 47,191 | 1,650 | 1,484 | 33 |
| interprocess | 20 | 46,485 | 2,408 | 298 | 49 |
| type_traits | 182 | 46,346 | 1,573 | 842 | 32 |
| mpl | 267 | 45,966 | 2,072 | 1,072 | 42 |
| python | 118 | 45,605 | 2,018 | 439 | 41 |
| iostreams | 113 | 41,110 | 1,665 | 871 | 34 |
| intrusive | 40 | 39,171 | 1,535 | 476 | 31 |
| multi_index | 24 | 37,454 | 1,196 | 406 | 24 |
| regex | 91 | 36,763 | 2,315 | 956 | 47 |
| compute | 233 | 36,138 | 2,258 | 571 | 46 |
| redis | 296 | 35,240 | 1,443 | 1,527 | 29 |
| parser | 9 | 35,195 | 930 | 54 | 19 |
| container | 11 | 34,942 | 1,519 | 327 | 31 |
| histogram | 127 | 34,210 | 1,457 | 462 | 30 |
| serialization | 43 | 32,374 | 1,065 | 97 | 22 |
| iterator | 52 | 31,381 | 1,275 | 549 | 26 |
| filesystem | 16 | 30,776 | 1,531 | 67 | 31 |
| mqtt5 | 239 | 30,364 | 1,344 | 582 | 27 |
| tti | 107 | 29,053 | 1,208 | 377 | 25 |
| bimap | 41 | 28,990 | 1,319 | 533 | 27 |
| pool | 78 | 28,593 | 804 | 628 | 17 |
| proto | 4 | 27,354 | 1,026 | 94 | 21 |
| static_string | 276 | 26,477 | 1,023 | 852 | 21 |
| statechart | 13 | 26,180 | 1,050 | 72 | 21 |
| fiber | 64 | 25,752 | 1,043 | 456 | 21 |
| range | 160 | 24,800 | 1,085 | 623 | 22 |
| date_time | 11 | 23,830 | 1,463 | 165 | 30 |
| graph_parallel | 38 | 23,778 | 828 | 281 | 17 |
| metaparse | 9 | 22,810 | 1,422 | 92 | 29 |
| algorithm | 155 | 22,219 | 714 | 803 | 15 |
| safe_numerics | 53 | 22,013 | 846 | 221 | 17 |
| dynamic_bitset | 304 | 20,374 | 361 | 1,807 | 8 |
| phoenix | 96 | 19,417 | 939 | 243 | 19 |
| chrono | 5 | 19,039 | 1,029 | 90 | 21 |
| nowide | 71 | 18,230 | 2,971 | 727 | 60 |
| wave | 20 | 17,288 | 846 | 54 | 17 |
| local_function | 33 | 16,174 | 477 | 292 | 10 |
| utility | 45 | 15,978 | 668 | 99 | 14 |
| xpressive | 5 | 15,802 | 824 | 95 | 17 |
| parameter | 3 | 15,517 | 623 | 55 | 13 |
| decimal | 38 | 15,417 | 699 | 490 | 14 |
| config | 9 | 15,371 | 692 | 93 | 14 |
| tool:boostbook | 88 | 14,544 | 489 | 133 | 10 |
| scope | 30 | 14,218 | 527 | 312 | 11 |
| flyweight | 23 | 13,769 | 541 | 150 | 11 |
| quickbook | 11 | 13,692 | 1,125 | 78 | 23 |
| convert | 111 | 13,603 | 588 | 268 | 12 |
| leaf | 3 | 13,500 | 748 | 57 | 15 |
| atomic | 9 | 13,367 | 478 | 110 | 10 |
| hof | 83 | 12,964 | 602 | 186 | 13 |
| core | 58 | 12,704 | 830 | 172 | 17 |
| (others: 210 libs) | 851 | 446,789 | | | |

## 5. calibration vs plan section 4.4

| item | plan estimate | measured |
|---|---|---|
| html pages | 25k-40k | 25,622 |
| english words | 10M-20M | 5,684,492 (5.7M) |
| common-segment reduction | 20-40% | 3.8% |
| LLM batches | thousands | 5,043 (252,114 segs) |
| chinese output | 15M-30M chars | ~9,095,187 chars (1 word ~ 1.6 chars) |

## 6. exclusions and anomalies

- none

basis: translatable text nodes + whitelist attrs (alt/title/meta
description); pre/code/script/style excluded; unique key = normalized
text sha256 truncated; common = key on >=3 pages; batches=ceil(n/50).