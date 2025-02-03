class CropVideoEffect:
    """Crops video by pixel size from the center."""
    
    def __init__(self):
        self.name = "Crop Video"
        self.width = None
        self.height = None
        self.video_path = None
        self.can_be_applied = True

    def return_settings_widget(self, video_path, main_controller):
        """
        Returns a UI widget for cropping settings.
        """
        from moviepy import VideoFileClip
        
        self.video_path = video_path
        
        self.main_controller = main_controller
        
        
        
        from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

        widget = QWidget()
        layout = QVBoxLayout()

        self.width_input = QLineEdit()
        self.height_input = QLineEdit()

        self.width_input.setPlaceholderText("Enter video width in pixels")
        self.height_input.setPlaceholderText("Enter video height in pixels")

        original_width, original_height = VideoFileClip(self.video_path).size
        
        layout.addWidget(QLabel(f"Width: {original_width}"))
        layout.addWidget(self.width_input)
        layout.addWidget(QLabel(f"Height: {original_height}"))
        layout.addWidget(self.height_input)

        widget.setLayout(layout)
        
        return widget

    def applyEffect(self):
        """
        Applies the crop effect to the video, cropping from the center based on user input.
        """
        from moviepy import VideoFileClip
        from PyQt5.QtWidgets import QMessageBox
        import datetime
        import os
        from views.VideoWidget import VideoWidget


        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Processing")
            msg_box.setText("Please wait... Processing video...")
            msg_box.setStandardButtons(QMessageBox.NoButton)
            msg_box.setIcon(QMessageBox.Information)

            msg_box.show()
                
            width = int(self.width_input.text())
            height = int(self.height_input.text())
            
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive integers.")
            
            clip = VideoFileClip(self.video_path)
            original_width, original_height = clip.size

            centerx, centery = original_width / 2, original_height / 2

            if width > original_width or height > original_height:
                raise ValueError("Crop dimensions must not exceed original video dimensions.")

            cropped_clip = clip.cropped(x_center=centerx, y_center=centery, width=width, height=height)

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join("temp", f"cropped_video_{timestamp}.mp4")

            cropped_clip.write_videofile(output_path)

            msg_box.close()
            self.main_controller.changeWidgetOfMainWindow(VideoWidget, file_path=output_path)
            

        except ValueError as e:
            self.show_message("Invalid Input", str(e))

        except Exception as e:
            self.show_message("Error", f"An error occurred: {str(e)}")

    def show_message(self, title, message):
        """
        Shows a message box with the specified title and message.
        """
        from PyQt5.QtWidgets import QMessageBox

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()
