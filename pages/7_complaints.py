import streamlit as st
import pickle
import joblib
from datetime import datetime
import os
import pandas as pd

# Load model and vectorizer
model = joblib.load("citizen_sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("💬 Citizen Complaints Analysis (NLP)")
st.write("Enter a citizen complaint and analyze sentiment")

complaint = st.text_area("Enter complaint text:")

lat = st.text_input("Enter Latitude (example: 12.9716)")
lon = st.text_input("Enter Longitude (example: 77.5946)")

if st.button("Submit Complaint"):
    if complaint.strip() == "":
        st.warning("Please write your complaint")
    else:
        text_vec = vectorizer.transform([complaint])
        prediction = model.predict(text_vec)[0]

        sentiment = "Negative" if prediction == 0 else "Neutral" if prediction == 1 else "Positive"

        st.success(f"Sentiment: {sentiment}")

        # Save to CSV

        data = {
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Complaint": complaint,
            "Sentiment": sentiment,
            "Latitude":  lat,
            "Longitude": lon
        }

        file = "data/complaints.csv"
        os.makedirs("data", exist_ok=True)

        df = pd.DataFrame([data])
        if os.path.exists(file):
            df.to_csv(file, mode='a', header=False, index=False)
        else:
            df.to_csv(file, index=False)

        st.info("Complaint saved successfully")