# Boost C++ 库系统调研（中文）· 总索引与验收

> 元数据
> 生成日期：2026-11-14 ｜ 最后更新：2026-11-24（git 纳管 + Read the Docs 上线核验，DR-011）｜ 版本基线：**Boost 1.92.0（2026-11-14 冻结）**
> 调研分级：正式调研（research-workflow 全闸门）；总纲《00_需求计划总纲.md》为唯一详细规则来源（执行会话未改动总纲）。
> 执行方式：P0–P8 逐阶段；P2/P4/P5/P6/P7 后台子代理并行 + P3 八批次翻译（全部落盘并独立校验后统一汇总）。

## 一、快速结论区（一句话答案）

| 问题 | 一句话结论 |
|---|---|
| 最新版本？ | **Boost 1.92.0**（2026-08-12 发布，GitHub API 核实）；1.93.0.beta1 已于 2026-11-11 出 beta、正式版定档 2026-12-09，基线冻结期内只预告不统计 |
| 当前主流使用版本？ | 各渠道主要落在 **1.80–1.92 区间**（活跃主流核心 1.83–1.90；滚动/包管理渠道已至 1.92.0，Conan 1.91.0，发行版 stable 多为 1.83–1.88，LTS/企业存量长尾 1.66–1.79）；发行版滞后上游约 2–4 个 minor（6–19 个月） |
| C++20–26 时代 Boost 还有必要吗？ | **仍有必要且部分领域为刚需**：截止 C++26，网络（Asio/Beast）、单测（Test）、JSON/URL、图（Graph）、几何（Geometry）、IPC（Interprocess）、序列化（Serialization）、任意精度/特殊函数（Multiprecision/Math）、解析器（Spirit）等 66 项仍无标准替代；通用词汇类型（optional/variant/expected/filesystem 等）已归 std，可用标准库 |

## 二、总索引（全部产出）

| 产出 | 文件 | 对应需求 |
|---|---|---|
| 调研总纲（未改动） | [00_需求计划总纲.md](00_需求计划总纲.md) | 闸门③落盘产物 |
| R1 官方资源与最新版本 | [docs/01_官方资源与最新版本.md](docs/01_官方资源与最新版本.md) | R1 |
| R2 组织架构与依赖详解 | [docs/02_组织架构与依赖详解.md](docs/02_组织架构与依赖详解.md) | R2 |
| R2 可视化（自包含 HTML） | [html/boost_architecture.html](html/boost_architecture.html)（图源 [html/_diagrams/](html/_diagrams/)） | R2 |
| R3 历史版本更新日志（58 份译文） | [docs/03_历史版本更新日志/README](docs/03_历史版本更新日志/README)（目录与进度） | R3 |
| R3 英文原文存档（106 份 + MD） | [data/boost_release_notes_en/README.md](data/boost_release_notes_en/README.md)（存档索引） | R3 |
| R4 主流使用版本调研 | [docs/04_主流使用版本调研.md](docs/04_主流使用版本调研.md) | R4 |
| R5 近 5 版标准支持矩阵 | [docs/05_近5版本标准支持矩阵.md](docs/05_近5版本标准支持矩阵.md) | R5（+R7 基准源） |
| R6 C++20–26 必要性分析 | [docs/06_Cpp20-26时代必要性分析.md](docs/06_Cpp20-26时代必要性分析.md) | R6（+R7 基准源） |
| R8 官方文档管理机制 | [docs/07_官方文档管理机制.md](docs/07_官方文档管理机制.md) | R8 |
| R9 全库开发者与维护者清单 | [docs/08_开发者与维护者清单.md](docs/08_开发者与维护者清单.md)（大纲 [00_R9_开发者维护者清单调研大纲.md](00_R9_开发者维护者清单调研大纲.md)） | R9 |
| 决策记录 DR-001~009 | [docs/decision_log.md](docs/decision_log.md) | 决策规范 |
| 术语表（~100 条，翻译共用） | [docs/glossary_术语表.md](docs/glossary_术语表.md) | 术语规范 |
| **全库文档中文翻译计划总纲**（S0–S7 执行规则唯一来源） | [01_全库文档翻译计划总纲.md](01_全库文档翻译计划总纲.md) | 翻译阶段 |
| UI 串译法表（页面框架固定字符串） | [docs/glossary_ui_strings.md](docs/glossary_ui_strings.md) | 翻译阶段 |
| **S1 语料盘点报告**（修正版 25,622 页 / 568 万词 / 5,043 批；早期版 22,010 页已被修正并标注） | [inventory/inventory_report.md](inventory/inventory_report.md)（修正版，英文）· [inventory/盘点报告.md](inventory/盘点报告.md)（初版+完成对照） | S1 产出 |
| **S2 流水线 v1 冻结记录**（试点 5 库 5 形态，门禁全绿） | [docs/translation_progress/S2_冻结记录.md](docs/translation_progress/S2_冻结记录.md) | S2 产出 |
| 库级进度账本 | [docs/translation_progress/progress.csv](docs/translation_progress/progress.csv) | 三账本 |
| 批次账本 + 吞吐统计 | [work/ledger/](work/ledger/) | 三账本 |
| **会话交接文档**（进度快照 + 操作手册 + 新会话启动提示词） | [docs/translation_progress/交接文档.md](docs/translation_progress/交接文档.md) | 跨会话续作 |
| **中文镜像站入口**（site/zh/index.html，含翻译性质声明） | [site/zh/index.html](site/zh/index.html) ｜ **在线阅读**：<https://boost-docs-zh.readthedocs.io/>（已上线，2026-11-24 预览核验通过） | S6 产出 / S7 托管 |
| **分层抽样回读报告**（2,624 页，三类缺陷计数与修复记录） | [docs/translation_progress/分层抽样回读报告.md](docs/translation_progress/分层抽样回读报告.md) | 第 5 道门禁 |

