from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful {domain} expert"),
        ("human", "Explain to me in simple terms what {topic} is.")
    ]
)

prompt = chat_template.invoke(
    {
        "domain": "teacher",
        "topic": "AI"
    }
)

print(prompt)