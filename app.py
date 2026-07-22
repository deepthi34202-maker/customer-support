import streamlit as st
from transformers import pipeline

# Load BlenderBot model (lighter, no tokenizers build issues)
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

def chat(user_message):
    response = chatbot(user_message)
    # BlenderBot returns a list of dicts, so we extract the text
    return response[0]['generated_text']

# Streamlit UI
st.title("AI Customer Support Assistant")
user_input = st.text_input("Ask a question:")
if user_input:
    answer = chat(user_input)
    st.write("**Assistant:**", answer)
