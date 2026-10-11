from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from backend.rag.config import GOOGLE_API_KEY

BASE_DIR = Path(__file__).resolve().parents[2]

VECTOR_DB = BASE_DIR / "backend" / "rag" / "vector_store"

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY
)

vector_store = FAISS.load_local(
    str(VECTOR_DB),
    embeddings,
    allow_dangerous_deserialization=True
)


def retrieve_context(question: str):

    documents = vector_store.similarity_search(
        question,
        k=3
    )

    return documents