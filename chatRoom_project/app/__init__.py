from flask import Flask, session
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from datetime import timedelta


bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('config')
    bootstrap.init_app(app)
    # moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    app.permanent_session_lifetime = timedelta(hours=24)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
