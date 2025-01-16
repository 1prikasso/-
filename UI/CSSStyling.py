class CSSStyling():
    @staticmethod
    def styleSheet_for_button():
        return """border-radius : 20; border : 1px solid black"""
    
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