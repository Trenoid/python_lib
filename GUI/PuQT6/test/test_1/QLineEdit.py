import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self._widget = QLineEdit()
        self._widget.setMaxLength(10)
        self._widget.setPlaceholderText("Enter your text")

        self._widget.returnPressed.connect(self.return_pressed)
        self._widget.selectionChanged.connect(self.selection_changed)
        self._widget.textChanged.connect(self.text_changed)
        self._widget.textEdited.connect(self.text_edited)

        # Маска ввода
        self._widget.setInputMask("000.000.000.000;_")

        self.setCentralWidget(self._widget)

    def return_pressed(self):
        print("Нажата клавиша Enter")
        self._widget.setText("BOOM!")

    def selection_changed(self):
        print("Изменение выделения")
        print(self._widget.selectedText())

    def text_changed(self, s):
        print("Текст изменен ")
        print(s)

    def text_edited(self, s):
        print("Текст отредактирован ")
        print(s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
