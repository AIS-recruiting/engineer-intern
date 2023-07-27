import csv
import sqlite3
from typing import List, Union


def csv_to_sqlite() -> None:
    means = inspect_data()
    conn = sqlite3.connect('data.db')
    cursor = create_table(conn)
    cursor = assign_to_database(cursor, means)
    cursor.execute("""COMMIT;""")
    conn.close()


def inspect_data() -> List[int]:
    with open('data.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader, None)  # skip header
        sum_elements: List[float] = [0] * 9
        count_elements = [0] * 9
        for row in datareader:
            for i in range(9):
                try:
                    detail = float(row[i])
                    sum_elements[i] += detail
                    count_elements[i] += 1
                # skips over damaged/missing data created by human error
                # other exceptions are not allowed
                except ValueError:
                    pass
        means = count_means(sum_elements, count_elements)
    return means


def count_means(sum_elements: List[float], count_elements: List[int]) \
        -> List[int]:
    means = []
    for i in range(len(sum_elements)):
        means.append(round(sum_elements[i]/count_elements[i]))
    return means


def create_table(conn: sqlite3.Connection) -> sqlite3.Cursor:
    cursor = conn.cursor()
    create_resort_table = """CREATE TABLE resorts_naive (
                            resort_id INTEGER PRIMARY KEY,
                            longitude REAL NOT NULL,
                            latitude REAL NOT NULL,
                            median_age INTEGER,
                            rooms INTEGER,
                            bedrooms INTEGER,
                            pop INTEGER,
                            households INTEGER,
                            median_income REAL,
                            median_house_value INTEGER,
                            ocean_proximity TEXT,
                            agency TEXT
                        );"""

    cursor.execute(create_resort_table)
    return cursor


def assign_to_database(cursor: sqlite3.Cursor, means: List[int]) \
        -> sqlite3.Cursor:
    header = 'resort_id, longitude, latitude, median_age, rooms, bedrooms, ' \
             'pop, households, median_income, median_house_value,' \
             'ocean_proximity, agency'
    id = 1
    with open('data.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader, None)  # skip header
        for row in datareader:
            numerical_values = extract_numerical_values(row, means, [id])
            non_numerical_values = extract_non_numerical(row)
            numerical_values_statement = \
                ", ".join(str(x) for x in numerical_values)
            insert_command = f"""INSERT INTO resorts1( {header} )
                                 VALUES( {numerical_values_statement},
                                 ? , ? );"""
            cursor.execute(insert_command,
                           (non_numerical_values[0], non_numerical_values[1]))
            id += 1
    return cursor


def extract_non_numerical(row: List[str]) -> List[str]:
    if row[9] == 'NB':
        ocean_proximity = 'NEAR BAY'
    elif ((row[9] != 'NEAR BAY') and (row[9] != 'OUT OF REACH')
          and (row[9] != '<1H OCEAN') and (row[9] != 'INLAND')
          and (row[9] != 'NEAR OCEAN') and (row[9] != 'ISLAND')):
        ocean_proximity = 'NO INFO'
    else:
        ocean_proximity = row[9]
    if (row[10].upper() != 'YES') and (row[10].upper() != 'NO'):
        agency = 'NO INFO'
    else:
        agency = row[10].upper()
    return [ocean_proximity, agency]


def extract_numerical_values(row: List[str], means: List[int],
                             numerical_values: List[Union[int, float]]) \
        -> List[Union[int, float]]:
    for i in range(9):
        try:
            detail = float(row[i])
        except ValueError:
            detail = float(means[i])
        numerical_values.append(detail)
    # converting to int types to fit in database
    numerical_values[3:8], numerical_values[9] = \
        list(map(lambda x: int(x), numerical_values[3:8])), \
        int(numerical_values[9])
    return numerical_values
