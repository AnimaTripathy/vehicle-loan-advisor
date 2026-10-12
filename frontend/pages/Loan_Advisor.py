import streamlit as st

from utils.api import (
    loan_advisor,
    vehicle as vehicle_api,
    explain
)

# =====================================================
# SESSION STATE
# =====================================================

if "loan_result" not in st.session_state:
    st.session_state.loan_result = None

if "ai_answers" not in st.session_state:
    st.session_state.ai_answers = {}

# =====================================================
# PAGE HEADER
# =====================================================

st.title("🚗 Vehicle Loan Advisor")

st.markdown(
"""
Welcome!

Complete the applicant information below to:

- Predict loan eligibility
- Calculate maximum loan amount
- Get vehicle recommendations
- Receive AI-powered explanations
"""
)

# =====================================================
# CLEAR RESULTS
# =====================================================

if st.button("🗑️ Clear Results"):

    st.session_state.loan_result = None
    st.session_state.ai_answers = {}

    st.rerun()

# =====================================================
# APPLICANT FORM
# =====================================================

with st.form("loan_form"):

    st.subheader("👤 Applicant Information")

    left, right = st.columns(2)

    # -----------------------------------------
    # LEFT
    # -----------------------------------------

    with left:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        married = st.selectbox(
            "Married",
            ["Yes", "No"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["0", "1", "2", "3+"]
        )

        education = st.selectbox(
            "Education",
            ["Graduate", "Not Graduate"]
        )

        self_employed = st.selectbox(
            "Self Employed",
            ["No", "Yes"]
        )

        property_area = st.selectbox(
            "Property Area",
            ["Urban", "Semiurban", "Rural"]
        )

    # -----------------------------------------
    # RIGHT
    # -----------------------------------------

    with right:

        applicant_income = st.number_input(
            "Applicant Monthly Income (₹)",
            min_value=0,
            value=85000,
            step=1000
        )

        coapplicant_income = st.number_input(
            "Co-applicant Monthly Income (₹)",
            min_value=0,
            value=12000,
            step=1000
        )

        requested_loan_amount = st.number_input(
            "Requested Loan Amount (Lakhs)",
            min_value=0,
            value=150
        )

        loan_term = st.number_input(
            "Loan Term (Months)",
            min_value=12,
            value=360
        )

        credit_history = st.selectbox(
            "Credit History",
            [1, 0],
            format_func=lambda x:
                "Good (1)" if x == 1 else "Poor (0)"
        )

        existing_emi = st.number_input(
            "Existing EMI (₹)",
            min_value=0,
            value=12000,
            step=500
        )

        down_payment = st.number_input(
            "Down Payment (₹)",
            min_value=0,
            value=150000,
            step=10000
        )

    submit = st.form_submit_button(
        "🚗 Check Loan Eligibility"
    )

# =====================================================
# PAYLOAD
# =====================================================

payload = {
    "Gender": gender,
    "Married": married,
    "Dependents": dependents,
    "Education": education,
    "Self_Employed": self_employed,
    "ApplicantIncome": applicant_income,
    "CoapplicantIncome": coapplicant_income,
    "LoanAmount": requested_loan_amount,
    "Loan_Amount_Term": loan_term,
    "Credit_History": credit_history,
    "Property_Area": property_area,
    "existing_emi": existing_emi,
    "down_payment": down_payment
}

# =====================================================
# CALL BACKEND
# =====================================================

if submit:

    with st.spinner("🔄 Analyzing your loan application..."):

        response = loan_advisor(payload)

    # --------------------------------------------
    # HTTP Validation
    # --------------------------------------------

    if response.status_code != 200:

        st.error(
            f"Server Error ({response.status_code})"
        )

        st.code(response.text)

        st.stop()

    result = response.json()

    # --------------------------------------------
    # Business Validation
    # --------------------------------------------

    if not result["success"]:

        st.error(result["message"])

        st.stop()

    # Save the successful result

    st.session_state.loan_result = result

# =====================================================
# DISPLAY SAVED RESULT
# =====================================================

if st.session_state.loan_result:

    result = st.session_state.loan_result

    prediction = result["data"]["prediction"]

    loan = result["data"]["loan"]

    budget = result["data"]["budget"]

    vehicles = result["data"]["recommended_vehicles"]

    # --------------------------------------------
    # Success Banner
    # --------------------------------------------

    st.success(
        "✅ Loan evaluation completed successfully."
    )

    st.divider()

    # --------------------------------------------
    # Prediction
    # --------------------------------------------

    st.subheader("📊 Loan Prediction")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Loan Status",
            prediction["prediction"]
        )

    with col2:

        st.metric(
            "Confidence",
            f"{prediction['confidence']}%"
        )

    st.divider()

    # --------------------------------------------
    # Loan Summary
    # --------------------------------------------

    st.subheader("💰 Loan Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Requested Loan Amount",
            f"₹ {loan['requested_loan']:,}"
        )

        st.metric(
            "Eligible Loan Amount",
            f"₹ {loan['eligible_loan']:,}"
        )

    with col2:

        st.metric(
            "Approved Loan Amount",
            f"₹ {loan['approved_loan']:,}"
        )

        st.metric(
            "Available Budget",
            f"₹ {int(budget):,}"
        )

    st.success(
        f"📌 Loan Decision: {loan['decision_message']}"
    )

    st.info(
        f"""
    Your total purchasing budget is **₹ {int(budget):,}**

    Budget = Approved Loan + Down Payment
    """
    )

    st.divider()

