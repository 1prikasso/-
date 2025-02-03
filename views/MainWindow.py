from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QPoint
from UI.CSSStyling import CSSStyling


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setFixedSize(800, 600)
        self.setWindowTitle("TrixApp")
        self.setStyleSheet(CSSStyling.styleSheet_for_window())
        

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)


        self.viewNow = None