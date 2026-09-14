from langchain_openai import OpenAI, ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
import chromadb
from dotenv import load_dotenv

load_dotenv()

"""
Radha Rani is revered as the eternal consort of Radha and the supreme symbol of pure, selfless love and devotion. 
In Hindu tradition, especially in the Bhakti movement, she represents unconditional love, compassion, and spiritual surrender. 
Her divine relationship with Krishna inspires millions of devotees to seek a deeper connection with God through love and devotion.
"""
# Document Loader
loader = TextLoader(r'D:\Gen Ai\about-radha.txt', encoding='utf-8')
text_loaded = loader.load()
print(f'document loaded successfully {text_loaded[0].metadata}')

# Text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=131,
    chunk_overlap=0
)
text_splitted = text_splitter.split_documents(text_loaded)
#print(f'Text splitted successully:\n {text_splitted} \n {type(text_splitted)}\n {len(text_splitted)}')

# Embedting model import
embeddings = OpenAIEmbeddings(model='text-embedding-3-large')
# create vectore store
vectore_store = Chroma(
    embedding_function=embeddings,
    collection_name='radhadb',
    persist_directory='D:\Gen Ai\Vector_Store'
)

#create 
vectore_stored = vectore_store.aadd_documents(text_splitted)
print(vectore_stored)
#print(len(vectore_stored))
print(type(vectore_stored))


