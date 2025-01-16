from PyQt5 import QtCore, QtGui, QtWidgets
from UI.CSSStyling import CSSStyling
from PyQt5.QtWidgets import QFileDialog
from views.VideoWidget import VideoWidget

class ChooseVideoForm(object):
    def setupUi(self, Form, main_controller):
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
        
        # connect goback button to goback method
        self.returnBackButton.clicked.connect(
            lambda: main_controller.goBack()
        )
        
        self.horizontalLayout_2.addWidget(self.returnBackButton)
        
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget.setObjectName("widget")
        
        self.horizontalLayout_2.addWidget(self.widget)
        
        self.widget_3 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_3.setObjectName("widget_3")
        
        self.horizontalLayout_2.addWidget(self.widget_3)
        
        self.widget_2 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.exportVideoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportVideoButton.sizePolicy().hasHeightForWidth())
        
        self.exportVideoButton.setSizePolicy(sizePolicy)
        self.exportVideoButton.setObjectName("exportVideoButton")
        
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
        self.horizontalLayout_3.setContentsMargins(40, 30, 40, 40)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.widget_4 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget_4.setObjectName("widget_4")
        
        self.importClipButton = QtWidgets.QPushButton(self.widget_4)
        self.importClipButton.setGeometry(QtCore.QRect(90, 220, 200, 50))
        self.importClipButton.setObjectName("importClipButton")
        
        self.importClipButton.clicked.connect(
            lambda: self.importVideo(main_controller=main_controller)
        )
        
        self.horizontalLayout_3.addWidget(self.widget_4)
        
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
        
        self.horizontalLayout_3.addWidget(self.listView)
        self.horizontalLayout_3.setStretch(0, 400)
        self.horizontalLayout_3.setStretch(1, 30)
        self.horizontalLayout_3.setStretch(2, 400)

        self.importClipButton.setStyleSheet(CSSStyling.styleSheet_for_button())
        self.returnBackButton.setStyleSheet(CSSStyling.styleSheet_for_button())
        self.exportVideoButton.setStyleSheet(CSSStyling.styleSheet_for_button())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.returnBackButton.setText(_translate("Form", "Back"))
        self.exportVideoButton.setText(_translate("Form", "Export Video"))
        self.importClipButton.setText(_translate("Form", "Import video"))

    def importVideo(self, main_controller):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Select Video", "", "Video Files (*.mp4 *.avi *.mov, *.*)"
        )
        if file_path:
            main_controller.changeWidgetOfMainWindow(VideoWidget, file_path=file_path)
