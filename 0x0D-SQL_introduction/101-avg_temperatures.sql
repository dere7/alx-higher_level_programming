--  displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT * FROM (SELECT city, AVG(`value`) AS avg_temp FROM temperatures GROUP BY
city) AS T ORDER BY avg_temp DESC;