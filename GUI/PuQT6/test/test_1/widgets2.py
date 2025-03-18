import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.checkbox = QCheckBox("This is a checkbox")
        self.checkbox.setCheckState(Qt.CheckState.Checked)
        self.setCentralWidget(self.checkbox)
        self.checkbox.stateChanged.connect(self._show_state)

    def _show_state(self, state: Qt.CheckState):
        print(Qt.CheckState(state) == Qt.CheckState.Checked)
        print(state)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
