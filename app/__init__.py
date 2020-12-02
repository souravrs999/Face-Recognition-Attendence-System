#! /env/usr/bin python

""" Necessary Imports """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .utils.utils import *

""" Declare some variable """
database_dir = "database/"
database_file = "db.sqlite3"

""" Initialize sqlalchemy """
db = SQLAlchemy()

""" Create app function """


def create_app():

    app = Flask(__name__)

    """ Set sqlalchemy configurations """
    app.config["SECRET_KEY"] = "justatempsecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + database_dir + database_file

    """ Sqlalchemy just wouldn't shut up about this """
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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

    """ Register these blue prints """
    app.register_blueprint(auth)
    app.register_blueprint(main)

    """ Create the database """
    if not os.path.exists(os.path.join(database_dir, database_file)):
        mk_dir("database")
        with app.app_context():
            db.create_all()

    return app
