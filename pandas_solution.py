import pandas as pd
import sqlite3


# Reads the data, labels columns, transforms data, creates connection,
# moves transformed data to the new sqlite table
def csv_to_sqlite():
    resorts = pd.read_csv('data.csv')
    resorts.columns = ['longitude', 'latitude', 'median_age', 'rooms',
                       'bedrooms', 'pop', 'households', 'median_income',
                       'median_house_value', 'ocean_proximity', 'agency']
    resorts = clear_data(resorts)
    resorts.insert(0, 'resort_id', range(1, len(resorts) + 1))
    resorts = type_dataframe(resorts)
    conn = sqlite3.connect('data.db')

    resorts.to_sql('resorts', conn, if_exists='replace', index=False,
                   dtype={'resort_id': 'INTEGER PRIMARY KEY',
                          'longitude': 'REAL NOT NULL',
                          'latitude': 'REAL NOT NULL'})
    conn.commit()
    conn.close()


def clear_data(resorts):
    resorts['agency'].str.upper()  # defensive fix (human error)
    resorts['ocean_proximity'].str.upper()  # defensive fix (human error)

    resorts.loc[(resorts['agency'] != 'YES')
                & (resorts['agency'] != 'NO'), 'agency'] = 'NO INFO'

    resorts.loc[(resorts['ocean_proximity'] == 'NB',
                 'ocean_proximity')] = 'NEAR BAY'

    # This could be changed to ENUM
    resorts.loc[(resorts['ocean_proximity'] != 'NEAR BAY')
                & (resorts['ocean_proximity'] != 'OUT OF REACH')
                & (resorts['ocean_proximity'] != '<1H OCEAN')
                & (resorts['ocean_proximity'] != 'INLAND')
                & (resorts['ocean_proximity'] != 'NEAR OCEAN')
                & (resorts['ocean_proximity'] != 'ISLAND'),
                'ocean_proximity'] = 'NO INFO'

    # Checking for numerical values in columns 0 - 8, if not numerical -> NA
    resorts[resorts.columns[:-2]] = \
        resorts[resorts.columns[:-2]].apply(pd.to_numeric, errors='coerce')

    # NA -> impute with median
    numeric_columns = resorts.select_dtypes(include=['number']).columns
    resorts[numeric_columns] = \
        resorts[numeric_columns].fillna(round(resorts[numeric_columns].mean()))
    return resorts


# Adds data type to a column
def type_dataframe(resorts):
    resorts = resorts.astype({'resort_id': 'int',
                              'longitude': 'float',
                              'latitude': 'float',
                              'median_age': 'int',
                              'rooms': 'int',
                              'bedrooms': 'int',
                              'pop': 'int',
                              'households': 'int',
                              'median_income': 'float',
                              'median_house_value': 'int',
                              'ocean_proximity': 'str',
                              'agency': 'str'})
    return resorts
