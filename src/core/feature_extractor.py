"""
=========================================================
RF FEATURE EXTRACTOR
Counter Drone Detection System
Author : Paila Akash
=========================================================
"""

import os
import glob
import numpy as np
from scipy.fft import fft
from scipy.stats import entropy, kurtosis, skew

# =====================================================
# CONFIGURATION
# =====================================================

CHUNK_SIZE = 10000

# Number of FFT bins to keep
FFT_BINS = 512

# =====================================================
# READ RF FILE
# =====================================================

def read_rf_file(file_path):
    """
    Reads one RF CSV file.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    signal : numpy.ndarray
    """

    print(f"\nReading : {os.path.basename(file_path)}")

    signal = np.loadtxt(
        file_path,
        delimiter=",",
        dtype=np.float32
    )

    signal = signal.flatten()

    print(f"Samples Loaded : {len(signal):,}")

    return signal


# =====================================================
# SPLIT SIGNAL INTO SMALL CHUNKS
# =====================================================

def split_signal(signal, chunk_size=CHUNK_SIZE):
    """
    Split RF signal into equal chunks.
    """

    chunks = []

    total_chunks = len(signal) // chunk_size

    for i in range(total_chunks):

        start = i * chunk_size
        end = start + chunk_size

        chunk = signal[start:end]

        chunks.append(chunk)

    print(f"Chunks Created : {len(chunks)}")

    return chunks


# =====================================================
# APPLY FFT
# =====================================================

def compute_fft(signal):

    spectrum = np.abs(fft(signal))

    spectrum = spectrum[:FFT_BINS]

    return spectrum


# =====================================================
# SIGNAL ENERGY
# =====================================================

def signal_energy(signal):

    return np.sum(signal ** 2)


# =====================================================
# RMS
# =====================================================

def rms(signal):

    return np.sqrt(np.mean(signal ** 2))

# =====================================================
# TIME DOMAIN FEATURES
# =====================================================

def extract_time_features(signal):
    """
    Extract time-domain features from one RF chunk.
    """

    features = {}

    features["mean"] = np.mean(signal)
    features["std"] = np.std(signal)
    features["variance"] = np.var(signal)

    features["minimum"] = np.min(signal)
    features["maximum"] = np.max(signal)

    features["rms"] = rms(signal)

    features["energy"] = signal_energy(signal)

    features["peak_to_peak"] = np.ptp(signal)

    features["median"] = np.median(signal)

    features["mean_absolute"] = np.mean(np.abs(signal))

    features["crest_factor"] = (
        np.max(np.abs(signal))
        /
        (features["rms"] + 1e-12)
    )

    features["skewness"] = skew(signal)

    features["kurtosis"] = kurtosis(signal)

    return features


# =====================================================
# FREQUENCY DOMAIN FEATURES
# =====================================================

def extract_frequency_features(signal):
    """
    Extract frequency-domain features.
    """

    spectrum = compute_fft(signal)

    features = {}

    features["fft_mean"] = np.mean(spectrum)

    features["fft_std"] = np.std(spectrum)

    features["fft_max"] = np.max(spectrum)

    features["fft_min"] = np.min(spectrum)

    features["fft_energy"] = np.sum(spectrum ** 2)

    power = spectrum ** 2

    power = power / (np.sum(power) + 1e-12)

    features["spectral_entropy"] = entropy(power)

    features["spectral_centroid"] = np.sum(
        np.arange(len(spectrum)) * spectrum
    ) / (np.sum(spectrum) + 1e-12)

    features["spectral_flatness"] = (
        np.exp(np.mean(np.log(spectrum + 1e-12)))
        /
        (np.mean(spectrum) + 1e-12)
    )

    features["peak_frequency_bin"] = np.argmax(spectrum)

    return features

# =====================================================
# COMBINE ALL FEATURES
# =====================================================

def extract_features(signal):
    """
    Extract RF features directly from a NumPy signal.
    """

    if len(signal) == 0:
        return None

    features = {}

    features.update(
        extract_time_features(signal)
    )

    features.update(
        extract_frequency_features(signal)
    )

    return features
# =====================================================
# PROCESS COMPLETE RF FILE
# =====================================================

def process_rf_file(file_path):

    signal = read_rf_file(file_path)

    chunks = split_signal(signal)

    feature_list = []

    print("\nExtracting Features...\n")

    total_chunks = len(chunks)

    for i, chunk in enumerate(chunks):

        features = extract_features(chunk)

        feature_list.append(features)

        if (i + 1) % 100 == 0 or i == total_chunks - 1:
            print(
                f"Processed {i+1}/{total_chunks} chunks"
            )

    print("\nFeature Extraction Complete!")

    return feature_list