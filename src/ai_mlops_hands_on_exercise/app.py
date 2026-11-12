import zipfile
from pathlib import Path

import pandas as pd
import streamlit as st


def load_data():
    zip_path = Path(__file__).resolve().parents[2] / "datasets" / "bank_marketing.zip"
    with zipfile.ZipFile(zip_path) as z, z.open("bank-additional-full.csv") as f:
        return pd.read_csv(f, sep=";")


df = load_data()
print(df.head())

st.title("Bank Marketing Dataset EDA")
st.caption("Interactive exploration of clients")
st.dataframe(df.head())
