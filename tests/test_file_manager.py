import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.file_toolkit.file_manager import catch_file_type, read_csv_file, read_txt_file

BASE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(BASE, ".."))



@pytest.fixture
def sample_txt(tmp_path):
    f = tmp_path / "example.txt"
    f.write_text("this is test file")
    return str(f)

@pytest.fixture
def sample_csv(tmp_path):
    f = tmp_path/ "sample.csv"
    f.write_text("Name,Age\nAlice,30\nBob,25")
    return str(f)

def test_read_txt_file(sample_txt):
    data = read_txt_file(sample_txt)
    assert "test file" in data


def test_read_csv_file(sample_csv):
    data = read_csv_file(sample_csv)
    assert len(data) > 0


def test_catch_file_type_txt():
    assert  catch_file_type("example.txt") == "txt_file"


def test_catch_file_type_csv():
    assert catch_file_type("titanic.csv") == "csv_file"
    
