from model.admin import Admin
from model.check import Check
from model.notification import Notification
from model.notification_worker import NotificationWorker
from model.user import User
from model.week import Week
from model.worker import Worker
from services.db_connection_service import db_connection_service


class FactoryDao:
    @staticmethod
    def get_worker(worker_id: str) -> Worker:
        with db_connection_service() as conn:
            worker = conn.querry('''
                SELECT users.user_id, users.name, users.salt, users.hash, workers.admin_id
                FROM users
                JOIN workers on users.user_id = workers.worker_id
                WHERE user_id = ?
            ''', (worker_id,))
        return Worker(*worker[0]) if worker else None

    @staticmethod
    def get_weeks(worker_id: str) -> list[Week]:
        with db_connection_service() as conn:
            weeks = conn.querry('''
                SELECT worker_id, monday, total
                FROM weeks
                WHERE worker_id = ?
            ''', (worker_id,))
        return [Week(*week) for week in weeks]

    @staticmethod
    def get_week(worker_id: str, monday: str) -> Week:
        with db_connection_service() as conn:
            week = conn.querry('''
                SELECT worker_id, monday, total
                FROM weeks
                WHERE worker_id = ? and monday = ?
            ''', (worker_id, monday))
        return Week(*week[0]) if week else None

    @staticmethod
    def get_user(user_id: str) -> User:
        with db_connection_service() as conn:
            user = conn.querry('''
                SELECT user_id, name, salt, hash
                FROM users
                WHERE user_id = ?
            ''', (user_id,))
        return User(*user[0]) if user else None

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
    def get_admin(admin_id: str) -> Admin:
        with db_connection_service() as conn:
            admins = conn.querry('''
                    SELECT user_id, name, salt, hash
                    FROM users
                    WHERE user_id = ?
                ''', (admin_id,))

        return Admin(*admins[0]) if admins else None

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
    def get_notifications_by_worker(worker_id: str) -> list[NotificationWorker]:
        with db_connection_service() as conn:
            notifications = conn.querry('''
                SELECT notifications.notification_id, workers_notifications.worker_id, notifications.title, notifications.description, notifications.datetime, workers_notifications.seen
                FROM notifications
                JOIN workers_notifications on notifications.notification_id = workers_notifications.notification_id
                WHERE workers_notifications.worker_id = ?
                ORDER BY notifications.datetime DESC
            ''', (worker_id,))
        return [NotificationWorker(*notification) for notification in notifications]
    @staticmethod
    def get_notifications_by_notification(notification_id: int) -> list[NotificationWorker]:
        with db_connection_service() as conn:
            notifications = conn.querry('''
                SELECT notifications.notification_id, workers_notifications.worker_id, notifications.title, notifications.description, notifications.datetime, workers_notifications.seen
                FROM notifications
                JOIN workers_notifications on notifications.notification_id = workers_notifications.notification_id
                WHERE workers_notifications.notification_id = ?
                ORDER BY notifications.datetime DESC
            ''', (notification_id,))
        return [NotificationWorker(*notification) for notification in notifications]
    
    @staticmethod
    def get_today_checks(worker_id: str, date: str) -> list[Check]:
        with db_connection_service() as conn:
            today_checks = conn.querry('''
                SELECT worker_id, date, time, is_entry
                FROM checks
                WHERE worker_id = ? and date = ?
                ORDER BY time
            ''', (worker_id, date))
        return [Check(*check) for check in today_checks]

    @staticmethod
    def get_last_today_check(worker_id: str, date: str) -> Check:
        with db_connection_service() as conn:
            last_check = conn.querry('''
                SELECT worker_id, date, time, is_entry
                FROM checks
                WHERE worker_id = ? and date = ?
                ORDER BY time DESC
            ''', (worker_id, date))
        return Check(*last_check[0]) if last_check else None
    
    
