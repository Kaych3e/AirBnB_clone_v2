-- This sript script that prepares a MySQL server for the project
-- creating a database:hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
--creating user: 'hbnb_test_db'@'localhost' with password
CREATE  USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting privileges to the user: hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'loicalhost';
-- Ensuring that the changes take effect immediately with flush privileges.
FLUSH PRIVILEGES
--granting SELECT privilege for the user on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- ensuring that the changes take effect immediately with flush privileges.
FLUSH PRIVILEGES;
