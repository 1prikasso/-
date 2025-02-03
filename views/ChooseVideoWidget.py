from PyQt5.QtWidgets import QWidget
from UI.ChooseVideoForm import ChooseVideoForm

class ChooseVideoWidget(QWidget):
    def __init__(self, mainController):
        super().__init__()

        self.mainController = mainController

        self.ui = ChooseVideoForm()
        self.ui.setupUi(self, self.mainController)
