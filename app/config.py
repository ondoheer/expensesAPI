# project general config objects

import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://ondoheer:@localhost/'
database_name = 'simple_expense'


class BaseConfig(object):
    """ Base configuration"""

    SECRET_KEY = os.environ.get("SECRET_KEY", "mellon")
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY", "mellon")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 45

class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name
    BCRYPT_LOG_ROUNDS = 4
