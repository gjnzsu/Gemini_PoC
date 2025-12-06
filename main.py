import streamlit as st
from dotenv import load_dotenv
import gemini_utils

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Gemini Chatbot PoC")

# Configure GenAI
try:
    gemini_utils.configure_gemini()
except Exception as e:
    st.error(f"Configuration Error: {e}")
    st.stop()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize Gemini Chat Session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = gemini_utils.create_chat_session()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Thinking..."):
            full_response = gemini_utils.get_gemini_response(st.session_state.chat_session, prompt)
            
        if full_response.startswith("Error:"):
            message_placeholder.error(full_response)
        else:
            message_placeholder.markdown(full_response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
