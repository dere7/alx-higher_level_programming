-- lists all genres contained IN hbtn_0d_tvshows that
-- and displays the number of shows linked to each.
SELECT  tv_genres.name
       ,count(tv_shows.id) as number_of_shows
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id,
tv_genres
WHERE tv_genres.id = tv_show_genres.genre_id
group by tv_show_genres.genre_id
ORDER BY number_of_shows DESC;