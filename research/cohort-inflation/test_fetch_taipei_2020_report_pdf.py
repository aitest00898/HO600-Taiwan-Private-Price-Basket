#!/usr/bin/env python3
"""Offline synthetic file-signature/HTML/truncation tests: NOT official PDF verification."""
import importlib.util
from pathlib import Path
import unittest

root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("pdfsrc",root/"fetch_taipei_2020_report_pdf.py")
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

class TaipeiPDFTests(unittest.TestCase):
    def test_accept_minimal_signature_fixture(self):
        mod.validate_pdf_bytes(b"%PDF-1.7\nfixture\n%%EOF\n")
    def test_reject_empty(self):
        with self.assertRaisesRegex(ValueError,"Empty"):
            mod.validate_pdf_bytes(b"")
    def test_reject_html(self):
        with self.assertRaisesRegex(ValueError,"NOT_PDF"):
            mod.validate_pdf_bytes(b"<html>Error 403</html>")
    def test_reject_json(self):
        with self.assertRaisesRegex(ValueError,"NOT_PDF"):
            mod.validate_pdf_bytes(b'{"error":"not available"}')
    def test_reject_truncated(self):
        with self.assertRaisesRegex(ValueError,"TRUNCATED"):
            mod.validate_pdf_bytes(b"%PDF-1.7\nfixture with no eof")
    def test_reject_size(self):
        with self.assertRaisesRegex(ValueError,"oversized"):
            mod.validate_pdf_bytes(b"%PDF-1.7"+b"x"*(mod.MAX_SIZE+1))
    def test_correct_official_host(self):
        self.assertTrue(mod.PDF_URL.startswith("https://www-ws.gov.taipei/Download.ashx?"))
        self.assertIn("8471417", __import__('base64').b64decode(mod.PDF_URL.split("u=")[1]).decode())

if __name__=="__main__":
    unittest.main()
