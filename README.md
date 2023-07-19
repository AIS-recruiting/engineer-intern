# Data engineer recruiting task submission
## Author: Matej Koreň, 19.7.2023

## Task Description: 
Create a Python script named "data_pipeline.py" that performs the following tasks:

    a. Read the data from the CSV file.
    b. Perform any necessary data transformations or cleaning.
    c. Establish a connection to a sqlite database (or any other database of your choice).
    d. Create a new table in the database to store the transformed data.
    e. Insert the transformed data into the newly created table.
___
## Implementation

Solution uses a data handling library for python named **pandas** [see footnote]. It provides automatic reading of 
.csv files and creating a dataframe, which is easier to work with. 

To store data permanently, sqlite3 database (which is included with Python) was used. Creation, connection and data 
insertion is handled in the script. 
___
## Solution
### Data manipulation
Firstly, the 'data.csv' was loaded and converted into a dataframe ( **df** ). It is possible to obtain information about its 
structure and values:

```print(df.shape)```
 
>(20639, 11)

Dataset contains 20639 rows and 11 columns. To see their names, we can use:

```print(df.keys())```
```
Index(['LONGITUDE', 'LAT', 'MEDIAN_AGE', 'rooms', 'BEDROOMS', 'POP',
       'HOUSEHOLDS', 'MEDIAN_INCOME', 'MEDIAN_HOUSE_VALUE', 
       'OCEAN_PROXIMITY', 'AGENCY'], dtype='object')
```
To keep key naming consistency, they were converted to uppercase. In the next step we can get rid of duplicates with:

```df.drop_duplicates()```

(**note**: shape of the dataframe hasn't changed, therefore no duplicates were detected.)

To show what data types are in each column ```print(df.dtypes)``` was used:
```
LONGITUDE             float64
LAT                   float64
MEDIAN_AGE             object
ROOMS                  object
BEDROOMS               object
POP                    object
HOUSEHOLDS             object
MEDIAN_INCOME          object
MEDIAN_HOUSE_VALUE     object
OCEAN_PROXIMITY        object
AGENCY                 object
dtype: object
```
This list says that the first two columns are real numbers, but according to **pandas**, others
contain characters and are considered as string objects. After checking for non-numeric characters in these columns,
some missing values were found - *NA*, *Null* or empty space. [ e.g. lines 33,1987 or 2108 ]. To take care of this, special parameter
```na_values = ["Null"," ",""]``` is added to the .csv reader (these are not included in default NaN values, see 
[pandas.read_csv documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)).
To maintain appropriate table structure, each column (except the last two) was changed to 'float64' type:

```
cols = df.columns.drop(df.iloc[:,-2:])                          # last two collumns are dropped
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')       # conversion
```

(**note**: errors='coerce' handles non-parsable values and converts them to NaN (see
[pandas.to numeric documentation](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html)).

### Data storage

After above-mentioned steps, data has been prepared for storage. Using the built-in *sqlite3*, local 
database **test.db** was created and connection established. To save time creating table manually according to dataframe 
keys and data types and then inserting values through a query, **pandas** offers an easy solution:

```
df.to_sql('real_estates', conn, if_exists='replace', index_name = 'ID')
```
which creates a table named 'real_estates' using the established connection (variable *conn*), checks for an existing table
and adds and index column named 'ID' into the table. Dataframe keys are then used as column names and values are inserted
automatically. After ```conn.commit()```, data is stored.
To verify the table structure, we can query the database:

```
SELECT name, type FROM pragma_table_info('real_estates')
```

|        name        |   type  |
|:------------------:|:-------:|
|         ID         | INTEGER |
|      LONGITUDE     |   REAL  |
|         LAT        |   REAL  |
|     MEDIAN_AGE     |   REAL  |
|        ROOMS       |   REAL  |
|      BEDROOMS      |   REAL  |
|         POP        |   REAL  |
|     HOUSEHOLDS     |   REAL  |
|    MEDIAN_INCOME   |   REAL  |
| MEDIAN_HOUSE_VALUE |   REAL  |
|   OCEAN_PROXIMITY  |   TEXT  |
|       AGENCY       |   TEXT  |

___
#### Footnote

The external library **pandas** needs to be installed first, either with package installer in IDE or through command line
> pip install pandas
