"""
Professional RF Spectrum Widget
"""

import numpy as np

from PyQt6.QtWidgets import QWidget

from PyQt6.QtGui import (
    QColor,
    QPainter,
    QPen
)


class SpectrumWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumHeight(260)

        self.spectrum = np.zeros(1024)

    def update_spectrum(self, spectrum):

        self.spectrum = np.asarray(spectrum)

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        w = self.width()

        h = self.height()

        # Background
        painter.fillRect(
            self.rect(),
            QColor(10, 15, 20)
        )

        # Grid
        pen = QPen(QColor(45, 45, 45))
        painter.setPen(pen)

        for x in range(0, w, 80):
            painter.drawLine(x, 0, x, h)

        for y in range(0, h, 40):
            painter.drawLine(0, y, w, y)

        if len(self.spectrum) < 2:
            return

        spec = self.spectrum.astype(float)

        spec -= spec.min()

        if spec.max() > 0:
            spec /= spec.max()

        pen = QPen(QColor(0, 255, 0))

        pen.setWidth(2)

        painter.setPen(pen)

        lastx = 0

        lasty = h

        for i, value in enumerate(spec):

            x = int(i * (w - 1) / (len(spec) - 1))

            y = int(h - value * h)

            if i > 0:
                painter.drawLine(lastx, lasty, x, y)

            lastx = x
            lasty = y

        # Frequency labels

        painter.setPen(QColor("white"))

        painter.drawText(10, h - 10, "400 MHz")

        painter.drawText(w - 80, h - 10, "6 GHz")