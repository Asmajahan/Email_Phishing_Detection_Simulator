🛡️ Email Phishing Detection Simulator
======================================

A machine learning-powered app that detects phishing emails using NLP and binary keyword features. Built with Streamlit, this simulator analyzes raw email content and flags it as **phishing** or **legit** based on patterns learned from real-world email data.

**Live Demo**: _\[Add deployment link here\]_

* * *

🔍 Project Overview
-------------------

This app is a cybersecurity-focused simulator that demonstrates how phishing detection can be automated using machine learning. It takes raw email content (subject + body), processes it with NLP techniques, and enhances detection using key binary indicators like the presence of links, money-related terms, urgency, and bank-related keywords.

The model is trained using a Random Forest classifier with TF-IDF vectorization, offering strong accuracy and practical value.

* * *

🚀 Features
-----------

*   📬 Accepts raw email input (subject + body combined)
    
*   🧹 Preprocesses text: lowercasing, HTML tag and punctuation removal
    
*   🧠 Adds binary features for phishing indicators (e.g., links, urgent words)
    
*   🤖 Trained using Random Forest + TF-IDF
    
*   💻 Streamlit app for an intuitive user interface
    
*   ⚠️ Flags emails as **Phishing** or **Legit**
    
*   ✅ Modular, tested, and ready for deployment
    

* * *

## 🗂️ Project Structure

```
EMAIL-PHISHING-SIMULATOR/
├── app/
│   └── email_app.py               # Streamlit UI + model prediction code
├── data/
│   ├── email_dataset.csv          # Raw labeled email data
│   └── combined_email_dataset.csv # Cleaned and combined data (generated after training)
├── model/
│   ├── phishing_model.pkl         # Trained ML model (Random Forest)
│   └── tfidf_vectorizer.pkl       # TF-IDF vectorizer used for preprocessing
├── notebooks/
│   └── emaildata.ipynb            # Jupyter notebook to train and save model
├── requirements.txt               # Python dependencies
└── README.md                      # You’re reading it!
```


* * *

📦 Installation & Running Locally
---------------------------------

### 1\. Clone the repository:

```
git clone https://github.com/yourusername/email-phishing-simulator.git
cd email-phishing-simulator
```

### 2\. Install required packages:

`pip install -r requirements.txt` 

### 3\. Train the model (if not done already):

`# Run this inside the notebooks/emaildata.ipynb` 

This generates:

*   `model/phishing_model.pkl`
    
*   `model/tfidf_vectorizer.pkl`
    
*   `data/combined_email_dataset.csv`
    

### 4\. Run the Streamlit app:

`streamlit run app/email_app.py` 

* * *

🧠 Model Overview
-----------------

**Preprocessing:**

*   Lowercase conversion
    
*   HTML tag removal
    
*   Punctuation and stopword cleaning
    

**Feature Extraction:**

*   TF-IDF vectorization (top 5000 terms)
    
*   Binary features:
    
    *   Contains a link
        
    *   Contains urgency terms
        
    *   Contains money-related words
        
    *   Contains bank/account terms
        

**Model Used:** Random Forest Classifier  
**Accuracy:** ~90% on test split  
**Dataset:** Custom labeled set of phishing and legit emails

* * *

✅ Use Cases
-----------

*   📚 Cybersecurity training tool for students
    
*   🧪 Simulation for phishing awareness campaigns
    
*   🛡️ Foundation for building real-time phishing detection systems
    
*   🧰 Integration-ready tool for future email security scanners
    

* * *

🧾 License
----------

This project is licensed under the **MIT License**.
