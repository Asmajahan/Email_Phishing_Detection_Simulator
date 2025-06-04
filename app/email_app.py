import streamlit as st
import joblib
import re
import numpy as np
from scipy.sparse import hstack, csr_matrix
import os

# === Load model and vectorizer ===
current_dir = os.path.dirname(__file__)
model_dir = os.path.abspath(os.path.join(current_dir, "..", "model"))

model_path = os.path.join(model_dir, "phishing_model.pkl")
vectorizer_path = os.path.join(model_dir, "tfidf_vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# === Clean email text ===
def clean_email(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# === Extract features ===
def extract_features(text):
    text = text.lower()
    has_link = int(bool(re.search(r'http[s]?://|www\.', text)))
    has_money_words = int(bool(re.search(r'win|prize|gift|money|cash|reward', text)))
    has_urgent_words = int(bool(re.search(r'urgent|immediate|alert|important|verify', text)))
    has_bank_words = int(bool(re.search(r'bank|account|secure|login|password', text)))
    return np.array([has_link, has_money_words, has_urgent_words, has_bank_words])

# === Streamlit UI ===
st.set_page_config(page_title="Email Phishing Detector", page_icon="🛡️")
st.title("🕵️‍♂️ Email Phishing Detection Simulator")
st.markdown("Check whether an email is **phishing** or **legit** by pasting its content below.")

email_input = st.text_area("📨 Paste the Email Content:", height=200)

if st.button("Detect"):
    if not email_input.strip():
        st.warning("⚠️ Please enter the email content.")
    else:
        cleaned = clean_email(email_input)
        vectorized = vectorizer.transform([cleaned])
        binary_feats = extract_features(email_input)
        combined_feats = hstack([vectorized, csr_matrix(binary_feats)])

        prediction = model.predict(combined_feats)[0]

        if prediction == 1:
            st.error("🚨 **Phishing Alert!** This email is likely a phishing attempt.")
        else:
            st.success("✅ This email appears to be **safe**.")

# === Footer ===
st.markdown("---")
st.caption("🔒 Built by Asmajahan Karkal | Email Phishing Detection Simulator 🚀")
