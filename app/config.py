import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")
SQLALCHEMY_TRACK_MODIFICATIONS = False

class BaseConfig:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "asdf"

class ProductionConfig(BaseConfig):
    DEBUG = False

class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True
