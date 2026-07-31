import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Setup NLTK
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+\s*', ' ', text)
    text = re.sub(r'RT|cc', ' ', text)
    text = re.sub(r'#\S+', '', text)
    text = re.sub(r'@\S+', '  ', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    tokens = word_tokenize(text)
    cleaned_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words and len(word) > 2
    ]
    return " ".join(cleaned_tokens)

# Load saved models
@st.cache_resource
def load_models():
    model = joblib.load('logistic_regression_model.pkl')
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    encoder = joblib.load('label_encoder.pkl')
    return model, tfidf, encoder

model, tfidf, encoder = load_models()

# Streamlit App UI
st.title("📄 AI Resume Categorizer")
st.write("Paste candidate resume text below to automatically classify their job domain.")

user_input = st.text_area("Paste Resume Text Here:", height=250)

if st.button("Categorize Resume"):
    if user_input.strip():
        cleaned = preprocess_text(user_input)
        vectorized = tfidf.transform([cleaned])
        pred_code = model.predict(vectorized)[0]
        category = encoder.inverse_transform([pred_code])[0]

        st.success(f"**Predicted Category:** {category}")
    else:
        st.warning("Please paste resume text before clicking predict.")
