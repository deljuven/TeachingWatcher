# -*- coding: utf-8 -*-
from flask import flash, session
from flask_login import login_user, logout_user, LoginManager

from database import db
from models import User


login_manager = LoginManager()


def signin(username, passwd):
    user = User.query.filter_by(name=username, password=passwd).first()
    if user is None:
        session.pop('_flashes', None)
        flash("Incorrect username or password")
        return False
    login_user(user)
    session['logged_in'] = True
    return True


def signout():
    logout_user()
    session.pop('logged_in', None)


def signup(username, passwd, email):
    user = User(username, passwd, email)
    db.session.add(user)
    db.session.flush()
    db.session.commit()
    login_user(user)


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
