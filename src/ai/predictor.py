"""
=========================================================
AI Predictor
Counter Drone RF Detection System
=========================================================
"""

import os
import joblib
import numpy as np


class AIPredictor:

    def __init__(self):

        self.model = None
        self.feature_names = None

    def load(self):

        model_path = os.path.join(
            "models",
            "rf_model.pkl"
        )

        feature_path = os.path.join(
            "models",
            "feature_names.pkl"
        )

        if not os.path.exists(model_path):
            raise FileNotFoundError(model_path)

        self.model = joblib.load(model_path)

        if os.path.exists(feature_path):
            self.feature_names = joblib.load(feature_path)

        print("AI Model Loaded Successfully")

    def predict(self, feature_dict):

        if self.model is None:
            raise RuntimeError("Model Not Loaded")

        if self.feature_names is None:

            feature_vector = np.array(
                list(feature_dict.values())
            ).reshape(1, -1)

        else:

            feature_vector = np.array(

                [
                    feature_dict[name]
                    for name in self.feature_names
                ]

            ).reshape(1, -1)

        prediction = self.model.predict(
            feature_vector
        )[0]

        confidence = np.max(

            self.model.predict_proba(
                feature_vector
            )

        )

        return {

            "prediction": int(prediction),

            "confidence": float(confidence)

        }