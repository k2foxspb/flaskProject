import os


class ProductionConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg123456"


class DevConfig(ProductionConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(ProductionConfig):
    TESTING = True
