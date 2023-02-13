import psycopg2

from constants import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USERNAME, POSTGRES_PASSWORD
from dao.sql_queries import CREATE_SHORTER_TABLE_IF_NOT_EXISTS


class ShorterDAO:
    def __init__(self):
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            user=POSTGRES_USERNAME,
            password=POSTGRES_PASSWORD,
        )
        cur = conn.cursor()
        cur.execute(CREATE_SHORTER_TABLE_IF_NOT_EXISTS)
        conn.commit()

    def update_map(self, old_map):
        ...

    def add_url_to_db(self, old_map):
        ...
