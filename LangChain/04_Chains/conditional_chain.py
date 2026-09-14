from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

class LanguageResponse(BaseModel):
    language: Literal["English", "Hindi", "Other"] =Field(description="The detected language of the input text.")

try:
    load_dotenv()
    model = ChatOpenAI()
    parser = StrOutputParser()
except Exception as e:
    print("Error",e)

parser2 = PydanticOutputParser(pydantic_object=LanguageResponse)

prompt1 = PromptTemplate(
    template='''You are an expert language detector.

    Analyze the following text and identify its language.

    Respond with only one of these values:
    - English
    - Hindi
    - Other

    Text:
    {text}\n
    format_instructions: {format_instructions}''',
    input_variables=['text'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}

)

prompt2 = PromptTemplate(
    template='''You are an expert translator.

Translate the following English text into natural and fluent Hindi.

Only return the translated text.

Text:
{text}''',
input_variables=['text']
)

prompt3 = PromptTemplate(
    template='''You are an expert translator.

Translate the following Hindi text into natural and fluent English.

Only return the translated text.

Text:
{text}'''
)

prompt4 = PromptTemplate(
    template='''The provided text is not written in English or Hindi.

Politely inform the user that this translator currently supports only English and Hindi.'''
)



def language_branch(text: str):
    language_chain = prompt1 | model | parser2
    language = language_chain.invoke({'text': text}).language

    if language == 'English':
        translation_chain = prompt2 | model | parser
        translated_text = translation_chain.invoke({'text': text})
        return translated_text
    elif language == 'Hindi':
        translation_chain = prompt3 | model | parser
        translated_text = translation_chain.invoke({'text': text})
        return translated_text
    else:
        return prompt4.invoke({})
    
text = """
print("Radha Rani")
num = 10 #
num = 45
# addtion
num + num
"""

result = language_branch(text=text)

print(result)

