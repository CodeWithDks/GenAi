from langchain_faiss import FAISS
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_classic.retrievers.document_compressors import LLMChainExtractor

load_dotenv()

documents = [

    Document(
        page_content="""
The healthcare industry has undergone significant transformation over the past decade.
Hospitals are increasingly adopting electronic health records to improve patient care and
reduce paperwork. Artificial intelligence is being used to detect diseases such as cancer
at earlier stages. Telemedicine has also become more common after the COVID-19 pandemic,
allowing patients to consult doctors remotely.

A balanced diet, regular exercise, and routine medical checkups remain the foundation of
preventive healthcare. Doctors recommend at least 150 minutes of moderate physical activity
per week.

Health insurance policies differ from one provider to another. Most comprehensive plans
cover hospitalization, diagnostic tests, emergency treatment, maternity benefits,
prescription medicines, and annual health checkups. Cosmetic procedures are generally not
covered unless medically necessary.

Medical researchers continue developing vaccines and personalized treatments using genomic
data. Healthcare spending worldwide has increased due to aging populations and chronic
diseases.
""",
        metadata={"topic": "healthcare"},
    ),

    Document(
        page_content="""
Solar energy is one of the fastest-growing renewable energy sources.
Photovoltaic panels convert sunlight directly into electricity. Modern systems
can operate for more than 25 years with minimal maintenance.

Installing rooftop solar panels typically reduces household electricity bills by
40–80%, depending on location and sunlight availability. Government subsidies
and tax incentives further reduce installation costs.

Excess electricity generated during the day can often be exported back to the
power grid through net metering programs.

Researchers are also developing solar batteries that store excess energy for
nighttime use. Large-scale solar farms are becoming increasingly common around
the world.
""",
        metadata={"topic": "solar_energy"},
    ),

    Document(
        page_content="""
Personal finance involves budgeting, saving, investing, and managing debt.
Experts recommend following the 50-30-20 budgeting rule, where 50% of income is
spent on necessities, 30% on personal expenses, and 20% is saved or invested.

An emergency fund should ideally cover three to six months of living expenses.

Long-term investments such as index funds have historically outperformed many
actively managed portfolios.

Credit card debt often carries high interest rates, making early repayment
financially beneficial. Financial planning should also include retirement savings,
insurance, and tax optimization.
""",
        metadata={"topic": "finance"},
    ),

    Document(
        page_content="""
Cybersecurity protects computer systems from unauthorized access and attacks.
Organizations implement firewalls, endpoint protection, intrusion detection systems,
and multi-factor authentication to improve security.

Employees remain one of the biggest security risks because phishing attacks rely
on human mistakes.

Strong passwords should contain at least 12 characters and should never be reused
across multiple websites.

Regular software updates and security patches reduce vulnerabilities exploited
by attackers.

Companies should also perform regular penetration testing and maintain encrypted
backups to recover from ransomware attacks.
""",
        metadata={"topic": "cybersecurity"},
    ),

    Document(
        page_content="""
Artificial Intelligence enables machines to perform tasks that traditionally
required human intelligence. Machine learning algorithms improve their performance
by learning patterns from data.

Deep learning models use neural networks with multiple layers to recognize images,
speech, and natural language.

Large Language Models (LLMs) are trained on enormous text datasets and can perform
question answering, summarization, translation, and code generation.

Retrieval-Augmented Generation (RAG) improves factual accuracy by retrieving
relevant documents before generating a response.

Contextual compression is a retrieval technique that removes irrelevant sections
from retrieved documents so only information relevant to the user's question is
passed to the language model.
""",
        metadata={"topic": "artificial_intelligence"},
    ),

]

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(
    documents=documents,
    embedding=embeddings,
)

vectorstore.save_local(r'D:\Gen Ai\Retriever')

base_retriever = vectorstore.as_retriever(search_kwargs={'k':2})


llm = ChatOpenAI()
compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_retriever = base_retriever,
    base_compressor= compressor
)

query = 'What does health insurance usually cover?'

compressed_result = compression_retriever.invoke(query)

for i, doc in enumerate(compressed_result):
    print(f'{i}: {doc.page_content}')

