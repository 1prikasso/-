from PyQt5.QtWidgets import QWidget
from UI.EffectSettingsForm import EffectSettingsForm

class EffectSettingsWidget(QWidget):
    def __init__(self, mainController, file_path, inner_widget):
        super().__init__()

        self.mainController = mainController

        self.ui = EffectSettingsForm()
        self.ui.setupUi(self, self.mainController, file_path, inner_widget)
