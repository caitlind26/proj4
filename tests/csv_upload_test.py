import csv
import logging
import os

from flask import current_app
from werkzeug.utils import secure_filename

from app import banking
from pathlib import Path
from app.db.models import Bank
from app.banking import upload_csv_file
from app import logging_config
from app.logging_config import configure_csv_logging


def transaction_upload_test():
    form = upload_csv_file()
    if form.validate_on_submit():
        log = logging.getLogger("myApp")
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

        form.file.data.save(filepath)
        assert form.file.data.exists()








