# Data engineer recruiting task
Assessed by: Timotej Ponek

## Requirements & Instructions:

Script was implemented using Python3.8 language.

For correct behavior of script, please ensure you have installed all needed libraries or install them via ``pip3 install -r requirements.txt``.

## Description:

Provided script ``data_pipeline.py`` loads data from 'data.csv' file, converts columns names to title case, then converts 'object' values into corresponding numeric values (casts to int/float), filling missing values with median and dropping duplicates. Then it stores data into sqlite db. Name of db is *task.db* and name of table is *engineer-intern_table*. You can access data in db via cmd, using commands: ``sqlite3 example.db`` and then ``SELECT * FROM 'engineer-intern_table';``.

## Additional information:

For usage of postgresql db, it is required to install ``sqlalchemy`` and ``psycopg2`` libraries via pip. Then, you need to adjust lines under *## Data upload to db* to following :
```
from sqlalchemy import create_engine

# Create engine object
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')

# Load DataFrame into PostgreSQL table
df.to_sql('table_name', engine, if_exists='replace', index=False)
```

I am writting this here as another option to store data into db, as it is not required by task. I want to note that I could not make this run, as I cannot install 'psycopg2' because I have some missing dependencies which are not easy to fix (and because of this I was using 'pg8000.dbapi' driver as workaround), so if you encounter similar errors, I have no fix for you.
