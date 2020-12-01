#! /env/usr/bin python

""" Necessary Imports """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Flask_login import LoginManager

""" Initialize sqlalchemy """
db = SQLAlchemy()

""" Create app function """


def create_app():

    app = Flask(__name__)

    """ Set sqlalchemy configurations """
    app.config["SECRET_KEY"] = "justatempsecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    db.init_app(app)

    """ Initialize flak login """
    login_manager = Loginmanager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    """ Import our user model """
    from .models import User

    """ Returns the current user_id """

    @login_manager.user_loader
    def load_user(reg_id):

        return User.query.get(str(reg_id))

    """ Import our blueprints """
    from .auth import auth
    from .main import main

    """ Register these blue prints """
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
