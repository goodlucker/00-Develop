import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow


class TestMainWindow(unittest.TestCase):
    @patch("ui.main_window.MainWindow")
    def test_main_window_initialization(self, MockMainWindow):
        # Mock QApplication to avoid creating a real application instance
        with patch("sys.argv", ["test"]):
            app = QApplication(["test"])

        # Mock MainWindow
        mock_window = MockMainWindow.return_value
        mock_window.show = MagicMock()

        # Instantiate MainWindow and check if show() is called
        window = MainWindow()
        window.show()
        mock_window.show.assert_called_once()

        # Clean up QApplication
        app.exit()


if __name__ == "__main__":
    unittest.main()
