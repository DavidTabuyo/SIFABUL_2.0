from PyQt5.QtWidgets import QMainWindow
from model.dao.user_dao import UserDao

from view.change_password_ui import ChangePasswordUi


class ChangePasswordController(QMainWindow):
    def __init__(self, main_controller,user_id:str) -> None:
        super().__init__()
        self.main_controller = main_controller
        
        #view
        self.view = ChangePasswordUi()
        self.view.setupUi(self)
        self.view.cancel_btn.clicked.connect(self.cancel_btn_clicked)
        self.view.accept_btn.clicked.connect(self.accept_btn_clicked)
        
        #model
        self.user=UserDao.get_user(user_id)
        
        
    def cancel_btn_clicked(self):
        self.returnToController()
        
    def accept_btn_clicked(self):
        try:
            self.change_password(self.view.old_password_imp.text(),self.view.new_password_imp.text())
            self.view.change_correct()
            self.returnToController()
        except Exception as e:
            self.view.showError(e)
        
    def returnToController(self):
        if UserDao.is_admin(self.user.getId()):
            self.main_controller.change_controller('admin',self.user.getId())
        else:
            self.main_controller.change_controller('worker',self.user.getId())

    def change_password(self,old_pssw:str, new_pssw:str):
        ...