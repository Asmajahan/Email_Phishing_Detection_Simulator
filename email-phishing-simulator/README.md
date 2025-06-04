# 🛡️ Email Phishing Detection Simulator

A machine learning-powered app that detects phishing emails using NLP and binary features. Built with Streamlit, this simulator analyzes raw email content and flags it as **phishing** or **legit** based on patterns learned from real-world email data.

Live Demo: _[Add deployment link here]_

---

## 🔍 Project Overview

This app is part of a cybersecurity simulation to demonstrate how phishing detection can be automated using machine learning. The model was trained on a custom dataset combining subject and body of emails, cleaned with NLP techniques, and enhanced with binary keyword-based features.

---

## 🚀 Features

- 📬 Accepts raw email input (subject + body)
- 🧹 Text cleaning + binary feature extraction
- 🧠 ML model using Random Forest + TF-IDF vectorization
- 💻 Built with Streamlit (easy to use UI)
- 📊 Classification output: Legit or Phishing
- ✅ Clean, tested, and ready for deployment

---

## 🗂️ Project Structure
 📁 EMAIL-PHISHING-SIMULATOR
 ├── 📁 data
 │   ├── email_dataset.csv                  # Original or raw dataset
 │   └── 📁 notebooks
 │       └── 📁 app\model
 │           ├── email_app.py               # Main backend script for Streamlit app
 │           ├── phishing_model.pkl         # Trained phishing detection model
 │           ├── tfidf_vectorizer.pkl       # TF-IDF vectorizer used for email preprocessing
 │           ├── combined_email_dataset.csv # Combined and cleaned dataset
 │           └── emaildata.ipynb            # Jupyter notebook for EDA and model training
 ├── README.md                              # Project overview and documentation
 └── requirements.txt                       # List of Python dependencies
               

