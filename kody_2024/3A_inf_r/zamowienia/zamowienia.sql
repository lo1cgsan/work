DROP TABLE IF EXISTS klienci;
CREATE TABLE klienci (
    id_klienta INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwisko TEXT,
    imie TEXT
);

DROP TABLE IF EXISTS zamowienia;
CREATE TABLE zamowienia (
    id_zamowienia INTEGER PRIMARY KEY AUTOINCREMENT,
    id_klienta INTEGER,
    nazwa_owocu TEXT,
    cena FLOAT,
    liczba_kg FLOAT,
    FOREIGN KEY (id_klienta) REFERENCES klienci (id_klienta)
);
