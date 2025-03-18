from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.input = QLineEdit()
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        self.input.textChanged.connect(self.label.setText)

        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
