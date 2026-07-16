"""
====================================================
Counter Drone RF Detection System
System Engine
====================================================
"""

from src.core.virtual_receiver import VirtualReceiver
from src.core.frequency_hopper import FrequencyHopper
from src.core.detector import AIDetector


class SystemEngine:

    def __init__(self):

        print("Initializing Engine...")

        self.receiver = VirtualReceiver()
        self.hopper = FrequencyHopper()
        self.detector = AIDetector()

        print("Engine Ready.")

    def get_band(self, frequency):

        if 2400 <= frequency <= 2500:
            return "ISM 2.4 GHz"

        elif 5725 <= frequency <= 5900:
            return "ISM 5.8 GHz"

        elif frequency < 1000:
            return "UHF"

        elif frequency < 2000:
            return "L Band"

        elif frequency < 4000:
            return "S Band"

        else:
            return "C Band"

    def get_dashboard_data(self):

        frequency = self.hopper.next_frequency()

        signal_type, signal = self.receiver.capture(frequency)

        result = self.detector.detect(signal)

        rssi = float(signal.max())

        peak_power = float(signal.max())

        distance = max(
            1.0,
            abs(rssi + 90) * 2
        )

        if result["prediction"] == 1 and result["confidence"] >= 80:

            prediction = "DRONE DETECTED"

        else:

            prediction = "NO DRONE"

        return {

            "frequency": frequency,

            "band": self.get_band(frequency),

            "signal": signal_type,

            "prediction": prediction,

            "confidence": result["confidence"],

            "rssi": rssi,

            "peak_power": peak_power,

            "distance": distance,

            "spectrum": signal

        }