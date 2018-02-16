# project general config objects

import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://ondoheer:@localhost/'
database_name = 'expenses'

testing_database_name = 'expenses_testing'


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
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=10)# False


class ProductionConfig(BaseConfig):
    """Production configuration"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name
    BCRYPT_LOG_ROUNDS = 4
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1) # let it last for a day?


class TestingConfig(BaseConfig):
    """Production configuration"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + testing_database_name
    BCRYPT_LOG_ROUNDS = 4


