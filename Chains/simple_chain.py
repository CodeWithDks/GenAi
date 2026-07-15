from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic} in hindi langauge',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'pakistan'})

print(result)

chain.get_graph().print_ascii()