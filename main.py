"""Train and evaluate a linear-regression salary model with MLflow tracking."""

import os

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:8080")
EXPERIMENT_NAME = os.getenv("MLFLOW_EXPERIMENT_NAME", "Salary_Model")
DATA_PATH = os.getenv("DATA_PATH", "Salary_predict.csv")
FEATURES = ["experience", "age", "interview_score"]
TARGET = "Salary"


def train_and_evaluate():
    df = pd.read_csv(DATA_PATH)
    required = FEATURES + [TARGET]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    X = df[FEATURES]
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    metrics = {
        "mae": mean_absolute_error(y_test, predictions),
        "rmse": mean_squared_error(y_test, predictions) ** 0.5,
        "r2": r2_score(y_test, predictions),
    }

    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)
    with mlflow.start_run():
        mlflow.log_param("test_size", 0.30)
        mlflow.log_param("random_state", 42)
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(
            model,
            artifact_path="model",
            input_example=X_train.head(3),
        )

    print("Model coefficients:", dict(zip(FEATURES, model.coef_)))
    print("Intercept:", model.intercept_)
    print({name: round(value, 4) for name, value in metrics.items()})
    return model, metrics


if __name__ == "__main__":
    train_and_evaluate()
