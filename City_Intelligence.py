import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("🌆 City Intelligence")

st.subheader("🗺 City Issues Map")

m = folium.Map(location=[19.07, 72.87], zoom_start=12)

folium.Marker([19.07,72.87], popup="High Traffic").add_to(m)
folium.Marker([19.08,72.88], popup="Accident Zone").add_to(m)
folium.Marker([19.06,72.86], popup="Pothole Area").add_to(m)

st_folium(m, width=700, height=400)

st.subheader("🤖 Smart City AI Assistant")

query = st.text_input("Ask about city status:")

if query:
    st.success("Traffic congestion is high in Zone 2.")

st.subheader("📑 Daily City Report")

st.text_area("Report", "Traffic high, AQI moderate, accidents detected.", height=150)
