#! env/usr/bin python

""" Necessary Imports """
from flask import Blueprint, render_template

""" Initialize the Blueprint """
error = Blueprint("error", __name__)

""" 403 forbidden error """


@error.app_errorhandler(403)
def forbidden_error(error):

    return render_template("page-403.html"), 403


""" 404 not found error """


@error.app_errorhandler(404)
def not_found_error(error):

    return render_template("page-404.html"), 404

""" 500 internal server error """


@error.app_errorhandler(500)
def int_server_error(error):

    return render_template("page-500.html"), 500
