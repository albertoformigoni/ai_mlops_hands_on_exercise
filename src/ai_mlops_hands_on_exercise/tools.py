import zipfile
from pathlib import Path

import joblib
import pandas as pd

DATASET = Path(__file__).resolve().parents[2] / "datasets" / "bank_marketing.zip"


def load_data():
    with zipfile.ZipFile(DATASET) as archive:
        with archive.open("bank-additional-full.csv") as file:
            return pd.read_csv(file, sep=";")


def get_dataset_info():
    df = load_data()

    return {
        "customers": len(df),
        "features": len(df.columns) - 1,
        "subscription_rate": float(round(df["y"].eq("yes").mean() * 100, 2)),
    }


def get_subscription_rate(job):
    df = load_data()

    if job != "All":
        if job not in df["job"].unique():
            return {"error": "Unknown job category"}
        df = df[df["job"] == job]

    return {
        "job": job,
        "customers": len(df),
        "subscription_rate": float(round(df["y"].eq("yes").mean() * 100, 2)),
    }


# predict subscription using the trained model
def predict_subscription(customer):
    model_path = Path(__file__).resolve().parents[2] / "models" / "bank_model.joblib"
    model = joblib.load(model_path)

    customer = customer.copy()
    customer["previously_contacted"] = int(customer.pop("pdays") != 999)

    data = pd.DataFrame([customer])
    probability = float(model.predict_proba(data)[0][1])
    prediction = int(probability >= 0.5)

    return {
        "prediction": "yes" if prediction == 1 else "no",
        "probability": round(probability, 3),
    }


if __name__ == "__main__":
    print(get_dataset_info())
    print(get_subscription_rate("student"))
    print(get_subscription_rate("admin."))
    df = load_data()

    customer = df.drop(columns=["y", "duration"]).iloc[887].to_dict()

    print(predict_subscription(customer))
