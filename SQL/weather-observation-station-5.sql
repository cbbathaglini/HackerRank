--- https://www.hackerrank.com/challenges/weather-observation-station-5/submissions/code/339472068
--- MySQL
SELECT CITY,MIN(LENGTH(CITY)) FROM STATION GROUP BY CITY ORDER BY MIN(LENGTH(CITY)) ASC, CITY ASC LIMIT 1;
SELECT CITY,MAX(LENGTH(CITY)) FROM STATION GROUP BY CITY ORDER BY MAX(LENGTH(CITY)) DESC,CITY LIMIT 1;