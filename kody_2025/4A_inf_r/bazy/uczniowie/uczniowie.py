import csv
import sqlite3

plik_sql = 'uczniowie.sql'
plik_bazy = 'uczniowie.db'

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
    print(dane)
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
    dodaj_dane('uczniowie.csv', cur, 'INSERT INTO uczniowie VALUES (?, ?, ?, ?)', separator='\t')
    dodaj_dane('przedmioty.csv', cur, 'INSERT INTO przedmioty VALUES (?, ?)', separator=',')
    dodaj_dane('oceny.csv', cur, 'INSERT INTO oceny VALUES (?, ?, ?, ?, ?)', separator='\t')

    wykonaj_zapytanie(cur, 'SELECT * FROM uczniowie LIMIT 10')
    wykonaj_zapytanie(cur, 'SELECT * FROM przedmioty LIMIT 10')
    wykonaj_zapytanie(cur, 'SELECT * FROM oceny LIMIT 10')

    con.commit()
    con.close()

main()
