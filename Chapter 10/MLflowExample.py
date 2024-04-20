
import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

mlflow.set_experiment('iris_rf_experiment')

with mlflow.start_run():
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)
    
    predictions = rf.predict(X_test)
    
    mlflow.log_param('n_estimators', 100)
    mlflow.log_metric('accuracy', accuracy_score(y_test, predictions))
    
    mlflow.sklearn.log_model(rf, "model")
