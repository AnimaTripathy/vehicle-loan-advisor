from backend.rag.explain import explain

question = "Why can a loan application be rejected?"

answer = explain(question)

print("\nAI Response\n")

print(answer)