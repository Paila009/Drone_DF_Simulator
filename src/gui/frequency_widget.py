"""
=========================================================
Frequency Hopper Widget
Counter Drone RF Detection System
=========================================================
"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt


class FrequencyWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.current_frequency = 2400

        self.setMinimumHeight(100)

    def set_frequency(self, frequency):

        self.current_frequency = frequency

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()

        h = self.height()

        # Background
        painter.fillRect(self.rect(), QColor("#0d1117"))

        # Frequency Line
        pen = QPen(QColor(0,255,0),3)

        painter.setPen(pen)

        painter.drawLine(40,h//2,w-40,h//2)

        # End Labels
        painter.setPen(QColor("white"))

        painter.setFont(QFont("Consolas",10))

        painter.drawText(10,h//2+25,"400 MHz")

        painter.drawText(w-90,h//2+25,"6 GHz")

        # Current Frequency Marker

        ratio = (self.current_frequency-400)/(6000-400)

        ratio = max(0,min(1,ratio))

        x = int(40 + ratio*(w-80))

        painter.setBrush(QColor(255,0,0))

        painter.drawEllipse(x-6,h//2-6,12,12)

        painter.drawText(

            x-35,

            h//2-15,

            f"{self.current_frequency:.0f} MHz"

        )