#!/usr/bin/env python3
"""Authenticated Taipei official CPI *raw-data capture*; NO CPI rate calculation.

Registered resource IDs are obtained from clickable data.taipei / data.gov.tw
official metadata. Uses strict curl --ca-native; no TLS bypass, system CA changes,
GitHub Actions or dependency on artifact_tool. Results stay research-only.
"""
from __future__ import annotations
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import urlsplit

URLS={
    "TPE-CPI-BASIC-MONTH":
        "https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=4a4ea957-c620-4056-89bb-50c7a4bd7325",
    "TPE-CPI-BASIC-YEAR":
        "https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=3e6ed9d0-0e86-4d99-8047-2fa68fb4ec90",
}
# The annual and monthly data are one source each. Alternative official URL
# routes are transport fallbacks, NOT independently observed confirmation.
ALTERNATE_URLS={
    "TPE-CPI-BASIC-MONTH": "https://data.taipei/api/dataset/f47d7930-c507-4b5d-9ad3-907746a28342/resource/4a4ea957-c620-4056-89bb-50c7a4bd7325/download",
}
MAX_BYTES=15_000_000

def decode_table(data: bytes, source: str) -> dict:
    if not data or len(data)>MAX_BYTES:
        raise ValueError("Empty or too-large CPI response")
    if data[:40].lstrip().lower().startswith((b"<html",b"<!doctype html",b"{",b"<xml")):
        raise ValueError("Official endpoint returned HTML/JSON/XML instead of CSV")
    errors=[]
    for enc in ("utf-8-sig","cp950"):
        try:
            text=data.decode(enc)
            rows=list(csv.reader(io.StringIO(text)))
            if len(rows)<2: raise ValueError("No data rows")
            header=rows[0]
            if not (4<=len(header)<=60) or len(set(header))!=len(header):
                raise ValueError("Unexpected or duplicate headings")
            # Official open-data catalog documents both historical "年月別"/"年別"
            # and updated "統計期" headers. Either is valid after checking grain.
            time_aliases=("年月別","統計期") if source.endswith("MONTH") else ("年別","統計期")
            period_columns=[i for i,h in enumerate(header) if h.strip() in time_aliases]
            class_columns=[i for i,h in enumerate(header) if h.strip()=="基本分類"]
            value_columns=[i for i,h in enumerate(header) if "原始值" in h]
            if len(period_columns)!=1 or len(class_columns)!=1 or len(value_columns)!=1:
                raise ValueError(f"Missing or ambiguous required CPI columns: time={period_columns}, class={class_columns}, value={value_columns}")
            if any(len(r)!=len(header) for r in rows[1:] if any(x.strip() for x in r)):
                raise ValueError("Nonrectangular CPI table; inspect actual delimiter/format")
            kyear=period_columns[0]
            kcategory=class_columns[0]
            kval=value_columns[0]
            observed=[r for r in rows[1:] if any(x.strip() for x in r)]
            if len(observed)<5:
                raise ValueError("Too few observations for historical price series")
            keys=[(r[kyear].strip(),r[kcategory].strip()) for r in observed]
            if len(keys)!=len(set(keys)):
                raise ValueError("Duplicate (period,classification) observation; require review")
            if not all(r[kyear].strip() and r[kcategory].strip() for r in observed):
                raise ValueError("Missing time or class labels")
            def has_y(v,year):
                val=v.strip()
                for prefix in (str(year),str(year-1911)):
                    if val==prefix or any(val.startswith(prefix+sep) for sep in ("年","/","-","."," ")):
                        return True
                    if len(val)==len(prefix)+2 and val.startswith(prefix) and val[-2:].isdigit():
                        month=int(val[-2:])
                        if 1<=month<=12:
                            return True
                return False
            observed2020=sum(has_y(r[kyear],2020) for r in observed)
            observed2026=sum(has_y(r[kyear],2026) for r in observed)
            if observed2020==0:
                raise ValueError("No recognizable 2020/ROC109 CPI records; cannot build baseline")
            return {"file_encoding":enc,"total_data_rows":len(observed),
              "columns":len(header),"date_field":header[kyear],
              "class_field":header[kcategory],"index_field":header[kval],
              "distinct_class_labels":len(set(r[kcategory] for r in observed)),
              "period_2020_rows":observed2020,"period_2026_rows":observed2026,
              "has_2026_data":bool(observed2026),
              "numeric_cpi_cells_verified":False,
              "all_12_spending_categories_mapped":False,
              "2020_to_2026_rebased":False,
              "published_inflation_rate":False}
        except (UnicodeError,ValueError,csv.Error) as exc:
            errors.append(f"{enc}: {exc}")
    raise ValueError("CPI CSV schema/HISTORICAL years validation failed: "+"; ".join(errors))

def fetch(source: str,out:Path)->dict:
    if source not in URLS:
        raise ValueError("Unknown/unauthorized official CPI resource")
    if out.exists() and any(out.iterdir()):
        raise FileExistsError("Use a new empty output directory; no overwrite")
    with tempfile.TemporaryDirectory(prefix="ho600-cpi-") as tmp:
        payload=Path(tmp)/"resource.tmp"
        cmd=["curl","--ca-native","--fail","--silent","--show-error","--location",
            "--proto","=https","--proto-redir","=https","--max-redirs","2",
            "--connect-timeout","12","--max-time","60","--max-filesize",str(MAX_BYTES),
            "--output",str(payload),"--write-out",
            "%{url_effective}\n%{http_code}\n%{content_type}\n",URLS[source]]
        result=subprocess.run(cmd,text=True,capture_output=True,timeout=70,check=False)
        if result.returncode!=0:
            raise RuntimeError(f"Strict HTTPS fetch failed curl {result.returncode}: {result.stderr[:300]}")
        fields=result.stdout.strip().splitlines()
        if len(fields)!=3 or fields[1]!="200":
            raise ValueError("No verifiable official HTTP 200 response")
        parsed=urlsplit(fields[0])
        if parsed.scheme!="https" or parsed.hostname!="data.taipei":
            raise ValueError("Redirect to unregistered host")
        blob=payload.read_bytes()
        profile=decode_table(blob,source)
        out.mkdir(parents=True,exist_ok=True)
        raw=out/(source+"-official-original.csv")
        rec=out/(source+"-receipt.json")
        if raw.exists() or rec.exists():
            raise FileExistsError("Original or receipt exists: no overwrite")
        raw.write_bytes(blob)
        record={
            "source_id":source,"status":"RAW_CPI_RETRIEVED_PROFILED_NOT_MAPPED_OR_REBASED",
            "requested":URLS[source],"final_url":fields[0],
            "content_type":fields[2],"http_code":200,
            "retrieved_utc":datetime.now(timezone.utc).isoformat(),
            "raw_bytes":len(blob),"sha256":hashlib.sha256(blob).hexdigest(),
            "scope":"TAIPEI_CITY_NOT_NATIONAL",
            "survey_weight_base":"Taipei 2020 household-head-age official survey",
            "raw_cpi_profile":profile,
            "no_index_or_inflation_rate_generated":True
        }
        rec.write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        return record

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",required=True,choices=tuple(URLS))
    p.add_argument("--out",required=True,type=Path)
    args=p.parse_args()
    print(json.dumps(fetch(args.source,args.out),indent=2,ensure_ascii=False))
if __name__=="__main__":
    main()
