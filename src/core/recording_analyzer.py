"""
=========================================================
Recording Analyzer
Counter Drone RF Detection System
=========================================================
"""

import numpy as np

from src.io.dataset_loader import DatasetLoader
from src.core.replay_engine import ReplayEngine
from src.core.feature_extractor import extract_features
from src.ai.predictor import AIPredictor


class RecordingAnalyzer:

    def __init__(self):

        self.loader = DatasetLoader()

        self.replay = ReplayEngine()

        self.ai = AIPredictor()

        self.ai.load()

    def load_recording(self, filename):

        samples = self.loader.load(filename)

        self.replay.load(samples)

    def next_frame(self):

        chunk = self.replay.next_chunk()

        if chunk is None:

            return None

        #################################################
        # FFT
        #################################################

        fft = np.abs(np.fft.fft(chunk))

        #################################################
        # FEATURES
        #################################################

        features = extract_features(chunk)

        #################################################
        # AI
        #################################################

        result = self.ai.predict(features)

        #################################################
        # RF PARAMETERS
        #################################################

        rssi = float(np.max(chunk))

        peak = float(np.max(fft))

        noise = float(np.mean(chunk))

        bandwidth = float(np.count_nonzero(
            fft > fft.mean()
        ))

        distance = max(
            1.0,
            abs(rssi + 90) * 2
        )

        return {

            "chunk": chunk,

            "fft": fft,

            "prediction": result["prediction"],

            "confidence": result["confidence"],

            "rssi": rssi,

            "peak_power": peak,

            "noise_floor": noise,

            "bandwidth": bandwidth,

            "distance": distance,

            "features": features

        }