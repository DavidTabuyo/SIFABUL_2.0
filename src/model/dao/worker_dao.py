from services.db_connection_service import db_connection_service


class WorkerDao:
    @staticmethod
    def is_worker(user_id: str) -> bool:
        with db_connection_service() as conn:
            worker = conn.querry('''
                SELECT worker_id
                FROM workers
                WHERE worker_id = ?
            ''', (user_id,))
        return worker != []

