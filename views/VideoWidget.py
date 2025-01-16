from PyQt5.QtWidgets import QWidget
from UI.VideoForm import VideoForm2
# from views.TemplatesWidget import TemplatesWidget
from controllers.VideoOperatorController import VideoOperatorController

class VideoWidget(QWidget):
    def __init__(self, mainController, file_path):
        super().__init__()

        self.mainController = mainController

        path_to_cropped_video = VideoOperatorController.crop_video(file_path, "C:/Users/Oleksandr/Desktop/курсова/Trix/temp/cropped_video.mp4")
        
        path_to_trimmed_video = VideoOperatorController.trim_video(path_to_cropped_video, "C:/Users/Oleksandr/Desktop/курсова/Trix/temp/trimmed_video.mp4")
        
        # Ініціалізація UI
        self.ui = VideoForm2()
        self.ui.setupUi(self, self.mainController, path_to_trimmed_video)
