from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#loading gemini pro vision to generate responses

model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
  if input!= "":
    response = model.generate_content([input, image])
  else:
    response = model.generate_content(image)
  return response.text

##setting up streamlit app

st.set_page_config(page_title="Image description")

st.header("LLM application")
input=st.text_input("Input: ", key="input")
uploaded_file = st.file_uploader("Choose an image: ", type=["jpg", "jpeg","png"])
image=""
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption="Uploaded image.", use_column_width=True)


submit=st.button("Tell me something about the image")

#if submit has been clicked
if submit:
  response=get_gemini_response(input,image)
  st.subheader("Response: ")
  st.write(response)