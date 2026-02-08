import streamlit as st
import subprocess

st.title("Urban Intelligence Chatbot 🤖")

prompt = st.text_input("Ask something:")

if st.button("Send"):
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    st.write(result.stdout)
