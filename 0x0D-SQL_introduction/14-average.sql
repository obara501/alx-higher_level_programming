-- Computes the average of all records in the table
ALTER TABLE second_table
ADD COLUMN average FLOAT;
WITH avg_score AS (SELECT AVG(score) FROM second_table)
	UPDATE second_table SET average = (SELECT * FROM avg_score);

