from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# load env
load_dotenv()

# step 1: sample documents
docments = [
    Document(
        page_content="Python is a popular programming language used for web development, automation, and data science.",
        metadata={"id": 1, "topic": "Python"}
    ),
    Document(
        page_content="Python is widely used in machine learning, artificial intelligence, and backend development.",
        metadata={"id": 2, "topic": "Python"}
    ),
    Document(
        page_content="Python provides simple syntax and a large ecosystem of libraries like NumPy and Pandas.",
        metadata={"id": 3, "topic": "Python"}
    ),
    Document(
        page_content="Java is an object-oriented programming language commonly used for enterprise applications.",
        metadata={"id": 4, "topic": "Java"}
    ),
    Document(
        page_content="Java supports platform independence through the Java Virtual Machine (JVM).",
        metadata={"id": 5, "topic": "Java"}
    ),
    Document(
        page_content="Machine learning enables computers to learn patterns from data without explicit programming.",
        metadata={"id": 6, "topic": "Machine Learning"}
    ),
    Document(
        page_content="Deep learning is a subset of machine learning that uses artificial neural networks.",
        metadata={"id": 7, "topic": "Machine Learning"}
    ),
    Document(
        page_content="Cricket is one of the most popular sports in India and is played between two teams.",
        metadata={"id": 8, "topic": "Sports"}
    ),
    Document(
        page_content="Football is the world's most popular sport and is played professionally in many countries.",
        metadata={"id": 9, "topic": "Sports"}
    ),
    Document(
        page_content="The Taj Mahal is located in Agra and is one of the Seven Wonders of the World.",
        metadata={"id": 10, "topic": "History"}
    ),
]

# step 2:  Initialize embedding
embedding = OpenAIEmbeddings()

# step 3: create the faiss vectore stor from documents
vectorstore = Chroma.from_documents(
    documents = docments,
    embedding = embedding,
    collection_name = 'programming_languages',
    persist_directory = r'D:\Gen Ai\Retriever'
)

# step 3: retriever
retriever = vectorstore.as_retriever(
    search_type = 'mmr',
    search_kwargs = {'k':2, 'lambda_mult':0.5}
)

# step 3: search query
query = 'Tell about about machine learning'

# step 4: retrieve relavent info
result = retriever.invoke(query)

# print the result
print('----Result----')
for i, doc in enumerate(result):
    print(f'{i+1}: {doc.page_content}')





