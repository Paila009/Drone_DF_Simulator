"""
signal_generator.py

Generates simulated RF spectrum
"""

import numpy as np
from src.utils.config import FFT_SIZE

class SignalGenerator:

    def __init__(self):
        self.noise_level = -90

    def generate_noise(self):
        """
        Generate background RF noise
        """
        return np.random.normal(-90, 2, FFT_SIZE)

    def add_drone_signal(self, spectrum):

        peak = np.random.randint(300, FFT_SIZE - 300)

        spectrum[peak-3:peak+3] = np.random.uniform(
            -35,
            -20,
            6
        )

        return spectrum

    def add_wifi_signal(self, spectrum):

        peak = np.random.randint(200, FFT_SIZE - 200)

        spectrum[peak-20:peak+20] = np.random.uniform(
            -55,
            -45,
            40
        )

        return spectrum

    def add_bluetooth_signal(self, spectrum):

        peak = np.random.randint(100, FFT_SIZE - 100)

        spectrum[peak-5:peak+5] = np.random.uniform(
            -60,
            -50,
            10
        )

        return spectrum

    def generate(self):

        spectrum = self.generate_noise()

        if np.random.rand() > 0.5:
            spectrum = self.add_drone_signal(spectrum)

        if np.random.rand() > 0.4:
            spectrum = self.add_wifi_signal(spectrum)

        if np.random.rand() > 0.6:
            spectrum = self.add_bluetooth_signal(spectrum)

        return spectrum

# =====================================================
# Compatibility function
# =====================================================

def generate_signal(signal_type="noise"):
    """
    Returns a simulated RF spectrum for the requested signal type.
    """

    generator = SignalGenerator()

    spectrum = generator.generate_noise()

    if signal_type == "drone":
        spectrum = generator.add_drone_signal(spectrum)

    elif signal_type == "wifi":
        spectrum = generator.add_wifi_signal(spectrum)

    elif signal_type == "bluetooth":
        spectrum = generator.add_bluetooth_signal(spectrum)

    return spectrum