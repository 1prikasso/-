from PyQt5.QtWidgets import QWidget
from UI.StartForm import StartForm

class StartWidget(QWidget):
    def __init__(self, mainController):
        super().__init__()

        self.mainController = mainController

        self.ui = StartForm()
        self.ui.setupUi(self, self.mainController)
