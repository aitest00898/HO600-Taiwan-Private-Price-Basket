#!/bin/bash
# HO600 TLS: Mac read-only chain recovery diagnosis. No Keychain or system CA changes.
# Usage: bash research/cohort-inflation/verify_twca_chain_macos_readonly.sh /tmp/ho600-tls-verified-*/ws.dgbas.gov.tw.leaf.pem
set -euo pipefail
if [ "$#" -ne 1 ] || [ ! -f "$1" ]; then
  echo "Usage: bash $0 /absolute/path/to/ws.dgbas.gov.tw.leaf.pem" >&2
  exit 64
fi
LEAF="$1"
OUT="$(mktemp -d /tmp/ho600-twca-untrusted-XXXXXX)"
umask 077
echo "EVIDENCE_DIR=$OUT"
echo "Do NOT import/install these files as trusted certificates."
urls=(
  "https://sslserver.twca.com.tw/cacert/Cyber_SSL_2023.crt"
  "https://sslserver.twca.com.tw/cacert/GlobalCrossCyber_2022.crt"
)
names=("TWCA_SSL_2023" "TWCA_GlobalCrossCyber_2022")
for i in 0 1; do
  URL="${urls[$i]}"
  DEST="$OUT/${names[$i]}.crt"
  echo "FETCH_VERIFIED_OFFICIAL_INTERMEDIATE=$URL"
  curl --ca-native --fail --silent --show-error --location \
     --proto '=https' --proto-redir '=https' --max-redirs 2 \
     --connect-timeout 10 --max-time 35 "$URL" -o "$DEST"
  [ -s "$DEST" ] || { echo "EMPTY_CERT" >&2; exit 65; }
  # Reject anything that is not a real X.509 certificate.
  if openssl x509 -inform DER -in "$DEST" -out "$OUT/${names[$i]}.pem" 2>/dev/null; then
    true
  elif openssl x509 -inform PEM -in "$DEST" -out "$OUT/${names[$i]}.pem" 2>/dev/null; then
    true
  else
    echo "INVALID_CERTIFICATE_FILE_OR_HTML: $URL" >&2; exit 65
  fi
  shasum -a 256 "$DEST"
  openssl x509 -in "$OUT/${names[$i]}.pem" -noout -subject -issuer -ext subjectKeyIdentifier -ext authorityKeyIdentifier
done
echo "LEAF_ORIGINAL_SHA256=$(shasum -a 256 "$LEAF" | awk '{print $1}')"
openssl x509 -in "$LEAF" -noout -subject -issuer -ext subjectAltName -ext authorityKeyIdentifier
echo "TRUST_EVALUATION: macOS system anchors only; candidates passed via -c, never as -r trust roots."
set +e
security verify-cert -c "$LEAF" -c "$OUT/TWCA_SSL_2023.pem" \
  -c "$OUT/TWCA_GlobalCrossCyber_2022.pem" \
  -p ssl -n ws.dgbas.gov.tw -L -v >"$OUT/security-verify.txt" 2>&1
RC=$?
set -e
cat "$OUT/security-verify.txt"
echo "SYSTEM_ANCHOR_SECURITY_VERIFY_EXIT=$RC"
if [ "$RC" -eq 0 ]; then
  echo "OFFLINE_FULL_CHAIN_VALIDATED_WITH_EXISTING_SYSTEM_ANCHOR"
  echo "NOT A WEB DOWNLOAD: official HTTP retrieval still requires its own strict HTTPS validation."
  set +e
  curl --ca-native --fail --silent --show-error -I --connect-timeout 10 --max-time 15 \
    "https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.xls" \
    >"$OUT/official-head.txt" 2>"$OUT/official-head.stderr"
  RC_CURL=$?
  set -e
  echo "STRICT_HTTP_HEAD_EXIT=$RC_CURL"
  if [ "$RC_CURL" -eq 0 ]; then echo "STRICT_HEAD_SUCCEEDED_CHECK_ACTUAL_GET_SEPARATELY"; else echo "ORIGINAL_OFFICIAL_TLS_STILL_BLOCKED"; fi
else
  echo "NO_VALIDATED_COMPLETE_CHAIN_DO_NOT_PROCEED_TO_ORIGINAL_FILE_FETCH"
fi
echo "No system trust/keychain settings were changed."
