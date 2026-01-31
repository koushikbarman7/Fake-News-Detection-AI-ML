import streamlit as st
import pickle
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords (only first time)
nltk.download('stopwords')

# Page config
st.set_page_config(
    page_title="Fake News Detection for Students",
    layout="centered"
)

# Title
st.title("📰 Fake News Detection for Students")
st.write("An AI-ML based web application to detect Fake or Real news")

# Load trained model & vectorizer
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("vectorizer.pkl", "rb"))

# Text preprocessing
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', str(text))
    text = text.lower().split()
    text = [ps.stem(word) for word in text if word not in stop_words]
    return ' '.join(text)

# User input
st.subheader("🔍 Enter News Text")
user_input = st.text_area(
    "Paste news headline or article here:",
    height=180,
    placeholder="Example: Government confirms new education policy..."
)

# Prediction function
def predict_news(news):
    cleaned_news = clean_text(news)
    vectorized_news = tfidf.transform([cleaned_news])
    prediction = model.predict(vectorized_news)

    if prediction[0] == 1:
        return "FAKE NEWS"
    else:
        return "REAL NEWS"

# Button
if st.button("Check News"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some news text.")
    else:
        result = predict_news(user_input)

        if result == "FAKE NEWS":
            st.error("🚨 This news is **FAKE**")
        else:
            st.success("✅ This news is **REAL**")

# Footer
st.markdown("---")
st.markdown("👨‍🎓 **Project:** Fake News Detection for Students")
st.markdown("🧠 **Technologies:** AI, Machine Learning, NLP, Streamlit")
