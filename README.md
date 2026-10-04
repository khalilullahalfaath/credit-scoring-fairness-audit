# Credit Scoring with Fairness Audit

A credit scoring model (score + probability + risk category) that passes a documented bias audit before it is allowed to ship.

**Status:** Started | **Roadmap:** Project 5 (Credit Score Calculator) + Project 127 (Bias & Fairness Audit)

## Table of Contents

- [Project Brief](#project-brief)
- [Fairness Decisions](#fairness-decisions)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Results](#results)
- [Model Card](#model-card)
- [Audit Report](#audit-report)
- [Limitations](#limitations)
- [References](#references)

## Project Brief

**The Request:** "A bank wants automatic credit scoring to evaluate customers. It must return a score, a probability, and a risk category. A report shows that results differ across demographic groups; before the model is used, we need an audit we can defend."

**Business constraint:** TODO

**Success criteria:**

| Criterion | Target |
|---|---|
| Ranking quality | ROC-AUC > 0.75 on the held-out test set |
| Probabilities | Calibrated; ECE and Brier reported before and after calibration |
| Minority (default) class | Precision and recall reported |
| Decision threshold | Chosen from an explicit business-cost curve |
| Fairness metrics | Demographic parity, equal opportunity and disparate impact ratio across at least 2 groups; ratios outside 0.80 flagged |
| Fairness reasoning | Two definitions defended, with the trade-off between them quantified |
| Metric correctness | Metric tests match hand-computed reference values; coverage >= 70% |
| API | Response < 200 ms, validated input, Swagger docs, Postman collection |
| Audit report | Readable without a statistics background; limitations stated per metric |
| LLM group-swap test | One LLM, group-swapped prompt pairs, output gap per group with a confidence interval |

**Out of scope:**
- More than one tabular dataset
- More than two fairness definitions
- More than one LLM for the group-swap test

## Fairness Decisions

**Sensitive attributes used:** TODO

**Fairness definitions defended:**

| Definition | Why | Cost |
|---|---|---|
| TODO | TODO | TODO |
| TODO | TODO | TODO |

**Trade-off:** equalizing false-positive rate across groups when base rates differ.

TODO

**Mitigation tried:** TODO

## Dataset

[Credit Score Classification](https://www.kaggle.com/datasets/parisrohan/credit-score-classification) (Kaggle). Anonymized/synthetic data, not real applicant records. Raw files go in `data/raw/` (git-ignored).

- Rows / features: TODO
- Target: TODO
- Class balance: TODO
- Sensitive-adjacent columns: TODO

## Project Structure

```
credit-scoring-fairness-audit/
├── data/
│   ├── raw/                     # git-ignored
│   └── processed/               # git-ignored
├── notebooks/
│   ├── 01-eda.ipynb
│   └── 02-threshold-analysis.ipynb
├── src/                         # preprocessing, training, fairness audit, API
├── models/                      # metrics.json committed; model files ignored
├── reports/
├── tests/                       # metric tests vs. reference values
├── postman/
├── requirements.txt
└── README.md
```

## Getting Started

```
python -m venv venv
venv\Scripts\activate            # Windows; use `source venv/bin/activate` on Linux/macOS
pip install -r requirements.txt
```

TODO

## Results

### Model comparison

| Model | ROC-AUC | Precision (default) | Recall (default) | Threshold |
|---|---|---|---|---|
| Baseline | TODO | TODO | TODO | TODO |
| Logistic Regression | TODO | TODO | TODO | TODO |
| Random Forest | TODO | TODO | TODO | TODO |

**Chosen model:** TODO

### Threshold choice

TODO

### Fairness metrics

| Group | Selection rate | TPR | FPR | Disparate impact ratio |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

### LLM group-swap test

- **LLM (name + version):** TODO
- **Prompt pairs:** TODO
- **Measure:** TODO

| Group swap | Mean gap | 95% CI | Notable examples |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

## Model Card

### Model Information
- **Type:** TODO
- **Version:** TODO
- **Training date:** TODO
- **Framework:** TODO

### Intended Use
- **Primary use:** TODO
- **Users:** TODO
- **Out of scope:** TODO

### Training Data
TODO

### Performance
TODO

### Risk categories

| Category | Probability range | Meaning |
|---|---|---|
| Low | TODO | TODO |
| Medium | TODO | TODO |
| High | TODO | TODO |

### Ethical Considerations
TODO

## Audit Report

TODO

## Limitations

TODO

## References

- [Fairlearn documentation](https://fairlearn.org/)
- [Credit Score Classification dataset](https://www.kaggle.com/datasets/parisrohan/credit-score-classification)
