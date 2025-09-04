import sqlite3
import csv
import os

plik_sql = 'szkola.sql'
plik_bazy = 'szkola.db'

def utworz_baze(cur):
    with open(plik_sql) as plik:
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
    dane.pop(0)
    # print(dane)
    cur.executemany(zapytanie, dane)


def wykonaj_zapytanie(cur, query):
    cur.execute(query)
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)

def main():
    con = sqlite3.connect(plik_bazy)  # połączenie z bazą
    cur = con.cursor()  # obiekt kursora

    utworz_baze(cur)
    dodaj_dane('uczniowie.txt', cur, 'INSERT INTO uczniowie VALUES (?, ?, ?, ?, ?, ?)')
    dodaj_dane('przedmioty.txt', cur, 'INSERT INTO przedmioty VALUES (?, ?, ?, ?)')
    dodaj_dane('oceny.txt', cur, 'INSERT INTO oceny VALUES (?, ?, ?, ?)')

    zapytanie = """
        SELECT COUNT(id_ucz) FROM uczniowie
        WHERE ulica = 'Sportowa' or ulica = 'Worcella'
    """
    zapytanie = 'SELECT COUNT(*) FROM uczniowie WHERE id_klasy = "1a"'
    zapytanie = """
        SELECT AVG(ocena) FROM oceny
        INNER JOIN przedmioty ON oceny.id_przedm = przedmioty.id
        INNER JOIN uczniowie ON oceny.id_ucz = uczniowie.id_ucz
        WHERE nazwa = 'polski' and id_klasy = '1a'
    """
    # 9;4;2008-09-05;3;3;niemiecki;Bednarek;Alina;9;Gnutek;Ewa;Kiedrzynska;15;1a

    zapytanie = """
        SELECT AVG(ocena) AS srednia, id_klasy FROM oceny
        INNER JOIN przedmioty ON oceny.id_przedm = przedmioty.id
        INNER JOIN uczniowie ON oceny.id_ucz = uczniowie.id_ucz
        WHERE nazwa = 'matematyka'
        GROUP BY id_klasy
        ORDER BY srednia DESC
    """

    wykonaj_zapytanie(cur, zapytanie)


    con.commit()
    con.close()

main()
