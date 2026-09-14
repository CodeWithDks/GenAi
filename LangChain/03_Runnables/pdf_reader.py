from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()

# Initialize the LLM
model = ChatOpenAI()

# Load the document
loader = PyPDFLoader(r"Documents_Loader/documents/Keerthana_Know_Me_Better.pdf")
documents = loader.load()

# Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Create embeddings and store them in FAISS
embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

# Create retriever
retriever = vectorstore.as_retriever()

# Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=model,
    retriever=retriever,
    chain_type="stuff"
)

# Ask a question
while True:
    query = input("Enter your question (or type 'exit' to quit): ")
    if query.lower() == 'exit':
        break

    # Get the answer
    response = qa_chain.invoke({"query": query})

    print("Answer:")
    print(response["result"])

