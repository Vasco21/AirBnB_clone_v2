#!/usr/bin/python3

import mysql.connector

# MySQL connection parameters
user = 'your_username'
password = 'your_password'
host = 'localhost'
database = 'hbnb_dev_db'

# Connect to MySQL server
connection = mysql.connector.connect(
    user=user,
    password=password,
    host=host,
)

# Create database if it doesn't exist
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database))
cursor.close()

# Grant privileges to the user
cursor = connection.cursor()
cursor.execute("GRANT ALL PRIVILEGES ON {}.* TO '{}'@'{}'".format(database, user, host))
cursor.execute("GRANT SELECT ON performance_schema.* TO '{}'@'{}'".format(user, host))
cursor.close()

# Close the connection
connection.close()
