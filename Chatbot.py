import streamlit as st
import subprocess

# FULL PATH to Ollama (from your system)
OLLAMA_PATH = r"C:\Users\priya\AppData\Local\Programs\Ollama\ollama.exe"

st.title("🤖 Smart City AI Chatbot (Local LLM)")

st.write("Ask about traffic, AQI, accidents, overcrowding, or city planning.")

prompt = st.text_input("Enter your question:")

if st.button("Ask"):
    if prompt.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                result = subprocess.run(
                    [OLLAMA_PATH, "run", "gemma:2b", prompt],
                    capture_output=True,
                    text=True
                )

                if result.stdout:
                    st.success("AI Response:")
                    st.write(result.stdout)
                else:
                    st.error("Ollama returned no output.")
                    st.write(result.stderr)

            except Exception as e:
                st.error(f"Error running Ollama: {e}")
