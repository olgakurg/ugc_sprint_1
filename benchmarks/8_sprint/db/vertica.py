import vertica_python

from db.store import BaseStorage


class Vertica(BaseStorage):

    def __init__(self, host, port, user, password, database):
        self.connetcion_settings = {
            'host': host,
            'port': port,
            'user': user,
            'password': '',
            'database': database,
            'autocommit': True,

        }

    def write(self, data: list, table: str, column: list) -> bool | None:
        if not data:
            return

        values = ','.join(['%s'] * len(column))

        with vertica_python.connect(**self.connetcion_settings) as connection:
            cursor = connection.cursor()

            query = (
                f'INSERT INTO {table}'
                f'({",".join(column)}) '
                f'VALUES ({values})'
            )

            cursor.executemany(query, data)

    def read(self, table: str, limit: int) -> list:
        with vertica_python.connect(**self.connetcion_settings) as connection:
            cursor = connection.cursor()

            query = f'SELECT * FROM {table} LIMIT {limit};'

            res = cursor.execute(query)

            return res.fetchall()
