USE CINEMA;

-- 1) Find titles of the longest movies. Note that there might be more than such movie.
SELECT title FROM Movies WHERE length = (SELECT MAX(length) FROM Movies);


-- 2) Find out titles of movies that contain "Twilight" and are directed by "Steven Spielberg".
SELECT m.title FROM Movies m JOIN DirectedBy db ON m.id = db.movie_id JOIN Directors d ON db.director_id = d.id WHERE m.title LIKE '%Twilight%'  AND d.name = 'Steven Spielberg';


-- 3) Find out how many movies "Tom Hanks" has acted in.

SELECT COUNT(*) AS num_movies FROM ActIn WHERE actor_id IN (SELECT id FROM Actors WHERE name = 'Tom Hanks');

-- 4) Find out which director directed only a single movie.
SELECT d.name FROM Directors d JOIN DirectedBy db ON d.id = db.director_id GROUP BY d.id HAVING COUNT(*) = 1;


-- 5) Find titles of movies which have the largest number of actors. Note that there may be multiple such movies.

SELECT title FROM Movies WHERE id IN (SELECT movie_id FROM ActIn GROUP BY movie_id HAVING COUNT(*) = (SELECT MAX(actor_count)
    FROM (
            SELECT COUNT(*) AS actor_count
            FROM ActIn
            GROUP BY movie_id
        ) 
        AS max_actor_count
    )
);
-- 6) Find names of actors who played in both English (language = "en") and French ("fr") movies.
SELECT a.name
FROM Actors a
JOIN ActIn ai ON a.id = ai.actor_id
JOIN Movies m ON ai.movie_id = m.id
WHERE m.language IN ('en', 'fr')
GROUP BY a.name
HAVING COUNT(DISTINCT m.language) = 2;

-- 7) Find names of directors who only directed English movies.
SELECT d.name
FROM Directors d
JOIN DirectedBy db ON d.id = db.director_id
JOIN Movies m ON db.movie_id = m.id
GROUP BY d.name
HAVING COUNT(DISTINCT m.language) = 1 AND MAX(m.language) = 'en';