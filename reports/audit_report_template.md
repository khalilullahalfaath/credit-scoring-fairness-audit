# Fairness Audit Report: Credit Scoring Model

**Model:** TODO (name + version) | **Date:** TODO | **Auditor:** TODO

Plain-language report for a non-technical reader.

## 1. Summary

- **Verdict:** TODO (approved / approved with conditions / not approved)
- **One-paragraph reason:** TODO
- **Biggest finding:** TODO

## 2. What was audited

- What the model decides: TODO
- Groups compared and how they were formed: TODO
- Data audited (size, period, source): TODO
- Not audited: TODO

## 3. Findings

Each metric with its value, a plain-language meaning, and whether it is a concern.

| Metric | Group A | Group B | Plain-language meaning | Concern? |
|---|---|---|---|---|
| Selection rate | TODO | TODO | Share of applicants approved | TODO |
| Disparate impact ratio | TODO | TODO | Lower group's approval rate ÷ higher group's. Below 0.80 is a common warning line. | TODO |
| Equal opportunity (TPR gap) | TODO | TODO | Of people who would repay, how many are approved | TODO |
| False-positive rate gap | TODO | TODO | Of people who would default, how many are approved | TODO |

### 3b. LLM group-swap findings

Same prompt, only the name or gender changed. LLM: TODO (name + version).

| Group swap | Prompt pairs | Mean output gap | Plain-language meaning | Concern? |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

Measure: TODO (sentiment or content gap). Number of prompt pairs: TODO.

## 4. Where the metrics disagree

TODO

## 5. Mitigation

- Tried: TODO
- Effect on fairness: TODO
- Effect on accuracy: TODO
- Decision: TODO

## 6. Limitations and certainty

- TODO: what this audit cannot show
- TODO: confidence in the numbers (sample size per group, intervals)
- TODO: data caveats

## 7. Recommendations

1. TODO
2. TODO

## 8. Reproduce

TODO
