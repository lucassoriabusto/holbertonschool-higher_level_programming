-- Script that creates the table unique_id.
-- id INT with the default value 1 and must be unique.
CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
