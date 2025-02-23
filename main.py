import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Set the tracking URI and experiment
mlflow.set_tracking_uri("http://127.0.0.1:8080")

# Check if the experiment exists, if not create it
experiment_name = "Salary_Model"
if not mlflow.get_experiment_by_name(experiment_name):
    mlflow.create_experiment(experiment_name)
mlflow.set_experiment(experiment_name)

# Training Data
df = pd.read_csv("./Salary_predict.csv") # Place the dataset in your project folder or replace it by its location

# Fix the column selection for X
X = df[["experience", "age", "interview_score"]]  
y = df[["Salary"]]

X_train, X_test, Y_train, Y_test = train_test_split(X, y, train_size=0.7, random_state=0)

# Set Auto logging for scikit-learn flavor
mlflow.sklearn.autolog()

# Train Model
lr = LinearRegression()
lr.fit(X_train, Y_train)

# Print Model Parameters
print("Model Coefficients (Weights):", lr.coef_)
print("Model Intercept (Bias):", lr.intercept_)
# Predicting a test data
print(X_test.iloc[[0]], lr.predict( X_test.iloc[[0]]))

# mlflow.delete_experiment(experiment_id="948967992832438054")
