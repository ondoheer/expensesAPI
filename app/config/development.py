import os
import datetime

TESTING = False
DEBUG = True

POSTGRES_URL = os.environ.get(
    'POSTGRES_URL', 'postgresql://spendy:spendy@postgres:5432/')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'spendy')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = POSTGRES_URL + DATABASE_NAME


BCRYPT_LOG_ROUNDS = os.environ.get('BCRYPT_LOG_ROUNDS', 45)

JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(
    seconds=900)
