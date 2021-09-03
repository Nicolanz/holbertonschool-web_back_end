-- Procedure to set the avg score of a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
  BEGIN
    SET @score = (SELECT ROUND(AVG(c.score)) FROM corrections c WHERE c.user_id = user_id GROUP BY c.user_id);
    UPDATE users SET average_score = @score WHERE id = user_id;
  END;
|
DELIMITER ;
