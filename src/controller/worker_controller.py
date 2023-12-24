from PyQt5.QtWidgets import QMainWindow

from view.worker_ui import WorkerUi


class WorkerController(QMainWindow):
    def __init__(self, main_controller) -> None:
        super().__init__()
        self.main_controller = main_controller
        self.update_checks()
        self.update_notifications()
        #view
        self.view = WorkerUi()
        self.view.setupUi(self)
        self.view.BtnFichar.clicked.connect(self.BtnFichar_clicked)
        self.view.btnResumen.clicked.connect(self.btnResumen_clicked)
        self.view.btnChangePassword.clicked.connect(self.btnChangePassword_clicked)
        self.view.refresh_btn.clicked.connect(self.refresh_btn_clicked)

        #model
        
    
    