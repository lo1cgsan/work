import csv
import sqlite3


class Baza:
    DEBUG = True

    def __init__(self, plik_bazy, plik_sql):
        self.con = sqlite3.connect(plik_bazy)  # połączenie z bazą
        self.cur = self.con.cursor()  # obiekt kursora
        self.plik_sql = plik_sql
        self.utworz_baze()

    def utworz_baze(self):
        zapytanie = "SELECT name FROM sqlite_master WHERE type='table'"
        if not self.wykonaj_select(zapytanie):
            print('Brak bazy.')
            with open(self.plik_sql) as plik:
                self.cur.executescript(plik.read())
                print(plik.read())
        else:
            print('Baza gotowa')

    def wczytaj_dane_z_pliku(self, nazwa_pliku, separator=';'):
        dane = []
        with open(nazwa_pliku) as plik:
            # print(plik.read())
            tresc = csv.reader(plik, delimiter=separator)
            for rekord in tresc:
                rekord = [wartosc for wartosc in rekord if wartosc]
                # print(rekord)
                dane.append(rekord)
        return dane

    def dodaj_dane(self, nazwa_pliku, zapytanie, separator=';'):
        dane = self.wczytaj_dane(nazwa_pliku, separator=separator)
        dane.pop(0)
        print(dane)
        self.cur.executemany(zapytanie, dane)

    def wykonaj_select(self, query, data=()):
        self.cur.execute(query, data)
        wyniki = self.cur.fetchall()
        if self.DEBUG:
            for row in wyniki:
                print(row)
        return wyniki

    def wykonaj_insert(self, query, data=()):
        self.cur.execute(query, data)
        id = self.cur.lastrowid
        self.con.commit()
        if self.DEBUG:
            print('Insert:', id)
        return id

    def wykonaj_insert_many(self, query, data=()):
        self.cur.executemany(query, data)
        self.con.commit()
        if self.DEBUG:
            print('Dane:', data)

    def wykonaj_zapytanie(self, query, data=()):
        self.cur.execute(query, data)
        self.con.commit()

    def __del__(self):
        print('Destruktor')
        self.con.close()
