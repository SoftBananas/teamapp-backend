import os

from dotenv import load_dotenv

load_dotenv(".env-dev")

DB_DRIVER = os.environ.get("DB_DRIVER")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

ORIGINS = ["*"]
