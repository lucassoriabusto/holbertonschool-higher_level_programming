-- Create the database hbtn_0d_usa if it doesn't exist..
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database.
USE hbtn_0d_usa;

-- Create the states table if it doesn't exist.
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
	name VARCHAR(256) NOT NULL
);
