CREATE TABLE musicas (
    musicas VARCHAR(100),
    autor VARCHAR(100),
    album VARCHAR(100),
    es_cover VARCHAR(100),
    es_remix VARCHAR(100),
    año INT
);

--INSERTAR
INSERT INTO musicas (musicas, autor, album, es_cover, es_remix, año) VALUES 
("No Time to Explain", "Good Kid", "NTTE", "no", "no", 2020),
("Premier Inn", "Good Kid", "PI", "no", "no", 2020),
("FOR YOUR LOVE", "Maneskin", "RUSH !", "no", "no", 2020),
("From the Start", "Good Kid", "FTS", "si", "no", 2020),
("R U MINE?", "Artick Monkeys", "AM", "no", "no", 2020),
("Fireside", "Artick Monkeys", "AM", "no", "no", 2020),
("Bubbly", "Good Kid", "B", "no", "no", "2020"),
("Teeth", "5 Seconds of Summer", "nose", "no", "no", 2014),
("Morirò da Re", "Maneskin", "IL BALLO DELLA VITA", "no", "no", 2015),
("Mucho Gusto", "Canserbero", "Vida", "no", "no", 2010),
("Osmosis", "Good Kid", "O", "no", "no", "2020"),
("Read Your Diary", "Maneskin", "RUSH !", "no", "no", 2020),
("Summer", "Good Kid", "S", "no", "no", "2020"),
("TRASTEVERE", "Maneskin", "TASTEVERE", "no", "no", 2020),
("Aloe Lite", "Good Kid", "AL", "no", "no", 2020);

--MODIFICAR/ACTUALIZAR
UPDATE musicas
SET año = 2021
WHERE musicas = "FOR YOUR LOVE";

UPDATE musicas 
SET es_cover = "si"
WHERE musicas = "Mucho Gusto";

UPDATE musicas
SET es_remix = "si"
WHERE musicas = "Premier Inn"

UPDATE musicas
SET año = 2023
WHERE musicas = "Read Your Diary"

UPDATE musicas
SET musicas = "Slingshot"
WHERE musicas = "Summer"

UPDATE musicas
SET album = "13 Reasons Why:"
WHERE musicas = "Teeth"

UPDATE musicas
SET autor = "Laufey"
WHERE musicas = "From the Start"

UPDATE musicas
SET es_cover = "no"
WHERE musicas = "TRASTEVERE"

--BORRAR
DELETE FROM musicas
WHERE musicas = "Aloe Lite"

DELETE FROM musicas
WHERE musicas = "Osmosis"

DELETE FROM musicas
WHERE musicas = "Morirò da Re"

DELETE FROM musicas
WHERE musicas = "R U MINE?"

DELETE FROM musicas
WHERE musicas = "Bubbly"


--INSERTAR... OTRA VEZ

INSERT INTO musicas (musicas, autor, album, es_cover, es_remix, año) VALUES
("Break", "Good Kid", "BK", "no", "no", 2024),
("DON´T WANNA SLEEP", "Maneskin", "RUSH !", "no", "no", 2023),
("Start Over", "Imagine Dragons", "EVOLVE", "no", "no", 2017);
