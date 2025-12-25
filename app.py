import streamlit as st
import pickle
import time

# --- Load trained model ---
with open("spam_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

# --- Custom CSS & HTML for background ---
st.markdown("""
<style>
/* Full-page container for background image */
[data-testid="stAppViewContainer"] > .main {
    background-image: url('https://images.unsplash.com/photo-1601597119094-5c0f86eecf78?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}

/* Overlay for text readability */
section.main {
    background: rgba(0, 0, 0, 0.6);
    padding: 20px;
    border-radius: 15px;
}

/* Neon title glow */
h1 {
    color: #00fff9;
    text-shadow: 0 0 5px #00fff9, 0 0 15px #00fff9, 0 0 30px #00fff9;
    text-align: center;
}

/* HUD input box */
textarea {
    background-color: rgba(0,0,0,0.5);
    color: #00fff9;
    border: 2px solid #00fff9;
    border-radius: 15px;
    padding: 15px;
    font-size: 16px;
    width: 100%;
}

/* Buttons neon effect */
.stButton>button {
    background-color: #00fff9;
    color: #0d0d0d;
    font-weight: bold;
    border-radius: 15px;
    border: 2px solid #00fff9;
    padding: 12px 30px;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #0d0d0d;
    color: #00fff9;
    box-shadow: 0 0 20px #00fff9, 0 0 40px #00fff9;
}

/* Prediction container */
.prediction {
    border: 2px solid #00fff9;
    border-radius: 15px;
    padding: 25px;
    margin-top: 20px;
    text-align: center;
    font-size: 22px;
    box-shadow: 0 0 25px #00fff9;
    animation: pulse 1.5s infinite alternate;
}

/* Pulse animation for prediction */
@keyframes pulse {
    0% {box-shadow: 0 0 20px #00fff9;}
    100% {box-shadow: 0 0 40px #00fff9;}
}
</style>
""", unsafe_allow_html=True)

# --- App Layout ---
st.title("🌌 Scam/Spam Detection AI")
st.write("<p style='text-align:center;'>Enter a message and let the AI scan it like a futuristic HUD.</p>", unsafe_allow_html=True)

# User input
user_input = st.text_area("Enter message here:")

# --- Prediction Logic ---
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message to predict.")
    else:
        placeholder = st.empty()
        
        # Scanner-style animation
        for i in range(3):
            placeholder.markdown(f"<div class='prediction'>🔍 Scanning{'.'*i}</div>", unsafe_allow_html=True)
            time.sleep(0.5)

        # Transform input and predict
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]

        # Show result
        if prediction == 1:
            placeholder.markdown("<div class='prediction'>⚠️ ALERT! SPAM DETECTED!</div>", unsafe_allow_html=True)
        else:
            placeholder.markdown("<div class='prediction'>✅ SAFE MESSAGE</div>", unsafe_allow_html=True)
