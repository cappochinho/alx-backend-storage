-- Creates a view need_meeting that lists all students that have a score under 80 (strict)

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT students.name
FROM students
WHERE
	students.score < 80 AND
	last_meeting IS NULL OR
	DATEDIFF(NOW(), last_meeting) > 30
