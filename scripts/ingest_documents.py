from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vector_db import create_vector_db


documents = load_documents()

chunks = split_documents(documents)

create_vector_db(chunks)

print("Knowledge Base Ready!")