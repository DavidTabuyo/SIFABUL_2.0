from PyQt5.QtWidgets import QMainWindow
import arrow
from model.dao.user_dao import UserDao
from model.dao.worker_dao import WorkerDao
from view.worker_ui import WorkerUi


class WorkerController(QMainWindow):
    def __init__(self, main_controller,username:str) -> None:
        super().__init__()
        self.main_controller = main_controller
        
        #view
        self.view = WorkerUi()
        self.view.setupUi(self)
        self.view.BtnFichar.clicked.connect(self.BtnFichar_clicked)
        self.view.btnResumen.clicked.connect(self.btnResumen_clicked)
        self.view.btnChangePassword.clicked.connect(self.btnChangePassword_clicked)
        self.view.refresh_btn.clicked.connect(self.refresh_btn_clicked)

        #model
        self.worker= WorkerDao.get_worker(username)
        
        #update view
        self.update_checks()
        #self.update_notifications()
        
    def update_checks(self):
        self.view.clear_layout(self.view.layoutFichajes)
        checks = WorkerDao.get_today_checks(self.worker.getID(), self.get_current_time()[1])
        self.view.addChecks(checks)
        
    
    def update_notifications(self):
        ...
    
    def BtnFichar_clicked(self):
        ...
    
    def btnResumen_clicked(self):
        ...
    
    def btnChangePassword_clicked(self):
        ...

    def refresh_btn_clicked(self):
        self.update_notifications()

    def get_current_time(self) -> tuple[str, str, str]:
        timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
        monday = timestamp.floor('week').format('YYYY-MM-DD')
        date = timestamp.format('YYYY-MM-DD')
        time = timestamp.format('HH:mm:ss')
        return (monday, date, time)

    
    