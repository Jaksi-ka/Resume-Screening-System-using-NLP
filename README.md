# Resume Screening System using NLP

An AI-powered web application built with Python, Natural Language Processing (NLP), and Machine Learning to automatically categorize resumes into job roles.

## 🚀 Features
* **Text Preprocessing:** Cleans resume text using Regular Expressions (Regex) and NLTK (lowercasing, stop-word removal, lemmatization).
* **Machine Learning Model:** Utilizes a **Logistic Regression** model trained with **TF-IDF Vectorization** achieving **99% accuracy**.
* **Interactive UI:** Built with **Streamlit** to allow users to paste candidate resumes and get instant category predictions.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Scikit-Learn, NLTK, Pandas, NumPy, Joblib, Streamlit

## 📂 Project Structure
* `app.py` - Main Streamlit web application script.
* `notebooks/` - Model training and evaluation code.
* `*.pkl` - Trained Logistic Regression model, TF-IDF vectorizer, and label encoder files.
