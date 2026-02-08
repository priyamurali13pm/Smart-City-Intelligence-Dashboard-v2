import streamlit as st

st.sidebar.title("Smart City Dashboard")

menu = st.sidebar.radio(
    "Select Module",
    ["Home", "AQI Forecast", "YOLO Detection", "Chatbot", "SQL Dashboard", "City Intelligence"]
)

if menu == "Home":
    st.title("🏙 Smart City Intelligence System")
    st.write("Welcome to Smart City Dashboard")

elif menu == "AQI Forecast":
    st.title("🌫 AQI Forecast")
    # paste your AQI code here

elif menu == "YOLO Detection":
    st.title("🚦 Traffic / Accident / Crowd Detection")
    # paste your YOLO code here

elif menu == "Chatbot":
    st.title("🤖 AI Chatbot")
    # paste your Ollama chatbot code here

elif menu == "SQL Dashboard":
    st.title("🗄 SQL Analytics")
    # paste your SQL code here

elif menu == "City Intelligence":
    st.title("🌆 City Intelligence Report")
    # integrate AQI + YOLO + chatbot + report

st.markdown("""
### 🚦 AI-Powered Urban Monitoring & Forecasting Platform

This project is designed to support **smart city decision-making** using  
**Computer Vision, Machine Learning, Deep Learning, and NLP**.

#### 🔍 What this dashboard does:
- Detects **road accidents, potholes, cracks, streetlights**
- Estimates **crowd density**
- Forecasts **traffic & air quality (AQI)**
- Analyzes **citizen complaints sentiment**
- Sends **real-time alerts**

---

### 🧠 Technologies Used
- YOLOv8 (Object Detection)
- CNN (Crowd Density Estimation)
- LSTM / ARIMA (Time Series Forecasting)
- NLP (Sentiment Analysis)
- Streamlit (Dashboard)
- AWS EC2 & SES (Deployment & Alerts)

---

👈 Use the **sidebar** to explore the project.
""")