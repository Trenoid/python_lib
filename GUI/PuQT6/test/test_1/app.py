from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.button_is_checked = True

        button = QPushButton("Press Me!")
        # Сделаем кнопку переключателем
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        # Передаем состояние кнопки
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("clicked")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()