"Tests the user table"

import logging
from app import db
from app.db.models import User, Bank

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count == 0
        assert db.session.query(Bank).count == 0

        user = User('cd394@njit.edu', 'testtesttesting')
        db.session.add(user)
        user = User.query.filter_by(email ='cd394@njit.edu').first()
        log.info(user)

        assert user.email == 'cd394@njit.edu'

        user.banking = [Bank(-420, 'DEBIT'), Bank(840, 'CREDIT')]
        db.session.commit()

        assert db.session.query(Bank).count == 2
        trans1 = Bank.query.filter_by(AMOUNT=-420).first()
        assert trans1.AMOUNT == -420

