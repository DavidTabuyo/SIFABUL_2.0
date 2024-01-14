from services.db_connection_service import db_connection_service


class CheckDao:

    @staticmethod
    def add_new_check(worker_id: str, date: str, time: str, is_entry: bool):
        with db_connection_service() as conn:
            conn.querry('''
                INSERT INTO checks (worker_id, date, time, is_entry) VALUES
                    (?, ?, ?, ?);
            ''', (worker_id, date, time, is_entry))
