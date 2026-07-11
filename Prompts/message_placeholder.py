from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful customer support agent"),
        MessagesPlaceholder(variable_name='chat_history'),
        ("human", "{query}")
    ]
)

chat_history = []
# load chat history
try:
    with open(file='D:\Gen Ai\Prompts\chat_history.txt') as f:
        chat_history.append(f.readline())
except FileNotFoundError:
    print('file not found')

print(chat_history)

# create prompt
prompt = chat_template.invoke({
    'chat_history':chat_history,
    'query':'where is my refund'
})


print(prompt)
