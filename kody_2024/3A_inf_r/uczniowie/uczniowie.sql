DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie (
    id_ucz VARCHAR(8) PRIMARY KEY,
    imie VARCHAR(20),
    nazwisko VARCHAR(20),
    klasa VARCHAR(4)
);
DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT
);
DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    id_oceny INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE,
    id_ucz TEXT,
    id_przedm INTEGER,
    ocena INTEGER,
    FOREIGN KEY(id_ucz) REFERENCES uczniowie(id_ucz),
    FOREIGN KEY(id_przedm) REFERENCES przedmioty(id)
);
