# SQLite to CSV Export Script

This Python script provides a simple utility to export data from a SQLite database table to a CSV file. It retrieves all rows from the specified table, along with the column names, and writes them to a CSV file in UTF-8 format.

## Features
- Exports all data from a specified SQLite database table.
- Automatically includes column headers in the CSV file.
- Supports UTF-8 encoding to handle special characters.

## Requirements
- Python 3.x
- Standard libraries: `sqlite3`, `csv`

## How to Use

### 1. Clone or Copy the Script
Copy the script to your local environment.

### 2. Prepare Your SQLite Database
Ensure you have a SQLite database file (`.db`) and know the name of the table you want to export.

### 3. Adapt file paths
Edit the `db_file`, `table_name`, and `csv_file` variables in the script.

Example:
```python
db_file = 'example.db'       # Path to your SQLite database file
table_name = 'users'         # Name of the table to export
csv_file = 'output.csv'      # Name of the output CSV file

sqlite_to_csv(db_file, table_name, csv_file)
```

### 4. Run the Script
```bash
python3 sqlite_to_csv.py
```
