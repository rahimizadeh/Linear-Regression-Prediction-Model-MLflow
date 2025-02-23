import mlflow
import mlflow.projects

mlflow.projects.run(
    uri='./',
    entry_point='main',
    experiment_name="Salary_Model",
    env_manager="local"  # <--- Critical for VS Code on Windows
)