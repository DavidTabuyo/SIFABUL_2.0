from PyQt5.QtWidgets import QMainWindow
import arrow
import requests
from model.dao.check_dao import CheckDao
from model.dao.user_dao import UserDao
from model.dao.week_dao import WeekDao
from model.dao.worker_dao import WorkerDao
from model.dao.notification_worker_dao import NotificationWorkerDao
from view.worker_ui import WorkerUi


class WorkerController(QMainWindow):
    def __init__(self, main_controller,username:str) -> None:
        super().__init__()
        self.main_controller = main_controller
        
        #view
        self.view = WorkerUi()
        self.view.setupUi(self)
        self.view.BtnFichar.clicked.connect(self.BtnCheck_clicked)
        self.view.BtnResumen.clicked.connect(self.btnResumen_clicked)
        self.view.BtnChangePassword.clicked.connect(self.btnChangePassword_clicked)
        self.view.refresh_btn.clicked.connect(self.refresh_btn_clicked)
        self.view.close_btn.clicked.connect(self.closeBtn_clicked)
        self.view.delete_btn.clicked.connect(self.delete_btn_clicked)


        #model
        self.worker= WorkerDao.get_worker(username)
        
        #update view
        self.update_checks()
        self.update_notifications()
        self.view.set_user(self.worker.getID())

        
    def update_checks(self):
        self.view.clear_layout(self.view.layoutFichajes)
        checks = WorkerDao.get_today_checks(self.worker.getID(), self.get_current_time()[1])
        self.view.addChecks(checks)
        
    
    def update_notifications(self):
        self.view.clear_layout(self.view.notifications_layout)
        notifications=WorkerDao.get_notifications(self.worker.getID())
        self.view.addNotifications(notifications)
    
    def BtnCheck_clicked(self):
        try:
            self.check()
            self.view.clear_layout(self.view.layoutFichajes)
            self.update_checks()
        except Exception as e:
            print(e)
            self.view.showError(e)
    
    def btnResumen_clicked(self):
        weeks=WeekDao.get_weeks(self.worker.worker_id)
        self.view.show_summary(weeks)
        
    def btnChangePassword_clicked(self):
        self.main_controller.change_controller('changepassword',self.worker.worker_id)

    def refresh_btn_clicked(self):
        self.update_notifications()

    def get_current_time(self) -> tuple[str, str, str]:
        timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
        monday = timestamp.floor('week').format('YYYY-MM-DD')
        date = timestamp.format('YYYY-MM-DD')
        time = timestamp.format('HH:mm:ss')
        return (monday, date, time)

    def check(self):
        # get actual time
        monday, date, time = self.get_current_time()

        # get last check
        last_check = WorkerDao.get_last_today_check(self.worker.getID(), date)
        if last_check and time[3:5] == last_check.time[3:5]:
            raise LookupError('Ya has fichado')

        # Add new check
        is_new_check_entry = not last_check.is_entry if last_check else True
        CheckDao.add_new_check(self.worker.getID(), date, time, is_new_check_entry)

        # Exit function if !is_entry
        if is_new_check_entry:
            return

        # Cupdate week and calculate check time
        week = WeekDao.get_week(self.worker.getID(), monday)
        week_total = week.total if week else 0

        entry = arrow.get(last_check.time, 'HH:mm:ss')
        exit = arrow.get(time, 'HH:mm:ss')
        total_seconds_check_in = (exit - entry).total_seconds()

        WeekDao.update_or_create_week(
            self.worker.getID(), monday, week_total + total_seconds_check_in)

    def closeBtn_clicked(self):
        self.close()
    
    def delete_btn_clicked(self):
        notifications=WorkerDao.get_notifications(self.worker.getID())
        #NotificationWorkerdao.update_notifications_status()
        self.view.clear_layout(self.view.notifications_layout)
    
    