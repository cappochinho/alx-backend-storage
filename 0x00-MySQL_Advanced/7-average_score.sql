-- Creates a stored procedure ComputeAverageScoreForUser

DELIMITER |

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id int)
BEGIN
	SET @avg := (
		SELECT AVG(score)
		FROM corrections
		WHERE corrections.user_id = user_id);
	UPDATE users
	SET average_score = @avg
	WHERE id = user_id;
END;
|
--end of script
