from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def create_agent(vector_store, topic):
    def filter_topic(doc):
        return doc.metadata["topic"] == topic

    retriever = vector_store.as_retriever(search_kwargs={"filter": filter_topic})
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        chain_type="stuff",
        retriever=retriever
    )
    return qa_chain





