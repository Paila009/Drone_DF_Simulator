"""
=========================================================
Counter Drone RF Analyzer
Professional Dashboard V2
=========================================================
"""

from pathlib import Path

from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QFrame,
    QComboBox
)

from PyQt6.QtCore import Qt, QTimer

from src.gui.spectrum_widget import SpectrumWidget
from src.gui.waterfall_widget import WaterfallWidget
from src.core.replay_engine import ReplayEngine


class DashboardV2(QWidget):

    def __init__(self):
        super().__init__()

        self.engine = ReplayEngine(
            r"D:\Drone_AI_Training\datasets"
        )

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_frame
        )

        self.setWindowTitle(
            "Counter Drone RF Analyzer"
        )

        self.resize(1700, 950)

        self.build_ui()

        self.playButton.clicked.connect(
            lambda: self.timer.start(100)
        )

        self.pauseButton.clicked.connect(
            self.timer.stop
        )

        self.stopButton.clicked.connect(
            self.stop_analysis
        )

        self.resetButton.clicked.connect(
            self.reset_analysis
        )

    def build_ui(self):
        root = QHBoxLayout()

        ##################################################
        # LEFT PANEL
        ##################################################

        left = QVBoxLayout()

        ##################################################
        # TOOLBAR
        ##################################################

        toolbar = QHBoxLayout()

        ##################################################

        self.uploadButton = QPushButton("📁 Upload RF Recording")

        self.uploadButton.setMinimumHeight(45)

        self.uploadButton.clicked.connect(
            self.open_file
        )

        toolbar.addWidget(self.uploadButton)

        ##################################################

        self.bandMode = QComboBox()

        self.bandMode.addItems([
            "400-600 MHz",
            "600-900 MHz",
            "900-1200 MHz",
            "1.2-2 GHz",
            "2-3 GHz",
            "3-4 GHz",
            "4-5 GHz",
            "5-6 GHz",
            "2.4 GHz ISM",
            "5.8 GHz ISM",
            "FULL SCAN"
        ])

        toolbar.addWidget(self.bandMode)

        ##################################################

        self.playButton = QPushButton("▶ Play")

        toolbar.addWidget(self.playButton)

        ##################################################

        self.pauseButton = QPushButton("⏸ Pause")

        toolbar.addWidget(self.pauseButton)

        ##################################################

        self.stopButton = QPushButton("⏹ Stop")

        toolbar.addWidget(self.stopButton)

        ##################################################

        self.resetButton = QPushButton("↻ Reset")

        toolbar.addWidget(self.resetButton)

        ##################################################

        left.addLayout(toolbar)

        ##################################################

        self.info = QTextEdit()

        self.info.setReadOnly(True)

        self.info.setMinimumHeight(500)

        left.addWidget(self.info)

        ##################################################
        # RIGHT PANEL
        ##################################################

        right = QVBoxLayout()

        header = QLabel(
            "COUNTER DRONE RF ANALYZER"
        )

        header.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        header.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#00ff66;
            padding:15px;
        """)

        right.addWidget(header)

        ##################################################
        # RF SPECTRUM
        ##################################################

        self.spectrum = SpectrumWidget()

        right.addWidget(self.spectrum)

        ##################################################
        # WATERFALL
        ##################################################

        self.waterfall = WaterfallWidget()

        right.addWidget(self.waterfall)

        ##################################################

        root.addLayout(left, 1)

        root.addLayout(right, 4)

        self.setLayout(root)

    ############################################################
    # OPEN RF FILE
    ############################################################

    def open_file(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open RF Recording",
            r"D:\Drone_AI_Training\datasets",
            "RF Files (*.csv *.txt *.npy)"
        )

        if filename == "":
            return

        self.info.clear()
        self.info.append("Loading Recording...\n")
        self.info.append(filename)

        self.engine.open_recording(filename)
        self.timer.start(100)

    ############################################################
    # UPDATE EVERY 100 ms
    ############################################################

    def update_frame(self):

        data = self.engine.process_next_chunk()

        if data is None:
            self.timer.stop()
            self.info.append("\n\nAnalysis Finished.")
            return

        self.spectrum.update_spectrum(
            data["spectrum"]
        )

        self.waterfall.update_waterfall(
            data["spectrum"]
        )

        self.update_information(data)

    ############################################################
    # INFORMATION PANEL
    ############################################################

    def update_information(self, data):
        
        f = data["features"]
        
        snr = data["peak_power"] - data["noise_floor"]
        
        self.info.setText(
f"""
========================================================
COUNTER DRONE RF ANALYZER
========================================================

Recording
--------------------------------
{data['file']}

Signal Category
--------------------------------
{data['category']}

Band Mode
--------------------------------
{self.get_current_band()}

========================================================
AI RESULT
========================================================

Prediction
--------------------------------
{data['prediction']}

Confidence
--------------------------------
{data['confidence']:.2f} %

========================================================
RF POWER
========================================================

RSSI
--------------------------------
{data['rssi']:.2f} dBm

Peak Power
--------------------------------
{data['peak_power']:.2f}

Noise Floor
--------------------------------
{data['noise_floor']:.2f}

Estimated SNR
--------------------------------
{snr:.2f} dB

========================================================
TIME DOMAIN FEATURES
========================================================

Mean            : {f['mean']:.4f}

Std Dev         : {f['std']:.4f}

Variance        : {f['variance']:.4f}

RMS             : {f['rms']:.4f}

Energy          : {f['energy']:.2f}

Peak-Peak       : {f['peak_to_peak']:.4f}

Median          : {f['median']:.4f}

Crest Factor    : {f['crest_factor']:.4f}

========================================================
FREQUENCY DOMAIN
========================================================

FFT Mean        : {f['fft_mean']:.2f}

FFT Std         : {f['fft_std']:.2f}

FFT Energy      : {f['fft_energy']:.2f}

Spectral Entropy : {f['spectral_entropy']:.4f}

Spectral Centroid : {f['spectral_centroid']:.2f}

Spectral Flatness : {f['spectral_flatness']:.4f}

Peak FFT Bin    : {int(f['peak_frequency_bin'])}

========================================================

Distance Estimate
--------------------------------
{data['distance']:.2f} m

Replay Progress
--------------------------------
Chunk {data['chunk']} / {data['total_chunks']}

========================================================
"""
        )

    ############################################################
    # BAND MODE
    ############################################################

    def get_current_band(self):
        return self.bandMode.currentText()

    ############################################################

    def stop_analysis(self):
        self.timer.stop()
        self.info.append("\nStopped.")

    ############################################################

    def reset_analysis(self):
        self.timer.stop()
        self.info.clear()
        self.info.setText(
"""
Counter Drone RF Analyzer

Ready.

Upload a recording.
"""
        )