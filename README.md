🚀 Salary Prediction Model with MLflow 

A machine learning project demonstrating Linear Regression for salary prediction, with experiment tracking and model management using MLflow.


📌 Overview

   This project predicts salaries based on three features: Years of Experience, Age, and Interview Score

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
   1. Install dependencies:
         pip install mlflow pandas scikit-learn  
   2. Run the project:
         python run.py  

View MLflow UI:

1. Run the following command on Powershell or cmd (for running mlflow ui --port 8080):

   C:\Users\Keyvan\AppData\Roaming\Python\Python312\Scripts\mlflow server --host 127.0.0.0 --port 8080
  
2. Open http://localhost:8080 to explore experiments.
   
📊 MLflow Tracking
         MLflow logs:
         
            Parameters: Model configuration. 
            
            Metrics: RMSE, R2 score.
            
            Artifacts: Trained model files and visualizations.
            
📂 Repository Structure

      ├── main.py             # Training script  
      ├── run.py              # MLflow project runner  
      ├── MLproject           # MLflow project configuration  
      ├── Salary_predict.csv  # Dataset  
      └── README.md           # Project documentation  


