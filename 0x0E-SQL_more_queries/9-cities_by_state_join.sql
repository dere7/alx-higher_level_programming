-- lists all cities contained IN the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
SELECT  c.id
       ,c.name
       ,s.name
FROM cities c, states s
WHERE c.state_id = s.id
ORDER BY c.id;