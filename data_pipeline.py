import pandas as pd
import sqlite3
from pathlib import Path


file = 'data.csv'

#dodelat IDcka
#prejmenovat LAT na LATITUDE, room na upper

users = pd.read_csv(file)

users['AGENCY'].str.upper() # defensive fix (human error)
users['OCEAN_PROXIMITY'].str.upper() # defensive fix (human error)

users.loc[(users['AGENCY'] != 'YES') & (users['AGENCY'] != 'NO'), 'AGENCY'] = 'NO INFO'

users.loc[(users['OCEAN_PROXIMITY'] == 'NB', 'OCEAN_PROXIMITY')] = 'NEAR BAY'
users.loc[(users['OCEAN_PROXIMITY'] != 'NEAR BAY')
          & (users['OCEAN_PROXIMITY'] != 'OUT OF REACH')
          & (users['OCEAN_PROXIMITY'] != '<1H OCEAN')
          & (users['OCEAN_PROXIMITY'] != 'INLAND')
          & (users['OCEAN_PROXIMITY'] != 'NEAR OCEAN')
          & (users['OCEAN_PROXIMITY'] != 'ISLAND'), 'OCEAN_PROXIMITY'] = 'NO INFO'

#checking for numerical values in columns 0 - 8, if not numerical or if NA - value imputed with median
users[users.columns[:-2]] = users[users.columns[:-2]].apply(pd.to_numeric, errors='coerce')
numeric_columns = users.select_dtypes(include=['number']).columns
users[numeric_columns] = users[numeric_columns].fillna(users[numeric_columns].median())

users = users.astype({'LONGITUDE': 'float',
                      'LAT': 'float',
                      'MEDIAN_AGE': 'Int64',
                      'rooms': 'Int64',
                      'BEDROOMS': 'Int64',
                      'POP': 'Int64',
                      'HOUSEHOLDS': 'Int64',
                      'MEDIAN_INCOME': 'float',
                      'MEDIAN_HOUSE_VALUE': 'Int64',
                      'OCEAN_PROXIMITY': 'str',
                      'AGENCY': 'str'})

#df = users.drop_duplicates(subset=['MEDIAN_AGE'])
#print(df)

conn = sqlite3.connect('my_data.db')
# write the data to a sqlite table
users.to_sql('users', conn, if_exists='append', index = False) # tenhle prikaz da pandas do sqlite