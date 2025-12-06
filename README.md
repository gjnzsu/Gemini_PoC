# Gemini Chatbot PoC

A simple, interactive chatbot application powered by Google's Gemini LLM and built with Streamlit.

## Features
- **Generative AI**: Uses Google's Gemini Pro model for natural language responses.
- **Chat Interface**: Clean, chat-like UI provided by Streamlit.
- **Session History**: Maintains context within the current chat session.

## Prerequisites
- Python 3.8+
- A Google Cloud Project with the **Gemini API** enabled.
- A valid **Gemini API Key**.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/gjnzsu/Gemini_PoC.git
    cd Gemini_PoC
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**:
    - Create a `.env` file in the root directory (you can copy `.env.example`).
    - Add your API Key:
      ```env
      GEMINI_API_KEY=your_api_key_here
      ```

## Usage

Run the Streamlit application:

```bash
streamlit run main.py
```

The application will open in your default web browser (usually at `http://localhost:8501`).

## Structure
- `main.py`: The entry point for the Streamlit application.
- `gemini_utils.py`: Helper functions for Gemini API configuration and interaction.
- `.env`: (Ignored by Git) Stores your sensitive API credentials.
