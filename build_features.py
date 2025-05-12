from data_cleaning import *

def get_total_study_time_df():
    df = clean_course_tracking_activity()
    
    df["TimeTaken"] = df["EndTime"] - df["StartTime"]
    total_study_time = df.groupby("UserID")["TimeTaken"].sum()
    
    total_study_time_df = total_study_time.reset_index(name='TotalStudyTime')
    return total_study_time_df


def get_material_engagement_df():
    df = clean_time_taken()

    unique_items = df.drop_duplicates(subset=["UserID", "ItemID"])
    user_item_counts = unique_items.groupby("UserID")["ItemID"].count()
    user_time_spent = df.groupby("UserID")["TimeTaken"].sum()
    expected_time = user_item_counts * 600000   # assuming each item is 10 min long (600,000 ms)
    material_engagement = (user_time_spent / expected_time)

    material_engagement_df = material_engagement.reset_index(name="MaterialEngagement")
    return material_engagement_df


def get_content_completion_rate_df():
    raw_df = clean_course_tracking_activity()
    df = raw_df[raw_df["ActivityItemType"] == "Chapter"].copy()

    no_of_total_chapters = df["ActivityItemID"].nunique()
    df_unique = df.drop_duplicates(subset=["UserID", "ActivityItemID"])
    user_chapter_counts = df_unique.groupby("UserID")["ActivityItemID"].count()

    completion_df = user_chapter_counts.reset_index(name="ChaptersViewed")
    completion_df["ContentCompletionRate"] = completion_df["ChaptersViewed"] / no_of_total_chapters

    content_completion_rate_df = completion_df.drop(columns="ChaptersViewed")
    return content_completion_rate_df


def get_exam_accuracy_df():
    df = clean_fe_response_select()
    total_questions = df.groupby('UserID').size()

    correct_answers = df.groupby('UserID')['IsAnswerCorrect'].sum()
    exam_accuracy = correct_answers / total_questions
    exam_accuracy_df = exam_accuracy.reset_index(name='ExamAccuracy')

    return exam_accuracy_df

def get_time_efficiency_df():
    df = clean_fe_response_select()
    df_sorted = df.sort_values(by=['UserID', 'ExamID', 'SubmitTime'])

    df_sorted['TimeTaken'] = df_sorted.groupby(['UserID', 'ExamID'])['SubmitTime'].diff()
    df_valid = df_sorted.dropna(subset=['TimeTaken'])

    avg_time_correct = df_valid[df_valid['IsAnswerCorrect'] == 1].groupby('UserID')['TimeTaken'].mean()
    avg_time_incorrect = df_valid[df_valid['IsAnswerCorrect'] == 0].groupby('UserID')['TimeTaken'].mean()

    time_efficiency = (avg_time_correct / avg_time_incorrect).dropna()
    time_efficiency_df = time_efficiency.reset_index(name='TimeEfficiency')

    return time_efficiency_df

def get_score_improvement_df():
    df = clean_fe_responses()
    df_sorted = df.sort_values(by='StartTime')

    first_scores = df_sorted.groupby('UserID').first()['Score']
    last_scores = df_sorted.groupby('UserID').last()['Score']

    score_improvement = (last_scores - first_scores) / first_scores
    score_improvement_df = score_improvement.reset_index(name='ScoreImprovement')

    return score_improvement_df