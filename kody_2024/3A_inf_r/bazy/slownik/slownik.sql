DROP TABLE IF EXISTS wyrazy;
CREATE TABLE wyrazy (
    id_wyraz INTEGER PRIMARY KEY AUTOINCREMENT,
    wyraz VARCHAR(20)
);

DROP TABLE IF EXISTS znaczenia;
CREATE TABLE znaczenia (
    id_znaczenie INTEGER PRIMARY KEY AUTOINCREMENT,
    znaczenie VARCHAR(20)
);

DROP TABLE IF EXISTS wyraz_znaczenie;
CREATE TABLE wyraz_znaczenie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_wyraz INTEGER,
    id_znaczenie INTEGER,
    FOREIGN KEY(id_wyraz) REFERENCES wyrazy(id_wyraz),
    FOREIGN KEY(id_znaczenie) REFERENCES znaczenia(id_znaczenie)
);