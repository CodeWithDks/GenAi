from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [

    SystemMessage(content="You are a helpful assistant."),
               
]

while True:

    user_query = input("You: ")

    if user_query != "bye":
        chat_history.append(HumanMessage(content=user_query))

        response = model.invoke(chat_history)
        chat_history.append(AIMessage(content=response.content))

        print("Ai: ", response.content)

    else:
        break

print(chat_history)