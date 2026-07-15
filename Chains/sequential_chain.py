from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template='You generate a detailed infromation about following {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='You generate a 5 points brief summary about following {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'Radha'})

print(result)

chain.get_graph().print_ascii()