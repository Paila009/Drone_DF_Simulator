"""
=========================================================
Dataset Loader
Supports:
1. DroneRF IQ CSV
2. WiFi Preamble Dataset
3. Bluetooth
4. LTE
=========================================================
"""

from pathlib import Path
import numpy as np
import pandas as pd
import re


class DatasetLoader:

    def __init__(self, dataset_root):

        self.dataset_root = Path(dataset_root)

        self.file_type = "DRONE"

    ############################################################

    def list_recordings(self):

        files = []

        for ext in ("*.csv", "*.txt", "*.npy"):

            files.extend(
                self.dataset_root.rglob(ext)
            )

        return sorted(files)

    ############################################################

    def load(self, file_path):

        file_path = Path(file_path)

        suffix = file_path.suffix.lower()

        if suffix == ".npy":

            self.file_type = "DRONE"

            signal = np.load(file_path)

            return signal.flatten()

        ########################################################
        # TXT
        ########################################################

        if suffix == ".txt":

            self.file_type = "DRONE"

            signal = np.loadtxt(
                file_path,
                dtype=np.float32
            )

            return signal.flatten()

        ########################################################
        # CSV
        ########################################################

        try:

            signal = np.loadtxt(
                file_path,
                delimiter=",",
                dtype=np.float32
            )

            self.file_type = "DRONE"

            return signal.flatten()

        except Exception:

            pass

        ########################################################
        # Detect Dataset Type
        ########################################################

        df = pd.read_csv(file_path)

        cols = [c.lower().strip() for c in df.columns]

        ########################################################
        # WIFI
        ########################################################

        if "preamble" in cols:

            self.file_type = "WIFI"

            preamble_column = df.columns[
                cols.index("preamble")
            ]

            samples = []

            for value in df[preamble_column]:

                if pd.isna(value):
                    continue

                text = str(value)

                text = text.replace("[", "")
                text = text.replace("]", "")
                text = text.replace("\n", " ")
                text = text.replace("\r", " ")

                numbers = re.findall(
                    r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?[-+]\d*\.?\d+(?:[eE][-+]?\d+)?j',
                    text
                )

                for n in numbers:

                    try:

                        samples.append(abs(complex(n)))

                    except Exception:

                        pass

            return np.asarray(samples, dtype=np.float32)

        ########################################################
        # BLUETOOTH
        ########################################################

        elif "central fre" in " ".join(cols):

            self.file_type = "BLUETOOTH"

            center_col = None

            for c in df.columns:

                if "central" in c.lower():

                    center_col = c

                    break

            signal = df[center_col].astype(float).to_numpy()

            return signal.astype(np.float32)

        ########################################################
        # LTE
        ########################################################

        elif "rsrp" in cols and "rsrq" in cols:

            self.file_type = "LTE"

            signal = df["RSSI"].astype(float).to_numpy()

            return signal.astype(np.float32)

        ########################################################

        raise ValueError("Unsupported CSV dataset.")

    ############################################################

    def stream(self, signal, chunk_size=10000):

        total = len(signal)

        for start in range(0, total, chunk_size):

            yield signal[
                start:start + chunk_size
            ]