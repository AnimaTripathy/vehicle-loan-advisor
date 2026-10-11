# 🚗 Vehicle Loan Advisor

## AI-Powered Loan Eligibility & Vehicle Recommendation System

An end-to-end AI Engineering application that predicts vehicle loan eligibility, calculates the maximum affordable loan amount, recommends vehicles within the approved budget, and provides AI-powered explanations using Retrieval-Augmented Generation (RAG).

---

## 🌟 Project Overview

The **Vehicle Loan Advisor** helps users make informed vehicle financing decisions by combining **Machine Learning**, **Business Rules**, and **Generative AI** into a single application.

The application performs the following tasks:

- 🤖 Predicts loan eligibility using a Machine Learning model
- 💰 Calculates the maximum affordable loan amount
- 🚗 Recommends vehicles within the customer's budget
- 📋 Displays complete vehicle specifications
- 🧠 Explains vehicle recommendations using Google Gemini and RAG
- 📚 Uses a policy document as the knowledge source for AI explanations

---

## 🎯 Project Objectives

- Automate vehicle loan eligibility prediction.
- Help customers understand their borrowing capacity.
- Recommend vehicles that match the customer's financial profile.
- Provide transparent AI-generated explanations using company policy.
- Demonstrate an end-to-end AI Engineering workflow.

---

# ✨ Features

### 🤖 Loan Eligibility Prediction

- Predicts whether a loan application is approved or rejected.
- Uses a Machine Learning classification model.
- Displays prediction confidence.

---

### 💰 Loan Amount Calculation

- Calculates the maximum affordable loan amount.
- Considers:
  - Monthly income
  - Existing EMI
  - Loan tenure
  - Interest rate
- Ensures EMI remains within the repayment capacity.

---

### 🚗 Vehicle Recommendation

- Recommends vehicles that best match the customer's approved budget.
- Retrieves vehicle information from a SQLite database.
- Displays:
  - Brand
  - Model
  - Variant
  - Price
  - Fuel Type
  - Transmission
  - Mileage
  - Engine
  - Seating Capacity
  - Body Type

---

### 📋 Vehicle Details

- View complete specifications for each recommended vehicle.
- Provides a clean and interactive user interface using expandable sections.

---

### 🧠 AI Recommendation (RAG)

- Generates AI-powered explanations for recommended vehicles.
- Uses Retrieval-Augmented Generation (RAG).
- Retrieves relevant information from the Vehicle Loan Policy.
- Uses Google Gemini to generate contextual explanations.

---

### ⚡ REST API

FastAPI backend exposes the following APIs:

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health Check |
| POST | `/predict` | Loan Eligibility Prediction |
| POST | `/loan-amount` | Loan Amount Calculation |
| POST | `/loan-advisor` | Complete Loan Advisor Workflow |
| GET | `/vehicle/{id}` | Vehicle Details |
| POST | `/explain` | AI Recommendation |

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| **Programming Language** | Python 3.12 |
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **Machine Learning** | Scikit-learn, Joblib |
| **Database** | SQLite |
| **Recommendation Engine** | Custom Business Logic |
| **Retrieval-Augmented Generation (RAG)** | LangChain, FAISS |
| **Large Language Model (LLM)** | Google Gemini |
| **API Testing** | Swagger UI |
| **Environment Management** | Python Virtual Environment |
| **Development Tools** | VS Code |

---
## Technology Architecture

```text
                    Streamlit
                        │
                        ▼
                 FastAPI Backend
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 Loan Prediction   Loan Amount   Vehicle Recommendation
      │                 │                 │
      └─────────────────┼─────────────────┘
                        ▼
                  SQLite Database
                        │
                        ▼
                 FAISS Vector Store
                        │
                        ▼
              Vehicle Loan Policy
                        │
                        ▼
                 Google Gemini AI
```

---
# 📁 Project Structure

