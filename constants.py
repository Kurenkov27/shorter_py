import os
from dotenv import load_dotenv

load_dotenv()


POSTGRES_HOST = os.getenv('POSTGRES_HOST', '')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)
POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME', '')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
POSTGRES_DB_NAME = os.getenv('POSTGRES_DB_NAME', '')
