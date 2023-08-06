--- https://www.hackerrank.com/challenges/weather-observation-station-9/submissions/code/338494330
SELECT DISTINCT CITY FROM STATION WHERE
(CITY NOT LIKE  "A%" AND CITY NOT LIKE    "E%" AND CITY NOT LIKE    "I%" AND CITY NOT LIKE    "O%" AND CITY NOT LIKE    "U%" )