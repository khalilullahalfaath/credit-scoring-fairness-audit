"""Held-out split by customer. The ids are saved once and reloaded afterwards, so the split never changes."""
from pathlib import Path

import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold


def holdout_customers(df, target="default_risk", path="../data/processed/holdout_customer_ids.csv", seed=42):
    """Customer_IDs of the held-out part (about 20%), stratified on the target, never splitting a customer."""
    path = Path(path)
    if path.exists():
        return set(pd.read_csv(path)["Customer_ID"])
    folds = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=seed)
    _, test_idx = next(folds.split(df, df[target], groups=df["Customer_ID"]))
    ids = df["Customer_ID"].iloc[test_idx].drop_duplicates()
    path.parent.mkdir(parents=True, exist_ok=True)
    ids.to_csv(path, index=False)
    return set(ids)
