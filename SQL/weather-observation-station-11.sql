--- https://www.hackerrank.com/challenges/weather-observation-station-11/submissions/code/338494428
--- MySQL
SELECT DISTINCT CITY FROM STATION WHERE
(CITY NOT LIKE  "A%" AND 
 CITY NOT LIKE  "E%" AND 
 CITY NOT LIKE  "I%" AND 
 CITY NOT LIKE  "O%" AND 
 CITY NOT LIKE  "U%" ) 
OR
(CITY NOT LIKE  "%A" AND 
 CITY NOT LIKE  "%E" AND 
 CITY NOT LIKE  "%I" AND 
 CITY NOT LIKE  "%O" AND 
 CITY NOT LIKE  "%U" ) 