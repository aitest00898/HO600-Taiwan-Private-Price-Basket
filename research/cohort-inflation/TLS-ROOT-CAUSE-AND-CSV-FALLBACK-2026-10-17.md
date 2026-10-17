# WGT-01 TLS issuer-chain diagnosis and no-artifact_tool fallback — 2026-10-17

**Scope:** research only, branch `research/batch-09`. **Not a WGT gate PASS.** Do not touch trust stores, `main`, HO600 canonical workbook/index or GitHub Actions.

## Observed facts from local Codex receipts

Source: [WGT-2026-10-17-acceptance-report.md](./WGT-2026-10-17-acceptance-report.md) and [wgt-2026-10-17-source-receipt.json](./wgt-2026-10-17-source-receipt.json) at preceding remote HEAD `1d8662d94157153c92a88b20c19b898ce7b5bf0f`.

- Sandbox-elevated DNS succeeded for `ws.dgbas.gov.tw` → 223.200.181.106, and `www.stat.gov.tw` → Cloudflare IPs. Initial DNS error resolved.
- `curl` HTTPS default strict verification and `--ca-native` failed `unable to get local issuer certificate`, 0 HTTP payload bytes, 0 source files.
- `openssl s_client` verify code **20**, local receipt identified server leaf subject `CN=www.dgbas.gov.tw`, issuer `TWCA SSL Certification Authority`, 2026-10-07 through 2027-04-23; other served chain certificates were described as ePKI/Government Server Digital Certificate Center rather than the issuer chain for TWCA leaf.
- The leaf's **subject CN does not by itself prove hostname mismatch**; SAN extension MUST be checked for `ws.dgbas.gov.tw`. The remote ePKI/TWCA chain mismatch is strong evidence of missing/wrong intermediate but is not proof the Mac trust store is functioning correctly for unrelated sites.
- Safari warned of an untrusted official website. Do not bypass, download with `curl -k`, use unverified CA packages or install system roots.
- No proxy *environment variables* found is not proof no system VPN, transparent proxy, outbound TLS interception or MDM certificate setting exists.

## Independent official CA background

On **2026-04-15**, TWCA announced TLS hierarchy updates effective **2026-05-04**, to include TWCA Global Root CA → TWCA CYBER Root CA → TWCA SSL CA → leaf. TWCA also explicitly noted potential Apple/iOS/macOS trust warnings for some Microsoft IIS deployments:

https://ssl.twca.com.tw/news_detail/ad2496ee-39cf-4d74-b44a-410470f99570

**This does not verify that DGBAS uses IIS or that its live leaf is properly chained.** The DGBAS leaf issuer seen in the local receipt is `TWCA SSL Certification Authority`; do not assume the similarly named CA at the TWCA announcement is the exact same key. Match issuer Distinguished Name + Authority Key Identifier to the candidate issuer Subject + Subject Key Identifier, validate cryptographic signatures and chain to a trusted root, and check SAN before accepting any proposed intermediate or alternative official URL.

## Precise next diagnostic, read-only only

Run the committed [`diagnose_official_tls_readonly.sh`](./diagnose_official_tls_readonly.sh) **on the user's Mac**, normal access or already approved elevated network if necessary. The script runs 3 SNI/hostname-verified OpenSSL handshakes, saves only public presented leaf certificates + diagnostic text under a fresh `/tmp/ho600-tls-verified-*` path. No content files, credential use or system trust change.

Compare:
1. `ws.dgbas.gov.tw`: supplied chain, leaf issuer, SAN, AIA and `Verify return code`.
2. `www.stat.gov.tw`: independent official page, identify if it also fails and which certificate issuer it presents.
3. `ssl.twca.com.tw`: CA provider official control website, whether normal strict TLS succeeds on same Mac.

Interpret in this order:

- Control site succeeds while `ws.dgbas.gov.tw` fails with incorrect/missing chain → **likely DGBAS server-side delivery problem**; pursue official authenticated alternative hostname/file service or await proper issuer chain. Do not mutate Mac-wide roots.
- All three unrelated certificate authorities fail → investigate Mac time, native Keychain trust status, managed VPN/MDM HTTPS inspection and company proxy, without changing settings. **Authorization required before any CA trust store alteration**.
- SAN does not include `ws.dgbas.gov.tw` → a missing intermediate CA alone cannot fix wrong hostname. Stop rather than use another hostname to an unverified IP.
- Chain/hostname both verify but only `curl` or Python fails → compare the exact CA bundles and TLS backends of the tool to the native verified chain, bounded per-process fixes only after independent verification, no system-wide installation.
- Alternate source route must be genuinely listed by `stat.gov.tw` or another official provider, and independently HTTPS-verified. Do not fabricate host remapping, use plain HTTP, mirror from unverified third party or manipulate DNS/SNI.