## 三、9 条验收清单（逐项对应 R1–R9）

| # | 验收项 | 结果 | 证据位置 |
|---|---|---|---|
| 1 | R1 官网/文档/源码 URL 三件套 + 最新版说明 | ✅ 13 条 URL 全实测（2026-11-14，含 302 终点与 GitHub 代理核实）；1.92.0 特性摘要按官方发布说明归纳（无新增库、C++20 modules 扩面、container::hub、lockfree 双新队列、URL 三轮安全修复、B2 5.5.3）；发布节奏（4/8/12 月）与版本谱系表（1.36–1.92 逐版日期全部来自存档 GMT 行/GitHub API） | docs/01 第 1、2、4、5 节 |
| 2 | R2 双视角 + ~150 库总表 + 依赖 + mermaid 5 图 + 自包含 HTML | ✅ 158 库模块（官网 157 顶级条目 + int128）、30 分类、每库一行中文简介/分类/编译属性/直接依赖；分类视角 vs superproject module 双视角；入度枢纽 config 156/158、core 100、assert 96；mermaid 5 图（图②拆 3 子图，共 7 源文件）mmdc 两轮校验全过；HTML 单文件 1.28MB、0 外链、分类筛选/搜索/依赖高亮浏览器实测可用 | docs/02；html/boost_architecture.html |
| 3 | R3 全部历史版本中文更新日志 | ✅ DR-001 分级执行：近 20 版（1.73–1.92）逐条完整翻译（20 份）；1.36–1.72 精要（37 份）；1.00–1.35 时代简述（1 份）；英文存档 106 份（1.10.3–1.92 全覆盖 + zcode-archive-meta 头）；倒序每版一文件 | docs/03 目录（58 份译文）；data/boost_release_notes_en |
| 4 | R3 翻译质量控制 | ✅ grep 术语一致性（宏/提案号 20/20、误译黑名单零命中、库名覆盖 20/20 含假阳性复核）；条目数机械对比抽样全对齐（43/43、51/51、35/35，另 B1–B5 批次自检 2209/203/243/172 等）；抽样回读 6/58 ≈ 10.3%（含 2 份全文精读） | docs/03/README 第 2.1 节 |
| 5 | R4 主流版本多源加权 | ✅ 9 类数据源逐个实测（Repology 1537 条目解析、Debian/Ubuntu/Fedora/Homebrew/vcpkg 162 端口/Conan/MSYS2/Cygwin/EL9-10；官方下载统计不可得已注明，GitHub release 下载量旁证）；"1.80–1.92 区间 + 滞后规律"结论；四件套比较矩阵 + 按场景选择结论 | docs/04 |
| 6 | R5 近 5 版 × C++11–26 双认定矩阵 | ✅ 矩阵 A（官方声明：无全局最低标准声明、事实底线 C++11 逐库收敛考证，修正"1.73 起官方最低 C++11"说法）+ 矩阵 B（CI 实测抽查 7 库 cxxstd 矩阵）；编译器最低版本表；34 条来源 URL 全实测 | docs/05 |
| 7 | R6/R7 必要性分析（cppreference 基准） | ✅ 三部分产出：已合入对照表 79 组件行（★血统标记，C++11 25/C++17 17/C++20 13/C++23 12/C++26 12）；必须 Boost 清单 66 项定稿（19 项已可被标准替代者移出）；三档场景矩阵 16 场景；cppreference C++11–26 六页 + WG21 提案归档为基准源并在来源清单显式标注（R7）；std::linalg/std::hive 入 26 等逐项核实修正 | docs/06 |
| 8 | R8 文档管理机制 | ✅ 13 库 doc/ 源格式抽查（QuickBook 9、AsciiDoc 3、Doxygen 1、手写 HTML 1；boostorg/graphite 404 如实记录）；b2 构建链（boostrelease 别名、xsltproc+DocBook XSL）；/doc/libs/{v}/ 归档 + latest 指向实测（latest=master 滚动快照 ≠1.92.0 字节级比对）；2023+ 新站（Django+S3+Antora）与 C++20 modules 文档化动向（1.87 PFR 起步等）；源格式→工具链→产物对照表 + 选型四件套 | docs/07 |
| 9 | R9 全库开发者与维护者清单 | ✅ 158 库 authors/maintainers 全量实测（逐库 master 分支 meta/libraries.json 158/159 命中，headers 伪模块 404 如实记录；superproject 根 libraries.json 404 已弃用 → DR-005）；作者字段与官网缓存 158 库全一致；总表 158 行（库/简介/作者/维护者/源码/文档/备注）+ 反向索引 Top25（120 位去重维护者、219 组配对、单人维护占 71.5%）；组织治理（SC 站点已私有化、基金会现任董事会 9 人实测、治理权在社区）+ 核心人物 26 人（Beman Dawes †2020-12-01 双源核实；1.93.0 发布经理 Marshall Clow 实证）；未核实事实全部备案不写入 | docs/08 |

