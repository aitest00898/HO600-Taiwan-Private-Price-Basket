# Mac host execution results — 2026-10-17

**Branch:** `research/batch-09`; **base revision after `git pull --ff-only`:** `ae4b7d4ccf854d6eb656a3e35558d4b0c1959752`. **Scope:** Complete the residual local Mac work from `SELF-EXECUTION-AND-RESIDUAL-HANDOFF-2026-10-17.md`. No GitHub Actions, `main`, canonical workbook, Basket seal, or Index state was touched.

## TWCA chain diagnosis

The initial default sandbox invocation could not resolve `sslserver.twca.com.tw` (curl exit 6). After granting this turn network access for the user-authorized, strict-TLS work, the committed `verify_twca_chain_macos_readonly.sh` completed its certificate downloads and macOS trust check. It used `curl 8.7.1 SecureTransport --ca-native` on Darwin 27.0 arm64.

- DGBAS leaf file SHA-256: `62ee162c784ec13e20fa7bd21e9f981c723d0104941907fa202f47cb3607d6c7`; X.509 DER SHA-256 fingerprint: `ee7e1a711e0772c854a4054eceef6975bf830f8d847bc7e95e93f1ec6f1ffbe3`.
- Leaf issuer: `TWCA SSL Certification Authority`; SAN includes `ws.dgbas.gov.tw` and `www.stat.gov.tw`. Leaf AKI `F2:28:D4:F9:D4:1C:7E:1A:6B:16:82:E5:EF:93:29:69:ED:CA:15:20` exactly matches the official `Cyber_SSL_2023.crt` intermediate SKI.
- Official `Cyber_SSL_2023.crt` raw SHA-256: `01af2324d098098f5e0cdf6faabada430b21cce777f47eacb26248b2fda3e531`. Official `GlobalCrossCyber_2022.crt` raw SHA-256: `c619f4e6f7b1baa7a6c6f244092a3f82e46a6d67bee26337fbaf02546f33133f`. The second certificate's key ID matches the first certificate's issuer key ID.
- `security verify-cert` exit 0: the leaf and these chain candidates validate for `ws.dgbas.gov.tw` under the **existing macOS system anchor**; candidates were supplied as untrusted chain inputs, with no trust-root override. Certificate Transparency was reported verified.
- The separate live DGBAS `curl --ca-native -I` still failed strictly with exit 60, `unable to get local issuer certificate` (no HTTP response). This supports a likely incomplete or mismatched chain delivered by the DGBAS endpoint. Local system trust is less likely to be the cause because the official chain validates to an existing system anchor and the Taipei/TWCA strict downloads below succeeded. Endpoint-specific transparent interception remains possible and unexcluded.
- No CA was installed, no keychain or network settings changed, and TLS validation was never disabled.

Full certificates and the native trust diagnostic logs are archived in [`evidence/twca-macos-20261017/`](./evidence/twca-macos-20261017/); machine-readable details are in [`twca-chain-diagnostic.receipt.json`](./evidence/twca-macos-20261017/twca-chain-diagnostic.receipt.json).

## Official Taipei City source acquisition

Both originals were obtained over strictly verified HTTPS and preserved with their source receipts and the official metadata page snapshot in [`source-archive/tpe-2020-age-head/`](./source-archive/tpe-2020-age-head/).

