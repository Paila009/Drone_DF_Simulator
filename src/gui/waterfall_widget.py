"""
Professional RF Waterfall Widget
"""

import numpy as np

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import (
    QColor,
    QPainter,
    QImage
)


class WaterfallWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumHeight(220)

        self.width_bins = 512

        self.history = np.zeros((220, self.width_bins))

    def update_waterfall(self, spectrum):

        spectrum = np.asarray(spectrum)

        if len(spectrum) > self.width_bins:

            spectrum = spectrum[:self.width_bins]

        spectrum = spectrum.astype(float)

        spectrum -= spectrum.min()

        if spectrum.max() > 0:

            spectrum /= spectrum.max()

        self.history = np.roll(
            self.history,
            -1,
            axis=0
        )

        self.history[-1] = spectrum

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        img = QImage(
            self.width_bins,
            self.history.shape[0],
            QImage.Format.Format_RGB32
        )

        for y in range(self.history.shape[0]):

            for x in range(self.width_bins):

                value = self.history[y, x]

                r = int(value * 255)

                g = int(value * 180)

                b = int(255 - value * 255)

                img.setPixel(
                    x,
                    y,
                    QColor(r, g, b).rgb()
                )

        painter.drawImage(
            self.rect(),
            img
        )