**验收总判定：9/9 通过（R9 于 2026-11-14 增量完成，见 docs/08 与 DR-004/005）。**

## 四、附加验证记录（2026-11-14）

- mermaid-cli（mmdc 12.2.0）独立复核：7/7 图源通过（P2 代理首轮渲染 + 主会话第二轮复核）。
- HTML 自包含自检：0 个外链资源（script/link/img 无 http(s) src；仅 W3C 命名空间 URI 为 SVG 内在属性）；7 个 SVG 内联；筛选/搜索/高亮交互函数在档。
- 文件名合规扫描：docs/html/data 全部产出文件（扩展名前仅字母/数字/汉字/下划线/连字符）通过。
- 交叉一致性修正：1.91.0 发布日期 P5（04-22）与 B1（04-15）分歧 → 经 GitHub tag/commit API 核实为 **2026-04-15**，docs/01 与 docs/05 已统一。
- 链接互查：README（本文件）↔ 各 docs 间相对链接均在同目录可解析；各文档内部来源 URL 以 2026-11-14 实测为准（含失败现象注明，如 boost.org/users/history/ 301、Repology API 404 等）。

## 五、基线冻结声明

本调研一切"当前/最新/主流"结论以 **2026-11-14、Boost 1.92.0** 为基线。执行期间出现的 1.93.0.beta1（2026-11-11）仅作预告引用、未计入任何统计；后续 1.93.0（定档 2026-12-09）发布后如需更新，应以本目录结构与术语表为增量基础。


