class InsertVideoClipEffect:
    def __init__(self):
        self.name = "Insert Video Clip"
        self.video_file = ""
        self.insert_time = 0
        self.start_time = 0
        self.end_time = 0
        self.can_be_applied = False
        self.video_duration = 0

    def applyEffect(self):
        import moviepy as mp
        from views.VideoWidget import VideoWidget
        import os
        import datetime
        from PyQt5.QtWidgets import QMessageBox

        if not self.video_file or not self.video_path:
            return

        
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Processing")
        msg_box.setText("Please wait... Processing video...")
        msg_box.setStandardButtons(QMessageBox.NoButton)
        msg_box.setIcon(QMessageBox.Information)

        msg_box.show()
            

        main_video = mp.VideoFileClip(self.video_path)
        insert_video = mp.VideoFileClip(self.video_file).subclipped(self.start_time, self.end_time)

        first_part = main_video.subclipped(0, self.insert_time)
        second_part = main_video.subclipped(self.insert_time)

        final_video = mp.concatenate_videoclips([first_part, insert_video, second_part], method="compose")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join("temp", f"video_inserted_{timestamp}.mp4")

        final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

        self.main_controller.changeWidgetOfMainWindow(VideoWidget, file_path=output_path)

    def return_settings_widget(self, video_path, main_controller):
        from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QFileDialog
        from PyQt5.QtCore import Qt

        self.settings_widget = QWidget()
        self.video_path = video_path
        self.main_controller = main_controller

        layout = QVBoxLayout()

        self.select_video_button = QPushButton("Select Video File")
        self.select_video_button.clicked.connect(self.select_video)
        layout.addWidget(self.select_video_button)

        self.insert_time_slider = QSlider(Qt.Horizontal)
        self.insert_time_slider.setRange(0, 100)
        self.insert_time_slider.valueChanged.connect(self.update_insert_time)
        
        self.insert_label = QLabel("Insert Position: 00:00")
        
        layout.addWidget(self.insert_label)
        layout.addWidget(self.insert_time_slider)

        self.start_time_slider = QSlider(Qt.Horizontal)
        self.start_time_slider.setRange(0, 100)
        self.start_time_slider.valueChanged.connect(self.update_start_time)
        self.start_label = QLabel("Start: 00:00")

        self.end_time_slider = QSlider(Qt.Horizontal)
        self.end_time_slider.setRange(0, 100)
        self.end_time_slider.setValue(100)
        self.end_time_slider.valueChanged.connect(self.update_end_time)
        self.end_label = QLabel("End: 00:00")

        layout.addWidget(self.start_label)
        layout.addWidget(self.start_time_slider)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_time_slider)

        self.settings_widget.setLayout(layout)
        return self.settings_widget

    def select_video(self):
        from PyQt5.QtWidgets import QFileDialog
        import os
        import moviepy as mp

        file_dialog = QFileDialog()
        self.video_file, _ = file_dialog.getOpenFileName(filter="Video Files (*.mp4 *.avi *.mov)")

        if self.video_file:
            file_name = os.path.basename(self.video_file)
            
            if len(file_name) > 19:
                self.select_video_button.setText(f"..{file_name[-13:]}")
            else:
                self.select_video_button.setText(file_name)
            
            self.can_be_applied = True

            clip = mp.VideoFileClip(self.video_file)
            self.video_duration = int(clip.duration)

            self.start_time_slider.setRange(0, self.video_duration)
            self.end_time_slider.setRange(0, self.video_duration)
            self.end_time_slider.setValue(self.video_duration)

            self.update_start_time()
            self.update_end_time()

    def update_insert_time(self):
        self.insert_time = self.insert_time_slider.value()
        self.insert_label.setText(f"Insert Position: {self.format_time(self.insert_time)}")
        

    def update_start_time(self):
        self.start_time = self.start_time_slider.value()
        self.start_label.setText(f"Start: {self.format_time(self.start_time)}")

        if self.start_time >= self.end_time:
            self.start_time_slider.setValue(self.end_time - 1)

    def update_end_time(self):
        self.end_time = self.end_time_slider.value()
        self.end_label.setText(f"End: {self.format_time(self.end_time)}")

        if self.end_time <= self.start_time:
            self.end_time_slider.setValue(self.start_time + 1)

    def format_time(self, time_in_seconds):
        minutes = int(time_in_seconds // 60)
        seconds = int(time_in_seconds % 60)
        return f"{minutes:02}:{seconds:02}"
