import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv, find_dotenv


def ask_and_get_answer(prompt, img):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content([prompt, img])
    return response.text

if __name__ == "__name__":
    load_dotenv(find_dotenv(), override=True)
    genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

