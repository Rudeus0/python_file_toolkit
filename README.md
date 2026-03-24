# Python File Toolkit CLI

A command-line tool that reads, detects, and summarises text and CSV files. Built with clean OOP structure, professional logging, error handling, and pytest test coverage.

---

## Problem

Reading and inspecting files is a common task in data engineering pipelines. This tool provides a reusable CLI interface that handles different file types gracefully — with retries, logging, and clean error messages instead of silent failures.

---

## Project Structure

```
python_file_toolkit/
├── src/
│   └── file_toolkit/
│       ├── __init__.py
│       ├── file_manager.py      # File type detection + read functions
│       └── main.py              # CLI entry point with argparse + retry loop
├── tests/
│   ├── __init__.py
│   └── test_file_manager.py    # pytest tests with tmp_path fixtures
├── logs/
│   └── toolkit.log              # Auto-generated log file
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Features

- Detects file type from extension (`.txt`, `.csv`)
- Reads `.txt` files and prints content
- Reads `.csv` files and prints row count, column count, and column names
- Retries up to 3 times on file errors before exiting
- Logs all operations and errors to `logs/toolkit.log`
- Raises clean exceptions instead of silent failures
- Full pytest test suite using `tmp_path` fixtures

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/python_file_toolkit.git
cd python_file_toolkit

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the toolkit
python -m src.file_toolkit.main yourfile.txt
python -m src.file_toolkit.main yourfile.csv
```

---

## Run Tests

```bash
pytest tests/ -v
```

Expected output:
```
tests/test_file_manager.py::test_read_txt_file        PASSED
tests/test_file_manager.py::test_read_csv_file        PASSED
tests/test_file_manager.py::test_catch_file_type_txt  PASSED
tests/test_file_manager.py::test_catch_file_type_csv  PASSED
4 passed in 0.05s
```

---

## Example Output

**Text file:**
```bash
$ python -m src.file_toolkit.main example.txt
Hi
this is a test file
for python toolkit experiment
```

**CSV file:**
```bash
$ python -m src.file_toolkit.main titanic.csv

CSV SUMMARY
-----------
Rows: 891
Columns: 12

Column Names:
PassengerId
Survived
Pclass
...
```

---

## Error Handling

| Error | Behaviour |
|-------|-----------|
| File not found | Logs error, increments retry counter |
| Permission denied | Logs error, increments retry counter |
| Unsupported file type | Prints message, increments retry counter |
| 3 failed attempts | Exits with message |

---

## Error Analysis

**Known limitations:**

- Only supports `.txt` and `.csv` — no `.json`, `.parquet`, or `.xlsx` support yet
- CSV summary shows column names only — no data preview or type information
- Retry logic retries the same file path — useful for permission errors, not for wrong filenames
- Log file grows indefinitely — no log rotation implemented

---

## Tech Stack

- Python 3.12
- `argparse` — CLI argument parsing
- `csv.DictReader` — CSV reading
- `logging` — file-based logging
- `pytest` + `tmp_path` — testing with auto-cleanup fixtures

---

## Key Learnings

- Relative imports require `__init__.py` in every folder in the package chain
- Running with `python -m` vs `python file.py` behaves differently for imports
- `tmp_path` fixtures make tests portable — no dependency on manually placed files
- Argparse must be outside the retry loop — it parses once at startup, not per attempt 