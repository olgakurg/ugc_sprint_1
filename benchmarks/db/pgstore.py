from contextlib import contextmanager

import psycopg2
from psycopg2.extensions import connection as pg_connection
from psycopg2.extras import DictCursor

from db.store import BaseStorage


class Postgres(BaseStorage):

    def __init__(self, host, port, db_name, user, password):

        self.dsl = {
            'dbname': db_name,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }

    def write(
            self, table: str, column: list, data: tuple
    ) -> None:

        column = ", ".join(column)
        conn = psycopg2.connect(**self.dsl, cursor_factory=DictCursor)

        with conn:
            with conn.cursor() as cursor:

                query = (
                    f'INSERT INTO public.{table} ({column}) '
                    f'VALUES %s ON CONFLICT (id) DO NOTHING'
                )

                psycopg2.extras.execute_values(cursor, query, data)

    def read(self, table: str, limit) -> list:

        with psycopg2.connect(**self.dsl) as conn:
            with conn.cursor() as cursor:
                query = f'SELECT * FROM public.{table} LIMIT {limit}'
                cursor.execute(query)

                data = cursor.fetchall()

        return data

    @contextmanager
    def pg_context(self) -> pg_connection:
        try:
            conn = psycopg2.connect(**self.dsl, cursor_factory=DictCursor)
            yield conn
            conn.close()
        except psycopg2.OperationalError as e:
            print(f'Unable to connect because {e}')
