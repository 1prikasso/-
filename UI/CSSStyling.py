import os

class CSSStyling():
    # @staticmethod
    def styleSheet_for_window():
        return """
/* General Dark Theme Styling */
 QMainWindow {
        background-image: url('UI/images/bgImage.jpg');
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        
    }
    
    
QWidget {
    border-radius: 8px;
    border: none; /* Видалення зайвих смуг */
    color: #ffffff; /* Білий текст */
    font-family: OCR A Extended;
    font-size: 8pt;
}

/* Style for Buttons */
QPushButton {
    background-color: #1E1E1E; /* Темний фон для кнопок */
    color: #ffffff;
    border: 2px solid #333333; /* Темний обвід */
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 14pt;
}

QPushButton:hover {
    background-color: #333333; /* Світліший фон при наведенні */
}

QPushButton:pressed {
    background-color: #555555; /* Ще світліший фон при натисканні */
}



/* Style for Labels */
QLabel {
    font-size: 14pt;
    color: #ffffff;
    padding: 5px;
}

/* Style for ListView */
QListView {
    background-color: #1E1E1E; /* Темний фон */
    border: none; /* Видалення рамок */
    border-radius: 10px;
    padding: 10px;
    color: #ffffff;
    font-size: 14pt;
}

QListView::item {
    padding: 10px;
    border-radius: 5px;
    color: #ffffff;
}

QListView::item:hover {
    background-color: #333333; /* Ефект при наведенні */
}

/* Video Widget Styling */
QVideoWidget {
    border: none; /* Видалення рамок */
    border-radius: 12px;
}

/* Styling for Input Fields */
QLineEdit, QTextEdit {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    border-radius: 10px;
    padding: 10px;
    color: #ffffff;
}

/* Layout Adjustments */
QHBoxLayout {
    spacing: 20px;
}

/* Remove Borders for All Widgets */
QWidget {
    border: none; /* Видалення зайвих рамок */
}

/* Style for Containers */
QWidget#workWidget {
    background-color: #1E1E1E; /* Темний фон */
    border-radius: 12px;
    padding: 20px;
}
    """
    
    @staticmethod
    def styleSheet_for_button():
        return """QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 12px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 10px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #45a049;
            }"""
    
    @staticmethod
    def styleSheet_for_play_button():
        return """
        QPushButton {
            border-radius: 20px;
            border: 1px solid black;
        }
        QCheckBox {
            --color: white;
            --size: 45px;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            cursor: pointer;
            font-size: var(--size);
            user-select: none;
        }
        QCheckBox::indicator {
            width: 0;
            height: 0;
        }
        QCheckBox::checked {
            color: green;
        }
        QCheckBox::indicator::unchecked {
            image: url(play_icon_path.svg); /* Замініть на шлях до іконки */
        }
        QCheckBox::indicator::checked {
            image: url(play_icon_path.svg)
            backgroundcolor : 
           
        """
    
    @staticmethod
    def styleSheet_for_ListView():
        return """
            QListView {
                background-color: #f8f9fa; /* Світлий фон */
                border: 2px solid #ced4da; /* Обрамлення списку */
                font-size: 14px; /* Розмір тексту */
                color: #212529; /* Колір тексту */
            }

            QListView::item {
                background-color: #ffffff; /* Фон для елемента */
                border: 1px solid #dee2e6; /* Обрамлення елемента */
                border-radius: 4px; /* Згладжені кути */
                margin: 4px; /* Відступи між елементами */
                padding: 8px; /* Відступи всередині елемента */
            }

            QListView::item:hover {
                background-color: #e9ecef; /* Зміна фону при наведенні */
                border: 1px solid #adb5bd; /* Зміна обрамлення при наведенні */
            }

            QListView::item:selected {
                background-color: #007bff; /* Синій фон для вибраного елемента */
                color: #ffffff; /* Білий текст для вибраного елемента */
                border: 1px solid #0056b3; /* Обрамлення вибраного елемента */
            }"""