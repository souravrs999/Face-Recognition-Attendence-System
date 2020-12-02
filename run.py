#! env/usr/bin python

""" Necessary Imports """
from os import environ
from app import create_app, db

app = create_app()

if __name__ == "__main__":

    app.run()
