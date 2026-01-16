import os
import sys
import streamlit as st

# -----------------------------
# FIX PYTHON PATH
# -----------------------------
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -----------------------------
# IMPORT SYSTEM MODULES
# -----------------------------
from src.agent.router import handle_action
from src.ingestion.pdf_loader import load_pdf_with_pages
from src.ingestion.pdf_chunker import chunk_pages
from src.retrieval.vector_store import build_or_load_vector_store

# -----------------------------
# STREAMLIT CONFIG
# -----------------------------
st.set_page_config(
    page_title="Agentic Enterprise Assistant",
    layout="wide"
)

st.title("🤖 Agentic Enterprise Assistant")
st.caption("HCLTech • NLP Challenge • Kshitij 2026")

# -----------------------------
# LOAD VECTOR STORE (ONCE)
# -----------------------------
@st.cache_resource
def load_rag_system():
    pdf_path = os.path.join(
        PROJECT_ROOT,
        "data",
        "raw",
        "HCLTech_Annual_Report_2024_25.pdf"
    )
    pages = load_pdf_with_pages(pdf_path)
    chunks = chunk_pages(pages)
    vectorstore = build_or_load_vector_store(chunks)
    return vectorstore

vectorstore = load_rag_system()

# -----------------------------
# USER INPUT
# -----------------------------
user_query = st.text_input(
    "Ask a question or give a command:",
    placeholder="e.g. What are the key risks mentioned in the report?"
)

# -----------------------------
# PROCESS QUERY
# -----------------------------
if user_query:
    st.divider()

    action_result = handle_action(user_query)

    # ---------- ACTION ----------
    if action_result:
        st.subheader("🛠️ Detected Action")
        st.json(action_result)

    # ---------- INFORMATION ----------
    else:
        st.subheader("📄 Information Response")

        results = vectorstore.similarity_search(user_query, k=3)

        if not results:
            st.warning("No relevant information found.")
        else:
            answer = results[0].page_content
            page = results[0].metadata.get("page", "N/A")

            st.markdown(answer)
            st.caption(f"📌 Source: HCLTech Annual Report — Page {page}")
