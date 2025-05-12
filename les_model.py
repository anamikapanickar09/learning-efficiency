import pandas as pd
import pickle

df = pd.read_pickle("dataset.pkl")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = df[['TotalStudyTime', 'MaterialEngagement', 'ContentCompletionRate', 'ExamAccuracy', 'TimeEfficiency', 'ScoreImprovement']]
y = df['LES']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

reg = LinearRegression()

reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)
print("R² Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
