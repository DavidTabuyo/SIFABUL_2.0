from controller.admin_controller import AdminController
from controller.change_password_controller import ChangePasswordController
from controller.edit_worker_list_controller import EditWorkerListController
from controller.login_controller import LoginController
from controller.send_notification_controller import SendNotificationController
from controller.update_worker_controller import UpdateWorkerController
from controller.worker_controller import WorkerController


class MainController:
    CONTROLLERS = {
        'login': LoginController,      
        'admin': AdminController,
        'worker': WorkerController,
        'changepassword': ChangePasswordController,
        'editworkerlist': EditWorkerListController,
        'sendnotification': SendNotificationController,
        'updateworker': UpdateWorkerController
    }
    
    def __init__(self) -> None:
        self.current_controller = None
        
    def change_controller(self, new_controler_name, *args):
        self.current_controller = self.CONTROLLERS[new_controler_name](self, *args)
        self.current_controller.show()