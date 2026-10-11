import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

GEMINI_CHAT_MODEL = "models/gemini-flash-latest"
GEMINI_EMBEDDING_MODEL = "models/gemini-embedding-001"

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found.")