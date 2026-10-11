import streamlit as st

st.title("🚗 Vehicle Loan Advisor")

st.markdown(
"""
## Welcome

The **Vehicle Loan Advisor** is an end-to-end AI application that helps users determine loan eligibility, calculate affordable loan amounts, recommend vehicles within budget, and explain recommendations using Retrieval-Augmented Generation (RAG).

---

### ✨ Features

🤖 Loan Eligibility Prediction

💰 Loan Amount Calculation

🚗 Budget-based Vehicle Recommendation

📖 Vehicle Details

🧠 AI-powered Recommendation Explanation

---

### 🚀 Getting Started

Use the navigation menu on the left and open **Loan Advisor** to begin.
"""
)

st.info(
    "This project demonstrates Machine Learning, FastAPI, Streamlit, SQLite, FAISS, LangChain and Google Gemini."
)