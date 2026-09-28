---
type: Attested Computation
title: Revenue YTD Computation
description: Sanctioned SQL computation for Revenue YTD metric
runtime: bigquery
executor:
  resource: bigquery-sql
  receipt:
    - job_id
    - executed_sql
    - result_rows
attester:
  resource: attesters/sql_equality.py
  receipt:
    - job_id
    - executed_sql
    - result_rows
status: stable
generated:
  by: "agent:bigquery-enricher"
  at: "2026-01-15T10:30:00Z"
verified:
  - by: "human:finance-lead@acme.com"
    at: "2026-01-20T14:00:00Z"
---

# Computation

```sql
SELECT 
  SUM(order_total) AS revenue_ytd
FROM `acme-retail.analytics.orders`
WHERE status = 'delivered'
  AND EXTRACT(YEAR FROM order_ts) = EXTRACT(YEAR FROM CURRENT_DATE());
```

## Parameters

None (uses current year implicitly).

## Attestation

When this computation runs:
1. The **executor** submits the SQL to BigQuery and returns a receipt with `job_id`, the exact `executed_sql`, and `result_rows`
2. The **attester** (`sql_equality.py`) canonicalizes both the sanctioned SQL above and the `executed_sql` from the receipt (stripping comments, normalizing whitespace, uppercasing keywords)
3. If canonical forms match **and** the displayed value matches `result_rows`, attestation passes
4. Any modification (added filter, changed table, different aggregation) fails attestation

This ensures the metric value displayed in dashboards was produced by **exactly this SQL**, not an agent's improvisation.