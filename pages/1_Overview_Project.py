import streamlit as st
import pandas as pd

st.title("📊 Project Overview")

st.markdown("""
## 🏗️ Smart City Intelligence System

This project consists of **multiple AI modules**, each solving a real urban problem.
""")

st.subheader("🔍 Computer Vision Modules")
st.markdown("""
- Accident Detection (YOLOv8)
- Pothole & Road Crack Detection
- Streetlight Detection
- Crowd Density Estimation (CNN)
""")

st.subheader("📈 Forecasting Modules")
st.markdown("""
- Traffic Forecasting (LSTM / ARIMA)
- Air Quality Index (AQI) Forecasting
""")

st.subheader("📝 NLP Module")
st.markdown("""
- Citizen Complaint Sentiment Analysis
- Issue categorization & insights
""")

st.subheader("☁️ Deployment & Alerts")
st.markdown("""
- Deployed on AWS EC2
- Email alerts using Amazon SES
- Interactive Streamlit dashboard
""")

st.markdown("## 🧠 Model Performance")

st.write("""
- **YOLOv8 Detection Accuracy:** ~92%
- **Crowd Density CNN Accuracy:** ~88%
- **Traffic Forecast MAE:** Low error (time-series optimized)
- **AQI Forecast R² Score:** ~0.91
- **NLP Sentiment Accuracy:** ~77%
""")


st.markdown("CHART")
data = pd.DataFrame({
    "Module": ["Accident", "Crowd", "Traffic", "AQI", "NLP"],
    "Performance (%)": [92, 88, 85, 91, 77]
})

st.bar_chart(data.set_index("Module"))


st.markdown("## 🔍 Key Insights")

st.markdown("""
- Accident detection helps identify **high-risk zones**
- Crowd density alerts prevent **overcrowding**
- AQI forecasting supports **health advisories**
- Complaint sentiment highlights **citizen pain points**
""")
