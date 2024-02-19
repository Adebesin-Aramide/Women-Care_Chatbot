from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables
import streamlit as st
import os
from streamlit_chat import message
import google.generativeai as genai

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Chatbot")

st.header("Women Care Chatbot")

# Container for chat history
response_container = st.container()
# Container for text input
text_container = st.container()

with text_container:
    query = st.text_input("Query: ", key="input")
    if query:
        with st.spinner("typing..."):
            response = get_gemini_response(query)
        with response_container:
            message(query, is_user=True)
            message(response)

