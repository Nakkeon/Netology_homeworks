SELECT name, track_duration
FROM Tracks
WHERE track_duration = (SELECT MAX(track_duration) FROM Tracks);

SELECT name, track_duration
FROM Tracks
WHERE track_duration >= 3.5;

SELECT name
FROM Album
WHERE release_year between 2018 and 2021;

SELECT name
FROM Bands
WHERE name NOT LIKE '% %';

SELECT name
FROM tracks
WHERE name LIKE '%My%';

SELECT g.name AS genre_name, COUNT(ag.band_id) AS band_count
FROM Genre g
LEFT JOIN genreband ag ON g.id = ag.genre_id
GROUP BY g.name

SELECT a.name AS album_name, COUNT(t.id) AS track_count
FROM Album a
LEFT JOIN Tracks t ON a.id = t.Album_id
WHERE a.release_year = 2018
GROUP BY a.id, a.name

SELECT a.name AS album_name, AVG(track_duration)
FROM Album a
LEFT JOIN Tracks track_duration ON a.id = track_duration.Album_id
GROUP BY a.id, a.name

SELECT b.name AS bands_name
FROM Bands b
WHERE b.id NOT IN (
    SELECT bb.band_id
    FROM Album al
    JOIN bandalbum bb ON al.id = bb.album_id
    WHERE al.release_year = 2020
);

SELECT DISTINCT c.name AS collection_name
FROM Bands b
JOIN BandAlbum ba ON b.id = ba.Band_id
JOIN Album a ON ba.Album_id = a.id
JOIN Tracks t ON a.id = t.Album_id
JOIN TrackCollection tc ON t.id = tc.Track_id
JOIN Collection c ON tc.Collection_id = c.id
WHERE b.name = 'Metallica';