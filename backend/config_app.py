import os

_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
_POSTGRES_DB = os.environ.get("DATABASE_URL", "")


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    SQLALCHEMY_DATABASE_URI = _POSTGRES_DB


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = "my_precious"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
