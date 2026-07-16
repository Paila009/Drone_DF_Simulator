"""
=========================================================
Counter Drone RF Analyzer
Main
=========================================================
"""

import sys

from PyQt6.QtWidgets import QApplication

from src.gui.dashboard_v2 import DashboardV2


def main():

    app = QApplication(sys.argv)

    window = DashboardV2()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":

    main()