class OverLayVideoEffect:
    def __init__(self):
        self.name = "Overlay Video"
        self.video_file = ""
        self.insert_time = 0
        self.start_time = 0
        self.end_time = 0
        self.can_be_applied = False
        self.video_duration = 0
        self.position = "bottom"
        self.use_main_audio = True
        self.use_overlay_audio = False

    def applyEffect(self):
        from moviepy import VideoFileClip, CompositeVideoClip, concatenate_audioclips
        from views.VideoWidget import VideoWidget
        from PyQt5.QtWidgets import QMessageBox
        import os

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Processing")
        msg_box.setText("Please wait... Processing video...")
        msg_box.setStandardButtons(QMessageBox.NoButton)
        msg_box.setIcon(QMessageBox.Information)

        msg_box.show()

        if not self.video_file or not self.video_path:
            return

        # Основне відео
        main_clip = VideoFileClip(self.video_path)

        # Накладене відео, яке розтягується по ширині основного
        overlay_clip = VideoFileClip(self.video_file).resized(width=main_clip.w)

        # Обрізаємо накладене відео до потрібних відрізків
        overlay_clip = overlay_clip.subclipped(self.start_time, self.end_time)

        # Позиція накладеного відео
        position_mapping = {
            "top": ("center", 0),
            "bottom": ("center", "bottom"),
        }
        overlay_clip = overlay_clip.with_position(position_mapping[self.position])

        # Час початку накладеного відео
        overlay_clip = overlay_clip.with_start(self.insert_time)

        # Налаштування аудіо
        final_audio = None
        if self.use_main_audio and self.use_overlay_audio:
            final_audio = concatenate_audioclips([main_clip.audio, overlay_clip.audio])
        elif self.use_overlay_audio:
            final_audio = overlay_clip.audio
        elif self.use_main_audio:
            final_audio = main_clip.audio

        # Створення фінального відео
        final_clip = CompositeVideoClip([main_clip, overlay_clip]).with_audio(final_audio)

        # Визначаємо шлях до папки temp
        output_folder = os.path.join(os.getcwd(), 'temp')

        # Перевірка наявності папки temp
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Шлях для збереження відео
        output_path = os.path.join(output_folder, "output_overlay.mp4")

        # Збереження відео
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

        msg_box.close()

        # Відкриваємо відео у відео-виджеті
        self.main_controller.changeWidgetOfMainWindow(VideoWidget, file_path=output_path)



    def return_settings_widget(self, video_path, main_controller):
        from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QCheckBox
        
        self.video_path = video_path
        self.main_controller = main_controller

        self.settings_widget = QWidget()
        layout = QVBoxLayout()

        self.select_video_label = QLabel("No video selected")
        layout.addWidget(self.select_video_label)

        file_dialog = QFileDialog()
        self.video_file, _ = file_dialog.getOpenFileName(filter="Video Files (*.mp4 *.avi *.mov)")

        if self.video_file:
            from moviepy import VideoFileClip
            self.select_video_label.setText(self.video_file.split("/")[-1])
            self.can_be_applied = True
            self.video_duration = VideoFileClip(self.video_file).duration

        self.start_slider = self.create_slider(0, self.video_duration, self.update_start_time)
        self.start_label = QLabel(f"Start Time: {self.start_time}s")
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_slider)

        self.end_slider = self.create_slider(0, self.video_duration, self.update_end_time)
        self.end_label = QLabel(f"End Time: {self.end_time}s")
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_slider)

        self.insert_slider = self.create_slider(0, self.video_duration, self.update_insert_time)
        self.insert_label = QLabel(f"Insert Time: {self.insert_time}s")
        layout.addWidget(self.insert_label)
        layout.addWidget(self.insert_slider)

        self.main_audio_checkbox = QCheckBox("Use Main Video Audio")
        self.main_audio_checkbox.setChecked(self.use_main_audio)
        self.main_audio_checkbox.stateChanged.connect(self.toggle_main_audio)

        self.overlay_audio_checkbox = QCheckBox("Use Overlay Video Audio")
        self.overlay_audio_checkbox.setChecked(self.use_overlay_audio)
        self.overlay_audio_checkbox.stateChanged.connect(self.toggle_overlay_audio)

        layout.addWidget(self.main_audio_checkbox)
        layout.addWidget(self.overlay_audio_checkbox)

        self.position_button = QPushButton("Down")
        self.position_button.setFixedHeight(40)
        self.position_button.clicked.connect(self.toggle_position)
        layout.addWidget(self.position_button)

        self.settings_widget.setLayout(layout)
        return self.settings_widget

    def create_slider(self, min_val, max_val, callback):
        from PyQt5.QtWidgets import QSlider
        from PyQt5.QtCore import Qt

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(int(max_val))
        slider.setValue(0)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.valueChanged.connect(callback)
        return slider

    def update_start_time(self, value):
        if value < self.end_time:
            self.start_time = value
            self.start_label.setText(f"Start Time: {value}s")

    def update_end_time(self, value):
        if value > self.start_time:
            self.end_time = value
            self.end_label.setText(f"End Time: {value}s")


    def update_insert_time(self, value):
        self.insert_time = value
        self.insert_label.setText(f"Insert Time: {value}s")

    def toggle_main_audio(self, state):
        self.use_main_audio = bool(state)

    def toggle_overlay_audio(self, state):
        self.use_overlay_audio = bool(state)

    def toggle_position(self):
        if self.position == "bottom":
            self.position = "top"
            self.position_button.setText("Up")
        else:
            self.position = "bottom"
            self.position_button.setText("Down")
