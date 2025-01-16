from PyQt5.QtWidgets import QFileDialog, QMessageBox
import ffmpeg
from moviepy import VideoFileClip



class VideoOperatorController():
    # def __int__(self, window_parent):
    #     self.window_parent = window_parent
        
    # def importVideo(self):
    #     # Відкрити діалог вибору файлу
    #     file_name, _ = QFileDialog.getOpenFileName(
    #         self.window_parent, 
    #         "Select Video", 
    #         "", 
    #         "Video Files (*.mp4 *.avi *.mov *.mkv)"
    #     )
        
    #     return file_name 
    
    def trim_video(input_video_path, output_video_path):
        clip = VideoFileClip(input_video_path)
    
        # Отримуємо розміри оригінального відео
        original_width, original_height = clip.size
        
        centerx, centery = original_width/2, original_height/2
        
        cropped = clip.cropped(x_center=centerx, y_center=centery, height=original_height, width=9*original_height/16)

        cropped.write_videofile(output_video_path)

        return output_video_path
    
    def crop_video(input_video_path, output_path):
        clip = VideoFileClip(input_video_path)
        
        clip.subclipped(0, 60).write_videofile(output_path)
        
        return output_path

    def save_video_to_path(input_video_path, output_path):
        try:
            # Обрізаємо відео і зберігаємо його у вибрану папку
            ffmpeg.input(input_video_path).output(output_path).run()
            
            return output_path
        
        except Exception as e:
            print(e)