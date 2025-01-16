from PyQt5.QtWidgets import QWidget
from UI.ChooseVideoForm import ChooseVideoForm
# from views.TemplatesWidget import TemplatesWidget

class ChooseVideoWidget(QWidget):
    def __init__(self, mainController):
        super().__init__()

        self.mainController = mainController

        # Ініціалізація UI
        self.ui = ChooseVideoForm()
        self.ui.setupUi(self, self.mainController)
