import sqlite3

# połączenie z bazą
con = sqlite3.connect('zamowienia.sqlite')
# obiekt kursora
cur = con.cursor()

with open('zamowienia.sql') as plik:
    cur.executescript(plik.read())
    print(plik.read())

dane = ['Adam', 'Nowak']
cur.execute(
    'INSERT INTO klienci (imie, nazwisko) VALUES (?, ?)',
    dane
    )

dane = [
        ['Anna', 'Kowalska'],
        ['Jerzy', 'Wiosło'],
    ]
cur.executemany(
    'INSERT INTO klienci (imie, nazwisko) VALUES (?, ?)',
    dane
    )

con.commit()
con.close()
