from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QUrl
from controllers.VideoOperatorController import VideoOperatorController
from PyQt5.QtGui import QStandardItemModel
from UI.CSSStyling import CSSStyling

class VideoForm2(object):
    def setupUi(self, Form, main_controller, video):
        self.input_video_path = video
        self.Form = Form
        
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 510, 801, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(40, 0, 40, 40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.returnBackButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnBackButton.sizePolicy().hasHeightForWidth())
        
        self.returnBackButton.setSizePolicy(sizePolicy)
        self.returnBackButton.setObjectName("returnBackButton")
        
        self.horizontalLayout_2.addWidget(self.returnBackButton)
        
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget.setObjectName("widget")
        
        self.horizontalLayout_2.addWidget(self.widget)
        
        # self.widget_3 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        # self.widget_3.setObjectName("widget_3")
        
        # self.horizontalLayout_2.addWidget(self.widget_3)
        
        self.widget_2 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        
        # Кнопка для додавання ефекту
        self.addEffectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addEffectButton.setObjectName("addEffectButton")
        self.addEffectButton.clicked.connect(self.add_effect)  # Зв'язуємо з методом додавання ефекту
        self.horizontalLayout_2.addWidget(self.addEffectButton)
        
        self.horizontalLayout_2.addWidget(self.widget_2)
        
        self.exportVideoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportVideoButton.sizePolicy().hasHeightForWidth())
        
        self.exportVideoButton.setSizePolicy(sizePolicy)
        self.exportVideoButton.setObjectName("exportVideoButton")
        
        self.exportVideoButton.clicked.connect(self.export_video)
        self.horizontalLayout_2.addWidget(self.exportVideoButton)
        
        self.horizontalLayout_2.setStretch(0, 100)
        self.horizontalLayout_2.setStretch(1, 30)
        self.horizontalLayout_2.setStretch(2, 100)
        self.horizontalLayout_2.setStretch(3, 30)
        self.horizontalLayout_2.setStretch(4, 100)
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, -1, 801, 511))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(40, 40, 40, 40)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.workWidget = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.workWidget.setObjectName("workWidget")
        
        self.videoWidget = QVideoWidget(self.workWidget)
        self.videoWidget.setGeometry(QtCore.QRect(80, 0, 180, 320))
        self.videoWidget.setObjectName("videoWidget")
        self.pushButton = QtWidgets.QPushButton(self.workWidget)
        self.pushButton.setGeometry(QtCore.QRect(133, 320, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.workWidget)
        self.widget_6 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.listView = QtWidgets.QListView(self.horizontalLayoutWidget_2)
        self.listView.setObjectName("listView")
        
        
        self.list_model = QStandardItemModel()
        self.listView.setModel(self.list_model)
        
        main_controller.return_list_of_effects(self.list_model)
        
        self.horizontalLayout_3.addWidget(self.listView)
        self.horizontalLayout_3.setStretch(0, 400)
        self.horizontalLayout_3.setStretch(1, 30)
        self.horizontalLayout_3.setStretch(2, 400)

        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        # Додатковий код для управління відео
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.videoWidget)
        self.pushButton.clicked.connect(self.play_video)
        
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(video)))
        self.media_player.play()
        self.media_player.pause()
        
        # self.pushButton.setStyleSheet(CSSStyling.styleSheet_for_button())
        # self.returnBackButton.setStyleSheet(CSSStyling.styleSheet_for_button())
        # self.exportVideoButton.setStyleSheet(CSSStyling.styleSheet_for_button())
        # self.listView.setStyleSheet(CSSStyling.styleSheet_for_ListView())
        # self.addEffectButton.setStyleSheet(CSSStyling.styleSheet_for_button())
        
        self.returnBackButton.clicked.connect(
            lambda: self.returnBack(main_controller=main_controller)
        )

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.returnBackButton.setText(_translate("Form", "Back"))
        self.exportVideoButton.setText(_translate("Form", "Export"))
        self.pushButton.setText(_translate("Form", "⏵"))
        self.addEffectButton.setText(_translate("Form", "Add Effect"))
        
    def play_video(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
            self.pushButton.setText("⏵")
        else:
            self.media_player.play()
            self.pushButton.setText("⏸")
            
            
    def export_video(self):
        folder = QFileDialog.getExistingDirectory(self.Form, "Select Folder")

        if folder:
            # Тут можна викликати функцію для обрізки і збереження відео
            input_video_path = self.input_video_path  # Вказати шлях до вашого відео
            output_video_path = f'{folder}\\trimmed_video.mp4'
            
            # Обрізаємо відео
            
            savedpath = VideoOperatorController.save_video_to_path(input_video_path, output_video_path)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Your video was saved by the following path:\n"+savedpath)
            msg.setWindowTitle("Clip was saved!")
            msg.exec_()
            
    def returnBack(self, main_controller):
        self.media_player.setMedia(QMediaContent())

        main_controller.goBack()
        
    def add_effect():
        return None