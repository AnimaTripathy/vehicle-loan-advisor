from services.loan_amount_service import calculate_max_loan

result = calculate_max_loan(
    monthly_income=80000,
    existing_emi=12000,
    tenure_years=5
)

print(result)