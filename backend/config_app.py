""" Configuration File """
import os

_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
_POSTGRES_DB = os.environ.get("DATABASE_URL", "")


class Config(object):
    """Main Configuration Class"""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    SQLALCHEMY_DATABASE_URI = _POSTGRES_DB
    BCRYPT_LOG_ROUNDS = 13


class ProductionConfig(Config):
    """Contains Production Configurations"""

    DEBUG = False
    SECRET_KEY = "my_precious"


class StagingConfig(Config):
    """Contains Staging Configurations"""

    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """Contains Development Configurations"""

    DEVELOPMENT = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(Config):
    """Contains Testing Configurations"""

    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
