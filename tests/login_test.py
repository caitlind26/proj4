from flask_login import login_user, login_required, logout_user, current_user
from flask_wtf import form


from app.db.models import User
from app import auth, db
from flask import flash
from app.auth.decorators import admin_required
from app.auth.forms import login_form, register_form, profile_form, security_form, user_edit_form


def login_test(client):
    "Tests that the user is successfully logged in"
    response = client.get('/login')
    user = User("cd394@njit.edu", "testtesttesting")
    db.session.add(user)
    db.session.commit()

    assert user.authenticated == True
    assert "Congratulations, you just created a user" in response.data


def unsuccessful_login_test():
    "Tests that the user cannot log in"
    user = User.query.filter_by(email=form.email.data).first()
    if user is None:
        assert user.authenticated == False



