"""
feature_schema.py

Defines the feature order used by both
Drone_AI_Training and CounterDroneProject.
"""

FEATURES = [
    "frequency_mhz",
    "rssi_dbm",
    "peak_power_dbm",
    "fft_energy",
    "noise_floor_dbm",
    "bandwidth_mhz",
    "band_id"
]

LABELS = [
    "No Drone",
    "Drone"
]

FEATURE_COUNT = len(FEATURES)