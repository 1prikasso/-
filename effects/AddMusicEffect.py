class AddMusicEffect:
    def __init__(self):
        self.name = "Add Music"
        self.audio_file = ""
        self.video_file = ""
        self.start_time = 0
        self.end_time = 0
        self.duration = 0
        self.can_be_applied = False

    def applyEffect(self):
        import datetime
        import os
        from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip
        from views.VideoWidget import VideoWidget

        video = VideoFileClip(self.video_path)
        audio = AudioFileClip(self.audio_file).subclipped(self.start_time, self.end_time)

        volume_factor = self.volume_slider.value() / 100.0
        audio = audio.with_volume_scaled(volume_factor)

        combined_audio = CompositeAudioClip([video.audio, audio])

        video.audio = combined_audio

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join("temp", f"video_with_audio_{timestamp}.mp4")
        video.write_videofile(output_path, codec='libx264', audio_codec='aac')

        self.main_controller.changeWidgetOfMainWindow(VideoWidget, file_path=output_path)


    
    def return_settings_widget(self, video_path, main_controller):
        from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QSizePolicy
        from PyQt5.QtCore import Qt
        
        self.settings_widget = QWidget()
        self.video_path = video_path
        self.main_controller = main_controller
        
        layout = QVBoxLayout()

        self.select_audio_button = QPushButton("Select Audio File")
        self.select_audio_button.clicked.connect(self.select_audio)
        
        layout.addWidget(self.select_audio_button)

        self.start_slider = QSlider(Qt.Horizontal)
        self.start_slider.setRange(0, 100)
        self.start_slider.valueChanged.connect(self.update_start_time)
        
        self.start_label = QLabel("Start: 00:00")

        self.end_slider = QSlider(Qt.Horizontal)
        self.end_slider.setRange(0, 100)
        self.end_slider.valueChanged.connect(self.update_end_time)
        
        self.end_label = QLabel("End: 00:00")
        
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_slider)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_slider)

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        layout.addWidget(QLabel("Volume:"))
        layout.addWidget(self.volume_slider)

        self.settings_widget.setLayout(layout)
        return self.settings_widget

    def select_audio(self):
        from PyQt5.QtWidgets import QFileDialog
        from pydub.utils import mediainfo
        import os
        
        file_dialog = QFileDialog()
        self.audio_file, _ = file_dialog.getOpenFileName(filter="Audio Files (*.mp3 *.wav)")

        if self.audio_file:
            file_name = os.path.basename(self.audio_file)
            if len(file_name) > 19:
                self.select_audio_button.setText(f"..{file_name[-13:]}")
            else:
                self.select_audio_button.setText(file_name)
            
            audio_info = mediainfo(self.audio_file)
            self.duration = float(audio_info['duration'])

            self.start_slider.setRange(0, int(self.duration * 1000))
            self.end_slider.setRange(0, int(self.duration * 1000))
            
            self.can_be_applied = True

    def update_start_time(self):
        self.start_time = self.start_slider.value() / 1000
        self.start_label.setText(f"Start: {self.format_time(self.start_time)}")
        
        if self.start_time >= self.end_time:
            self.start_slider.setValue(int(self.end_time * 1000) - 1)

    def update_end_time(self):
        self.end_time = self.end_slider.value() / 1000
        self.end_label.setText(f"End: {self.format_time(self.end_time)}")
        
        if self.end_time <= self.start_time:
            self.end_slider.setValue(int(self.start_time * 1000) + 1)

    def format_time(self, time_in_seconds):
        """Форматує час у хвилинах:секундах"""
        minutes = int(time_in_seconds // 60)
        seconds = int(time_in_seconds % 60)
        return f"{minutes:02}:{seconds:02}"