| Source | Result | Retrieved (UTC) | Bytes | Original SHA-256 |
|---|---|---|---:|---|
| [Taipei age-head CSV resource](https://data.taipei/dataset/detail?id=26c3817c-0713-4657-8cd8-aa842eb59f97), resource `63e4d839-ef65-46a8-b4d1-1bbfeeca5516` | HTTPS 200, `text/csv;charset=BIG-5`; 2012–2023 series, current resource update shown as 2025-11-20 13:58:57; landing metadata update 2025-12-11 17:58:12 | `2026-10-17T12:16:11.611699Z` | 35,120 | `d75682e408db19704c9c6dae726be3c54ab57560487697acc2d7a478ce801434` |
| [Taipei 2020 Family Income and Expenditure Report PDF](https://data.gov.tw/dataset/133235), official Taipei file host | HTTPS 200, `application/pdf`; title page identifies Taipei City ROC 109 / 2020 report; Table 8 spans printed pages 78–81 | `2026-10-17T12:16:12.635407Z` | 4,438,994 | `877a5da6e2bde0ccf860d08a19e5adbaab87a386cf78d21ac62505c2053710b8` |

The CSV contains 96 records and 58 unique columns, decodes as CP950/Big5, and has eight rows in each of the twelve years 2012–2023. After trimming outer whitespace for the profile, the year/age keys are unique and the eight labels are stable. Sixteen non-2020 age-label cells contain outer whitespace in the preserved raw file; all eight ROC 109/2020 labels are clean and unique. The 2020 rows are seven household-head age groups plus `總平均`. Its 12 expenditure columns and annual NT-dollar unit align with PDF Table 8. This is Taipei City evidence, not a Taiwan-wide source.

## Data reconciliation and proxy output

The PDF Table 8 was visually reviewed on its rendered pages 78–81 and independently read as table cells. The available Poppler renderer lacks the Adobe-CNS1 CMap, so some Chinese glyphs are missing from raster previews; the bilingual English continuation and numeric cells render, and the embedded PDF text was used to verify Chinese category names. PDF and CSV values agree for **96/96** category cells across all eight rows, and **8/8** published consumption totals match exactly. The twelve verified categories are: (1) 食品及非酒精飲料; (2) 菸酒及檳榔; (3) 衣著鞋襪及服飾用品; (4) 住宅服務水電瓦斯及其他燃料; (5) 家具設備及家務維護; (6) 醫療保健; (7) 交通; (8) 通訊; (9) 休閒與文化; (10) 教育; (11) 餐廳及旅館; (12) 什項消費.

Adding the displayed integer category values gives a maximum absolute difference of **NT$2** versus the separately displayed consumption total. Deltas by row are: general average 0; under 30 0; 30–34 +1; 35–39 0; 40–44 −1; 45–54 −1; 55–64 −2; 65+ +1. This bounded display-rounding delta is preserved rather than spread across categories. The proxy weights use the sum of the twelve displayed category cells as each row's denominator.

[`results/tpe-2020-age-head-proxy-20261017/TPE_AGE_HEAD_EXPENDITURE_PROXY_WEIGHTS_2020.csv`](./results/tpe-2020-age-head-proxy-20261017/TPE_AGE_HEAD_EXPENDITURE_PROXY_WEIGHTS_2020.csv) contains 84 weights: seven `TPE_AGE_HEAD_*_PROXY` age groups × twelve expenditure categories. The published `總平均` is not emitted as a cohort. A separate Python 3.14.5 standard-library recomputation matched all 84 source amounts and shares; exact unrounded shares sum to 1 for every age group. The CSV contains a separately named `TPE_AGE_HEAD_65_PLUS_PROXY` row set. **Age 65+ is an age-of-household-head grouping, not retirement status**; the source reports 0.43 employed people per 65+ household on average. No retired-household status is inferred.

Reconciliation details and the independent arithmetic receipt are in [`results/tpe-2020-age-head-proxy-20261017/tpe-2020-age-head-proxy-reconciliation.json`](./results/tpe-2020-age-head-proxy-20261017/tpe-2020-age-head-proxy-reconciliation.json) and [`results/tpe-2020-age-head-proxy-20261017/independent-weight-check.json`](./results/tpe-2020-age-head-proxy-20261017/independent-weight-check.json). The reproducible verifier is [`verify_taipei_2020_age_head_proxy.py`](./verify_taipei_2020_age_head_proxy.py); it uses the Codex bundled `pdfplumber` runtime, not `artifact_tool`.

## Tests and remaining gates

- CSV downloader tests: **11/11 PASS**, standard `python3 -m unittest discover ... -p 'test_fetch_taipei_age_2020_official_csv.py' -v`.
- PDF downloader tests: **7/7 PASS**, standard `python3 -m unittest discover ... -p 'test_fetch_taipei_2020_report_pdf.py' -v`.
- Both test modules use offline synthetic fixtures and standard library tests; neither imports or requires `artifact_tool`.
- National `NAT20-OCC` and `NAT20-AGE` XLS/ODS remain unavailable over strict TLS, so **national WGT-01 remains HOLD**. This run does not validate or replace the corrected national 2020 files, does not produce national work/retirement weights or inflation rates, and does not promote the regional proxies into HO600.
- The Taipei age-head proxy work is complete as a separate regional research output. National WGT-02 remains metadata-only; national WGT-03 and WGT-04 remain HOLD without national raw inputs; national WGT-05 remains 0/2.
