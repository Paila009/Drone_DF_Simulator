"""
frequency_hopper.py

Random / Sequential / Manual Frequency Hopper
Counter Drone RF Detection System
"""

import random
from enum import Enum

from src.utils.config import START_FREQUENCY, END_FREQUENCY


class HopMode(Enum):
    RANDOM = 1
    SEQUENTIAL = 2
    MANUAL = 3


class FrequencyHopper:

    def __init__(self):

        self.mode = HopMode.RANDOM

        self.current_frequency = START_FREQUENCY

        self.manual_frequency = START_FREQUENCY

        self.step_size = 20e6

    def set_mode(self, mode):

        self.mode = mode

    def set_manual_frequency(self, freq):

        if START_FREQUENCY <= freq <= END_FREQUENCY:
            self.manual_frequency = freq

    def next_frequency(self):

        if self.mode == HopMode.RANDOM:

            self.current_frequency = random.uniform(
                START_FREQUENCY,
                END_FREQUENCY
            )

        elif self.mode == HopMode.SEQUENTIAL:

            self.current_frequency += self.step_size

            if self.current_frequency > END_FREQUENCY:

                self.current_frequency = START_FREQUENCY

        elif self.mode == HopMode.MANUAL:

            self.current_frequency = self.manual_frequency

        return self.current_frequency

    def get_band(self):

        f = self.current_frequency / 1e6

        if 400 <= f < 1000:
            return "UHF"

        elif 1000 <= f < 2000:
            return "L Band"

        elif 2000 <= f < 4000:
            return "S Band"

        elif 4000 <= f <= 6000:
            return "C Band"

        return "Unknown"

    def get_frequency_mhz(self):

        return self.current_frequency / 1e6