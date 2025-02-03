from PyQt5.QtWidgets import QWidget
from UI.VideoForm import VideoForm2

class VideoWidget(QWidget):
    def __init__(self, mainController, file_path):
        super().__init__()

        self.mainController = mainController

        self.ui = VideoForm2()
        self.ui.setupUi(self, self.mainController, file_path)
