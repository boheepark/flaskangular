import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.db")
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")
# SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    SECRET_KEY = "asdf"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/test_db"

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]

app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}
