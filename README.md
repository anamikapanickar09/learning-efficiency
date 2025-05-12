# Learning Efficiency Score (LES) Prediction 

This project builds two AI models to assess and categorize students' learning efficiency based on their study patterns and academic engagement.

It was developed as part of an internship project.

## 📊 Project Overview 


The system uses learning activity data to:

 
1. **Predict the Learning Efficiency Score (LES)**  — a score between 0 and 1.
 
2. **Classify students into 3 learner categories**  — *Basic*, *Intermediate*, or *Expert*.


## ⚙️ Project Structure 



```bash
learning-efficiency-score/
│
├── data_cleaning.py                # Cleans and prepares raw Excel datasets
├── build_features.py               # Extracts features (e.g., Study Time, Exam Accuracy)
├── build_dataset.py                # Combines features into final dataset for training
├── les_model.py                    # Builds regression model to predict LES
├── category_model.py               # Builds classification model to predict student category
├── dataset.pkl                     # Saved dataset (features and labels)
├── Learning Efficiency Score.pdf   # Reference document for methodology
│
└── Report/                         # Folder containnig raw data
    ├── coursetrackingActivity.xlsx
    ├── exams.xlsx
    ├── exam_details.xlsx
    ├── login_activity.xlsx
    ├── timetaken.xlsx
    └── user_level_completion.xlsx
```


## 📝 Input Features 

| Feature | Description | 
| --- | --- | 
| Total Study Time (TST) | Total time spent logged in | 
| Material Engagement (ME) | Time spent on material ÷ total material duration | 
| Content Completion Rate (CCR) | Chapters viewed ÷ total chapters | 
| Exam Accuracy (EA) | Correct answers ÷ total questions | 
| Time Efficiency (TE) | Avg. time on correct answers ÷ avg. time on incorrect answers | 
| Score Improvement (SI) | (Latest score − First score) ÷ First score | 


All features are normalized to a 0–1 scale.


## 🎯 Outputs 

| Model | Output | Technique | 
| --- | --- | --- | 
| LES Model | Learning Efficiency Score (0 to 1) | Linear Regression | 
| Category Model | Student Category: Basic, Intermediate, Expert | Logistic Regression | 


> **Category Label Mapping** :

Basic → 0.25 LES

Intermediate → 0.50 LES

Expert → 0.75 LES


## 🛠️ How It Works 

 
1. **Data Cleaning** 

  → Cleans and standardizes raw Excel files (`Report/`) using `data_cleaning.py`.
 
2. **Feature Extraction** 

  → Calculates all 6 features with `build_features.py`.
 
3. **Dataset Building** 

  → Combines features and labels into a training dataset (`dataset.pkl`) using `build_dataset.py`.
 
4. **Model Training**

   - **Category Prediction** : Trains a logistic regression model (`category_model.py`)
 
   - **LES Prediction** : Trains a linear regression model (`les_model.py`)

 
5. **Applications**

 
   - Predict student’s **learning efficiency score**
 
   - Classify students into **Basic / Intermediate / Expert**
 
   - Provide **badges**  or **recommendations**  to students based on their category



## 🖋️ About 
- Developed during internship by Anamika Panickar