# =====================================================
# BEST MATCHES
# =====================================================

    st.subheader("🚗 Best Matches For Your Budget")

    st.caption(
        "Recommendations are selected from vehicles that best match your approved budget."
    )

    if not vehicles:

        st.warning("No suitable vehicles were found within your preferred budget range.")

    else:

        for vehicle in vehicles:

            with st.container(border=True):

                # -----------------------------------------
                # Vehicle Header
                # -----------------------------------------

                st.markdown(
                    f"## 🚗 {vehicle['brand']} {vehicle['model']} ({vehicle['variant']})"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Price",
                        f"₹ {vehicle['price']:,}"
                    )

                with col2:

                    st.metric(
                        "Fuel",
                        vehicle["fuel_type"]
                    )

                with col3:

                    st.metric(
                        "Transmission",
                        vehicle["transmission"]
                    )

                # -----------------------------------------
                # Vehicle Details
                # -----------------------------------------

                with st.expander("🔍 View Complete Details"):

                    details_response = vehicle_api(
                        vehicle["id"]
                    )

                    if details_response.status_code == 200:

                        details = details_response.json()

                        if details["success"]:

                            car = details["data"]

                            st.markdown(
                                "### Vehicle Specifications"
                            )

                            left, right = st.columns(2)

                            with left:

                                st.write(
                                    f"**Brand:** {car['brand']}"
                                )

                                st.write(
                                    f"**Model:** {car['model']}"
                                )

                                st.write(
                                    f"**Variant:** {car['variant']}"
                                )

                                st.write(
                                    f"**Fuel Type:** {car['fuel_type']}"
                                )

                                st.write(
                                    f"**Transmission:** {car['transmission']}"
                                )

                            with right:

                                st.write(
                                    f"**Price:** ₹ {car['price']:,}"
                                )

                                st.write(
                                    f"**Mileage:** {car['mileage']} km/l"
                                )

                                st.write(
                                    f"**Engine:** {car['engine']}"
                                )

                                st.write(
                                    f"**Seats:** {car['seating_capacity']}"
                                )

                                st.write(
                                    f"**Body Type:** {car['body_type']}"
                                )

                            st.divider()

                            if st.button(
                                "🤖 Why was this vehicle recommended?",
                                key=f"explain_{vehicle['id']}"
                            ):

                                question = f"""
                                Applicant Result

                                Prediction:
                                {prediction['prediction']}

                                Confidence:
                                {prediction['confidence']}%

                                Requested Loan Amount:
                                ₹ {loan['requested_loan']:,}

                                Eligible Loan Amount:
                                ₹ {loan['eligible_loan']:,}

                                Approved Loan Amount:
                                ₹ {loan['approved_loan']:,}

                                Loan Decision:
                                {loan['decision_message']}

                                Available Budget:
                                ₹ {int(budget):,}

                                Recommended Vehicle:
                                {vehicle['brand']} {vehicle['model']}

                                Variant:
                                {vehicle['variant']}

                                Vehicle Price:
                                ₹ {vehicle['price']:,}

                                Applicant Context:

                                This applicant has already received a loan decision and a vehicle recommendation.

                                Please explain:

                                1. Why this vehicle fits the approved budget.
                                2. How the approved loan amount and available budget influenced the recommendation.
                                3. Which vehicle loan policy rules support this recommendation.
                                4. Do not mention information that is not present in the policy.
                                5. If the policy does not specify any next steps, do not invent them.

                                Provide the explanation in clear business language.
                                """

                                with st.spinner(
                                    "Generating AI recommendation..."
                                ):

                                    ai_response = explain(
                                        question
                                    )

                                if ai_response.status_code == 200:

                                    answer = ai_response.json()

                                    st.session_state.ai_answers[
                                        vehicle["id"]
                                    ] = answer["answer"]

                                else:

                                    st.error(
                                        "Unable to generate AI recommendation."
                                    )

                            if vehicle["id"] in st.session_state.ai_answers:

                                with st.container(border=True):

                                    st.markdown(
                                        "### 🤖 AI Recommendation"
                                    )

                                    st.markdown(
                                        st.session_state.ai_answers[
                                            vehicle["id"]
                                        ]
                                    )

                                    st.caption(
                                        "Generated using the Vehicle Loan Policy and Google Gemini AI."
                                    )

                        else:

                            st.error(
                                details["message"]
                            )

                    else:

                        st.error(
                            "Unable to retrieve vehicle details."
                        )
# =====================================================
# FINAL SUMMARY
# =====================================================

    st.divider()

    st.markdown(
        """
### 📌 Next Steps

- ✅ Review the recommended vehicles.
- ✅ Expand a vehicle to view detailed specifications.
- ✅ Use **🤖 Why was this vehicle recommended?** to understand the recommendation.
- ✅ Compare the recommended vehicles before making a purchase decision.

---
"""
    )

    # --------------------------------------------
    # Applicant Summary
    # --------------------------------------------

    st.subheader("📋 Applicant Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:

        st.write(f"**Applicant Income:** ₹ {applicant_income:,}")

        st.write(f"**Existing EMI:** ₹ {existing_emi:,}")

        st.write(f"**Down Payment:** ₹ {down_payment:,}")

    with summary_col2:

        st.write(f"**Requested Loan:** ₹ {loan['requested_loan']:,}")

        st.write(f"**Approved Loan:** ₹ {loan['approved_loan']:,}")

        st.write(f"**Available Budget:** ₹ {int(budget):,}")

        st.metric(
            "Vehicles Recommended",
            len(vehicles)
        )

    st.divider()

    # --------------------------------------------
    # Footer
    # --------------------------------------------

    st.caption(
        """
🚗 Intelligent Vehicle Loan Advisor

Developed as an AI Engineering Capstone Project

Technologies:
FastAPI | Streamlit | Scikit-Learn | SQLite | FAISS | LangChain | Google Gemini
"""
    )                      
                       
                       