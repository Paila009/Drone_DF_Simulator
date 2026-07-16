"""
=========================================================
Dataset Browser
=========================================================
"""

import os

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTreeWidget,
    QTreeWidgetItem
)


class DatasetBrowser(QWidget):

    recordingSelected = pyqtSignal(str)

    def __init__(self, root_folder):

        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("RF Dataset"))

        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Datasets")

        self.tree.itemDoubleClicked.connect(
            self.item_double_clicked
        )

        layout.addWidget(self.tree)

        self.setLayout(layout)

        self.populate(root_folder)

    def populate(self, root):

        root_item = QTreeWidgetItem(
            self.tree,
            [os.path.basename(root)]
        )

        self.add_items(root_item, root)

        self.tree.expandAll()

    def add_items(self, parent, folder):

        for name in sorted(os.listdir(folder)):

            path = os.path.join(folder, name)

            item = QTreeWidgetItem(parent, [name])

            item.setData(0, 1, path)

            if os.path.isdir(path):

                self.add_items(item, path)

    def item_double_clicked(self, item):

        path = item.data(0, 1)

        print("DOUBLE CLICK:", path)

        if path is None:
            return

        if os.path.isfile(path):

            print("EMITTING:", path)

            self.recordingSelected.emit(path)