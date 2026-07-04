# Chatbot using open ai...

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=0)

respons = model("Where is the capital of India?")

print(respons.content)