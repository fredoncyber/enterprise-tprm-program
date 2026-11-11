# Risk Methodology

## 1. Inherent-risk dimensions
Score each 1–5 before considering vendor controls:

1. Data sensitivity and volume
2. Privileged/system access
3. Operational criticality
4. Connectivity and deployment depth
5. Regulatory/legal exposure
6. Substitutability and exit complexity
7. Concentration/systemic dependency
8. Geographic/geopolitical exposure
9. Financial and strategic dependency
10. AI/model use and automated decision impact

Apply dimension weights from `data/risk-taxonomy.csv`. The weighted score determines the tier, subject to mandatory overrides.

## 2. Mandatory tier overrides
A vendor is **Tier 1 Critical** when any of the following applies:
- Outage can breach a board-approved maximum tolerable downtime.
- Vendor has broad privileged, kernel, identity, security-control, production, payment, or regulated-data access.
- Failure can create material safety, legal, financial, or systemic impact.
- Vendor is a single/near-single source without a tested alternative.

## 3. Risk statement
Use: **Because of [threat/event], exploiting [condition], there is a possibility of [impact] affecting [asset/objective].**

## 4. Scoring

### Inherent risk
`Inherent = Likelihood (1–5) × Impact (1–5)`

| Score | Rating |
|---:|---|
| 1–4 | Low |
| 5–9 | Moderate |
| 10–16 | High |
| 17–25 | Critical |

### Control effectiveness
0.00–1.00, based on design, implementation, test results, issue history, scope, and evidence freshness.

### Evidence confidence
0.00–1.00. Use zero when supporting evidence is unavailable; independent current testing receives more confidence than unauthenticated claims.

### Residual risk
`Residual = Inherent × (1 − Control Effectiveness × Evidence Confidence)`

The calculation supports, but does not replace, professional judgment.

## 5. Evidence hierarchy
1. Direct technical validation or independently observed test
2. Current independent assurance report/certification with relevant scope
3. Current penetration test, resilience test, audit report, or attestation
4. Contractually enforceable documentation and approved architecture
5. Policies, procedures, screenshots, tickets, metrics and sampled records
6. Questionnaire response
7. Marketing statement or unsupported assertion

## 6. Disposition
- **Approve:** residual exposure within appetite.
- **Approve with conditions:** time-bound treatment and compensating controls.
- **Risk acceptance:** named executive accepts a specific residual risk through a defined expiry.
- **Reject:** prohibited or unmanageable exposure.
- **Exit:** active vendor no longer meets requirements or appetite.

## 7. Assessment frequency
| Tier | Full reassessment | Monitoring |
|---|---|---|
| Tier 1 Critical | Annual and material change | Continuous signals; monthly/quarterly review |
| Tier 2 High | 12–18 months | Quarterly |
| Tier 3 Moderate | 24 months | Semiannual |
| Tier 4 Low | 36 months / attestation | Annual |
