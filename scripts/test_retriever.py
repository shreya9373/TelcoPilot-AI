from rag.retrieval import get_retriever

retriever = get_retriever()

query = "Users are experiencing high latency."

docs = retriever.invoke(query)

print("=" * 60)

print("Retrieved Documents")

print("=" * 60)

for i, doc in enumerate(docs, start=1):
    print(f"\nDocument {i}")
    print("-" * 40)
    print(doc.page_content[:500])