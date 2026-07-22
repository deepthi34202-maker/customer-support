import streamlit as st
from transformers import pipeline

# Use BlenderBot model (no tokenizers build issues)
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

st.title("AI Customer Support Assistant")

user_input = st.text_input("Ask a question:")
if user_input:
    response = chatbot(user_input)
    st.write("**Assistant:**", response[0]['generated_text'])
