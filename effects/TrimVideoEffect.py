class TrimVideoEffect:
    """Removes frames from video"""

    def __init__(self):
        self.name = "Trim Video"
        self.start_time = 0
        self.end_time = 0
        self.video = None
        self.can_be_applied = True

    def applyEffect(self):
        import moviepy as mp
        import os
        import datetime
        from views.VideoWidget import VideoWidget
        from PyQt5.QtWidgets import QMessageBox
        
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Processing")
        msg_box.setText("Please wait... Processing video...")
        msg_box.setStandardButtons(QMessageBox.NoButton)
        msg_box.setIcon(QMessageBox.Information)

        msg_box.show()
        
        self.video = mp.VideoFileClip(self.video_path)

        trimmed_video = self.video.subclipped(self.start_time, self.end_time)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join("temp", f"trimmed_video_{timestamp}.mp4")

        trimmed_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

        msg_box.close()

        self.main_controller.changeWidgetOfMainWindow(VideoWidget, file_path=output_path)


    def return_settings_widget(self, video_path, main_controller):
        import moviepy as mp
        from PyQt5.QtCore import Qt
        from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QSizePolicy

        self.video_path = video_path

        self.video = mp.VideoFileClip(video_path)
        video_duration = self.video.duration
        
        self.main_controller = main_controller
        
        self.settings_widget = QWidget()

        layout = QVBoxLayout()

        self.start_slider = QSlider(Qt.Horizontal)
        self.start_slider.setRange(0, int(video_duration))
        self.start_slider.valueChanged.connect(self.update_start_time)

        self.start_label = QLabel()
        self.start_label.setText(f"Start: {self.format_time(self.start_time)}")

        self.end_slider = QSlider(Qt.Horizontal)
        self.end_slider.setRange(0, int(video_duration))
        self.end_slider.valueChanged.connect(self.update_end_time)

        self.end_label = QLabel()
        self.end_label.setText(f"End: {self.format_time(self.end_time)}")

        layout.addWidget(self.start_label)
        layout.addWidget(self.start_slider)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_slider)

        self.settings_widget.setMaximumHeight(400)

        self.settings_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.settings_widget.setLayout(layout)
        return self.settings_widget

    def update_start_time(self):
        self.start_time = self.start_slider.value()
        self.start_label.setText(f"Start: {self.format_time(self.start_time)}")

        if self.start_time >= self.end_time:
            self.start_slider.setValue(int(self.end_time) - 1)

    def update_end_time(self):
        self.end_time = self.end_slider.value()
        self.end_label.setText(f"End: {self.format_time(self.end_time)}")

        if self.end_time <= self.start_time:
            self.end_slider.setValue(int(self.start_time) + 1)

    def format_time(self, time_in_seconds):
        minutes = int(time_in_seconds // 60)
        seconds = int(time_in_seconds % 60)
        return f"{minutes:02}:{seconds:02}"