```text
VehicleLoanAdvisor/
│
├── backend/
│   ├── db/
│   │   ├── database.py
│   │   ├── init_database.py
│   │   ├── load_vehicles.py
│   │   └── vehicle.db
│   │
│   ├── rag/
│   │   ├── config.py
│   │   ├── explain.py
│   │   ├── ingest.py
│   │   ├── retriever.py
│   │   └── vector_store/
│   │
│   ├── services/
│   │   ├── eligibility_service.py
│   │   ├── loan_amount_service.py
│   │   ├── rag_service.py
│   │   └── vehicle_service.py
│   │
│   ├── schemas.py
│   └── main.py
│
├── frontend/
│   ├── pages/
│   │   ├── 1_Home.py
│   │   ├── 2_Loan_Advisor.py
│   │   └── 3_About.py
│   │
│   ├── utils/
│   │   └── api.py
│   │
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── vehicle_catalog.csv
│   │
│   └── policies/
│       └── vehicle_loan_policy.md
│
├── models/
│   └── loan_prediction_pipeline.pkl
│
├── requirements.txt
├── README.md
├── Dockerfile
└── docker-compose.yml
```

---
# 🔄 Application Workflow

```text
Applicant Details
        │
        ▼
Loan Eligibility Prediction
        │
        ▼
Loan Amount Calculation
        │
        ▼
Budget Calculation
        │
        ▼
Vehicle Recommendation
        │
        ▼
Vehicle Details
        │
        ▼
AI Recommendation (RAG)
        │
        ▼
Google Gemini
        │
        ▼
Final Recommendation
```

---
# ⚙️ Installation & Setup

## Prerequisites

Before running the application, ensure the following are installed:

- Python 3.12 or later
- pip (Python Package Manager)
- Git (Optional, for cloning the repository)

---

## Clone the Repository

```bash
git clone https://github.com/<your-username>/vehicle-loan-advisor.git
```

Navigate to the project directory:

```bash
cd vehicle-loan-advisor
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a file named:

```text
.env
```

Add your Google Gemini API key:

```text
GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
```

---

## Initialize the Database

```bash
python -m backend.db.init_database
```

---

## Load Vehicle Data

```bash
python -m backend.db.load_vehicles
```

---

## Start the FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Start the Streamlit Frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

The application will be available at:

```text
http://localhost:8501
```

---
# 🚀 How to Use

1. Launch the FastAPI backend.
2. Launch the Streamlit frontend.
3. Open the **Loan Advisor** page.
4. Enter applicant information.
5. Click **Check Loan Eligibility**.
6. Review:
   - Loan eligibility
   - Approved loan amount
   - Available budget
   - Recommended vehicles
7. Expand a vehicle to view detailed specifications.
8. Click **🤖 Why was this vehicle recommended?** to receive an AI-generated explanation based on the Vehicle Loan Policy.

---
# 🚀 Future Enhancements

The current application demonstrates a complete end-to-end AI workflow. Future improvements may include:

- 🔐 User Authentication and Login
- ☁️ Cloud Deployment (AWS / Azure / GCP)
- 🏦 Integration with Banking APIs
- 🚘 Live Vehicle Price Integration
- 📈 Credit Score Analysis
- 📱 Mobile Responsive UI
- 🌍 Multi-language Support
- 📊 Loan Comparison Dashboard
- 🤖 Personalized AI Financial Advisor

---
# ⭐ Project Highlights

- End-to-End AI Engineering Application
- Machine Learning-based Loan Eligibility Prediction
- Business Rule-based Loan Amount Calculation
- Budget-based Vehicle Recommendation Engine
- Retrieval-Augmented Generation (RAG)
- Google Gemini AI Integration
- REST APIs using FastAPI
- Interactive Dashboard using Streamlit
- SQLite Database Integration
- Modular Project Architecture

---
# 🙏 Acknowledgements

This project was developed as part of an **AI Engineering Capstone Project**.

Special thanks to:

- OpenAI
- Google Gemini
- LangChain
- FAISS
- FastAPI
- Streamlit
- Scikit-learn

for providing the tools and frameworks that made this project possible.

---
# 📄 License

This project is intended for educational and portfolio purposes.

---
