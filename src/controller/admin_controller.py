from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from model.dao.admin_dao import AdminDao
from model.dao.week_dao import Weekdao
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
        self.view.BtnChangePassword.clicked.connect(self.change_password_btn_clicked)
        self.view.edit_list_btn.clicked.connect(self.edit_list_btn_clicked)
        self.view.send_notification_btn.clicked.connect(self.send_notification_btn_clicked)
        self.view.refresh_btn.clicked.connect(self.update_btn_clicked)
        self.view.add_worker_btn.clicked.connect(self.add_btn_clicked)
        self.view.close_btn.clicked.connect(self.close_btn_clicked)

        
        
        #model
        self.admin=AdminDao.get_admin(username)
        
        
        #update view
        self.update_notifications()
        self.update_worker_list()
        self.view.set_user(self.admin.getID())
        
        
    def update_worker_list(self):
        self.view.clear_layout(self.view.workers_layout)
        workerList= self.get_workers()
        self.show_workers(workerList)

    
    def update_notifications(self):
        self.view.clear_layout(self.view.notifications_layout)
        notList= self.get_notifications()
        self.view.show_notifications(notList)

    def change_password_btn_clicked(self):
        self.main_controller.change_controller('changepassword',self.admin.getID())

    
    def edit_list_btn_clicked(self):
        self.main_controller.change_controller('editworkerlist',self.admin.getID())

    
    def send_notification_btn_clicked(self):
        self.main_controller.change_controller('sendnotification',self.admin.getID())

        
    def add_btn_clicked(self):
        self.main_controller.change_controller('addworker',self.admin.getID())

    
    def update_btn_clicked(self):
        self.update_notifications()
        self.update_worker_list()

    def get_workers(self)->list[Worker]:
        return AdminDao.get_workers(self.admin.getID())
        
    def get_notifications(self)->list[Notification]:
        return AdminDao.get_notifications(self.admin.getID())
    
    def show_workers(self, workerList: list[Worker]):
        for worker in workerList:
            button = QtWidgets.QPushButton(worker.get_output_for_list())
            self.view.workers_layout.addWidget(button)
            button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            button.setStyleSheet('background-color: #2c313c;'
                    'color: rgba(255, 255, 255, 210);'
                    'border-radius: 15px;'  
                    'font-size: 16px;'  
                    'font-weight: bold;')  

            button.clicked.connect(lambda _, w=worker: self.button_show_summary(w))
            
    def button_show_summary(self,worker:Worker):
        weeks=Weekdao.get_weeks(worker.worker_id)
        self.view.show_summary(weeks)
        
    def close_btn_clicked(self):
        self.close()
    