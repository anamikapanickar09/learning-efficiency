import pandas as pd

def get_cleaned_df_from_file(path: str, columns_to_remove: list):
    df = pd.read_excel(path)
    df.drop(columns_to_remove, axis=1, inplace=True)
    df.dropna(how='any', inplace=True)
    if "CreatedBy" in df.columns:
        df.rename(columns={"CreatedBy": "UserID"}, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def clean_course_tracking_activity():
    unwanted_columns = [
        "ActivityDependantData",
        "ActivityRelatedTo",
        "DownloadCount",
        "DateCreated",
        "ModifiedBy",
        "DateModified",
        "UserType",
        "LevelID",
        "CourseLID",
        "BatchID",
        "BatchCourseID",
        "StatusID",
        "ViewTimeline",
        "ViewCount",
    ]
    return get_cleaned_df_from_file("Report/coursetrackingActivity.xlsx", unwanted_columns)


def clean_time_taken():
    unwanted_columns = [
        "TimeTakenID",
        "DateCreated",
        "ModifiedBy",
        "DateModified",
        "UserType",
        "CourseLID",
        "BatchID",
        "StatusID",
    ]
    return get_cleaned_df_from_file("Report/timetaken.xlsx", unwanted_columns)

def clean_fe_responses():
    unwanted_columns = [
        "ResponseID",
        "FormID",
        "FormMappingID",
        "SourceType",
        "SourceID",
        "CompletionStatus",
        "CompletionTime",
        "TotalAttempts",
        "PartialQuestCount",
        "LateSubmissionStatus",
        "TotalScore",
        "Percentage",
        "OnBehalfOf",
        "Confidence",
        "AnswerSheetURL",
        "Comment",
        "ScormResponse",
        "StatusID",
        "DateCreated",
        "ModifiedBy",
        "DateModified",
    ]
    return get_cleaned_df_from_file("Report/exams.xlsx", unwanted_columns)

def clean_fe_response_select():
    df = pd.read_excel("Report/exam_details.xlsx")
    unwanted_columns = [
        "SelectedResponseID",
        "QuestionID",
        "AnswerID",
        "Skipped",
        "Confidence",
        "Comment",
        "ItemNumber",
        "ParentQuestionID",
        "LearnersComments",
        "StatusID",
        "ModifiedBy",
        "DateModified",
    ]
    return (
        get_cleaned_df_from_file("Report/exam_details.xlsx", unwanted_columns)
        .rename(columns={
        "ScoreAwarded": "IsAnswerCorrect",
        "DateCreated": "SubmitTime",
        "ResponseID": "ExamID",
        })
    )
