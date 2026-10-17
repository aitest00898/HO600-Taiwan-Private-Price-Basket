#!/bin/bash
# Read-only TLS verification diagnosis; no CA installation or SSL bypass.
set -u
OUT="$(mktemp -d /tmp/ho600-tls-verified-XXXXXX)"
echo "TLS_DIAGNOSTIC_OUTPUT=$OUT"
for HOST in ws.dgbas.gov.tw www.stat.gov.tw ssl.twca.com.tw; do
  LOG="$OUT/$HOST.handshake.txt"
  PEM="$OUT/$HOST.leaf.pem"
  echo "HOST=$HOST"
  openssl s_client -connect "$HOST:443" -servername "$HOST" \
    -verify_hostname "$HOST" -verify_return_error -showcerts \
    </dev/null >"$LOG" 2>&1
  RC=$?
  awk '/-----BEGIN CERTIFICATE-----/{p=1} p{print} /-----END CERTIFICATE-----/{exit}' "$LOG" >"$PEM"
  echo "OPENSSL_EXIT=$RC"
  grep -E 'Verify return code:|verify error:|Verification error:' "$LOG" | tail -n 5 || true
  if [ -s "$PEM" ]; then
    openssl x509 -in "$PEM" -noout -subject -issuer -dates 2>&1 || true
    openssl x509 -in "$PEM" -noout -ext subjectAltName 2>&1 || true
    openssl x509 -in "$PEM" -noout -ext authorityInfoAccess 2>&1 || true
  else
    echo "NO_LEAF_PRESENT"
  fi
done
echo "DIAG_ONLY: compare SAN, issuer/intermediate, official vs control host."
echo "Do not install CA, bypass SSL or treat DNS resolution as TLS PASS."
