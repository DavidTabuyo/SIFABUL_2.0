from model.admin import Admin
from model.notification import Notification
from model.worker import Worker
from services.db_connection_service import db_connection_service


class AdminDao:
    @staticmethod
    def get_admin(admin_id: str) -> Admin:
        with db_connection_service() as conn:
            admins = conn.querry('''
                    SELECT user_id, name, salt, hash
                    FROM users
                    WHERE user_id = ?
                ''', (admin_id,))

        return Admin(*admins[0]) if admins else None

    @staticmethod
    def get_notifications(admin_id: str) -> list[Notification]:
        with db_connection_service() as conn:
            notifications_data = conn.querry('''
                SELECT notifications.notification_id, notifications.title, notifications.description, notifications.datetime
                FROM notifications
                JOIN workers_notifications ON notifications.notification_id = workers_notifications.notification_id
                JOIN workers ON workers_notifications.worker_id = workers.worker_id
                WHERE workers.admin_id = ?
            ''', (admin_id,))

        return [Notification(*notification) for notification in notifications_data]

    @staticmethod
    def get_workers(admin_id: str) -> list[Worker]:
        with db_connection_service() as conn:
            workers_data = conn.querry('''
                SELECT users.user_id, users.name, users.salt, users.hash, workers.admin_id
                FROM users
                JOIN workers ON users.user_id = workers.worker_id
                WHERE workers.admin_id = ?
            ''', (admin_id,))

        return [Worker(*worker) for worker in workers_data]

    @staticmethod
    def add_worker(worker: Worker):
        ...
