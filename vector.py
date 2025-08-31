from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def create_vector_store(texts, metadatas):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
    return vector_store
