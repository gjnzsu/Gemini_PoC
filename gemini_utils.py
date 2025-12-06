import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def configure_gemini():
    """Configures the Gemini API using the key from environment variables."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")
    
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        raise Exception(f"Failed to configure Gemini: {e}")

def create_chat_session():
    """Creates and returns a new chat session."""
    model = genai.GenerativeModel('gemini-pro')
    return model.start_chat(history=[])

def get_gemini_response(chat_session, prompt):
    """
    Sends a prompt to the chat session and returns the text response.
    """
    try:
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
