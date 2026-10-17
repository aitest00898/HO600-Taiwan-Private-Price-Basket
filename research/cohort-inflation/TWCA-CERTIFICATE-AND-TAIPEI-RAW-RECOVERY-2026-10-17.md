# WGT — Exact TWCA issuer certificates and Taipei 2020 raw-data safe recovery

**Record date:** 2026-10-17 (Taiwan). Branch: `research/batch-09`. **No formal source WGT gate has passed.**

## Important new discovery: exact official TWCA CA download URLs

The issuer reported by real on-Mac OpenSSL diagnostic for the October 2026 DGBAS leaf (`www.dgbas.gov.tw`, SAN includes both `ws.dgbas.gov.tw` and `www.stat.gov.tw`) is `TWCA SSL Certification Authority`. Leaf AIA references `Cyber_SSL_2023.crt`. This exact same certificate is listed in TWCA's **2026-04-15 new-chain official notice**:

- TWCA 2026-04-15: https://ssl.twca.com.tw/news_detail/ad2496ee-39cf-4d74-b44a-410470f99570
- **Official HTTPS TWCA SSL intermediate:** https://sslserver.twca.com.tw/cacert/Cyber_SSL_2023.crt
- **Official HTTPS TWCA CYBER cross-signed root:** https://sslserver.twca.com.tw/cacert/GlobalCrossCyber_2022.crt
- Official HTTPS TWCA Global Root: https://sslserver.twca.com.tw/cacert/global_root_2012.crt (reference only, **do not import or trust manually**)
- TWCA certificate repository: https://ssl.twca.com.tw/repository (SSL server CA archive; source includes a ZIP containing CA certificates)
- Official TWCA certificate information catalog identifies `TWCA SSL Certification Authority` under the CYBER Root (2023) with documented serial `400134b04f0000000000000003e324ac`; **this document identifies an expected CA, not its current key ID or actual leaf signature.**

Previous local receipt's DGBAS leaf AKI = `F2:28:D4:F9:D4:1C:7E:1A:6B:16:82:E5:EF:93:29:69:ED:CA:15:20`, and *none* of the three ePKI certificates actually presented by `ws.dgbas.gov.tw` have matching SKI. Separate `www.stat.gov.tw` sent only the leaf. TWCA control hostname `ssl.twca.com.tw` had complete verified chain. This supports server-delivered **wrong/missing CA intermediate**.

**Important caveat:** The official .crt binaries have NOT been downloaded or cryptographically inspected in this model environment because direct container DNS is unavailable and web PDF/certificate binary readers cannot expose PKIX raw bytes. The exact TWCA source URLs are now verified by its HTML notice; they **must** undergo real HTTPS / MAC system-anchor verification. Do not state that the live official website can already be accessed.

### Committed macOS-only certificate-chain evidence tool

[`verify_twca_chain_macos_readonly.sh`](./verify_twca_chain_macos_readonly.sh) performs:

1. Download only TWCA *official* intermediary files over full-verification HTTPS using `curl --ca-native`; parse **real X.509**, save SHA-256 for both.
2. Examine leaf SAN/issuer/AKI and intermediate SKI/issuer/AKI. Compare to the leaf from previously recorded local `openssl s_client` evidence.
3. Run `security verify-cert -c <leaf> -c <ssl-intermediate> -c <cross-root> -p ssl -n ws.dgbas.gov.tw -L` on macOS. Crucially `-c` **provides an untrusted chain**; **no `-r` trust override** is passed. macOS may accept it **only by chaining to a pre-existing trusted system anchor**; offline `-L` does not AIA-fetch another unknown CA. Cryptographic signature, hostname and certificate validity remain subject to native policy.
4. Even upon successful offline chain validation, follow with a **separate strict `curl --ca-native -I`** to DGBAS. It may still fail because the server has not corrected its presented chain; **offline valid chain ≠ accepted live HTTPS request, WGT-01 remains HOLD**.
5. Never import the CA into macOS trust stores, run `curl -k`, use `--insecure`, change DNS, spoof SNI, enable `partial_chain` or bypass TLS. If actual official files cannot be fetched over strictly verified transport, HOLD and preserve diagnostics.

Use:
```bash
bash research/cohort-inflation/verify_twca_chain_macos_readonly.sh \
  /tmp/ho600-tls-verified-TBJIkQ/ws.dgbas.gov.tw.leaf.pem
```
If prior temporary files are gone, collect a new public leaf through the existing **read-only** diagnostic script first.

## Parallel raw data retrieval via another legitimate government TLS host

DGBAS source may not be repaired promptly. Taiwan's official [open data catalog entry 133235](https://data.gov.tw/dataset/133235) and [Taipei government native dataset](https://data.taipei/dataset/detail?id=26c3817c-0713-4657-8cd8-aa842eb59f97) explicitly list **2012–2023 Taipei age-of-head household consumption** in historical 12 divisions, therefore covering **2020 / ROC 109**. The official resource UUID is `63e4d839-ef65-46a8-b4d1-1bbfeeca5516`.

