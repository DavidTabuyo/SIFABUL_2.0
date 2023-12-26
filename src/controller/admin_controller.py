from PyQt5.QtWidgets import QMainWindow

from model.dao.admin_dao import AdminDao
from model.notification import Notification
from model.worker import Worker
from view.admin_ui import AdminUi


class AdminController(QMainWindow):
    def __init__(self, main_controller,username:str) -> None:
        super().__init__()
        self.main_controller = main_controller
        
        #view
        self.view=AdminUi()
        self.view.setupUi(self)
        self.view.change_password_btn.clicked.connect(self.change_password_btn_clicked)
        self.view.edit_list_btn.clicked.connect(self.edit_list_btn_clicked)
        self.view.send_notification_btn.clicked.connect(self.send_notification_btn_clicked)
        self.view.update_btn.clicked.connect(self.update_btn_clicked)
        
        #model
        self.admin=AdminDao.get_admin(username)
        
        
        #update view
        self.update_notifications()
        self.update_worker_list()
        
        
    def update_worker_list(self):
        self.view.clear_layout(self.view.list_layout)
        workerList= self.get_workers()
        self.view.show_workers(workerList)

    
    def update_notifications(self):
        self.view.clear_layout(self.view.notifications_layout)
        notList= self.get_notifications()
        self.view.show_notifications(notList)

    def change_password_btn_clicked(self):
        self.main_controller.change_controller('changepassword',self.admin.getID())

    
    def edit_list_btn_clicked(self):
        self.main_controller.change_controller('addworker',self.admin.getID())

    
    def send_notification_btn_clicked(self):
        ...
    
    def update_btn_clicked(self):
        self.update_notifications()
        self.update_worker_list()

    def get_workers(self)->list[Worker]:
        return AdminDao.get_workers(self.admin.getID())
        
    def get_notifications(self)->list[Notification]:
        return AdminDao.get_notifications(self.admin.getID())
    
        
    