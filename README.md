# Data engineer recruiting task

## Submission Description: 

The script reads given csv file and stores its content into given `sqlite` database. You can change the path to the csv file or the path to the database by changing constants at the beginning of the script.

if you are running the script from a console use `python3 data_pipeline.py`


## Validation:
	
The script validates csv lines by:
- comparing number of columns to number of columns in the header of the file. `Make sure the header is correct`
- checking for null values

In case the validation fails the program issues a warning containing the number of damaged line.

## Prerequisites

To use this script, you need to have the following:
- Python installed on your system (Python 3.x is recommended).
- The csv and sqlite3 modules, which are part of the Python Standard Library.

