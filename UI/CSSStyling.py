import os

    

class CSSStyling():
    def styleSheet_for_window():
        return """
/* General Dark Theme Styling */
QMainWindow {
    background-image: url('UI/images/bgImage3.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-size: auto 100%;
    backgroud-color: #ddd2fc;
}
    
QWidget {
    border-radius: 8px;
    border: none; /* Видалення зайвих смуг */
    color: #121212; /* Білий текст */
    font-family: OCR A Extended;
    font-size: 8pt;
}

QWidget#effectsContainer{
    
    background-color: #ddd2fc; /* Темний фон */
    border: none; /* Видалення рамок */
    border-radius: 10px;
    padding: 10px;
    color: #121212;
    font-size: 14pt;
    outline: 0;
}

QLabel{
    white-space: nowrap;
}

/* Style for Buttons */
QPushButton {
    background-color: #ddd2fc; /* Темний фон для кнопок */
    color: #121212;
    border: 2px solid #333333; /* Темний обвід */
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 14pt;
}

QPushButton:hover {
    background-color: #9078aa; /* Світліший фон при наведенні */
}

QPushButton:pressed {
    background-color: #8970aa; /* Ще світліший фон при натисканні */
}

/* Style for Labels */
QLabel {
    font-size: 14pt;
    color: #121212;
    padding: 5px;
}

/* Style for ListView */
QListView {
    background-color: #ddd2fc; /* Темний фон */
    border: none; /* Видалення рамок */
    border-radius: 10px;
    padding: 10px;
    color: #121212;
    font-size: 14pt;
    outline: 0;
}

QListView::item {
    padding: 10px;
    border-radius: 9px;
    color: #121212;
    margin-bottom: 3px;
}

QListView::item:hover {
    background-color: #9078aa; /* Ефект при наведенні */
}


QListView::item:selected {
    background-color: #9078aa; /* Колір фону для вибраного елемента */
    color: #121212; /* Колір тексту для вибраного елемента */
    outline: 0;
}

QListView::item:focus {
    outline: 0; /* Видаляє фокусну лінію */
}

/* Video Widget Styling */
QVideoWidget {
    border: none; /* Видалення рамок */
    border-radius: 12px;
}

QMediaPlayer {
    border: none; /* Видалення рамок */
    border-radius: 12px;
}

/* Styling for Input Fields */
QLineEdit, QTextEdit {
    background-color: #ddd2fc;
    border: 1px solid #333333;
    border-radius: 10px;
    padding: 10px;
    color: #121212;
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
    background-color: transparent; /* Темний фон */
    border-radius: 12px;
    padding: 20px;
}

QScrollArea {
    background-color: #333333; /* Темний фон */
    border: none; /* Видалення рамок */
    border-radius: 18px;
    padding: 10px;
}

QScrollArea > QWidget {
    background-color: #333333; /* Фон контейнера */
    border-radius: 18px; /* Скруглені краї */
    padding: 10px;
    color: #121212; /* Білий текст */
    font-size: 14pt;
}

QScrollArea QScrollBar:vertical, QScrollArea QScrollBar:horizontal {
    background: #5e217d; /* Темний фон для скролбарів */
    border-radius: 5px;
    width: 12px; /* Ширина скролбарів */
}

QScrollArea QScrollBar::handle {
    background: #555555; /* Ручка скролу */
    border-radius: 5px;
}

QScrollArea QScrollBar::handle:hover {
    background: #777777; /* Світліша ручка при наведенні */
}

QScrollArea QScrollBar::add-line, QScrollArea QScrollBar::sub-line {
    background: none; /* Прибираємо лінії зверху/знизу */
}

QScrollBar:horizontal {
    background: #ddd2fc; /* Темний фон */
    border-radius: 5px;
    height: 12px;
}

QScrollBar::handle:horizontal {
    background: #5e217d; /* Фіолетова ручка */
    border-radius: 5px;
}

QScrollBar::handle:horizontal:hover {
    background: #777777; /* Світліший відтінок при наведенні */
}

QScrollBar::add-line:horizontal, 
QScrollBar::sub-line:horizontal {
    background: none; /* Без кнопок на краях */
}

/* Стиль для полів введення */
QLineEdit, QTextEdit {
    background-color: #ddd2fc; /* Темний фон */
    border: 2px solid #333333; /* Темний обвід */
    border-radius: 10px;
    padding: 10px;
    color: #121212; /* Білий текст */
    font-size: 12pt;
    font-family: OCR A Extended;
}

QLineEdit:focus, QTextEdit:focus {
    border: 2px solid #5e217d; /* Виділення при фокусі */
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
                border-radius: 18px;
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
                background-color: #121212; /* Фон для елемента */
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
                color: #121212; /* Білий текст для вибраного елемента */
                border: 1px solid #0056b3; /* Обрамлення вибраного елемента */
            }"""