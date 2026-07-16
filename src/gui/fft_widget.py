"""
=========================================================
FFT Spectrum Widget
Counter Drone RF Detection System
=========================================================
"""

import numpy as np
import pyqtgraph as pg


class FFTWidget(pg.PlotWidget):

    def __init__(self):

        super().__init__()

        self.setBackground("#0d1117")

        self.showGrid(x=True, y=True)

        self.setLabel("left", "Power (dBm)")

        self.setLabel("bottom", "Frequency (MHz)")

        self.setYRange(-100, -10)

        self.setXRange(400, 6000)

        self.curve = self.plot(
            pen=pg.mkPen(
                color=(0,255,0),
                width=2
            )
        )

    def update_fft(self, spectrum):

        x = np.linspace(
            400,
            6000,
            len(spectrum)
        )

        self.curve.setData(x, spectrum)