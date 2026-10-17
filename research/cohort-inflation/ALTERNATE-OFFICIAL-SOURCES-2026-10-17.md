# WGT official-source recovery options — 2026-10-17

**Research-only. Decision state:** `NATIONAL_WGT_HOLD`; alternative source discovery validated at *metadata* level, **not raw data**. No GitHub Actions. No change to canonical main 181/600 / Basket NOT SEALED / Index LOCKED.

## 1. Root cause from real Mac diagnostics

The actual Mac diagnostic receipt at [TLS-DIAGNOSTIC-RESULT-2026-10-17.md](./TLS-DIAGNOSTIC-RESULT-2026-10-17.md) shows:
- `ws.dgbas.gov.tw`: issuer = TWCA SSL Certification Authority; leaf AKI `F2:28:D4:F9:D4:1C:7E:1A:6B:16:82:E5:EF:93:29:69:ED:CA:15:20` does not match SKI of any three server-presented ePKI certificates, OpenSSL code 20. SAN includes domain.
- `www.stat.gov.tw`: same leaf certificate, no intermediate, code 20. SAN includes domain.
- `ssl.twca.com.tw`: issuer chain complete, strict code 0 and macOS native `curl` HTTP 200.
- **Likely site-side wrong/missing intermediate, not a generalized Mac CA problem**; transparent network intermediary not fully excluded.
- **11/11 standard-library synthetic CSV unit tests PASS** on user's Mac after numeric-zero fix, but WGT-01..05 still HOLD; no genuine raw XLS/ODS or derived weights.

TWCA [2026-04-15 official chain-change notice](https://ssl.twca.com.tw/news_detail/ad2496ee-39cf-4d74-b44a-410470f99570) documents a change to CYBER Root chain and Apple/IIS warning. That notice does **not** establish that DGBAS uses IIS or that any similarly named intermediate is the actual issuer of the DGBAS leaf. Compare AKI/SKI **and verify signatures**, not names alone. Leaf AIA HTTP URL remains untrusted/unused.

## 2. Independently verified official metadata for alternative datasets

| ID | Official landing page | Geographic/temporal scope | Contents | Fit for national WGT? | Original bytes |
| --- | --- | --- | --- | --- | --- |
| TPE-AGE-2012-2023 | https://data.gov.tw/dataset/133235 | Taipei City, 2012–2023 | Age-of-economic-head, 12 original expense divisions, family size, employed count, sources of income | **NO — Taipei-only**, useful 2020 regional age-head proxy and schema QA | Not retrieved in this environment |
| TPE-AGE-2024PLUS | https://data.gov.tw/dataset/133235 | Taipei City, >=2024 | Annual later city age-head expenditures, categories may differ | **NO** | Not retrieved |
| TPE-DISTRICT-2020-2023 | https://data.taipei/dataset/detail?id=d4142821-6cb6-4678-8fd6-709f620ced26 | Taipei, district by year incl 2020 | Household expenditure by district with 12 primary categories in historical period | **NO — geography and grain differ** | Not retrieved |
| NATIONAL-AGE-2024-TOTAL-ONLY | https://data.gov.tw/dataset/108265 | Taiwan 2024 | Age-of-head × income quintile **total** consumption, not 12-division category matrix | **NO** for baseline category weights or 2020 | Not retrieved |
| NATIONAL-PRIVATE-CONSUMPTION-COICOP | https://data.gov.tw/dataset/44226 | Taiwan yearly national-account aggregates | 12 consumption purposes across total private consumption; **not** household-head age/occupation survey | **NO** for cohort weights; useful different-method benchmark only | Not retrieved |

The `data.gov.tw` listing is official *metadata*. CSV links for the Taipei age series point to `data.taipei` (different host from bad `ws.dgbas.gov.tw` chain); this is a promising **separate TLS route, not proof of working HTTPS download**. Model container DNS failed for `data.taipei`; web access to the CSV returned a fetch error, so do not assert that a real age record has been obtained.

**Important 2024 schema drift:** Taipei city separate district series published a 2024+ variant with categories including `8.資通訊`, `9.休閒運動與文化`, `12.保險及金融服務`, `13.個人清潔照護社會保障及其他`. This differs from the older 12-category scheme. Do not join these unmodified with 2020 codes or assume 12-digit positions have persistent meanings across revisions. First audit actual headers and documented classification year.

## 3. Recommended highest-value execution, bounded

### A. Short official-original HTTPS recovery attempt

1. On local Mac, fetch only the **TWCA official HTTPS** [certificate repository](https://ssl.twca.com.tw/repository) and official [2026 chain notice](https://ssl.twca.com.tw/news_detail/ad2496ee-39cf-4d74-b44a-410470f99570), normally trusted. Inspect whether TWCA publishes the candidate **exact issuing intermediate**, with certificate full subject, SKI, signature and chain to an **already locally trusted** root. Never presume that the 2026 announcement's `TWCA SSL CA` is the same key as DGBAS issuer.
2. A standard `openssl verify` test can evaluate a candidate intermediate as **untrusted chain-building input**, retaining default **system roots as the only trust anchors**. This is a read-only diagnostic; do not import/install a root, add a new trust anchor, set `partial_chain`, alter macOS Keychain, override hostname, suppress revocation requirements, or disable verification. If verification fails, stop and retain WGT-01 HOLD.
3. A full real HTTPS download is acceptable only when strict hostname, validity, chain-to-existing-trusted-root and response content succeed **in the actual retrieval process**. Offline verification of one leaf alone does not prove a subsequent HTTP connection succeeded. Save HTTPS URL, original bytes, exact UTC, length, binary header and SHA-256; reject HTML/empty data.

### B. Parallel trusted other-host official research

1. Probe `https://data.taipei` with ordinary default trust and hostname verification; if it passes, download the 2012–2023 **age-of-household-head** 2020-containing CSV from its *official dataset resource link*. Store actual URL/final URL, status, length, SHA-256 and response headers. Check year coding (ROC 109 or 2020), ages, survey definitions and exact 12 categories; do not use another provider's mirror.
2. If city raw data succeeds, construct **`TPE_AGE_HEAD_*_PROXY` as a separate regional exploratory vector only**, *not* `NAT20-AGE` or nationally representative `RETIRE`. The national WGT-01 stays HOLD. The existing national proxy parser intentionally refuses this city source: **do not relax the nationality validation or mislabel the output**. Write and test a separate city-only parser/mapping when actual schema is available.
3. Compare age-specific spending in Taipei with the all-household city control row and data revision rules. Do not compare Taipei city annual total to the national 815,100 reference as though it should reconcile.

### C. Work that remains possible without raw national files

- Preserve 11/11 Python stdlib fixture tests as actual test PASS; 7 original artifact_tool-dependent tests remain BLOCKED if that interpreter still lacks it.
- Continue Batch9 original price-evidence work independently. No fabricated inflation rates or full-spend coverage.
- Keep official `NAT20-OCC` and `NAT20-AGE` under WGT-01 HOLD until their corrected authentic raw binaries become available.

## Decision

**Alternative site discovered, raw national dataset not recovered.** Primary WGT-01 remains HOLD, not BLOCKED FOREVER. A safe, strictly validated per-process intermediate-chain **diagnostic** can be attempted without modifying system trust *only when official and cryptographically verifiable*, while alternate official Taipei data can support a separately labelled regional age-head study. Neither should be presented as solving Taiwan-wide WORK/RETIRE inflation.
