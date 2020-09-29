import configparser
from oauth2client.service_account import ServiceAccountCredentials
import os
# from app.common.function import is_local
import json
import socket

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# if is_local():
if socket.gethostname()[:7] == "DESKTOP":

    config = configparser.ConfigParser()
    config.read('config.ini')

    pg_db_username = config['DEFAULT']['LOCAL_DB_USERNAME']
    pg_db_password = config['DEFAULT']['LOCAL_DB_PASSWORD']
    pg_db_name = config['DEFAULT']['LOCAL_DB_NAME']
    pg_db_hostname = config['DEFAULT']['LOCAL_DB_HOSTNAME']

    SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER=pg_db_username,
        DB_PASS=pg_db_password,
        DB_ADDR=pg_db_hostname,
        DB_NAME=pg_db_name)

    SECRET_KEY = config['DEFAULT']['SECRET_KEY']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(config['DEFAULT']['GOOGLE_CREDENTIALS_PATH'], scope)
    YOUTUBE_KEY = config["DEFAULT"]["YOUTUBE_KEY"]

else:

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
    SECRET_KEY = os.environ.get('SECRET_KEY', None)
    print(os.environ.get('GOOGLE_CREDENTIALS', None))
    print(json.loads(os.environ.get('GOOGLE_CREDENTIALS', None)))
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        json.loads(os.environ.get('GOOGLE_CREDENTIALS', None)), scope)

    YOUTUBE_KEY = os.environ.get("YOUTUBE_KEY", None)