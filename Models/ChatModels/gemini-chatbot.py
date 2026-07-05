import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
)

st.title("🤖 Gemini Chatbot")
st.write("Ask me anything!")

# Initialize the model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_query = st.chat_input("Type your message...")

if user_query:
    # Display user message
    st.chat_message("user").markdown(user_query)

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )

    # Custom response
    if user_query.lower().strip() == "who are you?":
        bot_response = "I am a large language model chatbot built by AB SINGH."
    else:
        try:
            response = llm.invoke(user_query)
            bot_response = response.content
        except Exception as e:
            bot_response = f"Error: {str(e)}"

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)

    # Save bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )