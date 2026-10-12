from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "models" / "loan_prediction_pipeline.pkl"


class EligibilityService:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, applicant_data: dict):

        applicant_df = pd.DataFrame([applicant_data])

        # Predict class
        prediction_code = self.model.predict(applicant_df)[0]

        # Predict probabilities
        probability = self.model.predict_proba(applicant_df)[0]

        prediction_text = (
            "Approved"
            if prediction_code == "Y"
            else "Rejected"
        )

        confidence = round(max(probability) * 100, 2)

        return {
            "prediction": prediction_text,
            "prediction_code": prediction_code,
            "confidence": confidence
        }