import os
import requests

BASE_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)

def check_health():
    return requests.get(f"{BASE_URL}/health")


def predict(data):
    return requests.post(
        f"{BASE_URL}/predict",
        json=data
    )


def loan_amount(data):
    return requests.post(
        f"{BASE_URL}/loan-amount",
        json=data
    )


def loan_advisor(data):
    return requests.post(
        f"{BASE_URL}/loan-advisor",
        json=data
    )


def vehicle(vehicle_id):
    return requests.get(
        f"{BASE_URL}/vehicle/{vehicle_id}"
    )


def explain(question):
    return requests.post(
        f"{BASE_URL}/explain",
        json={
            "question": question
        }
    )