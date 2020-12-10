# env/usr/bin python

""" Necessary Imports """
from .utils.utils import capture_data, train_model
from flask import Blueprint, render_template, Response, request, redirect, url_for
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


@main.route("/stream", methods=["GET", "POST"])
def stream():

    """ return the streaming template """
    return render_template("video-feed.html")


@main.route("/data_capture", methods=["GET", "POST"])
def data_capture():

    """Get the name and reg_id of the student to
    collect his data for training the face recognizer"""
    student_name = request.form.get("student_name")
    reg_id = request.form.get("reg_id")

    """ returns the encoded frame """
    frame_data = capture_data(name=student_name, reg_id=reg_id, src=1)

    return Response(frame_data, mimetype="multipart/x-mixed-replace; boundary=frame")


@main.route("/train_face_model")
def train_face_model():

    train_model()

    return redirect(url_for("main.profile"))


@main.route("/video_feed")
def video_feed():
    pass
