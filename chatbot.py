from dotenv import load_dotenv
import os
import google.generativeai as genai
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response
