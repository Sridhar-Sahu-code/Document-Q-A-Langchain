import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import time
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import warnings
import logging

# --- Suppress warnings for cleaner terminal ---
warnings.filterwarnings("ignore", category=FutureWarning)
logging.getLogger("transformers").setLevel(logging.ERROR)

# --- Load environment variables ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# --- Resource Caching ---
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"use_auth_token": HF_TOKEN}
    )

@st.cache_resource
def get_conversational_chain():
    prompt_template = """
Answer the question as detailed as possible using the provided context.
If the answer is not in the context say: "Answer is not available in the context."

Context:
{context}

Question:
{question}

Answer:
"""
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.3,
        google_api_key=GOOGLE_API_KEY
    )
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return model, prompt

# --- PDF Processing ---
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content
    return text

def get_text_chunks(text):
    # Bigger chunk size reduces number of chunks → faster FAISS
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=50)
    return text_splitter.split_text(text)

def get_vector_store(text_chunks):
    embeddings = load_embeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# --- User Input & Error Handling ---
def user_input(user_question):
    if not os.path.exists("faiss_index"):
        st.error("Please upload and process the PDF first.")
        return

    embeddings = load_embeddings()
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    # --- Local FAISS similarity search ---
    docs = db.similarity_search(user_question, k=1)

    if not docs:
        st.warning("No relevant content found in PDF.")
        return

    # --- Quick answer from FAISS (instant) ---
    quick_answer = docs[0].page_content[:2000]  # top chunk, trimmed
    st.write("### Quick Answer (from PDF):")
    st.write(quick_answer)

    # --- Ask Gemini only for detailed response ---
    ask_gemini = st.checkbox("Get detailed answer from Gemini 2.0", value=False)
    if not ask_gemini:
        return

    MAX_CONTEXT_CHARS = 2000
    context = "\n".join([doc.page_content for doc in docs])[:MAX_CONTEXT_CHARS]

    model, prompt = get_conversational_chain()
    final_prompt = prompt.format(context=context, question=user_question)

    # Retry logic for quota errors
    max_retries = 5
    retry_delay = 1
    for attempt in range(max_retries):
        try:
            response = model.invoke(final_prompt)
            st.write("### Detailed Answer (from Gemini 2.0):")
            st.write(response.content)
            break
        except Exception as e:
            if "429" in str(e):
                if attempt < max_retries - 1:
                    st.warning(f"Rate limit hit. Retrying in {retry_delay}s... (Attempt {attempt+1}/{max_retries})")
                    time.sleep(retry_delay)
                    retry_delay *= 2
                else:
                    st.error("Quota exhausted. Please wait a minute or check billing.")
            else:
                st.error(f"Unexpected error: {e}")
                break

# --- Streamlit UI ---
def main():
    st.set_page_config(page_title="Chat with PDF", layout="wide")
    st.header("📄 Chat with PDF using Gemini 2.0")

    user_question = st.text_input("Ask a question from the uploaded documents:")
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Settings & Upload")
        pdf_docs = st.file_uploader("Upload PDF Files", accept_multiple_files=True)

        if st.button("Submit & Process"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF.")
                return

            with st.spinner("Processing PDF content..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Indexing complete! You can now ask questions.")

if __name__ == "__main__":
    main()