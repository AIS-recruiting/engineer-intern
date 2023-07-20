import pandas as pd
import sqlite3

# Import CSV
data = pd.read_csv ('data.csv',na_values = ["Null"," ",""])
df = pd.DataFrame(data)

# Key consistency
df.columns = df.columns.str.upper()

# Duplicates removal
df.drop_duplicates()

# Type change
cols = df.columns.drop(df.iloc[:,-2:])
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')    #1985 & 1999 contains null,2108,2651,33 in agency contains NA

# Connect to local SQL database and store data
conn = sqlite3.connect('test.db')
df.to_sql('real_estates', conn, if_exists='replace', index_label='ID')
conn.commit()
conn.close()