import os
from dotenv import load_dotenv
from google import genai

from backend.rag.retriever import retrieve_context
from backend.rag.config import GEMINI_CHAT_MODEL

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def explain(question: str):

    documents = retrieve_context(question)

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = f"""
You are an AI Vehicle Loan Advisor.

You must answer ONLY using the policy below.

-------------------------
Vehicle Loan Policy

{context}

-------------------------

Question:
{question}

Instructions:

1. Answer ONLY using the retrieved policy.
2. Explain the reason clearly.
3. Mention the relevant policy section.
4. If the retrieved policy contains a "Next Steps" section, include it.
5. If the policy does NOT specify next steps, do NOT include a "Next Steps" section.
6. Do not invent information that is not present in the policy.
7. Format your response as:

Reason:
Relevant Policy:
Next Steps: (only if available)

Use simple professional English.
"""

    try:
        response = client.models.generate_content(
            model=GEMINI_CHAT_MODEL,
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(f"Gemini Error: {e}")

        return (
            "AI explanation is temporarily unavailable.\n\n"
            "Relevant policy information:\n\n"
            + context
        )