import sqlite3
import csv
import os

def utworz_baze(cur):
    with open('skoki.sql') as plik:
        cur.executescript(plik.read())
        print(plik.read())


def wczytaj_dane(nazwa_pliku, separator=';'):
    dane = []

    with open(nazwa_pliku) as plik:
        # print(plik.read())
        tresc = csv.reader(plik, delimiter=separator)
        for rekord in tresc:
            rekord = [wartosc for wartosc in rekord if wartosc]
            # print(rekord)
            dane.append(rekord)
    return dane


def dodaj_dane(nazwa_pliku, cur, zapytanie, separator=';'):
    dane = wczytaj_dane(nazwa_pliku, separator=separator)
    # print(dane)
    cur.executemany(zapytanie, dane)


def wykonaj_zapytanie(cur, query):
    cur.execute(query)
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)

def main():
    # połączenie z bazą
    con = sqlite3.connect('skoki.sqlite')
    # obiekt kursora
    cur = con.cursor()

#    if not os.path.isfile('skoki.sqlite'):
#        print('Tworzę bazę: ')
    utworz_baze(cur)
    dodaj_dane('Panstwa.txt', cur, 'INSERT INTO panstwa VALUES (?, ?)')
    dodaj_dane('Zawodnicy.txt', cur, 'INSERT INTO zawodnicy VALUES (?, ?, ?, ?)')
    dodaj_dane('Kuusamo28.txt', cur, 'INSERT INTO kuusamo VALUES (?, ?, ?, ?, ?)', separator=' ')
    dodaj_dane('Trondheim06.txt', cur, 'INSERT INTO trondheim VALUES (?, ?, ?, ?, ?)', separator=' ')
    dodaj_dane('Zakopane17.txt', cur, 'INSERT INTO zakopane VALUES (?, ?, ?, ?, ?)', separator=' ')

    # wykonaj_zapytanie(cur, 'SELECT * FROM panstwa')
    # wykonaj_zapytanie(cur, 'SELECT nazwisko, panstwo FROM zawodnicy')
    # wykonaj_zapytanie(cur, 'SELECT nazwisko, panstwo FROM zawodnicy WHERE panstwo="JPN"')
    # wykonaj_zapytanie(cur, 'SELECT nazwisko, panstwo, punkty FROM zawodnicy WHERE punkty>500 ORDER BY punkty DESC')
    # wykonaj_zapytanie(cur, 'SELECT * FROM panstwa')
    #wykonaj_zapytanie(cur,
    #"""SELECT nazwisko, nazwa FROM zawodnicy
    #   INNER JOIN panstwa ON zawodnicy.panstwo = panstwa.skrot
    #   """)
    # wykonaj_zapytanie(cur,
    # """SELECT COUNT(id_zawodnika) FROM kuusamo
    # WHERE nota11 > 220
    #   """)
    wykonaj_zapytanie(cur,
        """SELECT COUNT(kuusamo.id_zawodnika) AS lz, panstwo FROM kuusamo
        INNER JOIN zawodnicy ON zawodnicy.id_zawodnika = kuusamo.id_zawodnika
        GROUP BY panstwo
        ORDER BY lz
        """)

    con.commit()
    con.close()

main()