Two observed official paths to **the same** file:

- Frontstage download from the government site's own clickable link: `https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=63e4d839-ef65-46a8-b4d1-1bbfeeca5516`.
- Legacy published official resource endpoint: `https://data.taipei/api/dataset/26c3817c-0713-4657-8cd8-aa842eb59f97/resource/63e4d839-ef65-46a8-b4d1-1bbfeeca5516/download`.

This is **one source** offered by two URL routes, not two independent confirmations.

[`fetch_taipei_age_2020_official_csv.py`](./fetch_taipei_age_2020_official_csv.py) fetches **only** these allowlisted official URLs with verified macOS native CA TLS, refuses unexpected redirect hosts/empty/HTML/JSON, checks real CSV columns (year, economic-head age, expenditures, medical care, etc.) and that ROC109/2020 rows are present, then records exact raw bytes, SHA-256, HTTPS final URL and UTC receipt under a new output directory. If requests fail, it outputs `NO_TRUSTED_OR_SCHEMA_VALID_OFFICIAL_CSV` without pretending raw bytes were obtained.

[11 synthetic fixture tests](./test_fetch_taipei_age_2020_official_csv.py) exercise scope, ROC date detection, legacy `cp950` decoding, signature-free HTML/JSON rejection, mislabelled/missing columns and partial data. These tests are committed but **not yet run on the user's Mac**. They do not prove official data quality or government source availability.

Run locally:
```bash
python3 -m unittest discover -s research/cohort-inflation -p 'test_fetch_taipei_age_2020_official_csv.py' -v
python3 research/cohort-inflation/fetch_taipei_age_2020_official_csv.py --out /tmp/ho600-taipei-2020-official
```

**Regional-only statistical scope:** `TAIPEI_CITY + HEAD_AGE` is not the whole Taiwan, not retired families by employment status, and not a direct replacement for `NAT20-AGE`. Do not add city proxy rows to `NAT20` or released index calculations. If raw city CSV arrives, **first profile the actual 2020 rows, headers, units and rounding, then create a separate city-level reviewed mapping** and a regional-only proxy; the current script deliberately stops after original file and schema proof. Do not silently infer national weights.

### 2024+ classification break

The Taipei historic 2012–2023 12-category scheme should not be spliced to its 2024+ file with 13 categories (e.g. insurance & financial services broken out) without a separately evidenced official classification bridge. This also applies to comparison with official national CPI consumption classification.

## Outcome and release gates

| Stream | Verified in this turn | Still missing |
| --- | --- | --- |
| TWCA | Official exact HTTPS CA source URLs and native Mac offline chain-verification procedure | Raw CA bytes, AKI/SKI signature verification on Mac, real DGBAS strict HTTPS GET |
| Taipei | Government metadata, historical span, 2020 included, resource UUID and two valid published URL patterns | Actual 2020 CSV bytes, SHA, parsed exact spending rows and source revisions |
| Python tests | 11 city fixture tests committed, no `artifact_tool` import | Execute fixture tests on user's Mac |
| National cohort | Prior 11/11 CSV test PASS and 2020 general household indexed checksum only | Original corrected 2020 age/occupation XLS and 0/2 proxy weights |
| Canonical HO600 | 181/600, Basket NOT SEALED, Index LOCKED | No promotion allowed |

**Result: new authenticated sourcing/verification route CREATED; not SUCCESSFULLY EXECUTED on user Mac.** No contacts with agencies initiated. No GitHub Actions, branch merges, canonical data writes or published inflation rates.

## Mac execution update — 2026-10-17

The read-only Mac verifier later retrieved both exact TWCA certificate files over strict HTTPS. The DGBAS leaf AKI matches `Cyber_SSL_2023.crt` SKI; `security verify-cert` validated the complete candidate chain to an existing macOS system anchor (exit 0). The separate strict live DGBAS HEAD still fails with curl 60, `unable to get local issuer certificate`, so the likely endpoint-delivered chain problem remains. No trust settings changed. See [`evidence/twca-macos-20261017/twca-chain-diagnostic.receipt.json`](./evidence/twca-macos-20261017/twca-chain-diagnostic.receipt.json).

The official Taipei CSV and report PDF were both retrieved and hash-preserved. PDF Table 8 and CSV match across 96 category cells and eight consumption totals. Seven age-of-household-head **Taipei-only expenditure proxy** vectors were generated and independently recomputed; the 65+ grouping is not retirement status. National WGT-01 remains HOLD. Full receipts and outputs: [`MAC-EXECUTION-RESULTS-2026-10-17.md`](./MAC-EXECUTION-RESULTS-2026-10-17.md).
