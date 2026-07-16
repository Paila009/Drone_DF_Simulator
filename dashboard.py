"""
=========================================================
Professional Counter Drone RF Dashboard
Author : Paila Akash
=========================================================
"""

import numpy as np

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame
)

from PyQt6.QtCore import Qt

from PyQt6.QtGui import QFont

from src.gui.fft_widget import FFTWidget
from src.gui.waterfall_widget import WaterfallWidget
from src.gui.frequency_widget import FrequencyWidget


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Counter Drone RF Detection System"
        )

        self.resize(1700,950)

        self.setStyleSheet("""

        QWidget{

            background:#0b1220;
            color:white;

            font-family:Consolas;
            font-size:12pt;

        }

        QLabel{

            color:white;

        }

        QTextEdit{

            background:#111827;

            color:#00ff88;

            border:1px solid #444;

        }

        """)

        self.build_ui()

    def build_ui(self):

        root = QVBoxLayout()

        ##################################################
        # TITLE
        ##################################################

        title = QLabel(
            "COUNTER DRONE RF DETECTION SYSTEM"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setFont(
            QFont(
                "Consolas",
                20,
                QFont.Weight.Bold
            )
        )

        root.addWidget(title)

        ##################################################
        # FFT
        ##################################################

        self.fft = FFTWidget()

        root.addWidget(self.fft)

        ##################################################
        # WATERFALL
        ##################################################

        self.waterfall = WaterfallWidget()

        root.addWidget(self.waterfall)

        ##################################################
        # FREQUENCY HOPPER
        ##################################################

        self.frequency = FrequencyWidget()

        root.addWidget(self.frequency)

        ##################################################
        # LOWER PANEL
        ##################################################

        bottom = QHBoxLayout()

        ##################################################
        # LEFT STATUS
        ##################################################

        left = QGridLayout()

        self.lblFrequency = QLabel()

        self.lblBand = QLabel()

        self.lblSignal = QLabel()

        self.lblPrediction = QLabel()

        self.lblConfidence = QLabel()

        self.lblRSSI = QLabel()

        self.lblPeak = QLabel()

        self.lblDistance = QLabel()

        left.addWidget(
            self.lblFrequency,
            0,
            0
        )

        left.addWidget(
            self.lblBand,
            1,
            0
        )

        left.addWidget(
            self.lblSignal,
            2,
            0
        )

        left.addWidget(
            self.lblPrediction,
            3,
            0
        )

        left.addWidget(
            self.lblConfidence,
            4,
            0
        )

        left.addWidget(
            self.lblRSSI,
            5,
            0
        )

        left.addWidget(
            self.lblPeak,
            6,
            0
        )

        left.addWidget(
            self.lblDistance,
            7,
            0
        )

        bottom.addLayout(
            left
        )

        ##################################################
        # EVENT LOG
        ##################################################

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        self.log.setMinimumWidth(500)

      ##################################################
# RIGHT STATUS PANEL
##################################################

right = QVBoxLayout()

# -----------------------------------------------
# AI STATUS
# -----------------------------------------------

aiFrame = QFrame()

aiFrame.setStyleSheet("""

QFrame{

    border:2px solid #00ff88;

    border-radius:10px;

}

""")

aiLayout = QVBoxLayout()

self.lblAI = QLabel("AI MODEL")

self.lblAI.setFont(
    QFont("Consolas",14,QFont.Weight.Bold)
)

self.lblAIStatus = QLabel("READY")

self.lblGPIO = QLabel("GPIO : READY")

self.lblMode = QLabel("MODE : SEQUENTIAL")

aiLayout.addWidget(self.lblAI)

aiLayout.addWidget(self.lblAIStatus)

aiLayout.addWidget(self.lblGPIO)

aiLayout.addWidget(self.lblMode)

aiFrame.setLayout(aiLayout)

right.addWidget(aiFrame)

##################################################
# DETECTION CARD
##################################################

detectFrame = QFrame()

detectFrame.setStyleSheet("""

QFrame{

    border:2px solid red;

    border-radius:10px;

}

""")

detectLayout = QVBoxLayout()

self.lblDetect = QLabel("NO DRONE")

self.lblDetect.setAlignment(
    Qt.AlignmentFlag.AlignCenter
)

self.lblDetect.setFont(
    QFont("Consolas",18,QFont.Weight.Bold)
)

detectLayout.addWidget(
    self.lblDetect
)

detectFrame.setLayout(
    detectLayout
)

right.addWidget(
    detectFrame
)

##################################################
# EVENT LOG
##################################################

right.addWidget(self.log)

bottom.addLayout(left,2)

bottom.addLayout(right,1)

root.addLayout(bottom)


    ##################################################
    # LIVE UPDATE
    ##################################################

    def update_dashboard(self, data):

        frequency = data["frequency"]

        prediction = data["prediction"]

        confidence = data["confidence"]

        signal = data["signal"]

        rssi = data["rssi"]

        peak = data["peak_power"]

        distance = data["distance"]

        spectrum = data["spectrum"]

        ################################################
        # Frequency Band
        ################################################

        if frequency < 1000:

            band = "UHF"

        elif frequency < 2000:

            band = "L Band"

        elif frequency < 4000:

            band = "S Band"

        elif frequency < 6000:

            band = "ISM 5.8 GHz"

        else:

            band = "Unknown"

        ################################################
        # Labels
        ################################################

        self.lblFrequency.setText(

            f"Frequency : {frequency:.2f} MHz"

        )

        self.lblBand.setText(

            f"Band : {band}"

        )

        self.lblSignal.setText(

            f"Signal : {signal}"

        )

        self.lblPrediction.setText(

            f"Prediction : {prediction}"

        )

        self.lblConfidence.setText(

            f"Confidence : {confidence:.2f}%"

        )

        self.lblRSSI.setText(

            f"RSSI : {rssi:.2f} dBm"

        )

        self.lblPeak.setText(

            f"Peak Power : {peak:.2f} dBm"

        )

        self.lblDistance.setText(

            f"Distance : {distance:.2f} m"

        )

        ################################################
        # FFT
        ################################################

        self.fft.update_fft(

            spectrum

        )

        ################################################
        # Waterfall
        ################################################

        self.waterfall.update_waterfall(

            spectrum

        )

        ################################################
        # Frequency Hopper
        ################################################

        self.frequency.set_frequency(

            frequency

        )

        ################################################
        # AI
        ################################################

        self.lblAIStatus.setText(

            "MODEL LOADED"

        )

        ################################################
        # Detection Banner
        ################################################

        if prediction == "DRONE DETECTED":

            self.lblDetect.setStyleSheet("""

            color:red;

            font-size:22pt;

            font-weight:bold;

            """)

            self.lblDetect.setText(

                "🚨 DRONE DETECTED"

            )

            self.lblGPIO.setText(

                "GPIO : ACTIVE"

            )

        else:

            self.lblDetect.setStyleSheet("""

            color:lime;

            font-size:22pt;

            font-weight:bold;

            """)

            self.lblDetect.setText(

                "NO DRONE"

            )

            self.lblGPIO.setText(

                "GPIO : READY"

            )

        ################################################
        # Event Log
        ################################################

        self.log.append(

            f"{frequency:.2f} MHz   {prediction}"

        )

        cursor = self.log.textCursor()

        cursor.movePosition(cursor.MoveOperation.End)

        self.log.setTextCursor(cursor)