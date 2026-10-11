from typing import Dict


class LoanAmountService:

    MAX_EMI_PERCENTAGE = 0.40
    DEFAULT_INTEREST_RATE = 9.0

    @staticmethod
    def calculate(
        monthly_income: float,
        existing_emi: float,
        tenure_years: int,
        annual_interest_rate: float = DEFAULT_INTEREST_RATE,
    ) -> Dict:

        max_emi = monthly_income * LoanAmountService.MAX_EMI_PERCENTAGE

        available_emi = max_emi - existing_emi

        if available_emi <= 0:
            return {
                "approved": False,
                "loan_amount": 0,
                "available_emi": 0,
                "message": "Existing EMI exceeds repayment capacity."
            }

        monthly_interest = annual_interest_rate / (12 * 100)

        months = tenure_years * 12

        loan_amount = (
            available_emi
            * (((1 + monthly_interest) ** months) - 1)
            / (monthly_interest * ((1 + monthly_interest) ** months))
        )

        return {
            "approved": True,
            "loan_amount": round(loan_amount),
            "available_emi": round(available_emi),
            "max_allowed_emi": round(max_emi)
        }