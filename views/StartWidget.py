from PyQt5.QtWidgets import QWidget
from UI.StartForm import StartForm
# from views.TemplatesWidget import TemplatesWidget

class StartWidget(QWidget):
    def __init__(self, mainController):
        super().__init__()

        self.mainController = mainController

        # Ініціалізація UI
        self.ui = StartForm()
        self.ui.setupUi(self, self.mainController)
