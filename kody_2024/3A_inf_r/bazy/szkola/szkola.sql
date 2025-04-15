DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie (
    id_ucz INTEGER PRIMARY KEY,
    nazwisko VARCHAR(20),
    imie VARCHAR(20),
    ulica VARCHAR(20),
    dom VARCHAR(4),
    id_klasy VARCHAR(4)
);
DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT,
    nazwisko VARCHAR(20),
    imie VARCHAR(20)
);
DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    id_ucz INTEGER,
    ocena INTEGER,
    data DATE,
    id_przedm INTEGER,
    FOREIGN KEY(id_ucz) REFERENCES uczniowie(id_ucz),
    FOREIGN KEY(id_przedm) REFERENCES przedmioty(id)
);
