from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from dotenv import load_dotenv
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_chroma import Chroma

load_dotenv()


documents = [
    Document(
        page_content="""
Acme Corporation Employee Handbook

New employees attend a two-day onboarding session during their first week.
The company provides every employee with a laptop, monitor, and security key.

Employees are encouraged to maintain a healthy work-life balance.
Full-time employees receive 20 days of paid time off (PTO) every year.
Unused vacation days may be carried over to the next year, but no more than five days.
Requests for leave should be submitted through the HR portal at least two weeks in advance.

The company also observes 12 public holidays and offers flexible working hours.
Managers may approve work-from-home arrangements up to three days each week.

Employees can claim business travel expenses for flights, hotels, taxis, and meals.
Expense reports must be submitted within 30 days.

Every employee is eligible for a $2,000 annual learning budget that can be used
for certifications, online courses, technical books, or conferences.

The IT department performs maintenance every Friday evening.
Passwords must be changed every 90 days.
""",
        metadata={"doc": "employee_handbook"},
    ),

    Document(
        page_content="""
Acme IT Security Policy

Employees must enable multi-factor authentication (MFA) on all company accounts.

Passwords should contain at least 12 characters and should never be reused.

When working remotely, employees must connect through the company VPN.

Lost laptops must be reported within one hour.

Confidential customer information must never be stored on personal devices.

Managers should approve remote access requests before employees begin working outside the office.

Security awareness training is mandatory once every year.
""",
        metadata={"doc": "security_policy"},
    ),

    Document(
        page_content="""
Engineering Guidelines

Python is the primary backend language.

FastAPI is used for REST APIs.

Redis is used for caching.

PostgreSQL stores transactional data.

Developers should write unit tests before opening a pull request.

Every deployment goes through CI/CD pipelines.

Performance testing is required before major releases.

Developers receive access to an AI coding assistant after completing onboarding.
""",
        metadata={"doc": "engineering_guide"},
    ),
]

# initialize embedding model
embedding = OpenAIEmbeddings()

# step 3: create the faiss vectore stor from documents
vectorstore = Chroma.from_documents(
    documents = documents,
    embedding = embedding,
    collection_name = 'employee',
    persist_directory = r'D:\Gen Ai\Retriever'
)

# create retriever
similarity_retriever = vectorstore.as_retriever(
    search_type='similarity',
    search_kwargs ={'k':2}
)

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={'k':3}),
    llm=ChatOpenAI()
)

# query
query = 'What is the PTO policy'

similarity_result = similarity_retriever.invoke(query)
multiquery_result = multiquery_retriever.invoke(query)


print('This is result of similarity search\n')
for i, doc in enumerate(similarity_result):
    print(f'{i}: {doc.page_content}')


print('\n\nThis is multiquery search result\n')

for i, doc in enumerate(multiquery_result):
    print(f'{i}: {doc.page_content}')



