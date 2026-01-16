import os
from langchain_community.vectorstores import FAISS

try:
    from langchain_huggingface import HuggingFaceEmbeddings
except ImportError:
    from langchain_community.embeddings import HuggingFaceEmbeddings


INDEX_DIR = "data/processed/faiss_index"


def build_or_load_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    if os.path.exists(INDEX_DIR):
        print("Loading existing FAISS index...")
        return FAISS.load_local(
            INDEX_DIR,
            embeddings,
            allow_dangerous_deserialization=True
        )

    print("Building FAISS index (one-time cost)...")

    texts = [doc["content"] for doc in documents]
    metadatas = [{"page": doc["page_number"]} for doc in documents]

    vectorstore = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )

    os.makedirs(INDEX_DIR, exist_ok=True)
    vectorstore.save_local(INDEX_DIR)

    print("FAISS index saved.")

    return vectorstore
