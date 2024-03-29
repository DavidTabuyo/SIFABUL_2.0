from PyQt5.QtWidgets import QDialog
import bcrypt
from controller.main_controller import MainController
from model.dao.admin_dao import AdminDao
from model.dao.factory_dao import FactoryDao
from model.dao.worker_dao import WorkerDao
from model.worker import Worker
from view.add_worker_ui import AddWorkerUi


class AddWorkerController(QDialog):
    def __init__(self, admin_id: str) -> None:
        super().__init__()
        self.main_controller = MainController.get_instance()

        # view
        self.view = AddWorkerUi()
        self.view.setupUi(self, admin_id)

        self.view.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.view.btm_accept.clicked.connect(self.btn_accept_clicked)

        # model
        self.admin = FactoryDao.get_admin(admin_id)

    def btn_cancel_clicked(self):
        self.close()

    def btn_accept_clicked(self):
        try:
            # check if user exists before
            self.check_worker_exist()
            # check if password are the same
            self.check_passwords()
            # add worker to worker list
            self.add_worker()
            # send an advise
            self.view.change_correct()
            # change controller
            self.close()

        except Exception as e:
            self.view.showError(e)

    def check_worker_exist(self):
        return WorkerDao.is_worker(self.view.name_le.text())

    def check_passwords(self):
        if self.view.password_le.text() != self.view.confirm_password_le.text():
            raise ValueError('Las contraseñas no coinciden')

    def add_worker(self):
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(
            self.view.password_le.text().encode('utf-8'), salt)
        AdminDao.add_worker(Worker(self.view.name_le.text(), self.view.name_le_2.text(
        ), salt, hash, self.admin.admin_id), self.admin.admin_id)
