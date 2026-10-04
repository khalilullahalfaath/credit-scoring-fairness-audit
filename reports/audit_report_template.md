# Fairness Audit Report: Credit Scoring Model

**Model:** TODO (name + version) | **Date:** TODO | **Auditor:** TODO

Written for a reader without a data-science background. No metric appears without a plain-language sentence beside it.

## 1. Summary

- **Verdict:** TODO — approved / approved with conditions / not approved.
- **One-paragraph reason:** TODO
- **Biggest finding:** TODO

## 2. What was audited

- What the model decides: TODO
- Groups compared and how they were formed: TODO
- Data audited (size, period, source): TODO
- Not audited: TODO (be explicit)

## 3. Findings

For each metric: the number, what it means in plain language, and whether it is a concern.

| Metric | Group A | Group B | Plain-language meaning | Concern? |
|---|---|---|---|---|
| Selection rate | TODO | TODO | Share of applicants approved | TODO |
| Disparate impact ratio | TODO | TODO | Lower group's approval rate ÷ higher group's. Below 0.80 is a common warning line. | TODO |
| Equal opportunity (TPR gap) | TODO | TODO | Of people who would repay, how many are approved | TODO |
| False-positive rate gap | TODO | TODO | Of people who would default, how many are approved | TODO |

### 3b. LLM group-swap findings

Same prompt, only the name or gender changed. Measured on one LLM: TODO (name + version).

| Group swap | Prompt pairs | Mean output gap | Plain-language meaning | Concern? |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

State what the gap measures (sentiment or content) and how many pairs it rests on. A gap from a handful of pairs is an anecdote, not a finding.

## 4. Where the metrics disagree

TODO — when base rates differ between groups, these metrics cannot all be satisfied at once. State which two definitions this audit prioritises, why, and what that trades away.

## 5. Mitigation

- Tried: TODO
- Effect on fairness: TODO
- Effect on accuracy: TODO
- Decision: TODO

## 6. Limitations and certainty

- TODO — what this audit cannot show
- TODO — how confident the numbers are (sample size per group, intervals if computed)
- TODO — data caveats (e.g. synthetic data; sensitive attributes may be proxies)

## 7. Recommendations

1. TODO
2. TODO

## 8. Reproduce

TODO — the exact command that regenerates every number above.
