from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image

import google.generativeai as genai


genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text






# ______streamlit____________


st.header("Gemini Application")
input = st.text_input("Input Prompt", key="input")
uploaded_file = st.file_uploader("Choose an image from invoice", type=["jpeg","jpg","png"])

image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image', use_column_width=True)

submit = st.button("tell me about the invoice")


input_prompt="""
you are an expert in understanding an invoices, We will uploaded image as invoice and you have to answer any question based on uploaded invoices
"""

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")
    
    


if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    
    st.subheader("the response is:")
    st.write(response)
