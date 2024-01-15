import sqlite3
from model.check import Check
from model.notification_worker import NotificationWorker
from model.week import Week
from model.worker import Worker
from services.db_connection_service import db_connection_service


class WorkerDao:
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
    


