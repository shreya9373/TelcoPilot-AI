from langchain_community.document_loaders import DirectoryLoader, TextLoader


def load_documents():
    loader = DirectoryLoader(
        "data/sop",
        glob="*.md",
        loader_cls=TextLoader
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents.")

    return documents