import os

from click.testing import CliRunner
from pathlib import Path
from app import create_log_folder, create_database

runner = CliRunner()

def test_add():
    response = runner.invoke(create_log_folder)
    assert response.exit_code  == 0
    file_name = Path(__file__)
    test_dir = file_name.parent
    proj_dir = test_dir.parent
    app_dir = proj_dir / "app"
    log_dir = app_dir / "logs"
    #logdir = os.path.join(root, '../logs')
    assert log_dir.exists()