import sys
from PyQt5.QtWidgets import QApplication
from controllers.MainController import MainController
from views.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Створюємо головне вікно
    main_window = MainWindow()

    # Підключаємо контролер
    main_controller = MainController(main_window)

    sys.exit(app.exec_())