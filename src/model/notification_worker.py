class NotificationWorker:
    def __init__(self, notifiaction_id: int, worker_id: str, title: str, description: str, datetime: str, seen: str):
        self.notification_id = notifiaction_id
        self.worker_id = worker_id
        self.title = title
        self.description = description
        self.datetime = datetime
        self.seen = seen

    def get_output(self) -> str:
        return f"Título: {self.title}\nFecha y Hora: {self.datetime}\n\nDescripción: {self.description}"
