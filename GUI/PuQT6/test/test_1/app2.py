from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button_is_checked = True

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(
            self.the_button_was_released
        )
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())