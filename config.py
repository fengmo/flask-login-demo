# coding: utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or '$1$oX3Y3KOw$oUpYYi6gxebUmLI.329O8/'
    WTF_CSRF_SECRET_KEY = '$1$oX3Y3KOw$oUpYYi6gxebUmLI.329O8/'
	
    @staticmethod
    def init_app(app):
	    pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = ''
    MAIL_PORT = 25
    #MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'dev.db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')

config =  {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig 
}	
