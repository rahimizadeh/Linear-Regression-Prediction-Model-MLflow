# Salary Prediction Model with MLflow

A linear regression model trained using MLflow for tracking experiments.

## Setup
1. Install dependencies:  
   ```bash
   pip install mlflow pandas scikit-learn
2. Run the Project
    python run.py
   Salary Prediction Model with MLflow 🚀
A machine learning project demonstrating Linear Regression for salary prediction, with experiment tracking and model management using MLflow.

📌 Overview
This project predicts salaries based on three features:

Years of Experience

Age

Interview Score

It showcases:

MLflow Integration: Track experiments, metrics, and models.

Reproducibility: Use the MLproject file to run the project in a standardized environment.

Best Practices: Proper project structure, logging, and Git workflows.

🛠️ Tools & Libraries
Python

MLflow (Experiment tracking)

scikit-learn (Linear Regression)

pandas (Data handling)

🚀 Quick Start
Install dependencies:

bash
Copy
pip install mlflow pandas scikit-learn  
Run the project:

bash
Copy
python run.py  
View MLflow UI:

bash
Copy
mlflow ui --port 8080  
Open http://localhost:8080 to explore experiments.

📂 Repository Structure
Copy
├── main.py             # Training script  
├── run.py              # MLflow project runner  
├── MLproject           # MLflow project configuration  
├── Salary_predict.csv  # Dataset  
└── README.md           # Project documentation  
📊 MLflow Tracking
MLflow logs:

Parameters: Model configuration.

Metrics: RMSE, R2 score.

Artifacts: Trained model files and visualizations.

