import streamlit as st
from transformers import pipeline
from transformers.conversational import Conversation

# Load Hugging Face conversational model
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# FAQ data
faq_data = {
    "reset password": "Click 'Forgot Password' on the login page and follow the instructions.",
    "refund policy": "Refunds are available within 30 days of purchase with receipt.",
    "order status": "You can track your order in the 'My Orders' section of your account."
}

def get_faq_answer(user_query):
    for key in faq_data:
        if key in user_query.lower():
            return faq_data[key]
    return None

def chat(user_message):
    # First check FAQ
    faq_answer = get_faq_answer(user_message)
    if faq_answer:
        return faq_answer
    
    # Otherwise use DialoGPT
    conv = Conversation(user_message)
    response = chatbot(conv)
    return response.generated_responses[-1]

# Streamlit UI
st.title("AI Customer Support Assistant")
user_input = st.text_input("Ask a question:")
if user_input:
    answer = chat(user_input)
    st.write("**Assistant:**", answer)
