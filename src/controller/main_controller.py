class MainController:
    instance = None

    @classmethod
    def get_instance(cls):
        cls.instance = cls.instance or MainController()
        return cls.instance

    def init(self, changer_controller):
        self.controller = changer_controller

    def change_controller(self, new_controler_name, *args):
        if not hasattr(self, 'controller'):
            raise AttributeError('Tienes que inicializlo primero (init())')

        self.controller.controller_changer(new_controler_name, *args)
