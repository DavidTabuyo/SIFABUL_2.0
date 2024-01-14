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
    def delete_User(user_id:str):
        try:
            print("elimina a " +user_id)
            with db_connection_service() as conn:
                # Eliminar de la tabla 'workers'
                conn.querry('''
                    DELETE FROM workers
                    WHERE worker_id = ?
                ''', (user_id,))

                # Eliminar de la tabla 'admins'
                conn.querry('''
                    DELETE FROM admins
                    WHERE admin_id = ?
                ''', (user_id,))

                # Eliminar de la tabla 'users'
                conn.querry('''
                    DELETE FROM users
                    WHERE user_id = ?
                ''', (user_id,))

                # Eliminar de la tabla 'workers_notifications'
                conn.querry('''
                    DELETE FROM workers_notifications
                    WHERE worker_id = ?
                ''', (user_id,))

                # Eliminar de la tabla 'checks'
                conn.querry('''
                    DELETE FROM checks
                    WHERE worker_id = ?
                ''', (user_id,))

                # Eliminar de la tabla 'weeks'
                conn.querry('''
                    DELETE FROM weeks
                    WHERE worker_id = ?
                ''', (user_id,))

        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")
        
