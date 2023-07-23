# Author: Timotej Ponek
import pandas as pd
import sqlite3

## Data preparation

df = pd.read_csv('data.csv')

# convert column names to title case 
df.columns = df.columns.str.title()

# drop duplicates
df = df.drop_duplicates()
# drop missing or null
df = df.dropna()

numbers = ["Median_Age", "Rooms", "Bedrooms", "Pop", "Households",
           "Median_Income", "Median_House_Value"]
# cast 2 times numeric values to numbers
# 1 cast - to float64, creates some Nan/Inf values
# so we drop these values and with 2 cast we get int values
for x in numbers:
    df[x] = pd.to_numeric(df[x], downcast='signed', errors="coerce")
df = df.dropna()
for x in numbers:
    df[x] = pd.to_numeric(df[x], downcast='signed', errors="coerce")

## Data upload to db

# Create connection object
conn = sqlite3.connect('task.db')

df.to_sql('engineer-intern_table', conn, if_exists='replace', index=False)

# Cleanup
conn.close()