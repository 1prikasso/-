from PyQt5.QtWidgets import QFileDialog, QMessageBox
import ffmpeg
from moviepy import VideoFileClip



class VideoOperatorController():
    def save_video_to_path(input_video_path, output_path):
        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Processing")
            msg_box.setText("Please wait... Saving video...")
            msg_box.setStandardButtons(QMessageBox.NoButton)
            msg_box.setIcon(QMessageBox.Information)

            msg_box.show()
            
            ffmpeg.input(input_video_path).output(output_path).run()
            
            msg_box.close()
            
            return output_path
        
        except Exception as e:
            print(e)