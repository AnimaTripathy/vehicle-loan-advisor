from pydantic import BaseModel


class LoanAmountRequest(BaseModel):
    monthly_income: float
    existing_emi: float
    tenure_years: int
    annual_interest_rate: float = 9.0

class PredictionRequest(BaseModel):

    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str

    ApplicantIncome: float
    CoapplicantIncome: float

    LoanAmount: float
    Loan_Amount_Term: float

    Credit_History: float

    Property_Area: str

class VehicleRequest(BaseModel):

    budget: int

class LoanAdvisorRequest(BaseModel):

    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str

    ApplicantIncome: float
    CoapplicantIncome: float

    LoanAmount: float
    Loan_Amount_Term: float

    Credit_History: float

    Property_Area: str

    existing_emi: float
    down_payment: float

class ExplainRequest(BaseModel):
    question: str