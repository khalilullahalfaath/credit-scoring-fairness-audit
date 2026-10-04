# Project 127: Bias & Fairness Audit for LLM/Classifier Outputs

Ini adalah salinan kartu dari `dsml-roadmap.pdf` (Intermediate, AI Engineer Track).

**Difficulty:** INTERMEDIATE | **Time:** 1–1.5 weeks

## The Request

> "Ada laporan model scoring kita kasih hasil beda-beda buat kelompok demografis tertentu. Sebelum dipakai lagi, kita butuh audit yang bisa dipertanggungjawabkan."

## Description

Build a reusable bias/fairness auditing tool that measures disparity in model or LLM outputs across demographic groups (e.g. gender, region), using standard fairness metrics, and produces a report suitable for a non-technical stakeholder.

## Learning Objectives

- Fairness metrics: demographic parity, equal opportunity, disparate impact ratio
- Auditing generative (LLM) outputs for stereotyped or unequal treatment across group-swapped prompts
- Communicating fairness findings to non-technical stakeholders without overstating certainty

## Tech Stack

Python, Fairlearn/AIF360, pandas

## Dataset

- **Primary:** Reuse the Credit Score Classification model from Project 5 (Credit Score Calculator), which has demographic-adjacent features

## Core Requirements

- Compute demographic parity and equal opportunity metrics across at least 2 sensitive groups
- Compute disparate impact ratio and flag values outside the 80% rule of thumb
- For a generative use case, run group-swapped prompt pairs (e.g. same prompt, different names/genders) through an LLM and measure output sentiment/content differences
- Aggregate findings into a report with plain-language explanations, not just raw metric tables
- Document known limitations of each fairness metric used (metrics can conflict with each other)

## Deliverables

- [ ] Fairness-audit module (classifier metrics + LLM group-swap testing)
- [ ] Sample audit report (HTML/PDF) for a non-technical audience
- [ ] Test suite validating the metric calculations against known reference values
- [ ] README documenting each metric and its limitations

## Bonus Challenges

- Apply a bias-mitigation technique (reweighing/threshold adjustment) and re-measure
- Extend group-swap testing to intersectional groups (e.g. gender × region)
- Add the audit as a required check in the model's CI/CD pipeline (reuse Project 54, ML CI/CD Pipeline)

## Related concepts

Concepts guide: Bab 18 (Bias, Fairness, & Ethics), Bab 80 (LLM Safety, Red-Teaming & Evaluasi LLM).

## Non-functional requirements

Metrics match reference implementations; report readable without statistics background; limitations section prevents overclaiming; unit test coverage ≥70%; structured logging.

## Risks and assumptions

Risk: small protected-group samples, metric interpretation ambiguity, prompt-test flakiness. Asumsi: protected attributes available, reference implementations valid, report reviewer scope defined.

## Product Brief

- **Objective:** Defensible, repeatable bias/fairness audit for classifier and LLM outputs.
- **Scope:** Standard fairness metrics for classifiers plus group-swap prompt testing for generative outputs.
- **Success criteria:** Metrics match reference implementations on a known test case, report is understandable without a statistics background, limitations section prevents overclaiming.
- **Out of scope:** Automated bias mitigation deployment, legal/regulatory compliance certification, causal analysis of bias sources.
