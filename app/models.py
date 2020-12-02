#!/usr/bin/env python

"""Necessary Imports"""
from flask_login import UserMixin
from . import db

""" Set some roles for the users so we can control the flow """
user_roles = {"user": 0, "moderator": 1, "admin": 2}


class User(UserMixin, db.Model):

    """User database with admin user capable of vieweing
    certain topics

    :param int reg_id: registration id of the student
    :param string name: name of the student
    :param string email: email of the student
    :param string password: passoword for the student
    :param boolean authenticated: if user authenticated or not

    """

    reg_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    role = db.Column(db.Integer, nullable=False, default=user_roles["user"])

    """ Overriding the get_id method or this will cause an error """

    def get_id(self):

        return self.reg_id

    """ Function to return the User role """

    def get_role(self):

        return self.role

class Register(db.Model):

    ''' Create a table to store the attendence register for the students

    :param int id: unique id for the register
    :param int date: date of the recorded attendence '''

    id = db.Column(db.Integer, primary_key=True)

