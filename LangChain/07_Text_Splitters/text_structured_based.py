from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import TextSplitter, RecursiveCharacterTextSplitter

file_path = "D:/Gen Ai/Documents_Loader\documents/text.txt"
loader = TextLoader(file_path=file_path, encoding='utf-8')
documents = loader.load()

print(documents[0].page_content)



print('Document loaded successfully \n\n')

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = splitter.split_documents(documents)
for i, split in enumerate(splits):
    print(f"Split {i+1}:")
    print(split.page_content)

