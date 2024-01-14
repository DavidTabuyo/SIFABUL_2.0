from model.week import Week
from services.db_connection_service import db_connection_service

class WeekDao:
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
    def update_or_create_week(worker_id: str, monday: str, total: int):
        with db_connection_service() as conn:
            conn.querry('''
                INSERT OR REPLACE INTO weeks (worker_id, monday, total) VALUES
                    (?, ?, ?);
            ''', (worker_id, monday, total))