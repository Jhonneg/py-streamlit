import os
from click import prompt
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv, find_dotenv


def ask_and_get_answer(prompt, img):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content([prompt, img])
    return response.text

def st_image_to_pil(st_image):
    import io
    from PIL import Image


load_dotenv(find_dotenv(), override=True)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

st.image("logo.svg", width=75)
st.subheader("Talking with an Image")
# st.image()
img = st.file_uploader("Select an image: ", type=["jpg", "jpeg", "png", "gif"])
if img:
    st.image(img, caption="Talk with this image.")

    prompt = st.text_area("Ask a question about this image: ")
    if prompt:
