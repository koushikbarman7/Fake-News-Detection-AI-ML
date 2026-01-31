# 📰 Fake News Detection for Students (AI & ML)

An **Artificial Intelligence (AI)** and **Machine Learning (ML)** based project that detects whether a given news article is **Fake** or **Real** using **Natural Language Processing (NLP)** techniques.  
The trained model is deployed as a **Streamlit web application** for easy and interactive use by students.

---

## 📌 Project Description

Fake news has become a serious issue in the digital era, especially among students who rely heavily on online news and social media.  
This project aims to help students identify misinformation by analyzing news text and classifying it as **Fake** or **Real** using Machine Learning.

The system is trained using a labeled dataset and achieves an accuracy of **~91.47%**.  
Once trained, the model is saved and reused in a Streamlit-based web application for real-time predictions.

---

## 🎯 Objectives

- Detect fake and real news automatically  
- Apply NLP techniques for text preprocessing  
- Use Machine Learning for text classification  
- Deploy the trained model as a user-friendly web app  
- Help students avoid misinformation  

---

## 🧠 Technologies Used

### 🔹 Programming Language
- Python

### 🔹 AI / ML Concepts
- Artificial Intelligence
- Machine Learning
- Natural Language Processing (NLP)

### 🔹 Libraries & Frameworks
- scikit-learn
- pandas
- numpy
- nltk
- Streamlit

### 🔹 Algorithm
- Logistic Regression  
- TF-IDF (Term Frequency–Inverse Document Frequency)

---

## 📂 Dataset Information

- Dataset contains news articles labeled as **FAKE** or **REAL**
- Columns used:
  - `title`
  - `text`
  - `label`

Text data is cleaned and transformed into numerical form using **TF-IDF vectorization** before training.

---

## 🔄 Project Workflow

1. Data Collection  
2. Data Cleaning & Preprocessing  
3. Feature Extraction using TF-IDF  
4. Model Training (Logistic Regression)  
5. Model Evaluation (Accuracy ≈ 91.47%)  
6. Model Serialization (`model.pkl`, `vectorizer.pkl`)  
7. Web Application Development (Streamlit)  
8. Deployment  

---

## 📊 Model Performance

- **Accuracy:** 91.47%  
- Model trained and tested using train–test split  
- Balanced classification of fake and real news  

---

## 📁 Project Structure

```
Fake-News-Detection-AI-ML/
│
├── README.md
├── app.py
├── requirements.txt
├── model.pkl
└── vectorizer.pkl
```


---
## ▶️ How to Run the Project Locally
---

### 1️⃣ Clone the Repository

```bash
git clone https: https://github.com/koushikbarman7/Fake-News-Detection-AI-ML.git
cd Fake-News-Detection-AI-ML
```

### 2️⃣ Install Required Libraries
```bash
pip install -r requirements.txt
```
3️⃣ Run the Streamlit App
```bash
python -m streamlit run app.py
```
4️⃣ Open in Browser
```bash
http://localhost:8501
```
---
### 🌐 Web Application Features

User-friendly interface

Real-time fake/real news prediction

Fast and lightweight

No retraining required (uses saved model)
---
### 🚀 Deployment

The application can be deployed easily using Streamlit Community Cloud.

Steps:

Push project to GitHub

Login to Streamlit Community Cloud

Connect your GitHub repository

Select app.py

Deploy
---
### 🎓 Use Cases

College mini or major project

Internship project submission

AI / ML portfolio

Academic demonstrations
---
### 🔮 Future Enhancements

Deep Learning models (LSTM / BERT)

Multilingual fake news detection

News source credibility analysis

Visualization dashboard

User authentication system
---
### 👨‍🎓 Author

Koushik Barman
---
### 📜 License

This project is intended for educational and academic purposes only.
---
### ⭐ Acknowledgement

Thanks to open-source datasets and Python libraries that made this project possible.
