import sys
from PyQt5.QtWidgets import QApplication
from controller.changer_controller import ChangerController


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_controller = ChangerController()
    main_controller.controller_changer('login')
    sys.exit(app.exec())
    