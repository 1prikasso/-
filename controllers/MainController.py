from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QStandardItem
from views.StartWidget import StartWidget
from controllers.VideoOperatorController import VideoOperatorController


class MainController():
    def __init__(self, main_window):
        self.main_window = main_window
        
        self.history = []
        
        self.changeWidgetOfMainWindow(StartWidget)

        self.main_window.show()

    def changeWidgetOfMainWindow(self, widget_class, appendHistory=True, file_path=None):
        if self.main_window.viewNow:
            # Видаляємо поточний виджет
            self.main_window.layout.removeWidget(self.main_window.viewNow)
            self.main_window.viewNow.deleteLater()

        # Встановлюємо новий виджет
        if file_path:
            widget = widget_class(self, file_path)
        else:
            widget = widget_class(self)
        
        self.main_window.viewNow = widget
        self.main_window.layout.addWidget(widget)
        
        if(appendHistory):
            self.history.append(widget_class)
        
        self.main_window.viewNow.show()
        
    def goBack(self):
        if (self.history):
            self.history.pop()
            previous_state = self.history[-1]
            
            self.changeWidgetOfMainWindow(previous_state, False)
            
    def return_list_of_effects(self, list_model):
        items = ["Add music", "Crop Video", "Trim Video"]
        for item_text in items:
            item = QStandardItem(item_text)
            list_model.appendRow(item)