import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Smart City Reports", layout="wide")
st.title("📊 Smart City Analytics Dashboard")

# ---------- SUMMARY METRICS ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric("🚑 Accidents Today", 5)
col2.metric("👥 Crowd Alerts", 8)
col3.metric("💬 Negative Complaints", 12)
col4.metric("🌫️ AQI Level", "92 (Moderate)")

st.markdown("---")

# ---------- BAR CHART ----------
st.subheader("Overall Detection Summary")

summary_data = pd.DataFrame({
    "Module": ["Accident", "Crowd", "Traffic", "Complaints"],
    "Count": [5, 8, 12, 20]
})

st.bar_chart(summary_data.set_index("Module"))

# ---------- PIE CHART ----------
st.subheader("Citizen Complaint Sentiment Distribution")

file = "data/complaints.csv"

if os.path.exists(file):
    df = pd.read_csv(file)

    sentiment_counts = df["Sentiment"].value_counts()

    fig, ax = plt.subplots()
    ax.pie(sentiment_counts.values,
           labels=sentiment_counts.index,
           autopct="%1.1f%%",
           startangle=90)
    ax.set_title("Complaint Sentiment")
    st.pyplot(fig)

else:
    st.warning("No complaint data available yet")

# ---------- TABLE ----------
st.subheader("Recent Activity Log")

table_df = pd.DataFrame({
    "Time": ["10:20 AM", "10:35 AM", "11:00 AM", "11:15 AM"],
    "Type": ["Accident", "Complaint", "Traffic", "Complaint"],
    "Description": [
        "Two vehicles collision",
        "Streetlight not working",
        "Heavy congestion near station",
        "Garbage not collected"
    ],
    "Severity": ["High", "Negative", "Medium", "Negative"]
})

st.dataframe(table_df, use_container_width=True)

# ---------- INSIGHTS ----------
st.subheader("AI Insights")
st.info("""
- High number of complaints related to streetlight and garbage.
- Traffic congestion observed during peak hours.
- AQI level indicates moderate air pollution.
Authorities should prioritize road safety and waste management.
""")
