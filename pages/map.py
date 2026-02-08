import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

st.title("🗺️ Smart City Complaint Map")

file = "data/complaints.csv"

if os.path.exists(file):
    df = pd.read_csv(file)

    if "Latitude" not in df.columns or "Longitude" not in df.columns:
       st.error("Latitude and Longitude not found in complaints data. Please submit new complaints with location.")
       st.stop()


    # convert to numeric
    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

    df = df.dropna(subset=["Latitude", "Longitude"])

    m = folium.Map(location=[df["Latitude"].mean(), df["Longitude"].mean()], zoom_start=12)

    for i, row in df.iterrows():
        color = "red" if row["Sentiment"] == "Negative" else "orange" if row["Sentiment"] == "Neutral" else "green"

        folium.Marker(
            [row["Latitude"], row["Longitude"]],
            popup=f"{row['Complaint']} ({row['Sentiment']})",
            icon=folium.Icon(color=color)
        ).add_to(m)

    st_folium(m, width=700, height=500)

else:
    st.warning("No complaint data available yet")
