
from pathlib import Path

def upload_test():
    csv = Path(__file__)
    test_dir = csv.parent
    proj_dir = test_dir.parent
    app_dir = proj_dir / "app"
    csv_dir = app_dir / "uploads"
    csv_file = csv_dir / "transactions.csv"
    assert csv_file.exists()