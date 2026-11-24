#!/usr/bin/env bash
# 术语一致性校验：英文原文中的库名/宏/提案号必须原样出现在译文中
# 用法: bash scripts/check_terms.sh   （本副本自 scripts/ 相对定位，原版在 .work/，未入库）
# 说明: 仅检查, 不修改文件. 数据目录(data/)与本脚本分离存放.

BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EN_DIR="$BASE/data/boost_release_notes_en/md"
ZH_DIR="$BASE/docs/03_历史版本更新日志"
fail_total=0

# 完整翻译版本清单 (1.73-1.92)
full_versions="1_92_0 1_91_0 1_90_0 1_89_0 1_88_0 1_87_0 1_86_0 1_85_0 1_84_0 1_83_0 1_82_0 1_81_0 1_80_0 1_79_0 1_78_0 1_77_0 1_76_0 1_75_0 1_74_0 1_73_0"

# 英文源文件映射
src_for() {
  case "$1" in
    1_92_0) echo "boost_org_releases_1_92_0.md" ;;
    1_91_0) echo "boost_org_releases_1_91_0.md" ;;
    1_90_0) echo "boost_org_releases_1_90_0.md" ;;
    *) echo "version_$1.md" ;;
  esac
}

echo "== 逐版本库名覆盖校验 =="
for v in $full_versions; do
  zh="$ZH_DIR/version_$v.md"
  en="$EN_DIR/$(src_for "$v")"
  if [ ! -s "$zh" ]; then echo "MISS  version_$v.md 不存在"; fail_total=$((fail_total+1)); continue; fi
  if [ ! -s "$en" ]; then echo "MISS  英文源 $en 不存在"; continue; fi
  # 提取英文源中的库名锚点: - [Name](/libs/...) 或 ### [Name](...)
  missing=0
  while IFS= read -r lib; do
    [ -z "$lib" ] && continue
    if ! grep -qF "$lib" "$zh"; then
      echo "FAIL  version_$v.md 缺库名: $lib"
      missing=$((missing+1))
    fi
  done < <(grep -o '\[[A-Za-z][A-Za-z0-9_. ]\{1,40\}\](/libs/' "$en" | sed 's/^\[//;s/\](\/libs\/$//' | sort -u)
  if [ "$missing" -eq 0 ]; then echo "PASS  version_$v.md 库名全覆盖"; fi
done

echo
echo "== 宏/命名空间/提案号保真抽查 =="
# 译文里 BOOST_ 宏与 std:: 与 P\d{4,5} 必须存在(完整翻译版)
for v in $full_versions; do
  zh="$ZH_DIR/version_$v.md"
  en="$EN_DIR/$(src_for "$v")"
  [ -s "$zh" ] || continue
  n_boost_en=$(grep -o 'BOOST_[A-Za-z0-9_]*' "$en" | sort -u | wc -l)
  n_boost_zh=$(grep -o 'BOOST_[A-Za-z0-9_]*' "$zh" | sort -u | wc -l)
  n_std_en=$(grep -o 'std::[a-z_]*' "$en" | sort -u | wc -l)
  n_std_zh=$(grep -o 'std::[a-z_]*' "$zh" | sort -u | wc -l)
  n_p_en=$(grep -oE '\bP[0-9]{4,5}\b' "$en" | sort -u | wc -l)
  n_p_zh=$(grep -oE '\bP[0-9]{4,5}\b' "$zh" | sort -u | wc -l)
  flag=""
  [ "$n_p_en" -gt "$n_p_zh" ] && flag="FAIL 提案号丢失($n_p_en->$n_p_zh)"
  [ "$n_boost_en" -gt 0 ] && [ "$n_boost_zh" -eq 0 ] && flag="$flag FAIL BOOST宏丢失"
  if [ -n "$flag" ]; then echo "FAIL  version_$v.md $flag"; fail_total=$((fail_total+1)); else echo "PASS  version_$v.md 宏/提案号 (BOOST $n_boost_zh/$n_boost_en, P# $n_p_zh/$n_p_en)"; fi
done

echo
echo "== 常见误译黑名单扫描(全部译文) =="
# 黑名单: 库名被意译的常见错误词
bad_words="阿西奥|阿西欧|波斯特|提升库|增压库|助推库"
found=0
while IFS= read -r f; do
  hits=$(grep -nE "$bad_words" "$f" 2>/dev/null | head -3)
  if [ -n "$hits" ]; then echo "FAIL  $f 误译黑名单命中:"; echo "$hits"; found=$((found+1)); fi
done < <(find "$ZH_DIR" -name "version_*.md" -o -name "era_*.md")
[ "$found" -eq 0 ] && echo "PASS  无常见误译"

echo
echo "==== 汇总: 失败项 $fail_total ===="
