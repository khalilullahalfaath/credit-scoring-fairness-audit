# Credit Scoring with Fairness Audit

A credit scoring model (score + probability + risk category) that passes a documented bias audit before it is allowed to ship.

**Status:** Started | **Roadmap:** Project 5 (Credit Score Calculator) + Project 127 (Bias & Fairness Audit) | **Brief:** H2

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
    - [Fairness metrics (on the chosen model)](#fairness-metrics-on-the-chosen-model)
    - [LLM group-swap test (Project 127)](#llm-group-swap-test-project-127)
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

**Business constraint:** TODO — cost of approving a defaulter vs. rejecting a good customer, in numbers (state the assumption).

**Success criteria:** TODO — ROC-AUC, minority-class precision/recall, chosen threshold, API latency.

**Out of scope:**
- More than one tabular dataset
- More than two fairness definitions
- More than one LLM for the group-swap test (Project 127's generative part is in scope, kept to what the card asks)

## Fairness Decisions

This is the section reviewers read first. Answer it here, not in an interview.

**Sensitive attributes used:** TODO — column names, and how groups were formed (e.g. age bins). State what the dataset does *not* contain.

**The two fairness definitions I defend:**

| Definition | Why I chose it | What it costs |
|---|---|---|
| TODO (e.g. equal opportunity) | TODO | TODO |
| TODO (e.g. demographic parity) | TODO | TODO |

**Failure-mode question:**
> "You equalised false-positive rate across groups, but the base rates differ. Which do you pick and why?"

TODO — answer with numbers. Name the impossibility result explicitly: when base rates differ, the common fairness definitions cannot all hold at once.

**Mitigation tried:** TODO — what, and the accuracy cost.

## Dataset

**Primary:** [Credit Score Classification](https://www.kaggle.com/datasets/parisrohan/credit-score-classification) (Kaggle). Anonymised/synthetic data for learning, not real applicant records.

- Rows / features: TODO (verify after download)
- Target: TODO
- Class balance: TODO
- Sensitive-adjacent columns: TODO

Place the raw file in `data/raw/` (git-ignored).

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
│   └── audit_report_template.md
├── tests/                       # metric tests vs. known reference values
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

TODO — add the commands for: download data, train, run audit, start API, run tests.

## Results

### Model comparison

| Model | ROC-AUC | Precision (default) | Recall (default) | Threshold |
|---|---|---|---|---|
| Baseline | TODO | TODO | TODO | TODO |
| Logistic Regression | TODO | TODO | TODO | TODO |
| Random Forest | TODO | TODO | TODO | TODO |

**Chosen model and why:** TODO

### Threshold choice

TODO — the business-cost curve and the threshold picked from it.

### Fairness metrics (on the chosen model)

| Group | Selection rate | TPR | FPR | Disparate impact ratio |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

Flag any ratio outside the 80% rule of thumb.

### LLM group-swap test (Project 127)

Done last, after the classifier audit is finished. Needs access to one LLM (API or local) — prepare it before starting this part.

- **LLM used (name + version):** TODO
- **Prompt pairs:** TODO — count, and what differs within a pair (name / gender only)
- **Measure:** TODO — output sentiment or content difference per pair

| Group swap | Mean sentiment gap | Notable examples |
|---|---|---|
| TODO | TODO | TODO |

## Model Card

### Model Information
- **Type:** TODO
- **Version:** TODO
- **Training date:** TODO
- **Framework:** TODO

### Intended Use
- **Primary use:** TODO
- **Users:** TODO
- **Out of scope:** TODO — e.g. not for real lending decisions; trained on synthetic data.

### Training Data
- **Source / size / split:** TODO

### Performance
TODO — link to the Results section.

### Risk categories

| Category | Probability range | Meaning |
|---|---|---|
| Low | TODO | TODO |
| Medium | TODO | TODO |
| High | TODO | TODO |

### Ethical Considerations
TODO

## Audit Report

Written for a non-technical reader. Template: [`reports/audit_report_template.md`](reports/audit_report_template.md). Finished report: TODO (link).

## Limitations

- TODO — metric limitations (each fairness metric can conflict with the others)
- TODO — dataset limitations (synthetic; sensitive attributes may be proxies)

## References

- [Fairlearn documentation](https://fairlearn.org/)
- [Credit Score Classification dataset](https://www.kaggle.com/datasets/parisrohan/credit-score-classification)
- TODO — add the fairness papers/docs you actually read
