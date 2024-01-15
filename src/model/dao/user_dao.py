from model.user import User
from services.db_connection_service import db_connection_service


class UserDao:
    @staticmethod
    def is_worker(user_id: str) -> bool:
        with db_connection_service() as conn:
            worker = conn.querry('''
                SELECT worker_id
                FROM workers
                WHERE worker_id = ?
            ''', (user_id,))
        return worker != []

    @staticmethod
    def is_admin(user_id: str) -> bool:
        with db_connection_service() as conn:
            admin = conn.querry('''
                SELECT admin_id
                FROM admins
                WHERE admin_id = ?
            ''', (user_id,))
        return admin != []
        
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
    def update(user: User):
        with db_connection_service() as conn:
            conn.querry('''
                UPDATE users
                SET name = ?, salt = ?, hash = ?
                WHERE user_id = ? 
            ''', (user.name, user.salt, user.hash, user.user_id))
        
    @staticmethod
    def delete_user(user_id: str):
        with db_connection_service() as conn:
            conn.querry('''
                PRAGMA foreign_keys = ON
            ''')
            conn.querry('''
                DELETE FROM users
                WHERE user_id = ?
            ''', (user_id,))