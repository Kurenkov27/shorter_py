import psycopg2

from constants import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DB_NAME
from dao.sql_queries import CREATE_SHORTER_TABLE_IF_NOT_EXISTS, INSERT_SHORT_URL, GET_UNEXPIRED_SHORT_URLS


class ShorterDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=POSTGRES_DB_NAME,
            user=POSTGRES_USERNAME,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
        )
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.cur.execute(CREATE_SHORTER_TABLE_IF_NOT_EXISTS)

    def update_map(self, old_map):
        self.cur.execute(GET_UNEXPIRED_SHORT_URLS)
        for db_record in self.cur.fetchall():
            old_map[db_record[0]] = (db_record[1], db_record[2])

    def add_url_to_db(self, short_url, original_url, expiration_date):
        self.cur.execute(INSERT_SHORT_URL, (short_url, original_url, expiration_date))
