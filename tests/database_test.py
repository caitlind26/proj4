import os

root = os.path.dirname(os.path.abspath(__file__))

def test_database():
    db = os.path.join(root, '../database/db.sqlite')
    assert os.path.exists(db) == True