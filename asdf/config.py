import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.db")
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")
# SQLALCHEMY_TRACK_MODIFICATIONS = False

class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    SECRET_KEY = "asdf"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_TEST_URL"]

class StagingConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}
