from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
 
load_dotenv()
 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
 
st.set_page_config(page_title="My Image Chat Bot", page_icon="🤖")
 
st.header("My Image Chat Bot")
 
question = st.text_input("Ask me anything about image")
 
uploaded_image = st.file_uploader("Choose an image...",type=["jpg", "jpeg", "png"])
 
submit_button = st.button("Ask")
 
image = ""
 
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
 
if submit_button:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([question,image])
    st.write(response.text)
 