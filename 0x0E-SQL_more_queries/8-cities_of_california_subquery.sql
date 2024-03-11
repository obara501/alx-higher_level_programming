-- List cities that are linked to a certain state
SELECT id,name FROM cities
WHERE state_id = 1
ORDER BY cities.id ASC;

