#!/usr/bin/env python3
"""Regenerate dashboard/snapshot.js from reviewed dashboard/snapshot.json (offline).
No GitHub data reads, no secrets, no branch writes. --check is non-mutating.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

DASHBOARD=Path(__file__).resolve().parents[1]
SOURCE=DASHBOARD/"snapshot.json"
TARGET=DASHBOARD/"snapshot.js"
PREFIX="/* Pin: see snapshot.json for source SHAs and provenance. No network or user token access. */\nwindow.HO600_SNAPSHOT = "

def create() -> str:
    document=json.loads(SOURCE.read_text(encoding="utf-8"))
    if document.get("schemaVersion")!="1.0.0":
        raise ValueError("Unsupported snapshot schema")
    if document["canonical"]["indexStatus"]!="LOCKED" or document["canonical"]["basketSealed"]:
        raise ValueError("Refuse generating a sealed or unlocked preview")
    if document["cohort"]["fullCohortRatesReleased"] != 0:
        raise ValueError("Refuse generating unapproved full cohort CPI")
    encoded=json.dumps(document,ensure_ascii=False,separators=(",",":"),allow_nan=False)
    return PREFIX+encoded.replace("</script","<\\/script").replace("\u2028"," ").replace("\u2029"," ")+";\n"

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--check",action="store_true")
    args=p.parse_args()
    data=create()
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding="utf-8")!=data:
            raise SystemExit("SNAPSHOT_MISMATCH: run script without --check and retest")
        print("SNAPSHOT_SYNC=PASS")
    else:
        TARGET.write_text(data,encoding="utf-8")
        print("SNAPSHOT_REBUILT=PASS; requires normal review before commit")

if __name__=="__main__":
    main()
