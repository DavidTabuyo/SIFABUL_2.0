import sys
from PyQt5.QtWidgets import QApplication
from controller.login_controller import LoginController
from controller.main_controller import MainController


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_controller = MainController()
    main_controller.change_controller(LoginController)
    sys.exit(app.exec())
    