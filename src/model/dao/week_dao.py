from services.db_connection_service import db_connection_service


class WeekDao:

    @staticmethod
    def update_or_create_week(worker_id: str, monday: str, total: int):
        with db_connection_service() as conn:
            conn.querry('''
                INSERT OR REPLACE INTO weeks (worker_id, monday, total) VALUES
                    (?, ?, ?);
            ''', (worker_id, monday, total))
