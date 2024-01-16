import sys
from PyQt5.QtWidgets import QApplication
from controller.changer_controller import ChangerController
from controller.main_controller import MainController


if __name__ == '__main__':
    app = QApplication(sys.argv)
    changer_controller = ChangerController()

    main_controller = MainController.get_instance()
    main_controller.init(changer_controller)
    main_controller.change_controller('login')
    sys.exit(app.exec())
    