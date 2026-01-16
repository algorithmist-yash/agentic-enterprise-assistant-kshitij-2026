try:
    # Newer LangChain versions
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    # Older LangChain fallback
    from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_pages(pages, chunk_size=1000, chunk_overlap=200):
    """
    Splits page-wise content into chunks while preserving page numbers.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    documents = []

    for page in pages:
        chunks = splitter.split_text(page["content"])
        for chunk in chunks:
            documents.append({
                "page_number": page["page_number"],
                "content": chunk
            })

    return documents
