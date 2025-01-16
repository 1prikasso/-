from PyQt5 import QtCore, QtGui, QtWidgets
from views.ChooseVideoWidget import ChooseVideoWidget
from UI.CSSStyling import CSSStyling

class StartForm(object):
    def setupUi(self, Form, main_controller):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(800, 600)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 225, 300, 150))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(
            lambda: main_controller.changeWidgetOfMainWindow(ChooseVideoWidget)
        )
        
        self.pushButton.setStyleSheet(CSSStyling.styleSheet_for_button())
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Start"))
