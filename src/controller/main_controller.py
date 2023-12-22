from controller.login_controller import LoginController


class MainController:
    CONTROLLERS = {
        'login': LoginController,
        'admin': AdminController,
        'worker': WorkerController,
        'changepassword': ChangePasswordController,
        'editworkerlist': EditWorkerListController,
        'sendnotification': SendNotificationController,
        'sumary': SummaryController,
        'updateworker': UpdateWorkerController
    }
    
    def __init__(self) -> None:
        self.current_controller = None
        
    def change_controller(self, new_controler_name, *args):
        self.current_controller = self.CONTROLLERS[new_controler_name](self, *args)
        self.change_controller.show()