#! env/usr/bin python

""" Necessary Imports """
from os import environ
from sys import exit
from decouple import config

from config import config_dict
from app import create_app, db

""" Do not run using DEBUG mode in production """
DEBUG = config("DEBUG", default=True)

""" Grab the configuration and set it """
get_config_mode = "Debug" if DEBUG else "Production"

""" Try except block to catch any other config mode other
then Debug and Production """
try:

    """ Load configuration usind default values """
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit("Error invalid <config_mode>. Expected values [Debug, Production]")

""" Create app with all these configurations """
app = create_app(app_config)


if __name__ == "__main__":

    app.run(threaded=True)