Report result `TLS_ROOT_CAUSE_CONFIRMED`, `TLS_ROOT_CAUSE_LIKELY`, or `UNKNOWN` based on collected evidence. Preserve raw `s_client` diagnostics privately; SHA receipts of cert DER if useful but never present a cert fingerprint as proof of legitimate chain by itself.

## Separate dependency blocker: `artifact_tool` missing

The original XLSX extractor and its seven synthetic tests remain unavailable on local Python because neither Python 3.14 nor 3.12 includes `artifact_tool`; **do not claim those tests passed**.

A new parallel **standard-library-only** route avoids importing that package, without relaxing the source/authenticity gates:

1. Only **after** official `NAT20-AGE` and `NAT20-OCC` XLS/ODS sources pass normal strict HTTPS verification, save original files and URL+UTC+SHA download receipts using [`fetch_official_weight_tables.py`](./fetch_official_weight_tables.py).
2. Open original in Numbers and select the actual official worksheet. Export that worksheet to CSV preserving all 12 category rows and directly labelled total. **Record source sheet name, group column, original SHA and CSV SHA**. Manually compare all 12 labels and amounts against on-screen official table. CSV is a conversion, not a second independent source.
3. Review [`cohort-weight-mapping.template.json`](./cohort-weight-mapping.template.json) for the original XLSX route; the CSV route requires a *separate exact-field mapping* documented below. Keep mapping file outside repository and populate positions **1-based**; do not infer demographic column.
4. Execute `python3 research/cohort-inflation/extract_revised_2020_cohort_csv.py --original /path/original.xls --csv /path/Numbers-export.csv --mapping /path/reviewed-csv-mapping.json --out /tmp/ho600-cohort-csv-qc`.
5. Tests: `python3 -m unittest discover -s research/cohort-inflation -p 'test_extract_revised_2020_cohort_csv.py'` require **only Python stdlib**; note they are synthetic and cannot validate real source provenance.
6. For genuine data, independently compare all 12 source-cell amounts, nonnegative figures, and total within declared rounding tolerance (max 12 TWD); no final index or actual employment/retirement cohort inferred from head-occupation or age proxies. **Index still LOCKED.**

CSV mapping exact keys:
`source_id, source_url, reference_year=2020, cohort_code=AGE_HEAD_*_PROXY or OCC_HEAD_*_PROXY, source_sheet, numbers_export_confirmed=true, manual_reviewed=true, original_sha256, csv_sha256, label_column, amount_column, category_rows (keys 01..12), total_row, total_label_column, total_tolerance_twd`. All row/column positions are positive 1-based integers. Empty placeholders or a modified original/CSV cause HOLD.

## Next gate decision table

| Gate | As-of latest accepted Codex report | Change in this research increment |
| --- | --- | --- |
| WGT-01 Official source | HOLD_TLS_CERTIFICATE_BLOCKED, 0 bytes | Read-only TLS root-cause protocol documented; raw bytes still 0 |
| WGT-02 Revised version | PARTIAL_METADATA_ONLY | No binary version evidence |
| WGT-03 XLS/CSV parsing | HOLD | New stdlib Numbers CSV path added; not yet exercised with government files |
| WGT-04 Cohort category totals | HOLD | Unchanged (only general-household indexed excerpt arithmetic PASS) |
| WGT-05 Proxy weights | HOLD 0/2 | No fabricated cohort shares |
| Extraction unit tests | XLSX tests BLOCKED | 11 new independent stdlib fixture cases committed, pending local execution |
| Canonical HO600 | 181/600; NOT SEALED; LOCKED | Unchanged |
| GitHub Actions | Paused | No Actions scheduled or invoked |

**Outcome: PATH_TO_RECOVERY_SPECIFIED, RAW_TLS_BLOCKER_STILL_OPEN.** Do not mark either network or actual cohort weights as resolved.
