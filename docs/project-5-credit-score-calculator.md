# Project 5: Credit Score Calculator

Ini adalah salinan kartu dari `dsml-roadmap.pdf` (Beginner, Classical ML).

**Difficulty:** BEGINNER | **Time:** 4–7 days

## The Request

> "Bank mau sistem scoring kredit otomatis untuk evaluasi nasabah. Harus bisa kasih skor, probabilitas, dan kategori risiko sekaligus."

## Description

Build a credit scoring model using Logistic Regression for interpretability and Random Forest for performance. Focus on ROC-AUC evaluation, threshold tuning, and returning actionable risk categories.

## Learning Objectives

- Logistic Regression and probability calibration
- ROC-AUC evaluation and threshold tuning for business objectives
- Feature engineering for financial data (ratios, utilization metrics)
- Fairness in credit scoring: demographic parity, equalized odds, and bias mitigation

## Tech Stack

Python, Pandas, scikit-learn, FastAPI

## Dataset

- **Primary:** Credit Score Classification — <https://www.kaggle.com/datasets/parisrohan/credit-score-classification> (100K rows, 28 features; anonymized/synthetic financial data for learning — not real applicant records)

## Core Requirements

- EDA on credit features and target distribution
- Feature engineering: debt-to-income ratios, credit utilization metrics
- Train Logistic Regression and Random Forest models
- ROC-AUC evaluation with threshold analysis and selection
- Fairness evaluation: report precision/recall on the minority (default) class and check for demographic disparity (demographic parity / equalized odds) across available sensitive attributes
- API returning credit score + probability + risk category (Low/Medium/High)

## Deliverables

- [ ] Jupyter notebook with EDA and threshold analysis
- [ ] Trained model artifact
- [ ] Fairness assessment report (disparity metrics across sensitive attributes + minority-class precision/recall)
- [ ] REST API with Swagger documentation
- [ ] Postman collection for API testing
- [ ] README with model card, risk category definitions, and fairness limitations

## Bonus Challenges

- Score explanation endpoint (which features contributed most to the score)
- Threshold optimization for business metrics (minimize default rate)
- Mitigation experiment: apply a fairness intervention (e.g. reweighing) and compare disparity before/after
- Build a simple frontend (Streamlit/HTML) to interact with the API

## Related concepts

Concepts guide: Bab 26 (Klasifikasi), Bab 15 (Uncertainty & Calibration).

## Non-functional requirements

API response < 200ms; Pydantic validation; calibrated probability output; configurable risk threshold; model serialization; Swagger docs; Postman collection.

## Risks and assumptions

Risk: bias/fairness pada keputusan kredit serta data leakage. Asumsi: data applicant akurat, fitur tersedia saat inference.

## Product Brief

- **Objective:** Automated credit scoring API returning score, probability, and risk category.
- **Scope:** Single model serving with threshold-based risk classification and a fairness check.
- **Success criteria:** AUC > 0.75, calibrated probabilities, minority-class (default) precision and recall reported alongside a quantified fairness/disparity gap, threshold set against an explicit business-cost trade-off (e.g. expected default loss).
- **Out of scope:** Real-time transaction monitoring, regulatory compliance reporting.
