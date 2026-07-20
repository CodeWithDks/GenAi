from langchain_community.document_loaders import TextLoader

file_path = "D:/Gen Ai/Documents_Loader\documents/text.txt"
loader = TextLoader(file_path=file_path, encoding='utf-8')
docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)
print(docs[0].metadata['source'])
print(len(docs,'\n'))
print(docs[0].page_content.splitlines())