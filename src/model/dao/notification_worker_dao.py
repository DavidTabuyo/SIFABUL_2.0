from model.notification_worker import NotificationWorker
from services.db_connection_service import db_connection_service


class NotificationWorkerDao:

    @staticmethod
    def get_notifications(worker_id: str) -> list[NotificationWorker]:
        with db_connection_service() as conn:
            notifications = conn.querry('''
                SELECT notifications.notification_id, notifications.title, notifications.description, notifications.datetime, workers_notifications.seen
                FROM notifications
                JOIN workers_notifications on notifications.notification_id = workers_notifications.notification_id
                WHERE workers_notifications.worker_id = ?
                ORDER BY notifications.datetime DESC
            ''', (worker_id,))
        return [NotificationWorker(*notification) for notification in notifications]

    @staticmethod
    def add_notification(worker_id: str, notification_id: str, seen: str):
        with db_connection_service() as conn:
            conn.querry('''
                INSERT INTO workers_notifications (worker_id, notification_id, seen) VALUES
                    (?, ?, ?);
            ''', (worker_id, notification_id, seen))

    @staticmethod
    def update_notification_status(worker_id: str, seen: str):
        with db_connection_service() as conn:
            conn.querry('''
                UPDATE workers_notifications
                SET seen = ?
                WHERE worker_id = ?; 
            ''', (seen, worker_id))