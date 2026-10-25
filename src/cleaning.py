"""Cleaning for the credit score data (rules and evidence: notebooks/eda.ipynb, "Cleaning decisions").

Layer 1, `clean_rows`, looks at one row at a time, so the API can use it.
Layer 2, `recover_by_customer`, fills values from the same customer's other months, so it only runs where
that history exists (training and evaluation data).
"""
import re

import numpy as np
import pandas as pd

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August"]

# Plausible ranges, read from the value counts of train.csv. Values outside become missing.
RANGES = {
    "Age": (18, 100),
    "Annual_Income": (0, 200_000),
    "Num_Bank_Accounts": (0, 11),
    "Num_Credit_Card": (0, 11),
    "Interest_Rate": (1, 34),
    "Num_of_Delayed_Payment": (0, 28),
    "Num_Credit_Inquiries": (0, 17),
}
# Stored as text, only a trailing underscore or a placeholder stops them from being numbers
NUMERIC = list(RANGES) + [
    "Monthly_Inhand_Salary", "Outstanding_Debt", "Changed_Credit_Limit", "Amount_invested_monthly",
    "Monthly_Balance", "Total_EMI_per_month", "Delay_from_due_date", "Credit_Utilization_Ratio",
]
PLACEHOLDERS = {"Occupation": "_______", "Credit_Mix": "_"}  # become missing
UNKNOWN = {"Payment_Behaviour": "!@9#%8"}  # become their own category
SENTINEL_BALANCE = -1e10  # Monthly_Balance holds -3.33e26 in corrupted rows
FILLER_INVESTED = 10_000  # Amount_invested_monthly filler, same rows as the trailing underscore
LOAN_TYPES = [
    "Auto Loan", "Credit-Builder Loan", "Debt Consolidation Loan", "Home Equity Loan", "Mortgage Loan",
    "Not Specified", "Payday Loan", "Personal Loan", "Student Loan",
]


def loan_column(loan_type):
    return "loan_" + re.sub(r"\W+", "_", loan_type.lower())


LOAN_COLUMNS = [loan_column(t) for t in LOAN_TYPES]

# Layer 2 fill rules
MODE_COLS = ["Occupation", "Credit_Mix", "Annual_Income", "Interest_Rate"]  # constant per customer
FILL_COLS = ["Age", "Monthly_Inhand_Salary", "Num_Bank_Accounts", "Num_Credit_Card", "Total_EMI_per_month"]
MEDIAN_COLS = [
    "Num_of_Delayed_Payment", "Num_Credit_Inquiries", "Amount_invested_monthly", "Monthly_Balance",
    "Changed_Credit_Limit",
]


def _to_float(s):
    """Text to float; strips a trailing underscore, blanks become NaN. Goes through float64 because some
    corrupted values overflow int64."""
    t = s.astype("string").str.strip().str.strip("_")
    return t.where(t != "").astype("float64")


def drop_minors(df):
    """Remove every customer who has a valid age of 14-17 in any month. Run on the raw frame, before clean_rows."""
    age = _to_float(df["Age"])
    minors = df.loc[age.between(14, 17), "Customer_ID"].unique()
    return df[~df["Customer_ID"].isin(minors)].reset_index(drop=True)


def clean_rows(df):
    """Layer 1: row-level rules. Returns a copy; columns that are absent are skipped."""
    out = df.copy()
    for col in NUMERIC:
        if col in out:
            out[col] = _to_float(out[col])
    for col, (lo, hi) in RANGES.items():
        if col in out:
            out[col] = out[col].where(out[col].between(lo, hi))
    if "Monthly_Balance" in out:
        out["Monthly_Balance"] = out["Monthly_Balance"].where(out["Monthly_Balance"] > SENTINEL_BALANCE)
    if "Amount_invested_monthly" in out:
        out["Amount_invested_monthly"] = out["Amount_invested_monthly"].where(
            out["Amount_invested_monthly"] != FILLER_INVESTED)
    if "Total_EMI_per_month" in out:  # genuine values are 0 or have many decimals; whole numbers above 0 are corrupted
        emi = out["Total_EMI_per_month"]
        out["Total_EMI_per_month"] = emi.where(~((emi % 1 == 0) & (emi > 0)))
    for col, placeholder in PLACEHOLDERS.items():
        if col in out:
            out[col] = out[col].where(out[col] != placeholder)
    for col, placeholder in UNKNOWN.items():
        if col in out:
            out[col] = out[col].where(out[col] != placeholder, "Unknown")
    if "Credit_History_Age" in out:  # "22 Years and 3 Months" -> 267
        parts = out["Credit_History_Age"].astype("string").str.extract(r"(\d+) Years and (\d+) Months").astype("float64")
        out["Credit_History_Age"] = parts[0] * 12 + parts[1]
    if "Type_of_Loan" in out:  # one item per loan, types may repeat; empty means no loans
        loans = out.pop("Type_of_Loan").astype("string")
        for t in LOAN_TYPES:
            out[loan_column(t)] = loans.str.count(re.escape(t)).fillna(0).astype(int)
        out["Num_of_Loan"] = out[LOAN_COLUMNS].sum(axis=1)
    return out


def _mode(s):
    m = s.mode()
    return m.iloc[0] if len(m) else np.nan  # ponytail: ties pick the smallest value


def recover_by_customer(df):
    """Layer 2: fill missing values from the same customer's other valid months. Expects clean_rows output."""
    out = df.copy()
    out["month_idx"] = out["Month"].map({m: i for i, m in enumerate(MONTHS)})
    out = out.sort_values(["Customer_ID", "month_idx"], kind="stable").reset_index(drop=True)
    g = out.groupby("Customer_ID", sort=False)
    for col in [c for c in MODE_COLS if c in out]:
        out[col] = out[col].fillna(g[col].transform(_mode))
    for col in [c for c in MEDIAN_COLS if c in out]:  # ponytail: customer median, never compared with the global median
        out[col] = out[col].fillna(g[col].transform("median"))
    for col in [c for c in FILL_COLS if c in out]:  # ponytail: previous valid month, else next, not the nearest one
        out[col] = out.groupby("Customer_ID", sort=False)[col].ffill()
        out[col] = out.groupby("Customer_ID", sort=False)[col].bfill()
    if "Credit_History_Age" in out:  # grows by exactly one month per month
        offset = out["Credit_History_Age"] - out["month_idx"]
        out["Credit_History_Age"] = out["Credit_History_Age"].fillna(
            offset.groupby(out["Customer_ID"]).transform(_mode) + out["month_idx"])
    return out
