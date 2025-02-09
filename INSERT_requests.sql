Insert into Bands(id, name) values (1, 'Metallica');
Insert into Bands(id, name) values (2, 'Helloween');
Insert into Bands(id, name) values (3, 'Therion');
Insert into Bands(id, name) values (4, 'Nightwish');

Insert into Genre(id, name) values (1, 'Trash-metal');
Insert into Genre(id, name) values (2, 'Speed-metal');
Insert into Genre(id, name) values (3, 'Symphonic-metal');

Insert into Album(id, name, release_year) values (1, 'Kill em All', 1983);
Insert into Album(id, name, release_year) values (2, 'Walls of Jericho', 1985);
Insert into Album(id, name, release_year) values (3, 'Of Darkness...', 1991);
Insert into Album(id, name, release_year) values (4, 'Angels Fall First', 2018);

Insert into Tracks(name, track_duration, Album_id) values ('Hit the Lights', '00:04:16', 1);
Insert into Tracks(name, track_duration, Album_id) values ('The four Horsemen', '00:07:12', 1);
Insert into Tracks(name, track_duration, Album_id) values ('Walls of Jericho', '00:00:53', 2);
Insert into Tracks(name, track_duration, Album_id) values ('Ride the Sky', '00:05:54', 2);
Insert into Tracks(name, track_duration, Album_id) values ('The Return', '00:04:51', 3);
Insert into Tracks(name, track_duration, Album_id) values ('Asphyxiate by Fear', '00:03:58', 3);
Insert into Tracks(name, track_duration, Album_id) values ('Elvenpath', '00:04:54', 4);
Insert into Tracks(name, track_duration, Album_id) values ('Beauty and the Beast', '00:06:22', 4);
Insert into Tracks(name, track_duration, Album_id) values ('My Astral Romance', '00:05:12', 4);
Insert into Tracks(name, track_duration, Album_id) values ('By myself', '00:03:12', 4);


Insert into Collection(id, name, release_year) values (1, 'Trash-metal Collection', 2021);
Insert into Collection(id, name, release_year) values (2, 'Speed-metal Collection', 2022);
Insert into Collection(id, name, release_year) values (3, 'Symphonic-metal Collection', 2023);
Insert into Collection(id, name, release_year) values (4, 'Greatest Albums Collection', 2024);

Insert into GenreBand(Genre_id, Band_id) values (1, 1);
Insert into GenreBand(Genre_id, Band_id) values (2, 2);
Insert into GenreBand(Genre_id, Band_id) values (3, 3);
Insert into GenreBand(Genre_id, Band_id) values (3, 4);

Insert into BandAlbum(Album_id, Band_id) values (1, 1);
Insert into BandAlbum(Album_id, Band_id) values (2, 2);
Insert into BandAlbum(Album_id, Band_id) values (3, 3);
Insert into BandAlbum(Album_id, Band_id) values (4, 4);

Insert into TrackCollection(Track_id, Collection_id) values (1, 1);
Insert into TrackCollection(Track_id, Collection_id) values (2, 1);
Insert into TrackCollection(Track_id, Collection_id) values (3, 2);
Insert into TrackCollection(Track_id, Collection_id) values (4, 2);
Insert into TrackCollection(Track_id, Collection_id) values (5, 3);
Insert into TrackCollection(Track_id, Collection_id) values (6, 3);
Insert into TrackCollection(Track_id, Collection_id) values (7, 3);
Insert into TrackCollection(Track_id, Collection_id) values (8, 3);
Insert into TrackCollection(Track_id, Collection_id) values (1, 4);
Insert into TrackCollection(Track_id, Collection_id) values (2, 4);
Insert into TrackCollection(Track_id, Collection_id) values (3, 4);
Insert into TrackCollection(Track_id, Collection_id) values (4, 4);
Insert into TrackCollection(Track_id, Collection_id) values (5, 4);
Insert into TrackCollection(Track_id, Collection_id) values (6, 4);
Insert into TrackCollection(Track_id, Collection_id) values (7, 4);
Insert into TrackCollection(Track_id, Collection_id) values (8, 4);