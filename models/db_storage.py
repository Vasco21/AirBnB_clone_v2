#!/usr/bin/python3

-- Create the development database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the development user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the development user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Create the testing database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the testing user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the testing user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to the testing user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
