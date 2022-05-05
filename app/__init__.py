"""A simple flask web app"""
import os
from flask import Flask, render_template
from app.cli import create_database
from app.db import db
from app.db.models import User

import flask_login
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from app.auth import auth
from app.cli import create_database, create_log_folder, create_uploads_folder
from app.context_processors import utility_text_processors
from app.db import db
from app.db.models import User
from app.error_handlers import error_handlers
from app.logging_config import log_con
from app.simple_pages import simple_pages
from app.banking import banking, upload

login_manager = flask_login.LoginManager()

def page_not_found(e):
    return render_template("404.html"), 404

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'

    if app.config["ENV"] == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("app.config.TestingConfig")

    app.register_error_handler(404, page_not_found)
    db_dir = "database/db.sqlite"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # https://flask-login.readthedocs.io/en/latest/  <-login manager
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    # Needed for CSRF protection of form submissions and WTF Forms
    # https://wtforms.readthedocs.io/en/3.0.x/
    csrf = CSRFProtect(app)
    # https://bootstrap-flask.readthedocs.io/en/stable/
    bootstrap = Bootstrap5(app)
    # these load functions with web interface
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    app.register_blueprint(banking)
    app.register_blueprint(upload)


    # these load functionality without a web interface
    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)
    app.context_processor(utility_text_processors)


    # add command function to cli commands
    app.cli.add_command(create_database)
    app.cli.add_command(create_log_folder)
    app.cli.add_command(create_uploads_folder)
    db.init_app(app)


    return app

@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None

  #  @app.route('/')
   # def hello():
    #    return 'Hello, World!'

  #  return app