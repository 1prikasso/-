from PyQt5.QtWidgets import QFileDialog, QMessageBox
import ffmpeg
from moviepy import VideoFileClip



class VideoOperatorController():
    def save_video_to_path(input_video_path, output_path):
        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Processing")
            msg_box.setText("Please wait... Saving video...")
            msg_box.setStandardButtons(QMessageBox.NoButton)  # Без кнопок, лише повідомлення
            msg_box.setIcon(QMessageBox.Information)

            # Відображаємо повідомлення
            msg_box.show()
            
            # Обрізаємо відео і зберігаємо його у вибрану папку
            ffmpeg.input(input_video_path).output(output_path).run()
            
            msg_box.close()
            
            return output_path
        
        except Exception as e:
            print(e)