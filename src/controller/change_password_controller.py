from PyQt5.QtWidgets import QDialog
import bcrypt
from model.dao.user_dao import UserDao

from view.change_password_ui import ChangePasswordUi


class ChangePasswordController(QDialog):
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
        self.close()

    def accept_btn_clicked(self):
        try:
            self.change_password(
                self.view.old_password_imp.text(), self.view.new_password_imp.text())
            self.view.change_correct()
            self.close()
        except ValueError as e:
            self.view.showError(e)

    def change_password(self, old_pssw: str, new_pssw: str):
        if bcrypt.hashpw(old_pssw.encode('utf-8'), self.target.salt) != self.target.hash:
            raise ValueError('Contraseña incorrecta')

        self.target.salt = bcrypt.gensalt()
        self.target.hash = bcrypt.hashpw(new_pssw.encode('utf-8'), self.target.salt)
        UserDao.update(self.target)
