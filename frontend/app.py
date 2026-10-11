import streamlit as st

home = st.Page(
    "pages/Home.py",
    title="Home",
    icon="🏠",
    default=True,
)

loan = st.Page(
    "pages/Loan_Advisor.py",
    title="Loan Advisor",
    icon="📝",
)

about = st.Page(
    "pages/About.py",
    title="About",
    icon="ℹ️",
)

pg = st.navigation(
    {
        "Vehicle Loan Advisor": [
            home,
            loan,
            about,
        ]
    }
)

st.set_page_config(
    page_title="Vehicle Loan Advisor",
    page_icon="🚗",
    layout="wide"
)

pg.run()