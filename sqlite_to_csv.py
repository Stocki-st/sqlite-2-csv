import sqlite3
import csv

def sqlite_to_csv(db_file, table_name, csv_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    column_names = [description[0] for description in cursor.description]

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)
        for row in cursor.fetchall():
            writer.writerow(row)
    conn.close()

if __name__ == "__main__":
    db_file = 'tile_tracker.db'
    table_name = 'tile_locations'
    csv_file = 'tile_export.csv'

    sqlite_to_csv(db_file, table_name, csv_file)
    print(f'Database "{table_name}" exported to "{csv_file}".')