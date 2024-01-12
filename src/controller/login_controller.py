from PyQt5.QtWidgets import QMainWindow
import bcrypt
from model.dao.user_dao import UserDao
from view.login_ui import loginUI

class LoginController(QMainWindow):
    def __init__(self, main_controller) -> None:
        super().__init__()
        self.main_controller = main_controller
        #view
        self.view = loginUI()
        self.view.setupUi(self)
        self.view.BotonOk.clicked.connect(self.BotonOk_clicked)
        self.view.btn_cancel.clicked.connect(self.btn_cancel_clicked)

    # boton aceptar
    def BotonOk_clicked(self):
        self.main_controller.change_controller(self.login(self.view.UserName.text(), self.view.Password.text()),self.view.UserName.text())

        # check if correct
        try:
            ...
        except Exception as e:
            self.view.showError(e)
        
    def btn_cancel_clicked(self):
        self.close()
            
    
    def login(self, user_id: str, password: str) -> str:

        # Check if exists
        if UserDao.is_worker(user_id):
            type = 'worker'
        elif UserDao.is_admin(user_id):
            type = 'admin'
        else:
            raise LookupError('Usuario no encontrado')

        # Comprueba contraseña
        if not self.check_password(user_id, password):
            raise ValueError('Contraseña incorrecta')

        return type


    def check_password(self, user_id: str, password: str) -> bool:
        user = UserDao.get_user(user_id)
        return user.hash == bcrypt.hashpw(password.encode('utf-8'), user.salt)

            
        
    