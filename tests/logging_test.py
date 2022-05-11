import os

root = os.path.dirname(os.path.abspath(__file__))

#tests for errors, handlers, myapp, request, sqalchemy, uploads, wekzerg log

from pathlib import Path
import os

root = os.path.dirname(os.path.abspath(__file__))

def test_errorLog():
    errorLog = os.path.join(root, '../logs/errors.log')
    assert os.path.exists(errorLog) == True


def test_myappLog():
    myappLog = os.path.join(root, '../logs/myapp.log')
    assert os.path.exists(myappLog) == True

def test_requestLog():
    requestLog = os.path.join(root, '../logs/request.log')
    assert os.path.exists(requestLog) == True

def test_sqlalchemyLog():
    sqlalchemyLog = os.path.join(root, '../logs/sqlalchemy.log')
    assert os.path.exists(sqlalchemyLog) == True

def test_werkzeugLog():
    werkzeugLog = os.path.join(root, '../logs/werkzeug.log')
    assert os.path.exists(werkzeugLog) == True

def test_upload_csvLog():
    root = os.path.dirname(os.path.abspath(__file__))
    myappLog = os.path.join(root, '../logs/csv.log')
    if not os.path.exists(myappLog):
        os.mknod(myappLog)
    assert os.path.exists(myappLog) == True

