--- https://www.hackerrank.com/challenges/draw-the-triangle-2/submissions/code/339477275
--- MySQL

DELIMITER //
 CREATE PROCEDURE ASTERISCO(qtde INT)
 BEGIN
    DECLARE contador INT DEFAULT 1;
    WHILE contador < 21 DO
        SELECT repeat('* ',contador);
        SET  contador =  contador + 1;
    END WHILE;
 END;
 //
 CALL ASTERISCO(20)
 