## 六、全库文档中文翻译（S0–S6 已完成 · 2026-11-24）

基于《01_全库文档翻译计划总纲.md》（DR-006~009）执行的全量翻译已完成并通过验收。

- **交付物**：`site/zh/index.html`（中文入口页，含非官方社区翻译/BSL-1.0/以英文原文为准声明）+
  `site/zh/1.92.0/` 与官方发布树同构的中文镜像（26,045 页 HTML + 链接所及源码/附件原样镜像）。
- **范围**：以 inventory manifest 为准的文档森林全量（doc/html、doc/antora、libs/*/doc、tools/*/doc、
  根与遗留手册页）；代码/签名/宏/标识符不译，代码清单内英文注释已译。
- **流水线**：extract_segments → build_batches → 子代理翻译 → merge（TM 幂等）→ reemit（字节切片回写）
  → 四道自动门禁；累计 **6,698 批 / 297,095 段**全部 merged（账本 queued=0），TM 318,178 行。
- **五道门禁终版（全站 26,045 页）**：DOM 对等 fails=0 ｜ 术语零汉化 violations=0 ｜
  站内链接 hard=0、deferred=0（21,182→0，九轮链接闭包收敛）｜ 漏译覆盖 misses=0 ｜
  分层抽样回读 2,624 页（T1 10%/T2 5%/T3 2%），漏译 124、错译 2 全部修复，**术语违规 0（硬门禁）**。
- **已知限制**：Antora 页内 JS（搜索/高亮）不汉化，站内搜索仍查英文索引；
  upstream=4,677 为上游既有缺陷与策略排除（example/、boost/ 源码树目录链接等），镜像如实保留。
- **S7 托管发布（已完成并上线 · 2026-11-24，DR-011）**：项目已纳入 git（GitHub `boost-docs-zh` 公开仓库，
  site/zh 完整入库）；静态站托管于 Read the Docs 并已核验上线：<https://boost-docs-zh.readthedocs.io/>
  （`.readthedocs.yaml` build.commands 直发，push 后 webhook 自动重建）。1.93.0 起的增量维护另起决策（TODO ②类）。

### 在线阅读与本地预览（已核实：纯静态站）

**在线阅读**：<https://boost-docs-zh.readthedocs.io/>（Read the Docs 托管，git push 自动重新渲染；
2026-11-24 上线核验通过，渲染符合预期）。

站点为纯静态 HTML + 相对链接（已核实无 fetch/XHR 调用，CSS/图片均为本地相对路径），
`file://` 协议下浏览器可直接完整浏览：

1. **入口**：双击打开 `site/zh/index.html`（声明页）→
   点击"进入 → Boost 1.92.0 文档首页（中文）"→ `site/zh/1.92.0/index.html`（与官方树同构的根页）；
2. `site/zh/1.92.0/index.htm` 为 meta-refresh 跳转桩，直接双击亦可自动跳转 `index.html`；
3. 小事项（无需处理）：631 页引用外网 JS（如语法高亮），断网时仅高亮失效；
   Antora 组件站（msm/url）页内搜索为已知限制（未汉化且静态镜像无搜索索引）；
   `doc/antora/404.html` 使用根绝对路径，仅该错误页在 `file://` 下样式失效；
4. **可选**：模拟真实托管体验时再起本地服务器——
   `cd site/zh && python -m http.server 8000`，浏览器打开 <http://localhost:8000/>；
   仅 S7 发布前整站验证时有必要。

