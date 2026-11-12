import zipfile
from pathlib import Path

import pandas as pd
import seaborn as sns
import streamlit as st

# setting color palette
BG = "#0B1426"
PANEL = "#111D33"
GRID = "#24324D"
TEXT = "#E6EAF2"
MUTED = "#8A97B1"

PALETTE = [
    "#4FC3F7",
    "#F5A65B",
    "#7BD88F",
    "#C792EA",
    "#F0657D",
    "#E8D44D",
]

sns.set_theme(
    style="darkgrid",
    palette=PALETTE,
    rc={
        "figure.facecolor": BG,
        "axes.facecolor": PANEL,
        "axes.edgecolor": GRID,
        "axes.labelcolor": TEXT,
        "axes.titlecolor": TEXT,
        "grid.color": GRID,
        "text.color": TEXT,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "savefig.facecolor": BG,
    },
)


# dataset loading
@st.cache_data
def load_data():
    zip_path = Path(__file__).resolve().parents[2] / "datasets" / "bank_marketing.zip"

    with zipfile.ZipFile(zip_path) as archive:
        with archive.open("bank-additional-full.csv") as file:
            return pd.read_csv(file, sep=";")


df = load_data()


# Streamlit app
st.title("Bank Marketing Dataset EDA")
st.caption("Interactive exploration of bank customers")

# job filter
job = st.selectbox("Filter by job", ["All"] + sorted(df["job"].unique()))

filtered = df if job == "All" else df[df["job"] == job]

# key metrics
subscription_rate = filtered["y"].eq("yes").mean() * 100

col1, col2 = st.columns(2)

col1.metric("Customers", f"{len(filtered):,}")
col2.metric("Subscription Rate", f"{subscription_rate:.1f}%")

# subscription rate visualization
st.progress(
    subscription_rate / 100, text=f"Subscribed customers: {subscription_rate:.1f}%"
)
