import sys

from PyQt6.QtWidgets import QApplication, QListWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.widget = QListWidget()
        self.widget.addItems(["One", "Two", "Three"])
        self.widget.currentItemChanged.connect(self.on_current_item_changed)
        self.widget.currentTextChanged.connect(self.on_current_text_changed)
        self.setCentralWidget(self.widget)

    def on_current_item_changed(self, item):
        print(f" Новый текущий элемент:{item.text()} ")

    def on_current_text_changed(self, text):
        print(f"Текст изменился на: {text}")
        print()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
