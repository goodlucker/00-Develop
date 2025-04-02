def get_stylesheet():
    return """
    QMainWindow {
        background-color: #f5f5f5;
    }
    QListWidget {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 3px;
    }
    QPushButton {
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        padding: 5px 10px;
        min-width: 80px;
        border-radius: 3px;
    }
    QPushButton:hover {
        background-color: #e9ecef;
    }
    QPushButton:pressed {
        background-color: #dee2e6;
    }
    QLineEdit {
        padding: 5px;
        border: 1px solid #ddd;
        border-radius: 3px;
    }
    QProgressBar {
        text-align: center;
        border: 1px solid #ddd;
        border-radius: 3px;
    }
    QProgressBar::chunk {
        background-color: #4CAF50;
    }
    """