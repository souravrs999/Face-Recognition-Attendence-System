#! env/usr/bin python

""" Necessary Imports """
from flask import Blueprint, render_template

""" Initialize the Blueprint """
error = Blueprint("error", __name__)

""" 400 bad request error """


@error.app_errorhandler(400)
def bad_req_error():

    return render_template("400.html"), 400


""" 403 forbidden error """


@error.app_errorhandler(403)
def forbidden_error():

    return render_template("403.html"), 403


""" 404 not found error """


@error.app_errorhandler(404)
def not_found_error():

    return render_template("404.html"), 404


""" 429 too many request error """


@error.app_errorhandler(429)
def too_many_req_error():

    return render_template("429.html"), 429


""" 500 internal server error """


@error.app_errorhandler(500)
def int_server_error():

    return render_template("500.html"), 500


""" 502 bad gateway error """


@error.app_errorhandler(502)
def bad_gate_error():

    return render_template("502.html"), 502


""" 503 service unavailable error """


@error.app_errorhandler(503)
def service_uanavailable_error():

    return render_template("503.html"), 503


""" 504 gateway error """


@error.app_errorhandler(504)
def gate_error():

    return render_template("504.html"), 504
