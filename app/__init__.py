# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()
lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    lm.init_app(app)

    from main import main
    app.register_blueprint(main)

    from auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
