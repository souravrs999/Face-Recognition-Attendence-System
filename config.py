#! env/usr/bin python

""" Necessary Imports """
import os
from decouple import config


class Config(object):

    """ Get the base dir of the app """

    basedir = os.path.abspath(os.path.dirname(__file__))

    """ SecretKey needed for SQLAlchemy """
    SECRET_KEY = config("SECRET_KEY", default="makesomethingup")

    """ Will create the database file in the same directory """
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite3")
    """ Need this or alchemy will keep yelling at us """
    SQLALCHEMY_TRACK_MODIFICATION = False


class ProductionConfig(Config):

    """ Runs in DEBUG=False mode use it in production """

    DEBUG = False

    """ Makes it unable to be accessible by the javascript. This
    makes XSS attacks harder to perform"""
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    """ PostgreSQL database """
    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(
        config("DB_ENGINE", default="postgresql"),
        config("DB_USERNAME", default="sourav"),
        config("DB_PASS", default="password"),
        config("DB_HOST", default="localhost"),
        config("DB_PORT", default="6000"),
        config("DB_NAME", default="FaceAttend"),
    )


class DebugConfig(Config):

    """ Runs in DEBUG mode dont use this in production """

    DEBUG = True


""" Create a dictionary of both the configurations """
config_dict = {"Production": ProductionConfig, "Debug": DebugConfig}
