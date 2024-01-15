import sys
from PyQt5.QtWidgets import QApplication
from controller.login_controller import LoginController
from controller.main_controller import MainController
from model.dao.notification_dao import NotificationDao
from model.dao.user_dao import UserDao


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # main_controller = MainController()
    # main_controller.change_controller('login')
    # sys.exit(app.exec())
    UserDao.delete_user('dtabum00')
    