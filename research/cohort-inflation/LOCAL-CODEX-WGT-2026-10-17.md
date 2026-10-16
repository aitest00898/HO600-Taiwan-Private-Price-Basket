# Local Codex — 2020 revised DGBAS cohort baseline: WGT-01→WGT-05

**Date:** 2026-10-17. **Branch:** `research/batch-09` only, no `main` merge or canonical workbook/index update.

## Verified web evidence vs not yet verified raw files

- DGBAS 2020 official occupation Table 4: https://www.stat.gov.tw/News_Content.aspx?n=3908&s=210989 (EXCEL link https://ws.dgbas.gov.tw/001/Upload/463/relfile/11530/235896/65.xls ).
- DGBAS 2020 official age-group detail: https://www.stat.gov.tw/News_Content.aspx?n=3911&s=211017 (EXCEL link https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.xls ).
- DGBAS flags the **2026-02-13 reupload/correction** in housing/rent/utilities and consumption. The government pages load; the XLS URLs returned web cache-miss/502 in the app network and the model container's DNS resolution of `ws.dgbas.gov.tw` failed. This is **NETWORK_BLOCKED**, not source absent.
- 2020 all-household 12 division indexed excerpt totals **815,100**, but remains `RAW_UNVERIFIED` and may differ from official corrected revisions. If revised source differs, create `SOURCE_CONFLICT`, do not force-fit to this old excerpt.

## Exact local steps (no GitHub Actions)

1. On Mac: `git switch research/batch-09; git pull --ff-only`. Never enable Actions. Download the official 2020 age and occupation XLS originals via the URL/official page with the user's normal browser or shell network if reachable. Use `fetch_official_weight_tables.py --plan`, `--download NAT20-AGE`, `--download NAT20-OCC` for official-only download receipt, SHA and valid file-signature checks. If XLS is blocked, try official ODF age variant; do not reinterpret failure as no file.
2. Preserve original `.xls`/`.ods`, UTC download receipt, SHA-256 and source URL **outside Git repo**, and never overwrite. Verify original archive timestamp/revision and readable binary. Reject error HTML.
3. Convert source using macOS Numbers GUI to a separate `.xlsx` (no silent data changes). Record both raw and converted SHA and actual sheet names. Do **not** assert binary equality between formats. The parser uses `artifact_tool` for XLSX reading; do not substitute unrelated spreadsheet parser.
4. Run `python3 research/cohort-inflation/extract_revised_2020_cohort_xlsx.py --inspect /absolute/path/to/converted.xlsx`; inspect actual headings, 12 spending divisions, occupation/age columns, unit, total, footnotes and year. The inspection is deliberately informative, not an automatic model assignment.
5. Copy `cohort-weight-mapping.template.json` outside repository to a reviewed mapping file. Fill `sheet`, `label_col`, `amount_col`, each actual 1-based `category_rows`, `total_row`, original/conversion SHA, `cohort_code` as a named **PROXY**, then `reviewed: true` ONLY after source-to-cell mapping independently verified.
6. Run:
```bash
python3 research/cohort-inflation/extract_revised_2020_cohort_xlsx.py --extract /absolute/path/converted.xlsx --raw /absolute/path/original.xls --mapping /absolute/path/reviewed-mapping.json --out /tmp/ho600-cohort-weight-qc
python3 -m unittest discover -s research/cohort-inflation -p 'test_extract_revised_2020_cohort_xlsx.py'
python3 research/cohort-inflation/validate_exposure.py
```
7. Confirm each 12-category proxy group: nonnegative values, unit **TWD per household per year**, numeric category sum within 12 TWD of directly labelled total, 12 distinct category cells, source hashes pinned, no duplicated rows/child expenditure summed with parent. Inspect every source cell manually; compare 2020 all-household total only if the source genuinely provides an all-household column.
8. Commit **only the provenance, audit report, schemas, validated aggregate proxy weights if allowed by source usage, and any needed extraction code** to this research branch. Raw source files in private local working cache by default; don't submit potentially copyrighted XLS binaries by accident. Redact no factual evidence; record URLs/SHA. Do not edit `data/*.csv`, `canonical/status.json`, seven-sheet official workbook, or release an index.

## Mandatory acceptance cases

- Both official 2020 source files are actually downloaded: `WGT-01=PASS` only after two authenticated original binary SHA receipts.
- Revised version and year confirmed: `WGT-02`; numerical extraction: `WGT-03`; within-group source totals: `WGT-04`.
- Economy head occupation **≠** all salaried-worker households; household head age **≠** retired families. Use only `OCC_HEAD_*_PROXY` and `AGE_HEAD_*_PROXY`. Do not derive age × occupation joint matrix from separate marginals: `WGT-05`.
- Employment/retirement true population weights remain blocked unless separately evidenced. Do not calculate **HO600-WORK**, **HO600-RETIRE** or "experienced inflation" rates from proxy alone.
- Any unknown category, changed XLS layout, missing SHA, revised table conflict, nonmatching year, unqualified group, category mismatch, or partial expense coverage: **HOLD** without fabricated fixes.

## Built-in self-tests

`test_extract_revised_2020_cohort_xlsx.py` builds a synthetic 12-cell XLSX locally with `artifact_tool` and exercises success plus review/SHA/cohort/row/label/overwrite failure gates. The synthetic values are **fixtures**, never real consumer spending. Do not call the source-raw WGT gates passed merely because test fixtures pass.

## Branch and delivery contract

Always report two statuses separately: canonical HO600 stays **181/600, Basket NOT SEALED, Index LOCKED**; Batch 9 C01–C03 60 research-level PASS, C04 WIP unchanged. New cohort extraction remains distinct from the private-price basket. No Actions, no auto-merge, no background claims.
