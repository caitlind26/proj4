from app import db
from app.db.models import User
from app.auth.forms import *
from flask_login import FlaskLoginClient


def login_test(application, client):
    "Tests that the user is successfully logged in"
    form = login_form
    form.email.data = "cd394@njit.edu"
    form.password.data = "testtesttesting"
    assert form.validate()


def unsuccessful_login_test(application, client):
    "Tests that the user cannot log in"
    form = login_form()
    form.email.data = "cd394@njit.edu"
    form.password.data = ""
    assert not form.validate()



