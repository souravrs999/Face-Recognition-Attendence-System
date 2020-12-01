#!/usr/bin/env python

"""Necessary Imports"""
from flask import UserMixin
from . import db


class User(UserMixin, db.Model):

    """User database with admin user capable of vieweing
    certain topics

    :param int reg_id: registration id of the student
    :param string name: name of the student
    :param string email: email of the student
    :param string password: passoword for the student
    :param boolean authenticated: if user authenticated or not

    """

    reg_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
