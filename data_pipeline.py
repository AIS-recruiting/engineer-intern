import csv
import sqlite3
import logging

# Change if necessary
CSV_FILE = "data.csv"
DATABASE = "data.db"
DELIMITER = ','


def validate_csv_line(csv_line, csv_header, line_index):
    if len(csv_header) != len(csv_line):
        logging.warning(f"Invalid number of columns in line {line_index}")
        return False

    for value in line:
        if value is None or value.strip() == "":
            logging.warning(f"Null value present in line {line_index}")
            return False

    return True


with open(CSV_FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
    header = next(csv_reader)
    placeholders = ', '.join(['?'] * len(header))

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    columns = ', '.join([f'{column} TEXT' for column in header])

    create_table = f"CREATE TABLE IF NOT EXISTS data_table ({columns});"
    cursor.execute(create_table)

    for i, line in enumerate(csv_reader, 2):
        if validate_csv_line(line, header, i):
            insert = f"INSERT INTO data_table VALUES ({placeholders});"
            cursor.execute(insert, line)

    connection.commit()
    connection.close()


