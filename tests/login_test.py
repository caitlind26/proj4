from app import db
from app.db.models import User
from app.auth.forms import *
from flask_login import FlaskLoginClient
from app import auth


def test_login(application, client):
    """Tests that the user is successfully logged in"""
    form_user = login_form
    form_user.email.data = "cd394@njit.edu"
    form_user.password.data = "testtesttesting"
    assert form_user.validate


def test_dashboard_authorized_access(application, client, add_user):
    """ Tests user access dashboard when authorized """
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)
    assert db.session.query(User).count() == 1
    assert user.email == 'keith@webizly.com'
    with application.test_client(user=user) as client:
        response = client.get('/dashboard')
        assert b'keith@webizly' in response.data
        assert response.status_code == 200

def test_dashboard_denied(application, client):
    """ Tests denying access to dashboard"""
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0
    with application.test_client(user=None) as client:
        response = client.get('/dashboard')
        assert response.status_code != 200
        assert response.status_code == 302


def test_csv_upload_success(application, client, add_user):
    """ Test to verify that the CSV file is uploaded and processed """
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)
    assert db.session.query(User).count() == 1
    assert user.email == 'keith@webizly.com'
    with application.test_client(user=user) as client:
        response = client.get('/banking/upload')
        assert response.status_code == 200

