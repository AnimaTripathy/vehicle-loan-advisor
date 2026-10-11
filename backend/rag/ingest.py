from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from backend.rag.config import GOOGLE_API_KEY, GEMINI_EMBEDDING_MODEL

BASE_DIR = Path(__file__).resolve().parents[2]

POLICY_FILE = BASE_DIR / "data" / "policies" / "vehicle_loan_policy.md"

loader = TextLoader(str(POLICY_FILE))

documents = loader.load()

print("Documents Loaded:", len(documents))
print(documents)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("Chunks Created:", len(chunks))

for chunk in chunks:
    print(chunk.page_content[:100])

embeddings = GoogleGenerativeAIEmbeddings(
    model=GEMINI_EMBEDDING_MODEL,
    google_api_key=GOOGLE_API_KEY
)

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

VECTOR_DB = BASE_DIR / "backend" / "rag" / "vector_store"

vector_store.save_local(str(VECTOR_DB))

print("✅ Vector database created successfully!")
print(f"Chunks Created: {len(chunks)}")