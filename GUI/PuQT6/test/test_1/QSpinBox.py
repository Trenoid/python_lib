import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self._widget = QSpinBox()
        self._widget.setMinimum(-10)
        self._widget.setMaximum(3)
        self._widget.setPrefix("$")
        self._widget.setSuffix("c")
        self._widget.setSingleStep(3)
        self._widget.valueChanged.connect(self._on_value_changed)
        self._widget.textChanged.connect(self._on_value_changed_str)
        self.setCentralWidget(self._widget)

    def _on_value_changed(self, value: int):
        print("Значение изменилось:")
        print(value)
        print()

    def _on_value_changed_str(self, value: str):
        print("Текст изменился:")
        print(value)
        print()
        print()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
