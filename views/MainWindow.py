from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QPoint
from UI.CSSStyling import CSSStyling


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Центральний віджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setFixedSize(800, 600)
        self.setWindowTitle("TrixApp")
        print(CSSStyling.styleSheet_for_window())
        self.setStyleSheet(CSSStyling.styleSheet_for_window())
        

        # Основне компонування
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Заміна верхньої панелі
        # self.init_custom_titlebar()

        self.viewNow = None