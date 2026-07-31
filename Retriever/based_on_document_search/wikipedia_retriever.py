from langchain_community.retrievers import WikipediaRetriever

print("Radha!")

try:
    retriever = WikipediaRetriever(
        top_k_results=2,
        lang="en"
    )

    query = "India"

    docs = retriever.invoke(query)

    print("Number of docs:", len(docs))

    for i, doc in enumerate(docs):
        print(f"\n----- Result {i+1} -----")
        print(doc.page_content[:500])

except Exception as e:
    print("Error:", e)

