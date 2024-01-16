from model.worker import Worker
from services.db_connection_service import db_connection_service


class AdminDao:

    @staticmethod
    def add_worker(worker: Worker, admin_id: str):
        with db_connection_service() as conn:
            conn.querry('''
                INSERT INTO users (user_id, name, salt, hash)
                 VALUES (?, ?, ?, ?)
             ''', (worker.worker_id, worker.name, worker.salt, worker.hash))

            conn.querry('''
                INSERT INTO workers (worker_id, admin_id)
                    VALUES (?, ?)
                ''', (worker.worker_id, admin_id))
    
    @staticmethod
    def is_admin(user_id: str) -> bool:
        with db_connection_service() as conn:
            admin = conn.querry('''
                SELECT admin_id
                FROM admins
                WHERE admin_id = ?
            ''', (user_id,))
        return admin != []
