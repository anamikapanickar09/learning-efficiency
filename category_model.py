import pandas as pd
import pickle

df = pd.read_pickle("dataset.pkl")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

le = LabelEncoder()
df['Category_Label'] = le.fit_transform(df['Category'])

X = df[['TotalStudyTime', 'MaterialEngagement', 'ContentCompletionRate', 'ExamAccuracy', 'TimeEfficiency', 'ScoreImprovement']]
y = df['Category_Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=le.classes_))
