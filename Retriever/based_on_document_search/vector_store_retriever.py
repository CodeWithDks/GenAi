from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI,OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Step 1 Your source documents
documents = [
    Document(
        page_content="This is all about Radha Rani Ji.",
        metadata={"source": "book1", "page": 1}
    ),
    Document(
        page_content="This is all about Lord Ram.",
        metadata={"source": "book1", "page": 2}
    ),
    Document(
        page_content="This is all about Lord Krishna.",
        metadata={"source": "book2", "page": 1}
    ),
    Document(
        page_content="This is all about Sita Ji.",
        metadata={"source": "book2", "page": 2}
    )
]
# step 2, Initialize embedding model
embedding = OpenAIEmbeddings()

# step 3: Create a Faiss vector store in memory
vectorstore = FAISS.from_documents(
    documents=documents,
    embedding=embedding,  
)


# save the vectorstore in locall on disk
vectorstore.save_local(r'D:\Gen Ai\Retriever')

# Step 4 convert vector store into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# step 5 
query = 'Tell me about sita'
result = retriever.invoke(query)
print("------ Result ------")

for i, doc in enumerate(result):
    print(f'{i+1}: {doc.page_content}')
