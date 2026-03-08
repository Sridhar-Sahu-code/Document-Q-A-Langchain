# 📄 Chat with PDFs using Google Gemini 2.0 & LangChain

This project is a **Streamlit web app** that allows you to interact with multiple PDF documents using **Google Gemini 2.0** and **LangChain**. It uses **FAISS vector embeddings** for fast semantic search and can provide both **quick answers** from the PDFs and **detailed responses** using the LLM.

---

## 🚀 Features

- Upload **multiple PDF files** at once.
- Extract and process text from PDFs.
- Split text into **chunks** for better embeddings.
- Create and store a **FAISS vector index** for fast similarity search.
- Get **quick answers** from relevant PDF chunks instantly.
- Generate **detailed answers** using **Google Gemini 2.0** via LangChain.
- Handles **rate-limiting** and retries for API requests.
- Built with **Streamlit** for an interactive web interface.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – Web interface  
- **PyPDF2** – PDF text extraction  
- **LangChain** – LLM orchestration  
- **Google Gemini 2.0** – Large language model for detailed answers  
- **FAISS** – Vector similarity search  
- **HuggingFace Embeddings** – Semantic embeddings for PDFs  
- **dotenv** – Environment variable management  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sridhar-Sahu-code/Document-Q-A-Langchain.git
cd Document-Q-A-Langchain
