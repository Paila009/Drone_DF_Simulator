"""
fft_processor.py

Performs FFT processing on RF signals.
"""

import numpy as np


class FFTProcessor:

    def __init__(self):
        pass

    def process(self, signal):

        fft = np.fft.fft(signal)

        fft = np.fft.fftshift(fft)

        magnitude = np.abs(fft)

        magnitude_db = 20 * np.log10(magnitude + 1e-12)

        return magnitude_db