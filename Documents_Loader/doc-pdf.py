from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pathlib import Path

try:
    load_dotenv()
except Exception as e:
    print({"Error":e})

pdf_path = Path("D:\Gen Ai\Documents_Loader\documents\Keerthana_Know_Me_Better.pdf")

if not pdf_path.exists():
    raise FileNotFoundError(f"PDF not found: {pdf_path}")


loader = PyPDFLoader(str(pdf_path))
docs = loader.load()
try:
    model = ChatOpenAI()
except Exception as e:
    print({"Error": e})


prompt = PromptTemplate(
    template="""You are a helpul assistent. You have answers that questions \n
      {question} only from the following text \n {text}.  You search any query to the text. 
      when you get related answers to the queries then answers otherwise kindly reply.""",

      input_variables= ["question", "text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke(
    {
        "question":"Tell me about keerthana?",
        "text": docs[0].page_content
    }
)

print(response)
