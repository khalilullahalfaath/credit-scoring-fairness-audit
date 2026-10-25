import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from cleaning import clean_rows, drop_minors, recover_by_customer  # noqa: E402
from split import holdout_customers  # noqa: E402


def test_clean_rows_marks_corrupted_values_missing():
    raw = pd.DataFrame({
        "Age": ["24_"], "Annual_Income": ["42904.26_"], "Num_Bank_Accounts": ["429"],
        "Monthly_Balance": ["__-333333333333333333333333333__"], "Amount_invested_monthly": ["10000"],
        "Changed_Credit_Limit": ["_"], "Total_EMI_per_month": [15015.0], "Occupation": ["_______"],
        "Payment_Behaviour": ["!@9#%8"], "Credit_History_Age": ["22 Years and 3 Months"],
    })
    out = clean_rows(raw).iloc[0]
    assert out["Age"] == 24 and out["Annual_Income"] == 42904.26 and out["Credit_History_Age"] == 267
    assert np.isnan([out["Num_Bank_Accounts"], out["Monthly_Balance"], out["Amount_invested_monthly"],
                     out["Changed_Credit_Limit"], out["Total_EMI_per_month"]]).all()
    assert pd.isna(out["Occupation"]) and out["Payment_Behaviour"] == "Unknown"
    assert clean_rows(pd.DataFrame({"Total_EMI_per_month": [911.220179, 0.0]}))["Total_EMI_per_month"].tolist() == [911.220179, 0.0]


def test_num_of_loan_is_the_length_of_the_loan_list():
    out = clean_rows(pd.DataFrame({"Type_of_Loan": ["Auto Loan, Payday Loan, and Auto Loan", None]}))
    assert out["Num_of_Loan"].tolist() == [3, 0]
    assert out["loan_auto_loan"].tolist() == [2, 0] and out["loan_payday_loan"].tolist() == [1, 0]


def test_drop_minors_removes_every_row_of_the_customer():
    raw = pd.DataFrame({"Customer_ID": ["a"] * 3 + ["b"] * 3, "Age": ["16", "17", "18", "30", "-500", "31_"]})
    assert drop_minors(raw)["Customer_ID"].unique().tolist() == ["b"]


def test_recover_keeps_a_genuine_step_and_replaces_a_spike():
    months = ["January", "February", "March", "April", "May", "June", "July", "August"]
    raw = pd.DataFrame({
        "Customer_ID": ["a"] * 8, "Month": months,
        "Num_Bank_Accounts": ["4", "4", "4", "429", "5", "5", "5", "5"],
        "Credit_History_Age": ["10 Years and 0 Months", None, "10 Years and 2 Months", "10 Years and 3 Months"]
                              + [None] * 4,
        "Annual_Income": ["50000", "50000_", "5000000", "50000", "50000", "50000", "50000", "50000"],
        "Occupation": ["Teacher", "_______"] + ["Teacher"] * 6,
        "Num_Credit_Inquiries": ["5", "5", "5", "5", "5", "5", "5", "5000"],
    })
    out = recover_by_customer(clean_rows(raw))
    assert out["Num_Bank_Accounts"].tolist() == [4, 4, 4, 4, 5, 5, 5, 5]
    assert out["Credit_History_Age"].tolist() == [120 + i for i in range(8)]
    assert out["Annual_Income"].tolist() == [50000.0] * 8
    assert out["Occupation"].tolist() == ["Teacher"] * 8
    assert out["Num_Credit_Inquiries"].tolist() == [5.0] * 8


def test_holdout_never_splits_a_customer(tmp_path):
    rng = np.random.default_rng(0)
    df = pd.DataFrame({"Customer_ID": np.repeat([f"c{i}" for i in range(100)], 8)})
    df["default_risk"] = np.repeat(rng.integers(0, 2, 100), 8)
    ids = holdout_customers(df, path=tmp_path / "ids.csv")
    assert 15 <= len(ids) <= 25
    assert df[df["Customer_ID"].isin(ids)]["Customer_ID"].nunique() == len(ids)
    assert holdout_customers(df.sample(frac=1, random_state=1), path=tmp_path / "ids.csv") == ids  # frozen
