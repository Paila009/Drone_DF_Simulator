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
    QFrame,
    QTextEdit
)

from PyQt6.QtCore import Qt, QTimer

from src.gui.dataset_browser import DatasetBrowser
from src.gui.spectrum_widget import SpectrumWidget
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

        self.browser.recordingSelected.connect(
            self.load_recording
        )

        self.openButton.clicked.connect(
            self.open_selected_recording
        )

    def build_ui(self):

        root = QHBoxLayout()

        ##################################################
        # LEFT PANEL
        ##################################################

        left = QVBoxLayout()

        title = QLabel("RF DATASET")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""

            font-size:18px;
            font-weight:bold;
            color:white;
            padding:10px;

        """)

        left.addWidget(title)

        self.browser = DatasetBrowser(
            r"D:\Drone_AI_Training\datasets"
        )

        left.addWidget(self.browser)

        self.openButton = QPushButton(
            "Open Selected Recording"
        )

        left.addWidget(self.openButton)

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
        # WATERFALL PLACEHOLDER
        ##################################################

        self.waterfallFrame = QFrame()

        self.waterfallFrame.setMinimumHeight(220)

        self.waterfallFrame.setStyleSheet("""

            background:black;

            border:2px solid cyan;

        """)

        right.addWidget(self.waterfallFrame)

        ##################################################
        # INFORMATION PANEL
        ##################################################

        self.info = QTextEdit()

        self.info.setReadOnly(True)

        self.info.setMinimumHeight(180)

        self.info.setStyleSheet("""

            background:#101820;

            color:#00ff66;

            font-size:15px;

        """)

        self.info.setText(

            """
Ready.

Choose a recording from the dataset.

Click:

Open Selected Recording

FFT and Waterfall will appear here.
            """

        )

        right.addWidget(self.info)

        ##################################################

        root.addLayout(left, 1)

        root.addLayout(right, 4)

        self.setLayout(root)

    def open_selected_recording(self):

        current_item = self.browser.tree.currentItem()

        if current_item is None:

            self.info.clear()

            self.info.append("Select a recording first.")

            return

        path = current_item.data(0, 1)

        if not path or not Path(path).is_file():

            self.info.clear()

            self.info.append("Select a file, not a folder.")

            return

        self.load_recording(path)

    def load_recording(self, path):

        self.engine.open_recording(path)

        self.info.clear()

        self.info.append("Recording Loaded\n")

        self.info.append(path)

        self.timer.start(100)

    def update_frame(self):

        data = self.engine.process_next_chunk()

        if data is None:

            self.timer.stop()

            self.info.append("\nAnalysis Finished.")

            return

        self.spectrum.update_spectrum(
            data["spectrum"]
        )

        self.info.setText(

            f"""
Recording

{data['file']}

Chunk

{data['chunk']}/{data['total_chunks']}

Prediction

{data['prediction']}

Confidence

{data['confidence']:.2f} %

RSSI

{data['rssi']:.2f}

Peak Power

{data['peak_power']:.2f}

Noise Floor

{data['noise_floor']:.2f}

Bandwidth

{data['bandwidth']:.2f}

Distance

{data['distance']:.2f} m

Band

{data['band']}

"""

        )