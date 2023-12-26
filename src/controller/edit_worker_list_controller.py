from PyQt5.QtWidgets import QMainWindow

from model.dao.admin_dao import AdminDao


class EditWorkerListController(QMainWindow):
    def __init__(self, main_controller, admin_id:str) -> None:
        super().__init__()
        self.main_controller = main_controller
        
    
        #view
        
        #model
        self.admin= AdminDao.get_admin(admin_id)



