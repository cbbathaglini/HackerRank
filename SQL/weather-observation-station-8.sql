---https://www.hackerrank.com/challenges/weather-observation-station-8/submissions/code/338494235
SELECT DISTINCT CITY FROM STATION WHERE 
(CITY LIKE "A%" OR CITY LIKE "E%" OR CITY LIKE "I%" OR CITY LIKE "O%" OR CITY LIKE "U%" ) AND 
(CITY LIKE "%A" OR CITY LIKE "%E" OR CITY LIKE "%I" OR CITY LIKE "%O" OR CITY LIKE "%U" )  