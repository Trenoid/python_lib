import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        #widget.setEditable(True)
        #widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        #widget.setMaxCount(10)

        self.setCentralWidget(widget)

    def index_changed(self, index: int) -> None:
        print(index)

    def text_changed(self, text: str) -> None:
        print(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
