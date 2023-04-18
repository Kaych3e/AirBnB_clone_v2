-- Script thst prepares a MySQL server for the Airbnb clone project
-- Create the database hbnb_dev_db
CREATE DATATBASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user hbnb_dev (in localhost) with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on only the hbnb_dev_db database to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev`@`localhost';
FLUSH PRIVILEGES;
-- Grant select privilegests to hbnb_dev on only performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev`@`localhost';
FLUSH PRIVILEGES;
