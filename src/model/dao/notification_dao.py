from services.db_connection_service import db_connection_service


class NotificationDao:
    
    @staticmethod
    def addNotification(title: str, description: str, datetime: str):
        with db_connection_service() as conn:
            conn.querry('''
                INSERT INTO notifications (title, description, datetime) VALUES
                    (?, ?, ?);
            ''', (title, description, datetime))