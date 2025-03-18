import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDial, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.dial = QDial()
        self.dial.setRange(-10, 100)
        self.dial.setSingleStep(1)
        self.setCentralWidget(self.dial)
        self.dial.valueChanged.connect(self.value_changed)
        self.dial.sliderMoved.connect(self.slider_position)
        self.dial.sliderPressed.connect(self.slider_pressed)
        self.dial.sliderReleased.connect(self.slider_released)

    def value_changed(self, value):
        print(value)

    def slider_position(self, position):
        print("position", position)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
