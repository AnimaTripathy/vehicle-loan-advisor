import streamlit as st

st.title("ℹ️ About")

st.markdown(
"""
# Vehicle Loan Advisor

An end-to-end AI Engineering Capstone Project.

---

## Objectives

This application assists customers by:

- Predicting loan eligibility
- Calculating affordable loan amount
- Recommending vehicles
- Explaining recommendations using AI

---

## Technology Stack

### Frontend

- Streamlit

### Backend

- FastAPI

### Database

- SQLite

### Machine Learning

- Scikit-Learn
- Joblib

### AI

- LangChain
- FAISS
- Google Gemini

---

## Project Workflow

Applicant Details

↓

Loan Eligibility Prediction

↓

Loan Amount Calculation

↓

Vehicle Recommendation

↓

AI Recommendation using RAG

---
"""
)