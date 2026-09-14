from langchain_community.document_loaders import CSVLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader = CSVLoader(
        file_path=r"D:\Gen Ai\Documents_Loader\documents\faq_dataset.csv"
    )

prompt = PromptTemplate(
    template="""
You are a question-answering system.

Use ONLY the information provided in the context below.

Context:
{text}

Question:
{question}

Rules:
1. Answer only from the context.
2. Do not use your own knowledge.
3. If the answer is not present in the context, reply:
   "Sorry, I could not find the answer in the provided data."
4. Return only the answer.

Answer:
""",
    input_variables=["question", "text"]
)
docs = loader.load()
model = ChatOpenAI(
    temperature=0
)
parser = StrOutputParser()

question = "What is your favorite season?"

matched_docs = [
    doc.page_content
    for doc in docs
    if "favorite season" in doc.page_content.lower()
]

context = "\n".join(matched_docs)

print(context)
chain = prompt | model | parser

response = chain.invoke(
    {
        "question":"What is your favorite season?",
        "text": context
    }
)

print(response)





