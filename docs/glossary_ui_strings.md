# UI 串译法表（页面框架固定字符串 · 全体翻译子代理共用）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 用途：HTML 页面框架层（导航、admonition 标题、页脚等）固定 UI 字符串的唯一译法来源；
>       与 `docs/glossary_术语表.md` 第 0 节衔接——**库名 / API / 宏 / 工具名一律不译**，本表只收"非术语"的界面串。
> 机制：本表先由 S1 语料盘点统计高频公共段落定骨架，随后人工精翻一次存入
>       `pipeline/common_segments.json` 机械套用（不进 LLM 批次）；两文件保持同步，以 `common_segments.json` 为最终生效版。

## 0. 使用规则

1. 本表条目为**全站唯一译法**：同一英文 UI 串在任何页面不得出现第二译法。
2. 表中串若作为**文档正文语句的一部分**（非独立框架元素），仍按正文翻译，但核心词译法须与本表一致。
3. 与术语表的边界：`Asio`、`boost::`、`BOOST_*`、`b2` 等见 `docs/glossary_术语表.md` 第 0 节，本表不重复收录。

## 1. 导航串（BoostBook 产物页眉/页脚导航）

| 英文原文 | 固定译法 | 出现位置 |
|---|---|---|
| Home | 首页 | 页眉导航 |
| Prev | 上一页 | 页眉/页脚导航 |
| Next | 下一页 | 页眉/页脚导航 |
| Up | 上一级 | 页眉/页脚导航 |
| Tables of Contents / Table of Contents | 目录 | 侧栏/首页 |
| Contents | 目录 | 目录标题 |
| Index | 索引 | 索引页标题 |
| Reference | 参考 | 章节 |
| Glossary | 术语表 | 章节 |

## 2. Admonition 标题（提示框）

| 英文原文 | 固定译法 | 出现位置 |
|---|---|---|
| Note | 注释 | 提示框标题 |
| Warning | 警告 | 提示框标题 |
| Important | 重要 | 提示框标题 |
| Tip | 提示 | 提示框标题 |
| Caution | 注意 | 提示框标题 |
| Danger | 危险 | 提示框标题 |

## 3. 页脚与版权

| 英文原文 | 固定译法 | 出现位置 |
|---|---|---|
| Copyright | 版权 | 页脚 |
| Copyright © / Copyright (c) | 版权所有 © | 许可声明行（年份/权利人原样保留） |
| All rights reserved. | 保留所有权利。 | 许可声明行 |
| Distributed under the Boost Software License, Version 1.0. | 按 Boost 软件许可 1.0 版（Boost Software License, Version 1.0）分发。 | 页脚声明；"Boost Software License, Version 1.0" 作为许可证名不译 |
| (See accompanying file LICENSE_1_0.txt or copy at ...) | （随附文件 LICENSE_1_0.txt 或复制于 ...） | 页脚声明；文件名与 URL 原样保留 |
| Last revised: | 最后修订： | 页脚 |
| Last updated: | 最后更新： | 页脚（日期原样保留） |

## 4. 章节结构串（BoostBook / Doxygen 直出）

| 英文原文 | 固定译法 | 出现位置 |
|---|---|---|
| Description | 说明 | 章节 |
| Synopsis | 概要 | 章节 |
| Synopsis (headers) | 概要（头文件） | 章节 |
| Header | 头文件 | 章节 |
| Requirements | 要求 | 章节 |
| Requirements and Portability | 要求与可移植性 | 章节 |
| Examples | 示例 | 章节 |
| Example | 示例 | 章节 |
| Rationale | 设计理由 | 章节 |
| Design | 设计 | 章节 |
| References | 参考文献 | 章节 |
| Acknowledgments / Acknowledgements | 致谢 | 章节 |
| History | 历史 | 章节 |
| FAQ | 常见问题（FAQ） | 章节 |
| Overview | 概述 | 章节 |
| Introduction | 引言 | 章节 |
| Getting Started | 入门 | 章节 |
| Tutorial | 教程 | 章节 |
| Installation | 安装 | 章节 |
| Configuration | 配置 | 章节 |
| Testing | 测试 | 章节 |
| Future work | 后续工作 | 章节 |

## 5. Doxygen 直出参考页框架串

| 英文原文 | 固定译法 | 出现位置 |
|---|---|---|
| Defined in header | 定义于头文件 | 参考页 |
| Template Parameters | 模板参数 | 参考页 |
| Parameters | 参数 | 参考页 |
| Precondition(s) | 前置条件 | 参考页 |
| Postcondition(s) | 后置条件 | 参考页 |
| Requires | 要求 | 参考页 |
| Effects | 效果 | 参考页 |
| Returns | 返回 | 参考页 |
| Throws | 抛出 | 参考页 |
| Complexity | 复杂度 | 参考页 |
| Remarks | 备注 | 参考页 |
| Default | 默认 | 参考页 |
| Notes | 注释 | 参考页 |
| See Also | 参见 | 参考页 |
| Members | 成员 | 参考页 |
| Types | 类型 | 参考页 |
| Functions | 函数 | 参考页 |
| Classes | 类 | 参考页 |
| Namespaces | 命名空间 | 参考页 |
| Enumerations | 枚举 | 参考页 |
| Variables | 变量 | 参考页 |

## 6. 通用界面串（手写 HTML / Antora 产物）

| 英文原文 | 固定译法 | 出现位置 |
|---|---|---|
| Search | 搜索 | 站点控件（仅文本；Antora 页内 JS 不汉化） |
| Table of Contents | 目录 | Antora 侧栏 |
| On this page | 本页内容 | Antora 页内目录 |
| Version | 版本 | Antora 组件选择器 |
| Library | 库 | 页面标签 |
| Documentation | 文档 | 站点导航 |
| Downloads | 下载 | 站点导航 |
| Community | 社区 | 站点导航 |
| Support | 支持 | 站点导航 |
| Report a bug | 报告缺陷 | 页脚/正文链接 |
| GitHub | GitHub | 链接文字（不译） |

## 7. 待补清单（S1 盘点后回填）

> 状态注记（2026-11-24）：翻译已完成。common_segments.json 终版含公共段 **121 条**
> （S2 冻结记录的 117 条为冻结时点值）；项目实际以 common_segments.json + TM 既有译法
> 机械套用，未再逐项回填本清单——其余页面框架串（重载后缀、目录树、许可页脚等）
> 以 TM 既有译法为准（见术语增补 T2/T3 补录·惯用处理）。

- [ ] 按 `pipeline/common_segments.json` 高频统计回填漏收串（→ 已由 common_segments.json 121 条覆盖）
- [ ] Antora（msm / url）产物框架串按实测页补（→ 未回填；页内搜索为已知限制，见 TODO.md）
- [ ] docca+asciidoctor（json 等）参考页框架串按实测页补（→ 未回填；该类页框架串经 TM 统一套用）
- [ ] 手写 HTML 库页（multi_index 等）按实测页补（→ 未回填；同上）
