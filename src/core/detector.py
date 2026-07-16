"""
=========================================================
AI Detection Engine
Counter Drone RF Detection System
=========================================================
"""

from src.ai.predictor import AIPredictor
from src.core.feature_extractor import extract_features


class AIDetector:

    def __init__(self):

        self.ai = AIPredictor()
        self.ai.load()

    def detect(self, signal):

        # Extract AI features
        features = extract_features(signal)

        # AI Prediction
        result = self.ai.predict(features)

        return {

            "prediction": result["prediction"],

            "confidence": result["confidence"],

            "features": features

        }