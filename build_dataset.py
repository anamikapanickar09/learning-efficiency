from build_features import *

from functools import reduce
import pandas as pd

dfs = [
    get_total_study_time_df(),
    get_material_engagement_df(),
    get_content_completion_rate_df(),
    get_exam_accuracy_df(),
    get_time_efficiency_df(),
    get_score_improvement_df()
]

df = reduce(lambda left, right: pd.merge(left, right, on='UserID'), dfs)
df['TotalStudyTime'] = df['TotalStudyTime'].dt.total_seconds()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
features = ['TotalStudyTime', 'TimeEfficiency', 'ScoreImprovement']
df[features] = scaler.fit_transform(df[features])

def assign_category(les):
    if les < 0.35:
        return 'Basic'
    elif les < 0.65:
        return 'Intermediate'
    else:
        return 'Expert'
category_to_score = {'Basic': 0.25, 'Intermediate': 0.50, 'Expert': 0.75}

weight = 1/6
df['LES'] = (
    weight * df['TotalStudyTime'] +
    weight * df['MaterialEngagement'] +
    weight * df['ContentCompletionRate'] +
    weight * df['ExamAccuracy'] +
    weight * df['TimeEfficiency'] +
    weight * df['ScoreImprovement']
)

df['Category'] = df['LES'].apply(assign_category)
df['LES_Score'] = df['Category'].map(category_to_score)

df.to_pickle("dataset.pkl")
print(df)
