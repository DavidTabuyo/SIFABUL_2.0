from PyQt5.QtWidgets import QDialog
from controller.main_controller import MainController
from model.dao.factory_dao import FactoryDao
from model.dao.user_dao import UserDao
from model.worker import Worker
from view.edit_worker_list_ui import EditWorkerListUi


class EditWorkerListController(QDialog):
    def __init__(self, admin_id: str) -> None:
        super().__init__()
        self.main_controller = MainController.get_instance()

        # view
        self.view = EditWorkerListUi()
        self.view.setupUi(self)
        self.view.cancel_btn.clicked.connect(self.btn_cancel_clicked)
        self.view.accept_btn.clicked.connect(self.btn_accept_clicked)
        self.view.delete_user_btn.clicked.connect(self.btn_delete_user_clicked)
        self.view.change_password_btn.clicked.connect(
            self.btn_change_password_clicked)

        # model
        self.admin = FactoryDao.get_admin(admin_id)

        # setup view
        self.view.show_workers(self.get_workers())

    def get_workers(self) -> list[Worker]:
        return FactoryDao.get_workers(self.admin.admin_id)

    def btn_cancel_clicked(self):
        self.close()

    def btn_accept_clicked(self):
        try:
            # mirar que ha modificado y modificarlo
            if len(self.view.username_le.text()) == 0:
                raise TypeError("No has realizado ninguna accion")
            self.change_name()
            self.close()
        except Exception as e:
            self.view.showError(e)

    def btn_delete_user_clicked(self):
        UserDao.delete_user(self.view.get_selected_worker())
        self.close()

    def btn_change_password_clicked(self):
        self.main_controller.change_controller(
            'changepassword', self.admin.admin_id, self.view.get_selected_worker())

    def change_name(self):
        user = FactoryDao.get_user(self.view.get_selected_worker())
        user.name = self.view.username_le.text()
        UserDao.update(user)
