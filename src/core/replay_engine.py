"""
=========================================================
RF Replay Engine
Counter Drone RF Analyzer
=========================================================
"""

from pathlib import Path
import numpy as np

from src.io.dataset_loader import DatasetLoader
from src.core.feature_extractor import extract_features
from src.ai.predictor import AIPredictor


class ReplayEngine:

    def __init__(self, dataset_root):

        self.loader = DatasetLoader(dataset_root)

        self.ai = AIPredictor()
        self.ai.load()

        self.current_file = None
        self.chunk_generator = None

        self.chunk_index = 0
        self.total_chunks = 0

    # --------------------------------------------------

    def open_recording(self, file_path):

        file_path = Path(file_path)

        self.current_file = file_path

        signal = self.loader.load(file_path)

        chunk_size = 10000

        self.total_chunks = len(signal) // chunk_size

        self.chunk_index = 0

        self.chunk_generator = self.loader.stream(
            signal,
            chunk_size=chunk_size
        )

    # --------------------------------------------------

    def process_next_chunk(self):

        if self.chunk_generator is None:

            return None

        try:

            chunk = next(self.chunk_generator)

        except StopIteration:

            return None

        self.chunk_index += 1

        ##################################################
        # FFT
        ##################################################

        spectrum = np.abs(
            np.fft.fft(chunk)
        )[:512]

        spectrum = 20 * np.log10(
            spectrum + 1e-12
        )

        ##################################################
        # 22 FEATURES
        ##################################################

        features = extract_features(chunk)

        ##################################################
        # AI / WIFI CLASSIFICATION
        ##################################################

        if self.loader.file_type == "WIFI":

            result = {

                "prediction": "NOT DRONE",

                "confidence": 100.0

            }

        else:

            result = self.ai.predict(features)

        ##################################################
        # DISPLAY PREDICTION
        ##################################################

        if self.loader.file_type == "WIFI":

            prediction = "📶 WiFi SIGNAL"

        elif result["prediction"] == 1:

            prediction = "🟢 DRONE DETECTED"

        else:

            prediction = "🔴 NO DRONE"

        ##################################################
        # RF PARAMETERS
        ##################################################

        rssi = float(np.max(chunk))

        peak = float(np.max(spectrum))

        noise = float(np.mean(chunk))

        bandwidth = float(
            np.count_nonzero(
                spectrum > spectrum.mean()
            )
        )

        distance = max(
            1.0,
            abs(rssi + 90) * 2
        )

        ##################################################
        # BAND + SIGNAL CATEGORY
        ##################################################

        filename = self.current_file.name.lower()

        if "2400" in filename:

            band = "2.4 GHz"

        elif "5800" in filename:

            band = "5.8 GHz"

        elif "433" in filename:

            band = "433 MHz"

        elif "868" in filename:

            band = "868 MHz"

        elif "915" in filename:

            band = "915 MHz"

        else:

            band = "Unknown"

        ##################################################
        # SIGNAL CATEGORY
        ##################################################

        if self.loader.file_type == "WIFI":

            category = "WiFi"

        else:

            category = "Unknown"

            for part in self.current_file.parts:

                p = part.lower()

                if "ar drone" in p:

                    category = "AR Drone"

                    break

                elif "phantom" in p:

                    category = "Phantom Drone"

                    break

                elif "dji" in p:

                    category = "DJI Drone"

                    break

                elif "drone" in p:

                    category = "Drone"

                    break

                elif "ble" in p:

                    category = "Bluetooth"

                    break

                elif "wifi" in p:

                    category = "WiFi"

                    break

                elif "adsb" in p:

                    category = "ADS-B"

                    break

        ##################################################

        return {

            "file": self.current_file.name,

            "chunk": self.chunk_index,

            "total_chunks": self.total_chunks,

            "prediction": prediction,

            "confidence": result["confidence"],

            "spectrum": spectrum,

            "rssi": rssi,

            "peak_power": peak,

            "noise_floor": noise,

            "bandwidth": bandwidth,

            "distance": distance,

            "band": band,

            "category": category,

            "features": features

        }