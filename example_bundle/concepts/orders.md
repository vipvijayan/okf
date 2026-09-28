---
type: BigQuery Table
title: Orders
description: Customer orders fact table with order details and totals
resource: bigquery://acme-retail.analytics.orders
tags: [fact-table, orders, transactions]
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
    resource: bigquery://acme-retail.analytics.orders
    author: "BigQuery INFORMATION_SCHEMA"
    last_modified: "2026-01-15T10:30:00Z"
---

# Orders Table

Fact table containing all customer orders placed on the Acme Retail platform.

## Schema

| Column | Type | Mode | Description |
|--------|------|------|-------------|
| order_id | STRING | REQUIRED | Unique order identifier |
| customer_id | STRING | REQUIRED | Foreign key to Customers |
| product_id | STRING | REQUIRED | Foreign key to Products |
| quantity | INT64 | REQUIRED | Number of units ordered |
| unit_price | NUMERIC | REQUIRED | Price per unit at time of order |
| order_total | NUMERIC | REQUIRED | quantity × unit_price |
| order_ts | TIMESTAMP | REQUIRED | When the order was placed |
| status | STRING | REQUIRED | Order status (pending, shipped, delivered, cancelled) |

## Examples

```sql
-- Revenue by month
SELECT 
  DATE_TRUNC(order_ts, MONTH) AS month,
  SUM(order_total) AS revenue
FROM `acme-retail.analytics.orders`
WHERE status = 'delivered'
GROUP BY month
ORDER BY month;
```

## Relationships

- **Customers**: Each order links to one customer via `customer_id` → [Customers](customers.md)
- **Products**: Each order links to one product via `product_id` → [Products](products.md)
- **Revenue YTD**: This table is the source for the [Revenue YTD](revenue-ytd.md) metric computation