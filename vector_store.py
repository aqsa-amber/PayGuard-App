# vector_store.py
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

def create_vector_store(texts, metadatas):
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_texts(texts, embeddings, metadatas=metadatas)
    return vector_store
