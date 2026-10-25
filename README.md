# Credit Scoring with Fairness Audit

A credit scoring model (score + probability + risk category) that passes a documented bias audit before it is allowed to ship.

**Status:** Started | **Roadmap:** Project 5 (Credit Score Calculator) + Project 127 (Bias & Fairness Audit)

## Table of Contents

- [Credit Scoring with Fairness Audit](#credit-scoring-with-fairness-audit)
  - [Table of Contents](#table-of-contents)
  - [Project Brief](#project-brief)
  - [Fairness Decisions](#fairness-decisions)
  - [Dataset](#dataset)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)
  - [Results](#results)
    - [Model comparison](#model-comparison)
    - [Threshold choice](#threshold-choice)
    - [Fairness metrics](#fairness-metrics)
    - [LLM group-swap test](#llm-group-swap-test)
  - [Model Card](#model-card)
    - [Model Information](#model-information)
    - [Intended Use](#intended-use)
    - [Training Data](#training-data)
    - [Performance](#performance)
    - [Risk categories](#risk-categories)
    - [Ethical Considerations](#ethical-considerations)
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

**Sensitive attributes used:** Age, audited in four groups: 18-25, 26-35, 36-45 and 46+ (customers aged 14-17 are removed). Age is chosen because the default rate (share of `Poor` rows) is about 0.30-0.31 for ages 18-45 and about 0.13 for 46+, a difference far larger than sampling noise. Occupation is checked as a secondary attribute only: its default rates (0.26-0.31 across 15 occupations) are about what chance would give.

**Age as a model feature:** not used. Age is kept separately and only used for the audit. Removing it does not remove its proxies (for example `Credit_History_Age`), so how well the remaining features predict age is measured, and a model with `Age` and one without it are compared on ROC-AUC and on the fairness metrics below, to put a number on what excluding it costs. In this data the default rate drops sharply between the 36-45 and 46+ groups rather than gradually, so a model using `Age` would partly be learning that cut-off.

**Fairness definitions defended:**

| Definition | Why | Cost |
|---|---|---|
| Equal opportunity (primary): customers who would not default have the same chance of being approved in every age group | Wrongly rejecting a customer who would have repaid is the harm this audit must be able to defend, and this definition measures it directly | Overall approval rates can differ between groups, so the 80% rule can flag the model |
| Demographic parity, measured by the disparate impact ratio (secondary): each group's approval rate divided by the highest, flagged below 0.80 | It is the standard screening rule and is easy to explain without statistics | Equalizing approval rates when base rates differ means approving more likely defaulters in the higher-risk groups, or rejecting more good customers in 46+, so accuracy falls |

**Trade-off:** equalizing false-positive rate across groups when base rates differ.

"Selection" here means approved, not flagged as risky. Because the default rate is about 0.13 for 46+ and 0.30-0.31 for the other groups, an imperfect classifier cannot in general satisfy both definitions at once. Even a perfect classifier would approve about 69-70% of customers aged 18-45 against 87% of 46+, a disparate impact ratio of about 0.79-0.80, so the 80% rule can flag a model whose decisions are all correct (rough figures from the default rates above). When the two definitions conflict, equal opportunity decides, and the disparate impact ratio is reported with this gap explained instead of being forced to 0.80. The size of the conflict is measured on the held-out set in Results, Fairness metrics.

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

```bash
# I really recommend using uv, since it's faster and it's compatible with pip
uv venv
.venv/Scripts/activate # Windows; use `source .venv/bin/activate` on Linux/macOS
uv pip install -r requirements.txt

# regular pip
python -m venv venv
venv\Scripts\activate            # Windows; use `source venv/bin/activate` on Linux/macOS
pip install -r requirements.txt
```

Exploration on this project is in `notebooks/`, so I recommend using Jupyterlab since it's less buggy than vscode jupyter notebook extension.

```bash
# Assumed that the virtual environment is already activated
jupyter lab
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

- **LLM (name + version):** Deepseek v4.1 Pro
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
