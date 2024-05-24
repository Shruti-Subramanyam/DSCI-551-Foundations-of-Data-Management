-- Use the CINEMA database
USE CINEMA;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS DirectedBy, ActIn, Directors, Actors, Movies;


-- Please create the tables as per the structure given.
-- Remember to consider appropriate data types and primary/foreign key constraints.

-- Movies(id, title, year, length, language)
CREATE TABLE Movies(id INT PRIMARY KEY, title VARCHAR(200) NOT NULL, year INT NOT NULL, length INT NOT NULL, language VARCHAR(100) NOT NULL);

INSERT INTO Movies (id, title, year, length, language) VALUES
    (101, 'Your Name', 2016, 258, 'jp'),
    (102, '3 Idiots', 2009, 288, 'hd'),
    (103, 'Train to Busan', 2016, 290, 'ko'),
    (104, 'Whispers of the Wind: A Haunting Tale', 2020, 343, 'en'),
    (105, 'Twilight', 2008, 228, 'en'),
    (106, 'Eternal Love', 1997, 269, 'fr'),
    (107, 'Legacy of the Artisan', 2004, 353, 'gr'),
    (108, 'Romeo and Juliette', 1995, 325, 'ru');


-- Actors(id, name, gender)
CREATE TABLE Actors(id INT PRIMARY KEY, name VARCHAR(100) NOT NULL, gender VARCHAR(100) NOT NULL);
INSERT INTO Actors (id, name, gender) VALUES
    (201, 'Ryan Reynolds', 'Male'),
    (202, 'Priyanka Chopra', 'Female'),
    (203, 'Gal Gadot', 'Female'),
    (204, 'Mahesh Babu', 'Male'),
    (205, 'Shah Rukh Khan', 'Male'),
    (206, 'Tom Hanks', 'Male'),
    (207, 'Kiko Mizuhara', 'Female'),
    (208, 'Kimura Taruya', 'Male');
    

-- ActIn(actor_id, movie_id)
CREATE TABLE ActIn(actor_id INT, movie_id INT, PRIMARY KEY (actor_id, movie_id), FOREIGN KEY (actor_id) REFERENCES Actors(id) ON DELETE CASCADE, FOREIGN KEY (movie_id) REFERENCES Movies(id) ON DELETE CASCADE);
INSERT INTO ActIn (actor_id, movie_id) VALUES
    (201, 101),
    (204, 102),
    (203, 103),
    (204, 105),
    (204, 106),
    (204, 107),
    (206, 101),
    (206, 102),
    (208, 104),
    (206, 108),
    (207, 101),
    (202, 102),
    (204, 108),
    (205, 101),
    (208, 103),
    (203, 105),
    (202, 104),
    (207, 103);

-- Directors(id, name, nationality)
CREATE TABLE Directors(id INT PRIMARY KEY, name VARCHAR(100) NOT NULL, nationality VARCHAR(100) NOT NULL);
INSERT INTO Directors (id, name, nationality) VALUES
    (301, 'Hayao Miyazaki ', 'Japanese'),
    (302, 'Zoya Akhtar', 'Indian'),
    (303, 'Sofia Coppola', 'American'),
    (304, 'Guillermo del Toro', 'Mexican'),
    (305, 'Nuri Bilge Ceylan', 'Turkey'),
    (306, 'Christopher Nolan', 'American'),
    (307, 'Steven Spielberg', 'American');

-- DirectedBy(movie_id, director_id)
CREATE TABLE DirectedBy(movie_id INT, director_id INT, PRIMARY KEY (movie_id, director_id), FOREIGN KEY (movie_id) REFERENCES Movies(id) ON DELETE CASCADE, FOREIGN KEY (director_id) REFERENCES Directors(id) ON DELETE CASCADE);
INSERT INTO DirectedBy (movie_id, director_id) VALUES
    (101, 301),
    (102, 302),
    (103, 303),
    (104, 304),
    (105, 305),
    (106, 306),
    (107, 307),
    (105, 307),
    (108, 301);

-- Please insert sample data into the tables created above.
-- Note: Testing will be conducted on a blind test set, so ensure your table creation and data insertion scripts are accurate and comprehensive.
