import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.file_toolkit.file_manager import catch_file_type, read_csv_file, read_txt_file


def test_read_txt_file():
    data = read_txt_file("example.txt")
    assert "test file" in data


def test_read_csv_file():
    data = read_csv_file("titanic.csv")
    assert len(data) > 0


def test_catch_file_type_txt():
    file_type = catch_file_type("example.txt")
    assert file_type == "txt_file"


def test_catch_file_type_csv():
    file_type = catch_file_type("titanic.csv")
    assert file_type == "csv_file"
    
