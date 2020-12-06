#! /env/usr/bin python

""" Necessary Imports """
import sys
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

""" Initialize Blueprint """
auth = Blueprint("auth", __name__)

""" Login route handles GET method """


@auth.route("/login")
def login():

    return render_template("login.html")


""" Login route handles POST method """


@auth.route("/login", methods=["POST"])
def login_post():

    """ Get register id and password """
    reg_id = request.form.get("reg_id")
    password = request.form.get("password")

    """ Check if the remember me button is checked """
    remember = True if request.form.get("remember") else False

    """ Grab the user with the reg_id from the user table """
    user = User.query.filter_by(reg_id=reg_id).first()

    """ If the user is present and the password is not wrong
    redirect the user to the profile page """
    if user:
        if check_password_hash(user.password, password):

            """ If the credentials are correct login the user """
            login_user(user, remember=remember)

            """ If everything checks out redirect to dashboard """
            flash("Login Successful")
            return redirect(url_for("main.profile"))

    """ Flash the error message """
    flash(" Invalid Credentials !!!")
    return redirect(url_for("auth.login"))


""" Signup route handles GET method """


@auth.route("/signup")
def signup():

    return render_template("signup.html")


""" Signup route handles the POST method """


@auth.route("/signup", methods=["POST"])
def signup_post():

    """ Get all the necessary credentials from the fields """
    reg_id = request.form.get("reg_id")
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    conf_password = request.form.get("conf_password")

    """ Check to see if both the passwords are correct """
    if password != conf_password:

        """ Flash passwords are not same """
        flash("Passwords do not match !")
        return redirect(url_for(signup.html))

    """ Get the user with this reg_id from the user table """
    user = User.query.filter_by(reg_id=reg_id).first()

    """ If the user with reg_id already exist warn them """
    if user:

        """ Flash warning message and redirect """
        flash("User with this reg_id already exists !")
        return redirect(url_for("auth.signup"))

    """ During the first run of the app check for users with admin roles
    if no users are persent then the first user that signup after
    the app launch will be the admin user """

    admin_user = User.query.filter_by(role=int(2)).first()
    # print(admin_user, file=sys.stderr)

    """ At first run since the database does not contain any
    user with admin rights this will return None """

    if admin_user == None:

        """ Add this user to the database with admin role """
        new_user = User(
            reg_id=reg_id,
            name=name,
            email=email,
            password=generate_password_hash(password, method="sha256"),
            role=int(2),
        )

    else:
        """ Add this user to the database with user role """
        new_user = User(
            reg_id=reg_id,
            name=name,
            email=email,
            password=generate_password_hash(password, method="sha256"),
        )

    """ Add this user to table and commit changes then redirect to login"""
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


""" Logout route """


@auth.route("/logout")
@login_required
def logout():

    """ Logout the user and return to index page """
    logout_user()
    return redirect(url_for("main.index"))
