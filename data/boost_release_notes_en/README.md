# 英文发布说明存档索引（data/boost_release_notes_en/）

> 元数据：生成日期 2026-11-14 ｜ 版本基线 Boost 1.92.0 ｜ 用途：R3 历史更新日志翻译的英文原文存档（共 106 份 HTML + 106 份 MD 转换）
> 下载源（均核实于 2026-11-14）：
> - 主源：`https://raw.githubusercontent.com/boostorg/website/master/users/history/{文件名}`（boostorg/website 仓库，HTML 存档，覆盖 1.10.3–1.89.0 共 102 份）
> - 补源：`https://www.boost.org/releases/{版本}/` 发布页整页（覆盖 1.90.0 / 1.91.0 / 1.91.0-1 / 1.92.0 共 4 份；仓库 users/history 未收录 1.90+，boost.org `/users/history/version_1_92_0.html` 301 重定向至 `/releases/1.92.0/`）
> 兜底源（未用到）：archives.boost.io
> 每份文件头部有 `zcode-archive-meta` HTML 注释：来源 URL + 核实日期 + 格式。
> MD 转换：pandoc 3.8.3（`-f html -t gfm-raw_html --wrap=none`），存于 `md/` 子目录，文件名同 HTML。

## 清单

| 文件 | 版本 | 来源 | 备注 |
|---|---|---|---|
| version_1_10_3.html … version_1_35_0.html（46 份） | 1.10.3 → 1.35.0 | boostorg/website users/history | B8 时代简述素材；1.0–1.10.2 无存档（发布说明制度未建立前） |
| version_1_36_0.html … version_1_89_0.html（56 份） | 1.36.0 → 1.89.0 | boostorg/website users/history | 含 1.46.0+1.46.1、1.65.0+1.65.1 修补版 |
| boost_org_releases_1_90_0.html | 1.90.0 | boost.org /releases/1.90.0/ | 发布页整页 |
| boost_org_releases_1_91_0.html | 1.91.0 | boost.org /releases/1.91.0/ | 发布页整页 |
| boost_org_releases_1_91_0-1.html | 1.91.0-1 | boost.org /releases/1.91.0.1/ | 修补重发布；官网"What's new"摘要尚在生成中，正文无增量说明（打包级重发布） |
| boost_org_releases_1_92_0.html | 1.92.0 | boost.org /releases/1.92.0/ | 发布页整页 |

## 转换约定

- 翻译批次产出：`docs/03_历史版本更新日志/version_X_Y_Z.md`（每版一文件）与 `era_1_00-1_35_简述.md`
- 1.91.0 与 1.91.0-1 合并写入 version_1_91_0.md（-1 注明为打包重发布、原版未单独见于 GitHub Releases 列表）
