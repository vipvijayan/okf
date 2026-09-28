---
type: BigQuery Table
title: Customers
description: Customer dimension table with profile and segmentation data
resource: bigquery://acme-retail.analytics.customers
tags: [dimension-table, customers, pii]
status: stable
generated:
  by: "agent:bigquery-enricher"
  at: "2026-01-15T10:30:00Z"
verified:
  - by: "human:data-engineer@acme.com"
    at: "2026-01-16T09:00:00Z"
stale_after: "2026-07-15"
sources:
  - id: bq-metadata
    resource: bigquery://acme-retail.analytics.customers
    author: "BigQuery INFORMATION_SCHEMA"
    last_modified: "2026-01-15T10:30:00Z"
---

# Customers Table

Dimension table containing customer profiles and segmentation attributes.

## Schema

| Column | Type | Mode | Description |
|--------|------|------|-------------|
| customer_id | STRING | REQUIRED | Unique customer identifier |
| email | STRING | REQUIRED | Customer email (PII) |
| first_name | STRING | NULLABLE | Given name |
| last_name | STRING | NULLABLE | Family name |
| tier | STRING | REQUIRED | Loyalty tier (bronze, silver, gold, platinum) |
| signup_ts | TIMESTAMP | REQUIRED | Account creation timestamp |
| last_active_ts | TIMESTAMP | NULLABLE | Most recent activity |

## Examples

```sql
-- Active customers by tier
SELECT tier, COUNT(*) AS customer_count
FROM `acme-retail.analytics.customers`
WHERE last_active_ts >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY)
GROUP BY tier;
```

## Relationships

- **Orders**: One customer has many orders → [Orders](orders.md)