# 🤖 Agentic Enterprise Assistant — Kshitij 2026 NLP Challenge

An **Agentic Enterprise Assistant** built for large organizations such as **HCLTech**, combining **Retrieval-Augmented Generation (RAG)** with **agentic intent routing** to deliver accurate, explainable, and structured enterprise responses.

This project is designed for **offline evaluation**, **low hallucination risk**, and **deterministic behavior**, aligned with enterprise-grade AI requirements.

---

## 📌 Overview

The system enables:
- Page-level question answering over enterprise PDF documents  
- Deterministic intent classification for structured enterprise actions  
- Schema-validated JSON outputs (no real API execution)  
- Fully offline, restart-safe demonstration via Streamlit  

---

## ✨ Key Capabilities

- 📄 **Page-Level Question Answering**  
  Answers queries directly from the *HCLTech Annual Integrated Report* with page citations.

- 🧠 **Low-Hallucination RAG Pipeline**  
  FAISS-based semantic retrieval with sentence-transformer embeddings.

- 🤖 **Agentic Intent Routing**  
  Classifies user intent into:
  - *Enterprise Action* → Structured JSON output  
  - *Information Query* → RAG-based answer

- 🛠️ **Structured JSON Outputs**  
  All enterprise actions are returned as validated JSON schemas.

- 💻 **Offline & Restart-Safe Demo**  
  No external APIs or internet dependency after setup.

---

## 🏗️ System Architecture

User Input  
↓  
Intent Router  
├── Action Intent → JSON Schema Output  
└── Query Intent  → RAG Pipeline (FAISS + Embeddings)

---

## 🧰 Tech Stack

- Python 3.10+
- Streamlit
- LangChain
- FAISS
- Sentence-Transformers
- PyMuPDF

---

## 🚀 Running the Application

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Place Dataset

Download the **HCLTech Annual Integrated Report (2024–25)**  
and place it at:

```bash
data/raw/HCLTech_Annual_Report_2024_25.pdf
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📝 Notes

- No real enterprise actions are executed  
- All actions are returned as validated JSON outputs  
- Page-level citations reduce hallucinations  
- Fully offline after initial setup  

---

## 👥 Team

TeamID: 25KTJNATT986783 
Kshitij 2026 — NLP Challenge  

---

## 📄 License

Academic & competition use only.
