-- Lists all the cities of California.
SELECT cities.state_id, cities.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = "California"
ORDER BY cities.id ASC;