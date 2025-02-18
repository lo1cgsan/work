DROP TABLE IF EXISTS uczelnie;
CREATE TABLE uczelnie (
    id_uczelni INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa VARCHAR(30) NOT NULL
);

DROP TABLE IF EXISTS miasta;
CREATE TABLE miasta (
    id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa VARCHAR(30) NOT NULL,
    kod CHAR(6) DEFAULT ''
);

DROP TABLE IF EXISTS studenci;
CREATE TABLE studenci (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie VARCHAR(30) NOT NULL,
    nazwisko VARCHAR(30) NOT NULL,
    id_uczelni INTEGER NOT NULL,
    id_miasta INTEGER NOT NULL,
    rok_studiow CHAR(3) DEFAULT '',
    dochod DECIMAL(8,2),
    FOREIGN KEY (id_uczelni) REFERENCES uczelnie(id_uczelni),
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);
