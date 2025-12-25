import streamlit as st
import pickle
import os
import time
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Scam / Spam Detection AI",
    page_icon="🛡️",
    layout="centered"
)

MODEL_FILE = "spam_model.pkl"

# ---------------- MODEL LOADER ----------------
@st.cache_resource
def load_or_train_model():
    if os.path.exists(MODEL_FILE):
        with open(MODEL_FILE, "rb") as f:
            return pickle.load(f)

    # Train model if pickle doesn't exist
    df = pd.read_csv("spam.csv", encoding="latin-1")
    df = df[['v1', 'v2']]
    df.columns = ['label', 'text']
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['text'])
    y = df['label']

    model = MultinomialNB()
    model.fit(X, y)

    with open(MODEL_FILE, "wb") as f:
        pickle.dump((vectorizer, model), f)

    return vectorizer, model


# Load model safely
vectorizer, model = load_or_train_model()

# ---------------- FUTURISTIC UI ----------------
st.markdown("""
<style>

/* Background image */
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1601597119094-5c0f86eecf78");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Dark glass overlay */
section.main {
    background: rgba(0,0,0,0.65);
    padding: 30px;
    border-radius: 20px;
}

/* Title glow */
h1 {
    text-align: center;
    color: #00fff9;
    text-shadow: 0 0 10px #00fff9, 0 0 25px #00fff9;
}

/* Text area */
textarea {
    background: rgba(0,0,0,0.6) !important;
    color: #00fff9 !important;
    border: 2px solid #00fff9 !important;
    border-radius: 15px !important;
    padding: 15px !important;
    font-size: 16px !important;
}

/* Button */
.stButton>button {
    background: #00fff9;
    color: #000;
    font-weight: bold;
    border-radius: 15px;
    padding: 12px 30px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    background: #000;
    color: #00fff9;
    box-shadow: 0 0 15px #00fff9, 0 0 30px #00fff9;
}

/* Prediction box */
.prediction {
    border: 2px solid #00fff9;
    border-radius: 18px;
    padding: 25px;
    margin-top: 25px;
    text-align: center;
    font-size: 22px;
    box-shadow: 0 0 25px #00fff9;
    animation: pulse 1.5s infinite alternate;
}

@keyframes pulse {
    from { box-shadow: 0 0 15px #00fff9; }
    to { box-shadow: 0 0 35px #00fff9; }
}

</style>
""", unsafe_allow_html=True)

# ---------------- APP CONTENT ----------------
st.title("🛡️ Scam / Spam Detection AI")
st.markdown(
    "<p style='text-align:center;'>🔍 Enter a message and let the AI scan it like a cyber HUD</p>",
    unsafe_allow_html=True
)

user_input = st.text_area("📩 Enter message")

if st.button("⚡ Scan Message"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to scan.")
    else:
        placeholder = st.empty()

        # Scanner animation
        for i in range(3):
            placeholder.markdown(
                f"<div class='prediction'>🔎 Scanning{'.' * i}</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.6)

        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]

        if prediction == 1:
            placeholder.markdown(
                "<div class='prediction'>🚨 THREAT DETECTED<br>⚠️ This message is SPAM</div>",
                unsafe_allow_html=True
            )
        else:
            placeholder.markdown(
                "<div class='prediction'>✅ SYSTEM CLEAR<br>Safe Message</div>",
                unsafe_allow_html=True
            )
