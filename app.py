import streamlit as st
import joblib
import pandas as pd
from feature_extraction import extract_features

st.set_page_config(page_title="Phishing URL Detector", page_icon="🔍")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .stButton>button {
        background-color: #2c7da0;
        color: white;
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #61a5c2;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#0077b6;'>🔍 Phishing URL Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Paste a URL below to check if it's safe.</p>", unsafe_allow_html=True)

model = joblib.load("phishing_model.pkl")

url = st.text_input("Enter a URL:")

if st.button("Check URL"):
    if url:
        with st.spinner("Analyzing..."):
            features = extract_features(url)
            feature_order = ['url_length', 'valid_url', 'at_symbol', 'sensitive_words_count',
                              'path_length', 'isHttps', 'nb_dots', 'nb_hyphens', 'nb_and',
                              'nb_or', 'nb_www', 'nb_com', 'nb_underscore']
            input_df = pd.DataFrame([features])[feature_order]
            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0]

        if prediction == 0:
            st.error(f"⚠️ SUSPICIOUS (Phishing risk: {probability[0]*100:.1f}%)")
        else:
            st.success(f"✅ SAFE (Legitimate confidence: {probability[1]*100:.1f}%)")
    else:
        st.warning("Please enter a URL first.")