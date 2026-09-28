---
type: Metric
title: Revenue YTD
description: Year-to-date revenue from delivered orders
resource: bigquery://acme-retail.analytics.orders
tags: [metric, revenue, finance, kpi]
status: stable
generated:
  by: "agent:bigquery-enricher"
  at: "2026-01-15T10:30:00Z"
verified:
  - by: "human:finance-lead@acme.com"
    at: "2026-01-20T14:00:00Z"
stale_after: "2026-07-15"
sources:
  - id: bq-metadata
    resource: bigquery://acme-retail.analytics.orders
    author: "BigQuery INFORMATION_SCHEMA"
    last_modified: "2026-01-15T10:30:00Z"
  - id: finance-policy
    resource: https://wiki.acme.com/finance/revenue-recognition-policy
    author: "Finance Team"
    last_modified: "2025-11-01T00:00:00Z"
---

# Revenue YTD Metric

Total revenue recognized from delivered orders in the current calendar year.

## Definition

Revenue is recognized when orders reach `delivered` status. Only orders with `status = 'delivered'` are included. Returns and cancellations are excluded (handled in a separate metric).

## Computation

This metric is computed via an [Attested Computation](computations/revenue-ytd-computation.md) that ensures the calculation runs exactly as sanctioned.

## Current Value

As of 2026-01-20: **$2,847,391.52**

## Relationships

- **Source Data**: Derived from [Orders](orders.md) table
- **Computation**: [Revenue YTD Computation](computations/revenue-ytd-computation.md)
- **Policy**: Governed by [Finance Revenue Recognition Policy](https://wiki.acme.com/finance/revenue-recognition-policy)