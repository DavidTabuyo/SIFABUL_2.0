from model.dao.notification_worker_dao import NotificationWorkerDao


class Notification:
    def __init__(self, notifiaction_id: int, title: str, description: str, datetime: str):
        self.notification_id = notifiaction_id
        self.title = title
        self.description = description
        self.datetime = datetime
        
    def get_output(self) -> str:
        # Construir el string formateado
        return  f"Título: {self.title}\nFecha y Hora: {self.datetime}\n\nDescripción: {self.description}"
        