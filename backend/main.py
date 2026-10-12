from fastapi import FastAPI

from backend.schemas import (
    LoanAmountRequest,
    PredictionRequest
)

from backend.services.loan_amount_service import LoanAmountService
from backend.services.eligibility_service import EligibilityService

from backend.schemas import VehicleRequest
from backend.services.vehicle_service import VehicleService

from backend.schemas import LoanAdvisorRequest

from backend.schemas import ExplainRequest
from backend.services.rag_service import RAGService

app = FastAPI(
    title="Intelligent Vehicle Loan Advisor API",
    version="1.0.0",
    description="Backend APIs for the AI Engineering Capstone Project"
)

# Initialize services
eligibility_service = EligibilityService()
vehicle_service = VehicleService()
rag_service = RAGService()

@app.get("/")
def home():
    return {
        "message": "Welcome to Intelligent Vehicle Loan Advisor API"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "message": "API is running successfully"
    }


@app.post("/loan-amount")
def calculate_loan_amount(request: LoanAmountRequest):

    return LoanAmountService.calculate(
        monthly_income=request.monthly_income,
        existing_emi=request.existing_emi,
        tenure_years=request.tenure_years,
        annual_interest_rate=request.annual_interest_rate
    )


@app.post("/predict")
def predict(request: PredictionRequest):

    return eligibility_service.predict(
        request.model_dump()
    )

@app.post("/vehicles")
def get_vehicles(request: VehicleRequest):
    
    return vehicle_service.get_recommended_vehicles(
        request.budget
    )

@app.get("/vehicle/{vehicle_id}")
def get_vehicle(vehicle_id: int):

    vehicle = vehicle_service.get_vehicle(vehicle_id)

    if vehicle is None:
        return {
            "success": False,
            "message": "Vehicle not found."
        }

    return {
        "success": True,
        "data": vehicle
    }

@app.post("/loan-advisor")
def loan_advisor(request: LoanAdvisorRequest):

    applicant = request.model_dump()

    # -------------------------------------------------
    # Step 1 - Loan Eligibility Prediction
    # -------------------------------------------------

    prediction = eligibility_service.predict({
        "Gender": applicant["Gender"],
        "Married": applicant["Married"],
        "Dependents": applicant["Dependents"],
        "Education": applicant["Education"],
        "Self_Employed": applicant["Self_Employed"],
        "ApplicantIncome": applicant["ApplicantIncome"],
        "CoapplicantIncome": applicant["CoapplicantIncome"],
        "LoanAmount": applicant["LoanAmount"],
        "Loan_Amount_Term": applicant["Loan_Amount_Term"],
        "Credit_History": applicant["Credit_History"],
        "Property_Area": applicant["Property_Area"]
    })

    if prediction["prediction"] == "Rejected":
        return {
            "success": False,
            "message": "Loan application rejected.",
            "data": {
                "prediction": prediction
            }
        }

    # -------------------------------------------------
    # Step 2 - Calculate Maximum Eligible Loan
    # -------------------------------------------------

    loan = LoanAmountService.calculate(
        monthly_income=applicant["ApplicantIncome"],
        existing_emi=applicant["existing_emi"],
        tenure_years=int(applicant["Loan_Amount_Term"] / 12)
    )

    if not loan["approved"]:
        return {
            "success": False,
            "message": loan["message"],
            "data": loan
        }

    # -------------------------------------------------
    # Step 3 - Compare Requested vs Eligible Loan
    # -------------------------------------------------

    requested_loan = applicant["LoanAmount"] * 100000
    eligible_loan = loan["loan_amount"]

    if requested_loan <= eligible_loan:

        approved_loan = requested_loan

        decision_message = (
            "Requested loan amount is within the eligible limit."
        )

    else:

        approved_loan = eligible_loan

        decision_message = (
            "Requested loan amount exceeds eligibility. "
            "Maximum eligible loan has been approved."
        )

    loan["requested_loan"] = requested_loan
    loan["eligible_loan"] = eligible_loan
    loan["approved_loan"] = approved_loan
    loan["decision_message"] = decision_message

    # -------------------------------------------------
    # Step 4 - Budget Calculation
    # -------------------------------------------------

    budget = approved_loan + applicant["down_payment"]

    # -------------------------------------------------
    # Step 5 - Vehicle Recommendation
    # -------------------------------------------------

    vehicles = vehicle_service.get_recommended_vehicles(
        budget
    )

    # -------------------------------------------------
    # Step 6 - Response
    # -------------------------------------------------

    return {
        "success": True,
        "message": "Loan advisor completed successfully.",
        "data": {
            "prediction": prediction,
            "loan": loan,
            "budget": budget,
            "recommended_vehicles": vehicles
        }
    }

@app.post("/explain")
def explain_decision(request: ExplainRequest):

    return rag_service.explain(
        request.question
    )