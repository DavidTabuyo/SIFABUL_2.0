import sqlite3
from model.admin import Admin
from model.notification import Notification
from model.worker import Worker


class AdminDao:
    @staticmethod
    def get_admin(admin_id: str) -> Admin:
        connection = sqlite3.connect('db/db.sqlite')
        admin = connection.execute('''
            SELECT user_id, name, salt, hash
            FROM users
            WHERE user_id = ?
        ''', (admin_id,)).fetchone()
        connection.close()
        return Admin(*admin) if admin else None
    
    @staticmethod
    def get_notifications(admin_id: str) -> list[Notification]:
        connection = sqlite3.connect('db/db.sqlite')
        cursor = connection.cursor()
        notifications_data = cursor.execute('''
            SELECT notifications.notification_id, notifications.title, notifications.description, notifications.datetime
            FROM notifications
            JOIN workers_notifications ON notifications.notification_id = workers_notifications.notification_id
            JOIN workers ON workers_notifications.worker_id = workers.worker_id
            WHERE workers.admin_id = ?
        ''', (admin_id,)).fetchall()
        connection.close()
        return [Notification(*notification) for notification in notifications_data]


    @staticmethod
    def get_workers(admin_id: str) -> list[Worker]:
        # Devuelve una lista con los workers
        connection = sqlite3.connect('db/db.sqlite')
        workers_data = connection.execute('''
            SELECT users.user_id, users.name, users.salt, users.hash, workers.admin_id
            FROM users
            JOIN workers ON users.user_id = workers.worker_id
            WHERE workers.admin_id = ?
        ''', (admin_id,)).fetchall()
        connection.close()
        return [Worker(*worker) for worker in workers_data]
