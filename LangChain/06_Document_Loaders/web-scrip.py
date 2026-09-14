from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

url = "https://www.geeksforgeeks.org/python/introduction-to-python/"

loader = WebBaseLoader(url)
model = ChatOpenAI()
docs = loader.load()

prompt = PromptTemplate(
    template="""You are a helpfull assistent. You will get a question \n
      {question} and you have to search answer in given text \n
      {text} related to the question. and then answer.  if answers not in text then kindly relpy sorry i tried to search your query.
      in text but i didn't find answers related to your query. and most importaint. don't answers the random question.""",

      input_variables=["question","text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke(
    {"question":"Hello World Program in java?", 
     "text":docs[0].page_content
    }
     )

print(response)



