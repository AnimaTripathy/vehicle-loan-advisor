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

Your task is to explain the recommendation ONLY using the retrieved Vehicle Loan Policy.

==============================
VEHICLE LOAN POLICY
==============================

{context}

==============================
APPLICANT DETAILS
==============================

{question}

==============================
INSTRUCTIONS
==============================

You must answer ONLY using information present in the Vehicle Loan Policy.

Do NOT:
- invent rules
- invent calculations
- invent recommendations
- mention policy sections that were not retrieved
- use outside knowledge

If the retrieved policy does not contain the required information, explicitly state that the policy does not specify it.

This applicant has already:

- received a loan decision
- received an approved loan amount
- received a vehicle recommendation

Your task is ONLY to explain WHY this recommendation was made.

==============================
RESPONSE FORMAT
==============================

### Reason

Explain why this vehicle was recommended.

Mention:

- approved loan amount
- available budget
- vehicle price

Explain why the vehicle fits the approved budget.

---

### Relevant Policy

Quote or summarize ONLY the retrieved policy text.

If the retrieved policy does not support a statement,
do not include that statement.

---

### Next Steps

Include this section ONLY if:

- the applicant's current situation requires next steps, AND
- the retrieved policy explicitly provides them.

If the applicant has been APPROVED and the retrieved policy contains no next steps for approved applicants,

DO NOT generate a "Next Steps" section.

==============================
STYLE
==============================

- Use clear professional business English.
- Keep the explanation concise.
- Avoid repetition.
- Do not use Markdown tables.
- Do not include information that is unrelated to this applicant.
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