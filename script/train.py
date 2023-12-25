import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


data = pd.read_csv("training_data.csv")
print(data.columns)

split_size = 0.3
target = ["temperature"]
x = data.drop(target, axis=1)
y = data[target]
x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size=split_size)


def compute_regression_metrics(y_true, y_pred):
    return {
        "mae": mean_absolute_error(y_true, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_true, y_pred)),
        "r2": r2_score(y_true, y_pred)
    }

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def build_preprocessor(numeric_features: list, categorical_features: list) -> ColumnTransformer:
    numeric_transformer = Pipeline(steps=[("scaler", SimpleImputer())])
    categorical_transformer = Pipeline(steps=[
            ("nan_resolve", SimpleImputer(strategy="constant", fill_value=0)), 
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers = [
            ("numeric", numeric_transformer, numeric_features),
            ("categorical", categorical_transformer, categorical_features)
        ]
    )

    return preprocessor


numeric_features, categorical_features = ["month_", "day_", "hour_", "temp_1", "temp_2", "temp_3", "temp_4"], ["station_id"]
preprocessor = build_preprocessor(numeric_features, categorical_features)
classifier = LinearRegression()
model = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", classifier)])

model.train(x_train, y_train)

y_pred = model.predict(x_validation)
metrics = compute_regression_metrics(y_validation, y_pred)

print(metrics)