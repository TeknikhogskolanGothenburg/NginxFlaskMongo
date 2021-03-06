from os import environ
from os.path import realpath, dirname, join

SECRET_KEY = environ.get("SECRET_KEY")

DB_NAME = environ.get("DB_NAME")
DB_USER = environ.get("DB_USER")
DB_PASSWORD = environ.get("DB_PASSWORD")
DB_HOST = environ.get("DB_HOST")
DB_PORT = environ.get("DB_PORT")

AVATAR_FOLDER_BASE = join(dirname(realpath(__file__)))
AVATAR_FOLDER = environ.get("AVATAR_FOLDER")
MAX_CONTENT_LENGTH = int(environ.get("MAX_CONTENT_LENGTH"))
