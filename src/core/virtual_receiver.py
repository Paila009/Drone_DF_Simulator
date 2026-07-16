"""
Virtual RF Receiver
Simulates HackRF One
"""

import numpy as np

from src.core.signal_generator import generate_signal


class VirtualReceiver:

    def __init__(self):
        pass

    def capture(self, frequency):

        signal_type = np.random.choice(
            [
                "noise",
                "wifi",
                "bluetooth",
                "drone"
            ],
            p=[0.45, 0.20, 0.15, 0.20]
        )

        signal = generate_signal(signal_type)

        return signal_type, signal