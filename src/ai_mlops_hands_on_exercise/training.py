import zipfile
from pathlib import Path

import joblib
import pandas as pd
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# load dataset
def load_data():
    zip_path = Path(__file__).resolve().parents[2] / "datasets" / "bank_marketing.zip"

    with zipfile.ZipFile(zip_path) as archive:
        with archive.open("bank-additional-full.csv") as file:
            return pd.read_csv(file, sep=";")


df = load_data().drop_duplicates()

# feature engineering
df["previously_contacted"] = (df["pdays"] != 999).astype(int)

X = df.drop(columns=["y", "duration", "pdays"])
y = df["y"].map({"no": 0, "yes": 1})

# train / validation / test (70/15/15)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=123, stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=123, stratify=y_temp
)

# feature preprocessing
numeric_features = X.select_dtypes("number").columns
categorical_features = X.select_dtypes("object").columns

preprocessor = ColumnTransformer(
    [
        (
            "num",
            make_pipeline(SimpleImputer(strategy="median"), StandardScaler()),
            numeric_features,
        ),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ]
)

# models
models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=100, class_weight="balanced", random_state=123
    ),
    "MLP": MLPClassifier(
        hidden_layer_sizes=(64, 32), max_iter=200, early_stopping=True, random_state=123
    ),
}

# training and validation
for name, classifier in models.items():
    model = make_pipeline(clone(preprocessor), classifier)
    model.fit(X_train, y_train)

    models[name] = model

    print(f"\n{name}")
    print(classification_report(y_val, model.predict(X_val)))

# final evaluation on test set
best_model = models["Random Forest"]

print("\nRandom Forest - Test Set")
print(classification_report(y_test, best_model.predict(X_test)))

# save trained pipeline
model_path = Path(__file__).resolve().parents[2] / "models" / "bank_model.joblib"
model_path.parent.mkdir(exist_ok=True)

joblib.dump(best_model, model_path)
