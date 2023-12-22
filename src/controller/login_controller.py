from PyQt5.QtWidgets import QMainWindow


class LoginController(QMainWindow):
    def __init__(self, main_controller) -> None:
        super().__init__()
        self.main_controller = main_controller
        
    def aceptar(self):
        if valid():
            self.close()
            self.main_controller.change_controller('worker')