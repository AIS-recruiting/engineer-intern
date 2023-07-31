# Data engineer recruiting task
# Data Pipeline Project 

## Introduction 
This project is a simple data pipeline that extracts data from a CSV file, performs some transformations and loads the data into a SQLite database.

## Requirements 
- Python 3.8 or later 
- libraries:
    - pandas
    - sqlite3
    - numpy

## Setup and Usage 
1. Clone this repository to your local environment.
2. Install required libraries by running
```
pip install pandas
pip install numpy
```

_Please also note that you may want to use 'pip3' instead of 'pip'._

3. The main script is 'data_pipeline.py', which performs the following tasks:
    - read data from CSV file 'data.csv'.
    - transform the data, including handling missing values.
    - establish a connection to a SQLite database.
    - load the transformed data into a table in the database.
4. Run the script.

## Code Overview
- The function 'csv_data(filepath) reads data from a CSV file and performs data cleaning and transformation.
- The function 'create_connection(database)' established a connetion to a SQLite database.
- The function 'load_data(data, conn)' loads the transformed data into a SQLite database.
- The function 'view_data(query, conn)' queries the database and returns the results.

**Note:** This project is part of a submission for a data engineering internship application and adheres to the provided evaluation criteria,including correctness, code quality and documentation.

