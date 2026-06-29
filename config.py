import os

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL',
        'postgresql+psycopg2://postgres:Passer123@localhost:5432/blog_app_groupe1')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI= os.getenv('TEST_DATABASE_URL',
        'postgresql+psycopg2://postgres:Passer123@localhost:5432/blog_app_groupe1_test')


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
        '')



config_by_name = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig
}