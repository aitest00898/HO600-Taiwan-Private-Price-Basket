# HO600 WGT — assistant-run acquisition attempts and minimal Mac-only residual work

> **Execution update (2026-10-17):** `git pull --ff-only` completed on `research/batch-09`. The residual Mac tasks in this handoff were then executed. See [`MAC-EXECUTION-RESULTS-2026-10-17.md`](./MAC-EXECUTION-RESULTS-2026-10-17.md) for the verified TWCA chain, official Taipei originals and receipts, 18 offline tests, PDF/CSV reconciliation, regional proxy output, and remaining national HOLD gates. The original national DGBAS XLS/ODS remain HOLD.

**When:** 2026-10-17, Asia/Taipei. Branch `research/batch-09`; all WGT-01..05 remain on existing HOLD except the known WGT-02 landing-page metadata. This is not a publication approval. GitHub Actions remain disabled.

## Assistant actually attempted (not just planned)

1. Local container DNS: `socket.getaddrinfo(...,443)` on `sslserver.twca.com.tw`, `data.taipei`, `ws.dgbas.gov.tw`, `www.stat.gov.tw` each returned `gaierror: [Errno -3] Temporary failure in name resolution`. No TLS handshake was possible here. This is a restriction on **this container**, not proof that user Mac DNS still fails.
2. Official Taipei 2012–2023 history CSV: official catalog [dataset 133235](https://data.gov.tw/dataset/133235) and [Taipei detail page](https://data.taipei/dataset/detail?id=26c3817c-0713-4657-8cd8-aa842eb59f97) were both read. Original resource `63e4d839-ef65-46a8-b4d1-1bbfeeca5516`, 34.3 KB (as published on official landing), last resource update 2025-11-20. Tried both actual provider resource download paths via web tool; both returned fetch failures `(400) OK` (tool gateway errors, **not confirmed origin HTTP status**). Container downloader also failed. **No source bytes, no SHA.**
3. Official TWCA CA HTML notice [2026-04-15](https://ssl.twca.com.tw/news_detail/ad2496ee-39cf-4d74-b44a-410470f99570) read. Its direct links [Cyber_SSL_2023.crt](https://sslserver.twca.com.tw/cacert/Cyber_SSL_2023.crt) and [GlobalCrossCyber_2022.crt](https://sslserver.twca.com.tw/cacert/GlobalCrossCyber_2022.crt) yielded `application/pkix-cert` unsupported binary content in the web gateway. The container could not resolve the CA host. **Actual DER/PEM SHA, AKI/SKI, signature and native Mac trust evaluation not completed here**. Do not import CA or bypass TLS.
4. Discovered a **third official route** with a separate, non-DGBAS hostname, Taipei's published 2020 full survey: [2020 Taipei Family Income and Expenditure Report PDF](https://www-ws.gov.taipei/Download.ashx?icon=.pdf&n=MTA55bm06Ie65YyX5biC5a625bqt5pS25pSv6Kiq5ZWP6Kq%2F5p%2Bl5aCx5ZGKLnBkZg%3D%3D&u=LzAwMS9VcGxvYWQvMzY3L3JlbGZpbGUvNDU2NzIvODQ3MTQxNy8wNjFmMDZlMy1iZjE1LTQzODYtOWNhYi1iMWM1YzdiNzBkZDMucGRm). Its official searchable PDF index labels **Table 8: 2020 Taipei household expenditure by household-head age**, with 12 categories, age-group columns. A web fetch of the actual PDF returned **cache miss**, and PDF screenshot access was also unavailable, so **no PDF raw bytes, pages, weights, source hash or 65+ values were officially authenticated here**.
5. Assistant runtime has a working `artifact_tool` import. Independently exercised `Workbook.create`, creating 12 synthetic categories, `SpreadsheetFile.export_xlsx` and `SpreadsheetFile.import_xlsx`, with 12-row sum 1266 = synthetic total. Additionally inspected the supplied `fixture.xlsx` with `artifact_tool`: a **synthetic** tiny `Main` sheet of two categories + total, not official data. This validates **runtime capability only**, not the real project's 7 artifact_tool-dependent tests or official source.
6. Re-read GitHub and checked file classification/permissions. No `main` write, no remote branch merge or Actions dispatch.

### Actual conclusion

- **NATIONAL_WGT01:** HOLD — corrected source XLS/ODS never retrieved in any environment.
- **TPE_CITY_RAW_2020:** HOLD — official metadata+PDF searchable index verified, actual CSV/PDF raw not accessible through current assistant runtime.
- **TWCA_VERIFIED_INTERMEDIATE:** HOLD — official CA binary URLs confirmed, actual CA bytes inaccessible.
- **ASSISTANT_OFFLINE_TOOL_SMOKE:** PASS_SYNTHETIC_ONLY.
- **WORK/RETIRE (national) weights:** 0/2 and no CPI or experienced inflation.
- **No claim of successful downloads:** all source original SHA/date/bytes remain UNKNOWN.

## Committed executable helpers

- [Original exact-issuer chain verifier](./verify_twca_chain_macos_readonly.sh): `curl --ca-native` authenticated TWCA CA retrieval and macOS existing trust anchor chain evaluation; no trust store writes.
- [Taipei time-series CSV downloader](./fetch_taipei_age_2020_official_csv.py): separate city-host trusted HTTPS / 2020 schema check / raw bytes+SHA receipt.
- **New:** [Taipei 2020 full-report PDF downloader](./fetch_taipei_2020_report_pdf.py): separate `www-ws.gov.taipei` trusted TLS host, verifies PDF magic+EOF and SHA, tags regional-only, no invented weight cells.
- [11 CSV synthetic test cases](./test_fetch_taipei_age_2020_official_csv.py) and [7 PDF synthetic test cases](./test_fetch_taipei_2020_report_pdf.py) are committed, **not executed on user's Mac yet**.

## Only tasks that genuinely require the user's Mac now

Execute on the Mac with the already-connected `research/batch-09` repo (no global installation required):

```bash
git switch research/batch-09
git pull --ff-only

# Safe TLS issuer-chain diagnostic using existing Mac trust anchors
bash research/cohort-inflation/verify_twca_chain_macos_readonly.sh \
  /tmp/ho600-tls-verified-TBJIkQ/ws.dgbas.gov.tw.leaf.pem

# Offline pure Python tests: no network, pip, or artifact_tool needed
python3 -m unittest discover -s research/cohort-inflation \
  -p 'test_fetch_taipei_age_2020_official_csv.py' -v
python3 -m unittest discover -s research/cohort-inflation \
  -p 'test_fetch_taipei_2020_report_pdf.py' -v

# Separate strictly HTTPS-verified government-origin options (run both, capture receipts)
python3 research/cohort-inflation/fetch_taipei_age_2020_official_csv.py \
  --out /tmp/ho600-taipei-2020-city-csv
python3 research/cohort-inflation/fetch_taipei_2020_report_pdf.py \
  --out /tmp/ho600-taipei-2020-city-pdf
```

If the original `/tmp/.../leaf.pem` was lost, first run [`diagnose_official_tls_readonly.sh`](./diagnose_official_tls_readonly.sh) to regenerate it without altering trust.

- If TLS chain verification fails, maintain source HOLD. No `-k`, `--insecure`, manual CA trust installation, `partial_chain`, host spoofing or disabling certificate validation.
- If a verified government PDF is obtained, inspect and visually audit **Table 8's 2020 household-head age rows, all 12 categories, and category sum vs actual total** before any regional proxy calculation. Respect regional scope; PDF might be a different vintage from modern Taipei CSV, require explicit version reconciliation.
- If a verified CSV is obtained, profile actual header and age/annual rows; 2020 must be ROC 109 or Gregorian 2020, separately from 2024+ 13-class scheme. Do not infer actual retirement from age.
- Do not call city data national or treat 2020 Taipei Table 8 as the 2026-02 corrected national source. WGT-01 remains HOLD absent corrected national raw files.
- Once two legitimate inputs are available, create distinct **`TPE_AGE_HEAD_*_PROXY` only** with dual-source value checks where scopes/versions truly match.
- Return actual HTTP/TLS results, original SHA/bytes, source period, exact source cell/page and individual category weights only if verified. Otherwise keep no-value HOLD.
- Update existing GitHub research-only receipt and Handoff on same branch, maintain `main` 181/600 / NOT SEALED / LOCKED and GitHub Actions disabled.

## Scope discipline

No new user approval required for read-only retrieval with strict TLS and existing trust roots, but any change to Mac trust store, network preferences, or CA installation **requires separate explicit user authorization**. Do not retry the same broken DGBAS URLs more than once until chain evidence changes. Do not contact TWCA/DGBAS without explicit user request.
