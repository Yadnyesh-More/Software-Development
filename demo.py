'''import pandas as pd
import pymysql as psql

# Load the Excel file
excel_file = pd.read_excel('MM_properties.xlsx')

# Create a database connection
cnx = psql.connect(
    host='localhost',
    user='root',
    password='root',
    port = 3307,
    charset='utf8',
    database='middleman'
)

# Insert data into the database
excel_file.to_sql('fill_property', cnx, if_exists='replace', index=False)

# Close the connection
cnx.close()
print("done")'''

import pandas as pd
import pymysql as psql
from pandas.io.sql import SQLDatabase

# Load the Excel file
excel_file = pd.read_excel('MM_properties.xlsx')

# Create a database connection
cnx = psql.connect(
    host='localhost',
    user='user',
    password='password',
    port = 3307 ,
    charset = 'utf8',
    database='middleman'
)

# Create a SQLDatabase object
db = SQLDatabase(cnx, 'ysql')

# Insert data into the database
excel_file.to_sql('fill_property', db, if_exists='replace', index=False)