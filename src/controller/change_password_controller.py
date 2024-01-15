from PyQt5.QtWidgets import QMainWindow
import bcrypt
from model.dao.user_dao import UserDao

from view.change_password_ui import ChangePasswordUi


class ChangePasswordController(QMainWindow):
    def __init__(self, main_controller, changer_id: str, target_id: str) -> None:
        super().__init__()
        self.main_controller = main_controller

        # view
        self.view = ChangePasswordUi()
        self.view.setupUi(self)
        self.view.cancel_btn.clicked.connect(self.cancel_btn_clicked)
        self.view.accept_btn.clicked.connect(self.accept_btn_clicked)

        # model
        self.changer = UserDao.get_user(changer_id)
        self.target = UserDao.get_user(target_id)

    def cancel_btn_clicked(self):
        self.returnToController()

    def accept_btn_clicked(self):
        try:
            self.change_password(
                self.view.old_password_imp.text(), self.view.new_password_imp.text())
            self.view.change_correct()
            self.returnToController()
        except ValueError as e:
            self.view.showError(e)

    def returnToController(self):

        if UserDao.is_admin(self.changer.getId()):
            self.main_controller.change_controller(
                'admin', self.changer.getId())
        else:
            self.main_controller.change_controller(
                'worker', self.changer.getId())

    def change_password(self, old_pssw: str, new_pssw: str):
        if bcrypt.hashpw(old_pssw.encode('utf-8'), self.target.salt) != self.target.hash:
            raise ValueError('Contraseña incorrecta')

        new_salt = bcrypt.gensalt()
        new_hash = bcrypt.hashpw(new_pssw.encode('utf-8'), new_salt)
        UserDao.update_password(self.target.user_id, new_salt, new_hash)
