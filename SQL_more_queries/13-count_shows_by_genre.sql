SELECT tv_show_genres.genre, tv_shows.number_of_shows
FROM tv_show_genres
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
