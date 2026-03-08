# 📄 Chat with Multiple PDF Documents using LangChain & Google Gemini Pro

A **Streamlit web app** that lets you **ask questions across multiple PDFs** using:

- **LangChain** for text processing and chaining.
- **FAISS** for vector-based similarity search.
- **Google Gemini 2.0** for AI-generated detailed answers.
- **HuggingFace embeddings** for semantic search.

---

## 🚀 Features

- Upload multiple PDFs at once and extract text automatically.
- Split PDF content into chunks for efficient vector search.
- Index PDFs locally using **FAISS**.
- Ask questions and get:
  - **Quick Answer** from PDF content.
  - **Detailed Answer** using **Google Gemini 2.0**.
- Interactive **Streamlit UI** for easy usage.
- Retry logic for API rate limits.

---

## 📸 Screenshots

Put all screenshots in a `screenshots/` folder. Example table:

| PDF Upload | Quick Answer | Detailed Answer |
|------------|-------------|----------------|
| ![Upload](screenshots/upload.png) | ![Quick](screenshots/quick_answer.png) | ![Detailed](screenshots/detailed_answer.png) |
| ![Upload2](screenshots/upload2.png) | ![Quick2](screenshots/quick_answer2.png) | ![Detailed2](screenshots/detailed_answer2.png) |

> Add more rows as needed. Just reference your images in `screenshots/`.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
