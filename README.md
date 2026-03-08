# 📄 Chat with PDFs using Google Gemini 2.0 & LangChain


A **cutting-edge Streamlit web application** that allows users to **ask questions and interact with multiple PDF documents intelligently**. Leveraging **Google Gemini 2.0** for large language understanding, **FAISS vector embeddings** for semantic search, and **LangChain** for LLM orchestration, this app provides both **instant insights** and **detailed contextual answers** from documents.

---

## 🌟 Key Features

- ✅ **Multi-PDF Upload** – Upload and process multiple PDF files simultaneously.
- ✅ **Intelligent Text Extraction** – Extract and clean text from PDFs using `PyPDF2`.
- ✅ **Chunked Embeddings** – Split large documents into manageable chunks for more accurate embeddings.
- ✅ **Semantic Search with FAISS** – Quickly search for relevant content across all uploaded PDFs.
- ✅ **Quick Answers** – Instant answers from top relevant chunks.
- ✅ **Detailed Contextual Answers** – Use Google Gemini 2.0 via LangChain for full, context-aware responses.
- ✅ **Error Handling & Retry Logic** – Handles API rate limits gracefully.
- ✅ **User-Friendly Streamlit Interface** – Interactive and simple for all users.

---

## 🚀 Technologies Used

| Layer             | Technology                                      | Purpose |
|------------------|-----------------------------------------------|---------|
| Frontend          | Streamlit                                     | Web interface and user interaction |
| PDF Processing    | PyPDF2                                        | Extract text from PDFs |
| LLM Orchestration | LangChain                                     | Connects FAISS and Google Gemini 2.0 |
| LLM               | Google Gemini 2.0                             | Generates detailed contextual answers |
| Vector Search     | FAISS                                         | High-performance similarity search |
| Embeddings        | HuggingFace `sentence-transformers/all-MiniLM-L6-v2` | Converts text chunks to vectors |
| Environment       | dotenv                                        | Secure API key management |
| Utilities         | os, time, logging, warnings                   | File handling, retries, error logging |

---

## 🎯 Problem Solved

Working with **large PDF documents** can be time-consuming, especially when you need to extract **specific insights**. This project:

- Reduces manual reading of documents.
- Provides **semantic search** across multiple PDFs.
- Delivers **quick answers** for fast insights.
- Enables **detailed responses** via a state-of-the-art LLM (Google Gemini 2.0).

This is ideal for **analysts, researchers, students, or professionals** dealing with multiple technical reports, research papers, or corporate documents.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sridhar-Sahu-code/Document-Q-A-Langchain.git
cd Document-Q-A-Langchain
