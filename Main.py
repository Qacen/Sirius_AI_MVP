import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = window()
    sys.exit(app.exec())