import streamlit as st
from data_loader import load_texts
from vector_store import create_vector_store
from agents import create_agent
from coordinator import route_query

# --------------------------
# API Key from Streamlit Secrets
# --------------------------
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except KeyError:
    st.error("⚠️ OPENAI_API_KEY not found in Streamlit secrets")
    st.stop()

# --------------------------
# Streamlit Page Setup
# --------------------------
st.set_page_config(page_title="Multi-Agent RAG", layout="wide")
st.title("💡 Multi-Agent RAG System (Salary + Insurance)")

# --------------------------
# Load Data & Vector Store
# --------------------------
texts, metadatas = load_texts()
vector_store = create_vector_store(texts, metadatas)

# --------------------------
# Create Agents
# --------------------------
salary_agent = create_agent(vector_store, "salary")
insurance_agent = create_agent(vector_store, "insurance")

# --------------------------
# Streamlit UI
# --------------------------
user_query = st.text_input("Ask a question about salary or insurance:")

if user_query:
    with st.spinner("Thinking..."):
        answer = route_query(user_query, salary_agent, insurance_agent)
    st.markdown(f"**Answer:** {answer}")

# --------------------------
# Example Queries
# --------------------------
st.markdown("### Try these example queries:")
st.markdown("- `How do I calculate annual salary?`")
st.markdown("- `What is included in my insurance policy?`")



