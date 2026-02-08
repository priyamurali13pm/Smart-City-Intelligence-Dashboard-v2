import streamlit as st
import pandas as pd
import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(report_text, receiver_email):
    sender_email = "priyabharani13pm@gmail.com"        # 🔴 replace
    sender_password = "naed oyjl uapu looe"  # 🔴 replace

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Smart City Daily Report"

    msg.attach(MIMEText(report_text, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        return str(e)


st.title("🤖 Smart City AI Assistant")

file = "data/complaints.csv"

if not os.path.exists(file):
    st.warning("No complaints data found. Please submit complaints first.")
    st.stop()

# Load complaints
df = pd.read_csv(file)

st.write("Ask questions about citizen complaints:")

query = st.text_input("Your question:")

if st.button("Ask"):
    if query.strip() == "":
        st.warning("Please enter a question")
    else:
        # Convert CSV to text context
        context = df.to_string(index=False)

        prompt = f"""
You are a Smart City REPORT AGENT.

Your task is to generate a structured city report
based ONLY on the complaints data provided.

Follow this exact format:

SMART CITY DAILY REPORT
1. Total Complaints:
2. Key Issues Identified:
3. Locations Affected (Latitude, Longitude):
4. Sentiment Summary:
5. Recommended Actions:

Complaints Data:
{context}

User Request:
{query}

Generate the report now:
"""

        result = subprocess.run(
            ["ollama", "run", "gemma:2b"],
            input = prompt,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
           st.success(result.stdout)
           st.session_state["report_text"] = result.stdout


        st.markdown("---")
st.subheader("📧 Send Report to Authority")

receiver_email = st.text_input("Enter authority email address")

if st.button("Send Report Email"):
    if receiver_email.strip() == "":
        st.warning("Please enter an email address")
    elif "report_text" not in st.session_state:
        st.warning("Please generate a report first")
    else:
        email_status = send_email(
        st.session_state["report_text"],
        receiver_email
    )

        if email_status is True:
            st.success("✅ Report sent successfully!")
        else:
            st.error(f"❌ Email failed: {email_status}")

