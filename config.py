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
	
class SendMail():
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASK_MAIL_SUBJECT_PREFIX = '[Lunaticvi]'
    FLASK_MAIL_SENDER = MAIL_USERNAME

class DevelopmentConfig(Config, SendMail):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'dev.db')

class TestingConfig(Config, SendMail):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db')

class ProductionConfig(Config, SendMail):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')

config =  {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig 
}	
