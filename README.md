# Resume Screening System using NLP

## Project Overview

The Resume Screening System is a Natural Language Processing (NLP) based web application designed to automate the recruitment process by analyzing resumes and comparing them with job descriptions. The system helps recruiters identify the most suitable candidates by calculating similarity scores and ranking applicants based on their qualifications, skills, and experience.

---

## Objectives

- Automate resume screening and candidate ranking.
- Reduce manual effort in the recruitment process.
- Improve efficiency and consistency in candidate selection.
- Compare multiple Machine Learning and Deep Learning models for resume classification.

---

## Dataset Information

**Dataset Name:** Resume Dataset PDF

**Source:** Kaggle

**Link:** https://www.kaggle.com/datasets/hadikp/resume-data-pdf

**Categories Include:**
- Data Science
- Accountant
- Python Developer
- Java Developer
- HR
- Civil Engineer
- React Developer
- Banking
- DevOps Engineer
- And more

---

## NLP Pipeline

### Data Collection
Collect resume datasets for training and testing.

### Data Cleaning
Remove special characters, punctuation, and unwanted formatting.

### Tokenization
Split text into individual words or tokens.

### Stop Word Removal
Remove common words that provide little analytical value.

### Lemmatization
Convert words into their root forms.

### Feature Extraction
Generate numerical representations using:
- TF-IDF Vectorization
- Word Embeddings

---

## Machine Learning Models

### Logistic Regression
- Simple and efficient
- Performs well with TF-IDF features

### Random Forest
- Handles complex patterns
- Reduces overfitting through ensemble learning

### Support Vector Machine (SVM)
- Effective for high-dimensional text classification

---

## Deep Learning Models

### LSTM
Captures sequential and contextual information in text.

### Bi-LSTM
Processes text in both forward and backward directions for improved context understanding.

### BERT
Provides contextual word representations and achieves high NLP performance.

---

## Evaluation Metrics

The following metrics will be used to compare models:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC (if applicable)

---

## Application Workflow

Job Description Input
↓
Resume Upload
↓
Text Preprocessing
↓
Feature Extraction
↓
ML/DL Model Processing
↓
Similarity Score Calculation
↓
Candidate Ranking
↓
Results Dashboard

---

## Project Structure

```
Resume-Screening-System
│
├── data
├── notebooks
├── src
│   ├── preprocessing
│   ├── feature_extraction
│   ├── models
│   ├── evaluation
│   └── app
├── results
├── reports
├── presentations
├── screenshots
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Team Members and Responsibilities

### Member 01
- Dataset Collection
- Data Preprocessing
- Feature Extraction
- Logistic Regression Implementation

### Member 02
- Model Training
- Hyperparameter Tuning
- Performance Evaluation
- Random Forest and Bi-LSTM Implementation

### Member 03
- Application Development
- System Integration
- Report Writing
- SVM and BERT Implementation

---

## Technologies Used

- Python
- Natural Language Processing (NLP)
- Scikit-learn
- TensorFlow / Keras
- BERT Transformers
- Flask
- Pandas
- NumPy
- NLTK
- Git & GitHub

---

## Ethical Considerations

- Avoid bias in candidate ranking.
- Use balanced datasets.
- Perform fairness evaluations.
- Ensure human recruiters make final hiring decisions.
- Protect candidate data and privacy.

---

## Future Improvements

- Skill extraction and matching.
- Resume summarization.
- Interview recommendation system.
- Advanced semantic similarity using transformer models.
- Real-time recruiter dashboard.

---

## License

This project is developed for academic purposes as part of the NLP coursework project.
