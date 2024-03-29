from services.db_connection_service import db_connection_service


class NotificationWorkerDao:


    @staticmethod
    def add_notification_worker(worker_id: str, notification_id: str, seen: str):
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
