#!/usr/bin/env python3
"""HO600 task snapshot read-only verifier. No network, no Actions, no writes.

Run from any working directory:
  python3 dashboard/tools/check_todo_snapshot.py
  python3 dashboard/tools/check_todo_snapshot.py --linear-export /path/to/fresh-linear-export.json

The optional export must be a fresh user-provided JSON array or {"issues": [...]}
containing id, status (Todo / Backlog / In Progress / Done), priority.value, and url.
Without it, we can assert only internal GitHub snapshot consistency; we CANNOT
claim that Linear has not changed since the pinned snapshot was created.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DASH = ROOT / "dashboard"
CSV = ROOT / "research/todo/HO600-TODO-2026-10-20.csv"

def fail(msg):
    raise RuntimeError("TODO_DRIFT_OR_INTEGRITY_FAILURE: " + msg)

def state(value):
    values={"Todo":"TODO","Backlog":"BACKLOG","In Progress":"IN_PROGRESS","Done":"DONE",
            "TODO":"TODO","BACKLOG":"BACKLOG","IN_PROGRESS":"IN_PROGRESS","DONE":"DONE"}
    if value not in values: fail("unknown state " + str(value))
    return values[value]

def check(fresh_path=None):
    snap = json.loads((DASH/"todo-snapshot.json").read_text(encoding="utf-8"))
    js=(DASH/"todo-snapshot.js").read_text(encoding="utf-8")
    prefix="window.HO600_TODO_SNAPSHOT = "
    if prefix not in js: fail("missing offline JS wrapper")
    try:
        embedded=json.loads(js.split(prefix,1)[1].strip().removesuffix(";"))
    except ValueError as exc:
        fail("invalid JS snapshot: " + str(exc))
    if snap != embedded: fail("JSON/JS source mismatch")
    if snap.get("schemaVersion")!="1.0.0": fail("unsupported schema")
    if snap["authority"]["refresh"]!="EXPLICIT_MANUAL_ONLY_NO_ACTIONS": fail("unauthorized refresh")
    tasks = snap["tasks"]
    if len(tasks)!=42: fail("expected 42 pinned HO600 tasks")
    ids={t["id"] for t in tasks}
    if len(ids)!=len(tasks): fail("duplicate Linear issue IDs")
    for t in tasks:
        if t["status"] not in ("TODO","BACKLOG","IN_PROGRESS","DONE"): fail("invalid task state")
        if not t["linearUrl"].startswith("https://linear.app/001dev/issue/"): fail("wrong project URL")
        if not set(t["blockedBy"]).issubset(ids): fail("cross-project or unknown dependencies")
        if not t["acceptance"]: fail("missing acceptance criteria")
    summary=snap["summary"]
    observed={
        "todo":sum(t["status"]=="TODO" for t in tasks),
        "backlog":sum(t["status"]=="BACKLOG" for t in tasks),
        "inProgress":sum(t["status"]=="IN_PROGRESS" for t in tasks),
        "done":sum(t["status"]=="DONE" for t in tasks),
        "p0":sum(t["priority"]=="P0" for t in tasks),
        "p1":sum(t["priority"]=="P1" for t in tasks),
        "p2":sum(t["priority"]=="P2" for t in tasks),
        "blockedByCount":sum(bool(t["blockedBy"]) for t in tasks),
        "relations":sum(len(t["blockedBy"]) for t in tasks)}
    if observed!=summary: fail("summary mismatch")

    raw=CSV.read_bytes()
    git_blob_sha=hashlib.sha1(b"blob "+str(len(raw)).encode("ascii")+b"\x00"+raw).hexdigest()
    if git_blob_sha!=snap["authority"]["githubTaskCsvBlobSha"]:
        fail("pinned Git blob SHA mismatch: reviewed TODO CSV changed")
    with CSV.open(newline="",encoding="utf-8-sig") as f:
        records=list(csv.DictReader(f))
    if len(records)!=len(tasks): fail("GitHub TODO CSV row count drift")
    by_id={x["linear_id"]:x for x in records}
    if set(by_id)!=ids: fail("CSV Linear IDs drift")
    for t in tasks:
        x=by_id[t["id"]]
        for prop,field in (("todoId","todo_id"),("priority","priority"),
                           ("group","group"),("status","status"),("title","title"),
                           ("linearUrl","linear_url"),("acceptance","acceptance_criteria"),
                           ("sourceUrl","source_url")):
            if t[prop]!=x[field]: fail("CSV "+t["id"]+" "+prop+" drift")
        if t["blockedBy"]!=[v for v in x["blocked_by_linear_ids"].split(";") if v]:
            fail("dependency drift "+t["id"])
    if fresh_path is None:
        print("LOCAL_SNAPSHOT=PASS; LIVE_LINEAR_DRIFT=UNVERIFIED_NO_EXPORT")
        print("TASKS=42 TODO={todo} BACKLOG={backlog} IN_PROGRESS={inProgress} DONE={done}".format(**observed))
        return
    live=json.loads(Path(fresh_path).read_text(encoding="utf-8"))
    if isinstance(live,dict): live=live.get("issues")
    if not isinstance(live,list): fail("export must be an issues list")
    if len(live)!=42 or {x["id"] for x in live}!=ids:
        fail("current Linear issues or project membership differ from snapshot")
    for x in live:
        t=next(v for v in tasks if v["id"]==x["id"])
        p=x.get("priority")
        p=p.get("value") if isinstance(p,dict) else p
        if p is None or "P"+str(p-1)!=t["priority"]: fail("priority drift "+t["id"])
        if state(x.get("status"))!=t["status"]: fail("state drift "+t["id"])
        if x.get("url")!=t["linearUrl"]: fail("issue URL drift "+t["id"])
    print("LOCAL_SNAPSHOT=PASS; PROVIDED_LINEAR_EXPORT_DRIFT=NONE")
    print("TASKS=42 TODO={todo} BACKLOG={backlog} IN_PROGRESS={inProgress} DONE={done}".format(**observed))

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--linear-export",type=Path)
    args=parser.parse_args()
    try: check(args.linear_export)
    except (RuntimeError,KeyError,IndexError,TypeError,ValueError,OSError) as exc:
        print(str(exc),file=sys.stderr)
        raise SystemExit(1)
