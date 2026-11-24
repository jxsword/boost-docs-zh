# Boost 1.46.0 发布说明（中文精要）

> 元数据
> 生成日期：2026-11-14 ｜ 版本基线：Boost 1.92.0（2026-11-14 冻结）
> 原文来源：data/boost_release_notes_en/md/version_1_46_0.md（原始 URL：https://raw.githubusercontent.com/boostorg/website/master/users/history/version_1_46_0.html，核实 2026-11-14，原文格式 HTML→pandoc MD）
> 发布日期：2011-02-21 20:36 GMT（原文日期行：February 21st, 2011 20:36 GMT）
> 精要范围（DR-001）：仅"新增库 + 重大变更"；常规缺陷修复不逐条展开。

## 新增库（New Libraries）

- Icl（区间容器库）：Interval Container Library，区间集合与映射及关联值聚合，作者 Joachim Faulhaber。

## 重大变更（Breaking / 弃用 / 安全 / 标准要求 / 重大新特性）

- Proto（表达式模板/DSL 构建库）——破坏性变更：`boost/proto/core.hpp` 不再定义 `functional::pop_front` 与 `functional::reverse`，二者已移至 `boost/proto/functional` 下各自的头文件。
- Filesystem（可移植文件系统操作库）——默认行为变更：库的 Version 3 现已成为默认版本。
- Filesystem——默认行为变更：`recursive_directory_iterator` 新增 `symlink_option` 以控制是否递归进入目录符号链接，且默认改为不递归进入目录符号链接。

另有 19 项常规缺陷修复与改进（Array、Asio、Bind、Concept Check、Fusion、Graph、Hash、Iostreams、Iterator、Math、MSM、Optional、Pool、ProgramOptions、Proto、Signals、Spirit、Tokenizer、Unordered、Wave 等库），见英文原文存档。

### 1.46.1 修补版（2011-03-12）

修补版本，无新增库，以缺陷修复为主：Asio 修复 Mac OS X 上 kqueue 后端 `EV_ONESHOT` 引发的 `io_service` 析构卡死（改用 `EV_CLEAR`，\#5021）等若干缺陷；Filesystem 修复 STLPort 兼容性并支持 PGI 大文件；Unordered 在右值引用下补齐缺失的拷贝构造与赋值（\#5119）；另有 Fusion、Graph、Icl、Math、Polygon、Proto、PropertyTree、Signals2、TR1 等库的常规修复（原文来源：data/boost_release_notes_en/md/version_1_46_1.md，核实 2026-11-14）。
