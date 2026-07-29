from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import SimpleJsonOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader(
    r"D:\Gen Ai\Documents_Loader\documents\Keerthana_Know_Me_Better.pdf"
)

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size= 199,
    chunk_overlap = 0
)

chanks = splitter.split_documents(docs)

