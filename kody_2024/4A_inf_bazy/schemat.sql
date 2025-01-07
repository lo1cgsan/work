DROP TABLE IF EXISTS klasy;
CREATE TABLE klasy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa CHAR(2),
    rocznik CHAR(4)
);

DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie VARCHAR(30),
    nazwisko VARCHAR(30),
    id_klasy INTEGER,
    FOREIGN KEY (id_klasy) REFERENCES klasy(id)
);
