"""
hackrf_interface.py

Virtual HackRF
Counter Drone RF Detection System
"""

import numpy as np

from src.signal_generator import SignalGenerator

from src.frequency_hopper import FrequencyHopper


class VirtualHackRF:

    def __init__(self):

        self.generator = SignalGenerator()

        self.hopper = FrequencyHopper()

        self.connected = True

        self.sample_rate = 20e6

        self.center_frequency = 400e6

        self.gain = 30


    def connect(self):

        self.connected = True

        return True


    def disconnect(self):

        self.connected = False


    def set_frequency(self,freq):

        self.center_frequency = freq


    def hop(self):

        self.center_frequency = self.hopper.next_frequency()

        return self.center_frequency


    def receive(self):

        return self.generator.generate()


    def info(self):

        return {

            "Connected":self.connected,

            "Frequency":self.center_frequency,

            "SampleRate":self.sample_rate,

            "Gain":self.gain

        }