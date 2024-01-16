from model.user import User
from services.db_connection_service import db_connection_service


class UserDao:

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
