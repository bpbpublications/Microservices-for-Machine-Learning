
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_curve, auc

# Read the healthcare dataset into a Pandas DataFrame
data = pd.read_csv("healthcare_dataset.csv")

# Separate features and labels
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)

# Scale the features
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Train an SVM model
model_SVC = SVC(kernel='rbf', random_state=4)
model_SVC.fit(X_train, y_train)
y_pred_svm = model_SVC.decision_function(X_test)

# Train a logistic regression model
model_logistic = LogisticRegression(random_state=4)
model_logistic.fit(X_train, y_train)
y_pred_logistic = model_logistic.decision_function(X_test)

# Train a decision tree model
model_decision_tree = DecisionTreeClassifier(random_state=4)
model_decision_tree.fit(X_train, y_train)
y_pred_proba_decision_tree = model_decision_tree.predict_proba(X_test)[:, 1]

# Evaluate the models using ROC curve and AUC
logistic_fpr, logistic_tpr, _ = roc_curve(y_test, y_pred_logistic)
auc_logistic = auc(logistic_fpr, logistic_tpr)
svm_fpr, svm_tpr, _ = roc_curve(y_test, y_pred_svm)
auc_svm = auc(svm_fpr, svm_tpr)
decision_tree_fpr, decision_tree_tpr, _ = roc_curve(y_test, y_pred_proba_decision_tree)
auc_decision_tree = auc(decision_tree_fpr, decision_tree_tpr)

# Plot the ROC curve
plt.figure(figsize=(5,5), dpi=100)
plt.plot(svm_fpr, svm_tpr, linestyle='-', label=f'SVM (auc = {auc_svm:.3f})')
plt.plot(logistic_fpr, logistic_tpr, marker='.', label=f'Logistic (auc = {auc_logistic:.3f})')
plt.plot(decision_tree_fpr, decision_tree_tpr, marker='.', label=f'Decision Tree (auc = {auc_decision_tree:.3f})')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()
