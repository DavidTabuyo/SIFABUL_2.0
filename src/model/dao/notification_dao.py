from model.notification import Notification
from services.db_connection_service import db_connection_service


class NotificationDao:
    
    @staticmethod
    def get_notifications(admin_id: str) -> list[Notification]:
        with db_connection_service() as conn:
            notifications_data = conn.querry('''
                SELECT DISTINCT notifications.notification_id, notifications.title, notifications.description, notifications.datetime
                FROM notifications
                JOIN workers_notifications ON notifications.notification_id = workers_notifications.notification_id
                JOIN workers ON workers_notifications.worker_id = workers.worker_id
                WHERE workers.admin_id = ?
                ORDER BY notifications.notification_id
            ''', (admin_id,))

        return [Notification(*notification) for notification in notifications_data]

    @staticmethod
    def add_notification(title: str, description: str, datetime: str):
        with db_connection_service() as conn:
            conn.querry('''
                INSERT INTO notifications (title, description, datetime) VALUES
                    (?, ?, ?);
            ''', (title, description, datetime))
