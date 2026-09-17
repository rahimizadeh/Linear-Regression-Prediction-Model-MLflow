# Linear Regression Prediction Model with MLflow

A compact machine-learning project that predicts salary from `experience`, `age`, and `interview_score`, while tracking evaluation metrics and the trained model in MLflow.

## Setup

```bash
git clone https://github.com/rahimizadeh/Linear-Regression-Prediction-Model-MLflow.git
cd Linear-Regression-Prediction-Model-MLflow
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Start MLflow

```bash
mlflow server --host 127.0.0.1 --port 8080
```

Open `http://127.0.0.1:8080` in your browser.

The training script reads the tracking URI from `MLFLOW_TRACKING_URI`; if it is not set, it defaults to `http://127.0.0.1:8080`.

## Train and evaluate

```bash
python main.py
```

The script uses a held-out 30% test split (`random_state=42`) and logs:

- MAE
- RMSE
- R²
- test-split configuration
- trained scikit-learn model

You can also launch the MLflow Project wrapper:

```bash
python run.py
```

## Configuration

Optional environment variables:

```text
MLFLOW_TRACKING_URI
MLFLOW_EXPERIMENT_NAME
DATA_PATH
```

## Quick verification

```bash
python -m py_compile main.py run.py
```

With MLflow running:

```bash
python main.py
```

Then open the MLflow UI and confirm that the `Salary_Model` experiment contains `mae`, `rmse`, `r2`, and a model artifact.

## Repository structure

```text
├── main.py
├── run.py
├── MLproject
├── requirements.txt
├── Salary_predict.csv
└── README.md
```