### 修正与重建流程（DR-011）

译文修正以 TM（`tm/segments.jsonl`）为唯一事实源，站点 HTML 为重建产物：

1. **定位**：在 `site/zh/1.92.0/` 找到页面 relpath 及所属库（`inventory/manifest.csv` 按 relpath 查 lib），
   在 TM 中检索对应原文段；
2. **改 TM**：更新该段译文（整站级样板批量修正如 TODO ①类，参考历史模板 `work/scratch/fix_*.py`——
   本地留存未入库，按其模式重写即可）；注意 TM 双键（title 段 reemit 用 text 键查 TM，缺行需补孪生行）；
3. **重建页面**（按库粒度，`--lib` 传 manifest 中的原始库名，可重复传参）：
   `python -I pipeline/reemit_html.py --lib <原始库名>`
   （依赖本地 `data/boost_1_92_0/`，已排除出 git，需要时从 `data/boost_1_92_0.7z` 重解压）；
   仅缺资产（图片等）时用 `python -I pipeline/reemit_html.py --assets-only --all` 补齐；
4. **过门禁**（`--lib` 同样传原始名，可重复）：
   `python -I pipeline/qa_dom_parity.py --lib <库名>` → `qa_terms.py` → `qa_links.py` → `qa_coverage.py`；
5. **本地验证**：`file://` 直接浏览或 `cd site/zh && python -m http.server 8000`；
6. **发布**：`git add`（TM + 变更的 site 页面）→ commit → push，Read the Docs webhook 自动重建，
   几分钟后线上渲染更新；急用可在 RTD 控制台手动 Build Version；
7. **`docs/03_历史版本更新日志/` 等 md 的修正**：直接改文件即可，无需重建（RTD 只托管 site/zh，
   md 修正 push 后在 GitHub 查看）；历史批次术语校验用 `bash scripts/check_terms.sh`，
   十条验收机械核对用 `python -I scripts/verify_acceptance.py`。

**翻译验收总判定：10/10 通过（2026-11-24，逐项见下）。**

| # | 验收项（总纲 §8） | 结果 | 证据位置 |
|---|---|---|---|
| 1 | 语料 =1.92.0 发布树解压实测 | ✅ 2026-11-14 下载解压（archives.boost.io，代理+断点续传） | data/boost_1_92_0；inventory/盘点报告.md |
| 2 | 库覆盖以 manifest 为准 | ✅ manifest 26,045 行 status 全 ok；无文档库按"无文档"记录 | inventory/manifest.csv；progress.csv |
| 3 | 应翻页翻译率 ≥99% | ✅ zh 树 26,045/26,045 = **100%** | site/zh/1.92.0（核对脚本 scripts/verify_acceptance.py） |
| 4 | DOM 对等 100% + 代码块 hash 不变 | ✅ 全站 qa_dom fails=0 | 门禁终版输出（2026-11-24） |
| 5 | 术语 grep 零命中 | ✅ 全站 qa_terms violations=0（303 个受保护术语） | 同上 |
| 6 | 站内相对链接 0 断链 | ✅ 全站 hard=0、deferred=0（上游缺陷如实镜像归 upstream=4,677） | qa_links 终版输出（2026-11-24） |
| 7 | 全量漏译检测通过 | ✅ 全站 qa_coverage misses=0（288,896 段） | qa_coverage 终版输出（2026-11-24） |
| 8 | 分层抽样回读达标 + 三类计数 | ✅ 2,624 页回读；漏译 124/错译 2 全修复；术语违规=0 | docs/translation_progress/分层抽样回读报告.md |
| 9 | 三账本 / README / 总索引完整 | ✅ progress.csv 293 行、batch_ledger queued=0、本文件已更新 | docs/translation_progress/；work/ledger/ |
| 10 | DR-006~009 落盘 | ✅ 全部落盘且未被修改 | docs/decision_log.md |
