from PyQt5.QtWidgets import QMainWindow
import arrow
from controller.change_password_controller import ChangePasswordController
from controller.main_controller import MainController
from model.dao.check_dao import CheckDao
from model.dao.factory_dao import FactoryDao
from model.dao.week_dao import WeekDao
from model.dao.notification_worker_dao import NotificationWorkerDao
from services.current_time import get_current_time
from view.worker_ui import WorkerUi


class WorkerController(QMainWindow):
    def __init__(self, username: str) -> None:
        super().__init__()
        self.main_controller = MainController.get_instance()
        self.dialog=None

        # view
        self.view = WorkerUi()
        self.view.setupUi(self)
        self.view.BtnFichar.clicked.connect(self.BtnCheck_clicked)
        self.view.BtnResumen.clicked.connect(self.btnResumen_clicked)
        self.view.BtnChangePassword.clicked.connect(
            self.btnChangePassword_clicked)
        self.view.refresh_btn.clicked.connect(self.refresh_btn_clicked)
        self.view.close_btn.clicked.connect(self.closeBtn_clicked)
        self.view.delete_btn.clicked.connect(self.delete_btn_clicked)

        # model
        self.worker = FactoryDao.get_worker(username)

        # update view
        self.update_checks()
        self.update_notifications()
        self.view.set_user(self.worker.worker_id)

    def update_checks(self):
        self.view.clear_layout(self.view.layoutFichajes)
        checks = FactoryDao.get_today_checks(
            self.worker.worker_id, get_current_time()[1])
        self.view.addChecks(checks)

    def update_notifications(self):
        self.view.clear_layout(self.view.notifications_layout)
        notifications = [notification for notification in FactoryDao.get_notifications_by_worker(
            self.worker.worker_id) if not notification.seen]
        if notifications:
            self.view.addNotifications(notifications)
        else:
            self.view.show_label()

    def BtnCheck_clicked(self):
        try:
            self.check()
            self.view.clear_layout(self.view.layoutFichajes)
            self.update_checks()
        except Exception as e:
            print(e)
            self.view.showError(e)

    def btnResumen_clicked(self):
        weeks = FactoryDao.get_weeks(self.worker.worker_id)
        self.view.show_summary(weeks)

    def btnChangePassword_clicked(self):
        #we call change password controller because its a dialog
        self.dialog= ChangePasswordController(self.worker.worker_id,self.worker.worker_id)
        self.dialog.exec()

    def refresh_btn_clicked(self):
        self.update_notifications()

    def check(self):
        # get actual time
        monday, date, time, _ = get_current_time()

        # get last check
        last_check = FactoryDao.get_last_today_check(
            self.worker.worker_id, date)
        if last_check and time[3:5] == last_check.time[3:5]:
            raise LookupError('Ya has fichado')

        # Add new check
        is_new_check_entry = not last_check.is_entry if last_check else True
        CheckDao.add_new_check(self.worker.worker_id,
                               date, time, is_new_check_entry)

        # Exit function if !is_entry
        if is_new_check_entry:
            return

        # Cupdate week and calculate check time
        week = FactoryDao.get_week(self.worker.worker_id, monday)
        week_total = week.total if week else 0

        entry = arrow.get(last_check.time, 'HH:mm:ss')
        exit = arrow.get(time, 'HH:mm:ss')
        total_seconds_check_in = (exit - entry).total_seconds()

        WeekDao.update_or_create_week(
            self.worker.worker_id, monday, week_total + total_seconds_check_in)

    def closeBtn_clicked(self):
        self.close()

    def delete_btn_clicked(self):
        NotificationWorkerDao.update_notification_status(
            self.worker.worker_id, get_current_time()[3])
        self.view.clear_layout(self.view.notifications_layout)
        self.view.show_label()
