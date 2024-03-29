-- 0x0E. SQL - More queries, Genre ID for all shows 
-- Lists all shows in `hbtn_0d_tvshows` by title, genre.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
