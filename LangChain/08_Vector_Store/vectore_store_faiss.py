from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

# Document Loader
loader = PyPDFLoader(r'D:\Gen Ai\Vector_Store\AI Agents.pdf')
docs = loader.load()
print(f'Document loaded successfully: {docs[0].metadata}')

# Text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=20
)
text_splitted = text_splitter.split_documents(docs)

# Embedding model import
embeddings = OpenAIEmbeddings(model='text-embedding-3-large')

# 1. Correct way to create the vector store directly from your split text
vector_store = FAISS.from_documents(
    documents=text_splitted,
    embedding=embeddings
)

# 2. Persist/Save the FAISS index AFTER the documents are added
persist_directory = r"D:\Gen Ai\Vector_Store"
vector_store.save_local(persist_directory)
print("Vector store saved successfully.")

