from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader('D:/Gen Ai/Documents_Loader/documents/text.txt', encoding='utf-8')

docs = loader.load()

text = docs[0].page_content

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)

result = splitter.split_text(text)

print(result.content)