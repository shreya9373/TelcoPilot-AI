import os

from rag.retrieval import get_retriever

retriever = get_retriever()


def retriever_agent(state):
    """
    Retrieves relevant telecom knowledge and keeps
    only one chunk from each source document.
    """

    docs = retriever.invoke(state["question"])

    unique_docs = []
    seen = set()

    for doc in docs:

        source = os.path.basename(doc.metadata.get("source", ""))

        if source not in seen:
            seen.add(source)
            unique_docs.append(doc)

    context = "\n\n".join(
        doc.page_content
        for doc in unique_docs
    )

    return {
        "context": context,
        "documents": unique_docs
    }