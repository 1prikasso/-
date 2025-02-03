from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QStandardItem
from views.StartWidget import StartWidget
from views.EffectSettingsWidget import EffectSettingsWidget
from controllers.VideoOperatorController import VideoOperatorController
import os
import importlib

class MainController():
    def __init__(self, main_window):
        self.main_window = main_window
        
        self.history = []
        
        self.changeWidgetOfMainWindow(StartWidget)

        self.main_window.show()

    def changeWidgetOfMainWindow(self, widget_class, appendHistory=True, file_path=None, effect_object=None):
        if self.main_window.viewNow:
            # Видаляємо поточний виджет
            self.main_window.layout.removeWidget(self.main_window.viewNow)
            self.main_window.viewNow.deleteLater()

        # Встановлюємо новий виджет
        if file_path and effect_object:
            widget = widget_class(self, file_path, effect_object)
        elif file_path:
            widget = widget_class(self, file_path)
        else:
            widget = widget_class(self)

        self.main_window.viewNow = widget
        self.main_window.layout.addWidget(widget)

        if appendHistory:
            self.history.append((widget_class, file_path))

        self.main_window.viewNow.show()

    def goBack(self, video_path=None):
        if self.history:
            if type(self.main_window.viewNow) != EffectSettingsWidget:
                self.history.pop()  # Видаляємо поточний стан
            
            if self.history:  # Переконуємось, що є попередній стан
                previous_state = self.history[-1]
                
                if len(previous_state) == 3:  # (widget_class, file_path, effect_object)
                    widget_class, file_path, effect_object = previous_state
                    self.changeWidgetOfMainWindow(widget_class, False, file_path=file_path, effect_object=effect_object)
                elif len(previous_state) == 2:  # (widget_class, file_path)
                    widget_class, file_path = previous_state
                    self.changeWidgetOfMainWindow(widget_class, False, file_path=file_path)
                else:  # (widget_class,)
                    widget_class = previous_state[0]
                    self.changeWidgetOfMainWindow(widget_class, False)

    def return_list_of_effects(self):
        items = []
        classes = []
        
        for file_name in os.listdir("effects"):
            if file_name.endswith(".py") and file_name != "__init__.py" and file_name != "BaseEffect.py":
                module_name = file_name[:-3]  # Видаляємо ".py" з імені файлу

                module_path = f"effects.{module_name}"
                module = importlib.import_module(module_path)
                
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type):  # Перевіряємо, чи це клас
                        classes.append(attr)

        for cls in classes:
            try:
                obj = cls()  # Створюємо об'єкт класу без аргументів
                items.append(obj)
            except TypeError:
                print(f"Cannot instantiate class {cls.__name__} without arguments.")
                

        return items