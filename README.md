# Data engineer recruiting task

## Overview:
In this project, you will find a pipeline that transforms a CSV file into an SQLite database.
The project includes two approaches, the default approach is using pandas, and is simpler and faster. The second approach is implemented from scratch and demonstrates a more universal approach.

## Instructions:


You can run the script without an argument that uses the default approach (pandas) ```python data_pipeline.py```.
<br>
Or you can use the flag to determine the mode ```python data_pipeline.py --mode pandas```, ```python data_pipeline.py --mode naive```.

## Dependencies:
In order to run the project install pandas library ```pip install pandas```.

## Task description:
The script performs the following tasks: 
- a. Read the data from the CSV file.
- b. Perform any necessary data transformations or cleaning.
- c. Establish a connection to a SQLite database. 
- d. Create a new table in the database to store the transformed data. 
- e. Insert the transformed data into the newly created table.
