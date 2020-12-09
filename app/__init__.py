#! /env/usr/bin python

""" Necessary Imports """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

""" Initialize sqlalchemy """
db = SQLAlchemy()

""" Create the database """


def configure_database(app):
    @app.before_first_request
    def initialize_database():

        db.create_all()


""" Create app function """


def create_app(config):

    app = Flask(__name__)

    app.config.from_object("config.DebugConfig")

    db.init_app(app)

    """ Initialize flak login """
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    """ Import our user model """
    from .models import User

    """ Returns the current user_id """

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))

    """ Import our blueprints """
    from .auth import auth
    from .main import main
    from .error import error

    """ Register these blue prints """
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(error)

    configure_database(app)

    return app
