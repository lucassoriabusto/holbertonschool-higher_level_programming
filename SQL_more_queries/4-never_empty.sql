-- Script that creates the table id_not_null.
-- id INT with the default value 1.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT IF NOT NUL DEFAULT 1,
	name VARCHAR(256)
);