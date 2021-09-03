-- New view for students table
DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS SELECT s.name
FROM students s
WHERE (s.last_meeting IS NULL
OR s.last_meeting NOT BETWEEN ADDDATE(CURDATE(), INTERVAL -1 MONTH) AND CURDATE())
AND s.score < 80;
