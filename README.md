🚀 Salary Prediction Model with MLflow (https://mlflow.org/)

A machine learning project demonstrating Linear Regression for salary prediction, with experiment tracking and model management using MLflow.


📌 Overview

   This project predicts salaries based on three features: Years of Experience, Age, and Interview Score.

   It showcases:

      - MLflow Integration: Track experiments, metrics, and models.
      - Reproducibility: Use the MLproject file to run the project in a standardized environment.
      - Best Practices: Proper project structure, logging, and Git workflows.
   
🛠️ Tools & Libraries

      - Python
      - MLflow (Experiment tracking)
      - scikit-learn (Linear Regression)
      - pandas (Data handling)
   
🚀 Quick Start
   1. Install dependencies:

      ```bash

      pip install mlflow pandas scikit-learn
       
   3. Run the project:
      ```bash
         python run.py  

View MLflow UI:

1. Run MLflow like the following command on Powershell or cmd to run mlflow ui on port 8080:
      ```bash
   C:\Users\user-name\AppData\Roaming\Python\Python312\Scripts\mlflow server --host 127.0.0.0 --port 8080
  
2. Open http://localhost:8080 to explore experiments and Models.
   
📊 MLflow Tracking 

         MLflow logs:
         
            - Parameters: Model configuration. 
            - Metrics: RMSE, R2 score.
            - Artifacts: Trained model files and visualizations.     
📂 Repository Structure

      ├── main.py             # Training script  
      ├── run.py              # MLflow project runner  
      ├── MLproject           # YAML file for MLflow project configuration  
      ├── Salary_predict.csv  # Dataset  
      └── README.md           # Project documentation  


