from PyQt5.QtWidgets import QDialog

from model.dao.admin_dao import AdminDao
from model.dao.notification_dao import NotificationDao
from model.dao.notification_worker_dao import NotificationWorkerDao
from model.dao.user_dao import UserDao
from services.current_time import get_current_time
from view.send_notification_ui import SendNotificationUi



class SendNotificationController(QDialog):
    def __init__(self, main_controller,admin_id:str) -> None:
        super().__init__()
        self.main_controller = main_controller
        
        #view
        self.view=SendNotificationUi()
        self.view.setupUi(self)
        self.view.cancel_btn.clicked.connect(self.cancel_btn_clicked)
        self.view.send_btn.clicked.connect(self.send_btn_clicked)
        
        
        #model
        self.admin=AdminDao.get_admin(admin_id)
        
        
        
        
    def cancel_btn_clicked(self):
        self.close()
    
    def send_btn_clicked(self):
        try:
            self.add_notification()
            self.view.send_advise()
            self.close()
            # self.main_controller.change_controller('admin',self.admin.admin_id)
        except Exception as e:
            self.view.showError(e)

        
        
    def add_notification(self):
        #add notification, show error if no worker selected
        if len(self.view.title_edit.text())==0 or len(self.view.body_edit.text())==0:
            raise TypeError("El asunto o la descripción no pueden estar vacíos")
            
        selected_workers  =  self.view.select_worker_cb.text().split(';')
        if not selected_workers:
            raise ValueError('No has seleccionado ningún destinatario')
            
        for worker_id in selected_workers:       
            if not UserDao.is_worker(worker_id):
                raise TypeError('No existe un trabajdor con el nombre de usuario: ',worker_id)

        notification_id= NotificationDao.get_notifications(self.admin.admin_id)[-1].notification_id+1
        NotificationDao.add_notification(self.view.title_edit.text(),self.view.body_edit.text(),get_current_time()[3])

        for worker_id in selected_workers:       
            NotificationWorkerDao.add_notification_worker(worker_id,notification_id,None)
            
