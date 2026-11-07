# Research Workflow

## Candidate order

1. Upgrade existing `RESEARCHABLE-CURRENT-ONLY` concepts by finding Exact-2020 evidence.
2. Only when an existing candidate cannot be cleanly upgraded, add a brand-new concept in a genuine structural shortfall cell.

## Priority domains

Current structural priorities are clothing, home/household, transport, education, and daily/personal. Food work should focus on underfilled supermarket/home-cooking, packaged food/drink, snacks/desserts, and convenience-ready-food cells rather than already saturated restaurant/coffee surfaces.

## Internal checkpoints

Every ~20–25 admissible concepts, run internal QC for:

- Evidence Gate;
- duplicate economic concepts;
- brand / merchant concentration;
- source concentration;
- product-family concentration;
- quota balance;
- identity/spec/channel fidelity.

Internal QC does not update canonical progress or force an export.

## Batch close

A large batch normally closes around +75–100 high-quality Exact concepts, or earlier/later when marginal evidence yield clearly justifies it. Do not lower admission thresholds to hit a target count.

## Exact-first continuation (2026-11-07)

The large research-checkpoint target of 75–100 is **not a prerequisite** for a formal review package. Review 5–20 fully evidenced Exact candidates when available, then apply the unchanged canonical workbook export/reimport, source/identity, concentration, and approval gates. Never inflate the formal tally with research-only pairs.

For reproducible, price-blind prioritization of existing 2026-current-only candidates in underfilled subcategories:

```bash
python3 scripts/triage_exact_backfill.py --repo-root . --limit 30
```

See [Exact-first execution](exact-first-research-execution.md) and the held source probes under `research/batch-10/`. Research priority is based on missing historical evidence, structural shortfall and item identity; never on observed inflation magnitude. Existing Batch 9 fixed ledgers remain immutable; the authoritative formal status is still maintained in the canonical workbook on `main`.
