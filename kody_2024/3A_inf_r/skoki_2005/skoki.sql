DROP TABLE IF EXISTS panstwa;
CREATE TABLE panstwa (
    nazwa TEXT,
    skrot TEXT PRIMARY KEY
);

DROP TABLE IF EXISTS zawodnicy;
CREATE TABLE zawodnicy (
    id_zawodnika INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwisko TEXT,
    panstwo TEXT,
    punkty INTEGER,
    FOREIGN KEY (panstwo) REFERENCES panstwa (skrot)
);

DROP TABLE IF EXISTS kuusamo;
CREATE TABLE kuusamo (
    id_zawodnika INTEGER PRIMARY KEY,
    skok1 DECIMAL,
    nota1 DECIMAL,
    skok2 DECIMAL,
    nota11 DECIMAL
);

DROP TABLE IF EXISTS trondheim;
CREATE TABLE trondheim (
    id_zawodnika INTEGER PRIMARY KEY,
    skok1 DECIMAL,
    nota1 DECIMAL,
    skok2 DECIMAL,
    nota11 DECIMAL
);

DROP TABLE IF EXISTS zakopane;
CREATE TABLE zakopane (
    id_zawodnika INTEGER PRIMARY KEY,
    skok1 DECIMAL,
    nota1 DECIMAL,
    skok2 DECIMAL,
    nota11 DECIMAL
);
