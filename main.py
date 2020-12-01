# env/usr/bin python

""" Necessary Imports """
from flask import Blueprint, render_template
from flak_login import login_required, current_user

""" Initialize blueprint """
main = Blueprint("main", __name__)

""" Index route """


@main.route("/")
def index():

    """ Render the index webpage """
    return render_template("index.html")


""" User profile webpages """


@main.route("/profile")
def profile():

    """ Returns profile webpage for the current user """
    return render_template("profile.html", name=current_user.name)
