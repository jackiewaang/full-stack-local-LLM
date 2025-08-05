import streamlit as st
import requests
import time

st.title("Chat locally with your LLM")

# Message session
if "messages" not in st.session_state:
    st.session_state.messages = []

# LLM Model
model = st.selectbox(
            "Choose your LLM model",
            ("Qwen3-1.7B", "Llama3.2-1B")
        )

with st.form("chat_form", clear_on_submit=True):
    prompt = st.text_input("Query", key="input", placeholder="Ask your question here")
    submitted = st.form_submit_button("Send")

    if submitted and prompt:
        start_time = time.time()
        response = requests.post(
            "http://localhost:8000/",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        inference_time = time.time() - start_time
        result = response.json().get("response", "")

        st.session_state.messages.append({
            "user": prompt, 
            "bot": result, 
            "time": inference_time
        })

for chat in reversed(st.session_state.messages):
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown(f"**Inference time**: {chat['time']:.2f}s")
    st.markdown("---")





