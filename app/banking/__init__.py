import csv
import logging
from app.logging_config import configure_csv_logging
import os

from flask import Flask, Blueprint, render_template, abort, url_for,current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from app.db import db
from app.db.models import Bank
from app.banking.forms import upload_csv_file
from werkzeug.utils import secure_filename, redirect

banking = Blueprint('banking', __name__,
                        template_folder='templates')

upload = Blueprint('upload', __name__, template_folder = 'templates')

UPLOAD_FOLDER = '/app/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER']  = UPLOAD_FOLDER

@banking.route('/banking', methods=['GET'], defaults={"page": 1})
@banking.route('/banking/<int:page>', methods=['GET'])
@login.required
def transactions_browse(page):
    page = page
    per_page = 1000
    pagination = Bank.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('transactions_browse.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)


@banking.route('/banking/upload', methods=['POST', 'GET'])
@login_required
def transactions_upload():
    form = upload_csv_file()
    if form.validate_on_submit():
        log = logging.getLogger("csv")
        user = current_user.email
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        configure_csv_logging()
        logging.info('User: ' + user + ', File Name: ' + filename + ', File Path: ' + filepath)
        current_user.balance = 0.00
        list_of_transactions = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_transactions.append(Bank(row.get("\ufeffAMOUNT"), row.get("TYPE")))
                current_user.balance += float(row.get("\ufeffAMOUNT"))

        current_user.banking = list_of_transactions
        db.session.commit()

        return redirect(url_for('banking.transactions_browse'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)
