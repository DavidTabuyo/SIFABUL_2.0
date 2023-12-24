from PyQt5.QtWidgets import QMainWindow
from view.login_ui import Ui_MainWindow

class LoginController(QMainWindow):
    def __init__(self, main_controller) -> None:
        super().__init__()
        self.main_controller = main_controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    def aceptar(self):
        if valid():
            self.close()
            self.main_controller.change_controller('worker')