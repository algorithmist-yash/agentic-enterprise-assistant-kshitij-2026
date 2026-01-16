import os
import fitz  # PyMuPDF


def load_pdf_with_pages(pdf_path):
    print("DEBUG: Trying to open PDF at:")
    print(pdf_path)
    print("DEBUG: File exists?", os.path.exists(pdf_path))

    doc = fitz.open(pdf_path)
    pages = []

    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text()

        if text.strip():
            pages.append({
                "page_number": i + 1,
                "content": text
            })

    return pages


if __name__ == "__main__":
    PROJECT_ROOT = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )

    pdf_path = os.path.join(
        PROJECT_ROOT,
        "data",
        "raw",
        "HCLTech_Annual_Report_2024_25.pdf"
    )

    pages = load_pdf_with_pages(pdf_path)

    print("\nSUCCESS ✅")
    print("Total pages loaded:", len(pages))
    print("First page preview:\n", pages[0]["content"][:300])
