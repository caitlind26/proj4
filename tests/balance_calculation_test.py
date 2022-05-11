from app import db
from app.db.models import User, Bank
from flask_login import FlaskLoginClient
from app.auth.forms import *

def test_account_balance(application):
    application.test_client_class = FlaskLoginClient
    user = User('cd394@njit.edu', 'testtesttesting')
    db.session.add(user)
    db.session.commit()
    assert user.email == 'cd394@njit.edu'
    assert user.balance == 0.00
    user.balance += 500
    assert user.balance == 500

