# env/usr/bin python

""" Necessary Imports """
from .utils.utils import *
from flask import Blueprint, render_template, Response
from flask_login import login_required, current_user

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


@main.route("/video_feed", methods=["POST"])
def video_feed():

    """Get the name and reg_id of the student to
    collect his data for training the face recognizer"""
    student_name = request.form.get("student_name")
    reg_id = request.form.get("reg_id")

    return Response(
        capture_data(name=student_name, reg_id=reg_id, src=1),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )
