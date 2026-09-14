from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="""
You are an expert educator.

Convert the following text into well-structured study notes.

Requirements:
- Use Markdown headings.
- Use bullet points.
- Cover ALL important concepts.
- Do NOT write a paragraph summary.
- Include definitions where appropriate.
- Keep the notes concise but complete.

Text:
{text}
""",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="""
You are an expert quiz creator.

Based on the following text, generate 5 multiple-choice questions.

Requirements:
- Each question should have 4 options (A, B, C, D).
- Only one option should be correct.
- Include the correct answer after each question.
- Cover different important concepts from the text.
- Make the questions suitable for students.

Text:
{text}
""",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="""
You are a document formatter.

Create a single study guide.

Rules:
1. Include ALL of the notes exactly as provided.
2. Then write the heading "Quiz".
3. Include ALL quiz questions exactly as provided.
4. Do NOT summarize.
5. Do NOT remove any information.

# Notes

{note}

# Quiz

{quiz}
""",
    input_variables=["note", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'note':prompt1 | model |parser,
    'quiz':prompt2 | model |parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

chain.get_graph().print_ascii()
try:
    with open('D:\Gen Ai\Chains\Text.txt','r', encoding='utf-8') as f:
       text = f.read()

    result = chain.invoke({'text':text})
    print(result)
except Exception as e:
    print('Error', e)

try:
    with open("study_guide.md", "w", encoding="utf-8") as f:
      f.write(result)
except FileNotFoundError as e:
    print("File not found error:", e)

