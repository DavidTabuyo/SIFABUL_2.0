from contextlib import contextmanager
import sqlite3


@contextmanager
def db_connection_service():
    try:
        connection = sqlite3.connect('db/db.sqlite')
        yield DBConnection(connection)

    except sqlite3.DataError:
        raise ValueError('Probablemente valor no adecuado')

    finally:
        connection.close()


class DBConnection:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def querry(self, querry: str, args: tuple = ()) -> list[tuple[str, ...]]:
        response = self.connection.execute(querry, args).fetchall()
        self.connection.commit()
        return response


if __name__ == '__main__':
    with db_connection_service() as conn:
        a = conn.querry('''
            CREATE TABLE a (
                id TEXT PRIMARY KEY
            );            
        ''')
        print(a)
        
    with db_connection_service() as conn:
        a = conn.querry('''
            INSERT INTO a (id) VALUES
                (1);
        ''')
        print(a)
