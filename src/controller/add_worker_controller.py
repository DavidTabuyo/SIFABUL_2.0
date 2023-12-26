from PyQt5.QtWidgets import QMainWindow


class AddWorkerController(QMainWindow):
    def __init__(self, main_controller) -> None:
        super().__init__()
        self.main_controller = main_controller