# OKF Example Bundle

A simple [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/open-knowledge-format) knowledge bundle for a fictional retail company (Acme Retail).

## Bundle Structure

```
example_bundle/
├── index.md                              # Bundle root with navigation
└── concepts/
    ├── orders.md                         # BigQuery Table (fact table)
    ├── customers.md                      # BigQuery Table (dimension)
    ├── revenue-ytd.md                    # Metric with attestation
    └── computations/
        └── revenue-ytd-computation.md    # Attested Computation
```

## Concepts

| Concept | Type | Description |
|---------|------|-------------|
| [Orders](example_bundle/concepts/orders.md) | `BigQuery Table` | Customer orders fact table |
| [Customers](example_bundle/concepts/customers.md) | `BigQuery Table` | Customer dimension table |
| [Revenue YTD](example_bundle/concepts/revenue-ytd.md) | `Metric` | Year-to-date revenue KPI |
| [Revenue YTD Computation](example_bundle/concepts/computations/revenue-ytd-computation.md) | `Attested Computation` | Sanctioned SQL + verification |

## OKF Features Demonstrated

- **YAML frontmatter** with `type`, `title`, `description`, `resource`, `tags`, `status`
- **Trust signals**: `generated`, `verified`, `stale_after`, `sources` with credibility signals
- **Cross-linking** via standard markdown links
- **Attested Computation** — sanctioned SQL with executor/attester for verifiable metrics
- **Progressive disclosure** via `index.md`

## Visualize

Open the interactive graph view: **[example_bundle/viz.html](example_bundle/viz.html)**

![OKF Visualization](okf_screenshot.png)

Or generate your own:
```bash
python3 -m reference_agent visualize --bundle example_bundle --out example_bundle/viz.html
```

## Read Programmatically

```bash
python3 read_okf.py example_bundle
```

## Learn More

- [OKF Specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md)
- [Google Cloud Blog: Introducing OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
- [OKF v0.2 Trust Signals](https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals)

---

*Screenshot: Save your visualization as `okf_screenshot.png` in the repo root to display above.*