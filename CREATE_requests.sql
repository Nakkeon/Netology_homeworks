create table if not exists Genre (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

create table if not exists Bands (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

create table if not exists GenreBand (
	Genre_id INTEGER REFERENCES Genre(id),
	Band_id INTEGER REFERENCES Bands(id),
	CONSTRAINT pk_GenreBand PRIMARY KEY (Genre_id, Band_id)
);


create table if not exists Album (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) unique NOT NULL,
	release_year INT NOT NULL
);


create table if not exists BandAlbum (
	Album_id INTEGER REFERENCES Album(id),
	Band_id INTEGER REFERENCES Bands(id),
	CONSTRAINT pk_BandAlbum PRIMARY KEY (Album_id, Band_id)
);


create table if not exists Tracks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	track_duration TIME,
	Album_id INTEGER REFERENCES Album(id)
);

create table if not exists Collection (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) unique NOT NULL,
	release_year INT NOT NULL
);

create table if not exists TrackCollection (
	Track_id INTEGER REFERENCES Tracks(id),
	Collection_id INTEGER REFERENCES Collection(id),
	CONSTRAINT pk_TrackCollection PRIMARY KEY (Track_id, Collection_id)
);