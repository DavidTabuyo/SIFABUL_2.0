from PyQt5.QtWidgets import QMainWindow

from model.dao.admin_dao import AdminDao
from view.send_notification_ui import SendNotificationUi


class SendNotificationController(QMainWindow):
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
        
        #update list
        self.update_list()

        
        
        
    def cancel_btn_clicked(self):
        self.close()
    
    def send_btn_clicked(self):
        try:
            self.add_notification()
            self.view.send_advise()
            self.close()
        except Exception as e:
            self.view.showError(e)

        
    def update_list(self):
        name_list = [worker.get_output_for_list() for worker in AdminDao.get_workers(self.admin.getID())]
        #self.view.select_worker_cb.addItems(name_list)
        
    def add_notification(self):
        #add notification, show error if no worker selected
        selected_workers # = [item.text() for item in self.view.select_worker_cb.selectedItems()]
        if not selected_workers:
            raise ValueError('No has seleccionado ningún destinatario')
        else:
            #create and send notification to selected_workers
            ...
        
