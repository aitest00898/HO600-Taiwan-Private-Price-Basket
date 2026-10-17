# DGBAS TLS chain diagnosis — 2026-10-17

**Classification:** `TLS_ROOT_CAUSE_LIKELY` — the DGBAS endpoints presented a mismatched/incomplete certificate chain. The chain observed on the wire is the likely cause; transparent network interception cannot be ruled out absolutely. **WGT-01 remains HOLD.**

**Branch and base:** `research/batch-09`, `7d87ef5d7ba05ba7f932f41c58642176daba637a`. `git pull --ff-only` returned `Already up to date.` The checkout was clean before this follow-up.

**Execution:** `diagnose_official_tls_readonly.sh` ran at approximately `2026-10-17T08:01:28Z` using the normal local network with sandbox network permission. It used `openssl s_client -servername`, `-verify_hostname`, `-verify_return_error`, and `-showcerts`. No TLS validation was disabled. Raw handshakes and public certificate PEMs remain in `/tmp/ho600-tls-verified-TBJIkQ/`; they are not committed.

## Host comparison

| Host | Strict OpenSSL | Sent chain | Certificate result |
|---|---|---|---|
| `ws.dgbas.gov.tw` | Exit 1; verify code 20, `unable to get local issuer certificate` | 4 certificates: leaf plus three ePKI hierarchy certificates | Leaf SAN includes `ws.dgbas.gov.tw`; issuer is TWCA SSL CA, but leaf AKI does not match any sent certificate SKI. |
| `www.stat.gov.tw` | Exit 1; verify code 20, `unable to get local issuer certificate` | 1 certificate: leaf only | Same exact leaf DER fingerprint as `ws.dgbas.gov.tw`; SAN includes `www.stat.gov.tw`; no intermediate was sent. |
| `ssl.twca.com.tw` | Exit 0; verify code 0, `ok` | 3 certificates | Leaf SAN includes `ssl.twca.com.tw`; issuer/intermediate/root key identifiers link; native-trust `curl --ca-native` HEAD returned HTTP 200. |

The DGBAS leaf subject is `C=TW, L=臺灣, O=政府機關-行政院-主計總處, CN=www.dgbas.gov.tw`; issuer is `C=TW, O=TAIWAN-CA, OU=SSL Sub-CA, CN=TWCA SSL Certification Authority`. It is valid from `2026-10-07 08:58:01 UTC` through `2027-04-23 15:59:59 UTC`, serial `47EA000000097FEE414E3A40397BCE7C`, SHA-256 fingerprint `EE:7E:1A:71:1E:07:72:C8:54:A4:05:4E:CE:EF:69:75:BF:83:0F:8D:84:7B:C7:E9:5E:93:F1:EC:6F:1F:FB:E3`.

The SAN contains `www.dgbas.gov.tw`, `eng.dgbas.gov.tw`, `www.stat.gov.tw`, `eng.stat.gov.tw`, `ia.dgbas.gov.tw`, `ebook.dgbas.gov.tw`, `ws.dgbas.gov.tw`, and `ebasnew.dgbas.gov.tw`; this is not a hostname mismatch. Leaf AKI is `F2:28:D4:F9:D4:1C:7E:1A:6B:16:82:E5:EF:93:29:69:ED:CA:15:20`. The three certificates after the leaf on the `ws` connection were:

- `ePKI Root Certification Authority - G2`, SKI `72:5B:BA:AA:72:38:EE:25:90:24:B5:94:22:FA:09:88:CA:8B:0A:FB`;
- `政府伺服器數位憑證管理中心 - G1`, SKI `D6:EB:2D:9D:61:FE:2B:BB:70:88:2E:B8:07:B1:59:B0:F4:83:22:6A`;
- `ePKI Root Certification Authority`, SKI `1E:0C:F7:B6:67:F2:E1:92:26:09:45:C0:55:39:2E:77:3F:42:4A:A2`.

None has the DGBAS leaf AKI, and none is the leaf's declared TWCA SSL CA issuer. The leaf AIA names `http://sslserver.twca.com.tw/cacert/Cyber_SSL_2023.crt`; that HTTP URL was not fetched. No candidate CA was downloaded or trusted. By comparison, the TWCA control leaf AKI matches the sent Global EVSSL intermediate SKI, whose AKI matches the next sent certificate SKI.

## Attribution and limits

`curl --ca-native` passed to the TWCA control site and failed to both official endpoints with error 60, HTTP 000. The system proxy dictionary was empty and no proxy environment variables were present. This makes a general local CA-store failure less likely and supports a server-side chain-delivery problem. It does not prove the origin server, rather than a transparent network device or managed TLS inspection layer, supplied the mismatched chain. No Mac trust settings, DNS, network settings, or Safari state were changed.

No official XLS/ODS URL passed strict TLS, so no source file was downloaded in this follow-up. Existing receipts show the four source links had also returned HTTP 000 under strict verification. The raw-source cache remains empty; original and Numbers-converted file SHA-256 values do not exist. No Numbers conversion, XLSX inspection, or proxy extraction was performed.

## CSV fallback tests and arithmetic

The first run collected 11 tests but exposed a parser defect: `positive_number(0)` treated numeric zero as empty because of `value or ""`. The parser now distinguishes `None` from numeric zero. The independent standard-library command then passed all **11/11** synthetic tests under Python `3.14.5`; `artifact_tool` is unavailable and is not imported or needed by this CSV test path.

The existing indexed general-household excerpt independently rechecked as 12 distinct categories (01–12), zero negative amounts, category sum and declared total both `815,100` TWD/household/year, and stored percentages totaling `99.999999%`. Its evidence remains `OFFICIAL_PDF_SEARCH_INDEXED_DUAL_TABLE;RAW_BYTES_UNVERIFIED`, scope `ALL_HOUSEHOLDS_GENERAL`; this is arithmetic-only and **not** WGT-04 source acceptance or a cohort proxy.

## Gate status and next step

- **WGT-01:** `HOLD_TLS_CERTIFICATE_BLOCKED`; no authenticated original bytes.
- **WGT-02:** `PARTIAL_METADATA_ONLY`; landing-page revision note does not authenticate the binary file version.
- **WGT-03:** `HOLD`; no Numbers XLSX/CSV exported from a real source and no actual sheet/row mapping reviewed.
- **WGT-04:** `HOLD`; the 12-row calculation above is only the unverified all-household excerpt.
- **WGT-05:** `HOLD, 0/2`; no occupation-head or age-head proxy weights. Neither proxy represents all workers or actual retirees.

Next step: ask DGBAS/TWCA or a trusted network operator to correct or confirm the presented chain, then rerun strict verification. If chain repair requires a local CA trust change, stop for explicit authorization. Do not use the HTTP AIA, bypass Safari, download via TLS bypass, publish cohort inflation, modify `main`, run Actions, alter the canonical workbook, seal Basket, or unlock Index.
