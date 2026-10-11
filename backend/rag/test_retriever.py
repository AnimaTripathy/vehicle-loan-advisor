from backend.rag.retriever import retrieve_context

question = "What should an applicant do after loan rejection?"

results = retrieve_context(question)

print("\nRetrieved Chunks\n")

for index, document in enumerate(results, start=1):

    print("=" * 50)

    print(f"Chunk {index}")

    print(document.page_content)