from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QUrl
from controllers.VideoOperatorController import VideoOperatorController
from views.EffectSettingsWidget import EffectSettingsWidget

from UI.classes.EffectsListModel import EffectsListModel

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
        
        
        
        self.widget_2 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        
        self.addEffectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addEffectButton.setObjectName("addEffectButton")
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnBackButton.sizePolicy().hasHeightForWidth())
        
        self.returnBackButton.setSizePolicy(sizePolicy)
        
        self.addEffectButton.clicked.connect(lambda: self.add_effect(main_controller=main_controller, video=video))
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
        self.videoWidget.setGeometry(QtCore.QRect(30+35, 0, int(180*1.23), int(320*1.23)))
        self.videoWidget.setObjectName("videoWidget")
        
        self.pushButton = QtWidgets.QPushButton(self.workWidget)
        self.pushButton.setGeometry(QtCore.QRect(133+8-2, int(320*1.25), 75, 30))
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
        
        
        self.list_model = EffectsListModel(main_controller.return_list_of_effects())
        self.listView.setModel(self.list_model)
        
        self.horizontalLayout_3.addWidget(self.listView)
        self.horizontalLayout_3.setStretch(0, 400)
        self.horizontalLayout_3.setStretch(1, 30)
        self.horizontalLayout_3.setStretch(2, 400)

        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.videoWidget)
        self.pushButton.clicked.connect(self.play_video)
        
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(video)))
        self.media_player.play()
        self.media_player.pause()
        
        
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
            self.pushButton.setText("||")
            
            
    def export_video(self):
        folder = QFileDialog.getExistingDirectory(self.Form, "Select Folder")

        self.media_player.stop()

        if folder:
            input_video_path = self.input_video_path
            output_video_path = f'{folder}\\trimmed_video.mp4'
            
            
            savedpath = VideoOperatorController.save_video_to_path(input_video_path, output_video_path)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Your video was saved by the following path:\n"+savedpath)
            msg.setWindowTitle("Clip was saved!")
            msg.exec_()
            
    def returnBack(self, main_controller):
        self.media_player.setMedia(QMediaContent())

        main_controller.goBack()
        
    def add_effect(self, main_controller, video):
        selected_index = self.listView.selectedIndexes()
        
        self.media_player.setMedia(QMediaContent())
        
        if selected_index:
            index = selected_index[0]
            effect_object = self.list_model.effects_objects[index.row()]
            
            if self.media_player.state() == QMediaPlayer.PlayingState:
                self.media_player.pause()
                self.pushButton.setText("⏵")
            
            main_controller.changeWidgetOfMainWindow(widget_class=EffectSettingsWidget, file_path=video, effect_object=effect_object, appendHistory=False)
            
            
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("You must select an effect before applying!")
            msg.setWindowTitle("Warning")
            msg.exec_()
