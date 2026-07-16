"""
=========================================================
RF Replay Engine
Counter Drone RF Detection System
=========================================================
"""

import numpy as np
from pathlib import Path

from src.io.dataset_loader import DatasetLoader
from src.core.feature_extractor import extract_features
from src.ai.predictor import AIPredictor


class ReplayEngine:

    def __init__(self, dataset_folder):

        self.loader = DatasetLoader(dataset_folder)

        self.ai = AIPredictor()

        self.ai.load()

        self.files = self.loader.list_recordings()

        self.current_index = 0

        self.chunk_generator = None

        self.current_file = None

    def open_file(self, index):
        self.current_index = index

        self.current_file = self.files[index]

        signal = self.loader.load(self.current_file)

        self.chunk_generator = self.loader.stream(
            signal,
            chunk_size=10000
        )

    def open_path(self, file_path):

        self.current_index = -1

        self.current_file = Path(file_path)

        signal = self.loader.load(self.current_file)

        self.chunk_generator = self.loader.stream(
            signal,
            chunk_size=10000
        )

    def next_chunk(self):

        if self.chunk_generator is None:

            self.open_file(0)

        try:

            chunk = next(self.chunk_generator)

        except StopIteration:

            self.current_index += 1

            if self.current_index >= len(self.files):

                self.current_index = 0

            self.open_file(self.current_index)

            chunk = next(self.chunk_generator)

        return chunk

    def process(self):

        signal = self.next_chunk()

        features = extract_features(signal)

        result = self.ai.predict(features)

        spectrum = np.abs(
            np.fft.fft(signal)
        )[:512]

        spectrum = 20 * np.log10(
            spectrum + 1e-12
        )

        rssi = float(signal.max())

        peak = float(np.max(spectrum))

        distance = max(
            1.0,
            abs(rssi + 90) * 2
        )

        return {

            "file": self.current_file.name,

            "prediction": result["prediction"],

            "confidence": result["confidence"],

            "signal": signal,

            "spectrum": spectrum,

            "rssi": rssi,

            "peak_power": peak,

            "distance": distance

        }