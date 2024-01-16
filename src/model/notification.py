class Notification:
    def __init__(self, notifiaction_id: int, title: str, description: str, datetime: str):
        self.notification_id = notifiaction_id
        self.title = title
        self.description = description
        self.datetime = datetime

    def get_output(self) -> str:
        return f"Título: {self.title}\nFecha y Hora: {self.datetime}\n\nDescripción: {self.description}"
