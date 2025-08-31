from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
import os

def create_vector_store(texts, metadatas):
    embeddings = OpenAIEmbeddings()

    # Streamlit Cloud has /tmp folder for writable storage
    persist_directory = os.path.join("/tmp", "chromadb_collection")

    vector_store = Chroma.from_texts(
        texts,
        embeddings,
        metadatas=metadatas,
        persist_directory=persist_directory
    )
    return vector_store
