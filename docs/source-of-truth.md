# Source of Truth

Formal status is determined in this order:

1. Latest validated canonical workbook committed to `main`.
2. `canonical/status.json` and `Validation_Release` that agree with that workbook.
3. CSV snapshots exported from the same workbook.
4. Research branch notes and issue trackers.
5. Chat messages and verbal progress.

A search result, evidence lead, internal checkpoint, or in-memory workbook edit is **not** formal progress.

A batch is formal only after:

1. workbook update completed;
2. `.xlsx` export succeeded;
3. exported workbook was re-imported successfully;
4. active sheet architecture checked;
5. Candidate_Pool price blindness checked;
6. key ranges inspected;
7. formula-error scan passed;
8. quota and evidence counts reconciled;
9. Exact count reconciled;
10. concentration rules checked;
11. Basket remains correctly sealed/unsealed;
12. Index lock state checked;
13. SHA-256 recorded;
14. validated state merged to `main`.
