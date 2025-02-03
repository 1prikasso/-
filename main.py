import sys
from PyQt5.QtWidgets import QApplication
from controllers.MainController import MainController
from views.MainWindow import MainWindow
import os
import shutil

def clear_temp_folder():
    temp_folder = 'temp'
    if os.path.exists(temp_folder):
        for filename in os.listdir(temp_folder):
            file_path = os.path.join(temp_folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"{file_path}: {e}")
    else:
        os.makedirs(temp_folder)


if __name__ == "__main__":
    clear_temp_folder()
    
    app = QApplication(sys.argv)

    main_window = MainWindow()

    main_controller = MainController(main_window)

    sys.exit(app.exec_())