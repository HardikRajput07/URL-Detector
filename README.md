# 🔍 Phishing URL Detector

A machine learning-based web application that detects phishing URLs in real time, 
helping users identify potentially malicious links before clicking them.

## Overview

Phishing remains one of the most common and effective cyberattack vectors, with 
attackers increasingly using sophisticated, convincing URLs to deceive users. This 
project applies machine learning to automatically flag suspicious URLs by analyzing 
structural and content-based patterns commonly found in phishing attempts.

## Features

- Real-time URL analysis and classification (Safe / Suspicious)
- Live connectivity check to verify if a URL is reachable and uses HTTPS
- Confidence score displayed alongside each prediction
- Simple, user-friendly web interface — no technical knowledge required
- Trained on a labeled dataset of phishing and legitimate URLs

## How It Works

1. The user submits a URL through the web interface.
2. The app extracts 13 key features from the URL, including length, use of 
   sensitive keywords (e.g., "login," "verify," "secure"), HTTPS usage, and 
   domain-level patterns (dots, hyphens, symbols).
3. These features are passed to a trained Random Forest classifier.
4. The model returns a prediction — Safe or Suspicious — along with a confidence score.

## Tech Stack

- **Python** — core language
- **scikit-learn** — model training (Random Forest Classifier)
- **pandas** — data processing
- **Streamlit** — web application framework
- **Requests** — live URL validation

## Model Performance

- **Accuracy:** 91.6% on held-out test data
- Balanced precision and recall across both phishing and legitimate URL classes

## Getting Started

\`\`\`bash
git clone https://github.com/HardikRajput07/URL-Detector.git
cd URL-Detector
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
\`\`\`

## Future Improvements

- Expand the training dataset for improved generalization
- Add browser extension support for real-time protection while browsing
- Incorporate additional features such as domain age and SSL certificate details

## Authors

- Hardik Rajput
- Vyom Panchal
