from backend.rag.explain import explain


class RAGService:

    @staticmethod
    def explain(question: str):

        answer = explain(question)

        return {
            "success": True,
            "answer": answer
        }