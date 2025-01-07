-- tabela użytkowników
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id integer primary key autoincrement, -- unikalny indentyfikator
    email text unique not null, -- email
    haslo text not null, -- hasło
    data_d datetime not null -- data utworzenia konta
);

-- tabela z zadaniami
DROP TABLE IF EXISTS zadania;
CREATE TABLE zadania (
    id integer primary key autoincrement, -- unikalny indentyfikator
    zadanie text not null, -- opis zadania do wykonania
    zrobione boolean not null, -- informacja czy zadania zostalo juz wykonane
    data_pub datetime not null, -- data dodania zadania
    u_id integer not null,
    FOREIGN KEY (u_id) REFERENCES users (id) ON DELETE CASCADE
);
