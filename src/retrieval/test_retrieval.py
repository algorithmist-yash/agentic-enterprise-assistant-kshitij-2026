import os
import sys

# -----------------------------
# FIX PYTHON PATH (WINDOWS SAFE)
# -----------------------------
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -----------------------------
# NOW IMPORTS WILL WORK
# -----------------------------
from src.ingestion.pdf_loader import load_pdf_with_pages
from src.ingestion.pdf_chunker import chunk_pages
from src.retrieval.vector_store import build_vector_store

PDF_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw",
    "HCLTech_Annual_Report_2024_25.pdf"
)

if __name__ == "__main__":
    pages = load_pdf_with_pages(PDF_PATH)
    chunks = chunk_pages(pages)

    print("Total chunks:", len(chunks))

    vectorstore = build_vector_store(chunks)

    query = "What are the key risks mentioned in the report?"
    results = vectorstore.similarity_search(query, k=3)

    print("\n--- SEARCH RESULTS ---")
    for r in results:
        print(f"Page {r.metadata['page']}")
        print(r.page_content[:300])
        print("-" * 40)
