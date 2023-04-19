-- Script thst prepares a MySQL server for the Airbnb clone project
-- Create the database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user hbnb_dev (in localhost) with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant select privileges to hbnb_dev on only performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Grant all privileges on only the hbnb_dev_db database to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
