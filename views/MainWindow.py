from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
    
        self.central_widget = QWidget()
        
        self.setCentralWidget(self.central_widget)
        
        self.setFixedSize(800, 600)
        self.setWindowTitle("TrixApp")
        
        self.setStyleSheet("background-color : white;")

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.viewNow = None
        
    