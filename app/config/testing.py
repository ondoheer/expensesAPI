import os

TESTING = True
# this way we see when it raises an error
POSTGRES_URL = os.environ.get(
    'POSTGRES_URL', 'postgresql://spendy:spendy@postgres:5432/')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
SQLALCHEMY_DATABASE_URI = POSTGRES_URL + DATABASE_NAME
BCRYPT_LOG_ROUNDS = 4
