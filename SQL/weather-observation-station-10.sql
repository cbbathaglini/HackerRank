--- https://www.hackerrank.com/challenges/weather-observation-station-10/submissions/code/338494388
SELECT DISTINCT CITY FROM STATION WHERE
(CITY NOT LIKE  "%A" AND 
 CITY NOT LIKE  "%E" AND 
 CITY NOT LIKE  "%I" AND 
 CITY NOT LIKE  "%O" AND 
 CITY NOT LIKE  "%U" )