import sqlite3

def utworz_tabele(kursor, plik_sql):
    with open(plik_sql, newline='', encoding='utf-8') as plik:
        kursor.executescript(plik.read())


def dodaj_dane(kursor, tabela):
    import csv

    plik_csv = tabela + '.csv'
    
    dane = []
    with open(plik_csv, newline='', encoding='utf-8') as plik:
        for wiersz in csv.reader(plik, delimiter=','):
            dane.append(wiersz)
    
    # print(dane)
    dane.pop(0)  # usunięcie 1 wiersza
    zastepniki = ','.join(['?'] * len(dane[0]))
    zapytanie = 'INSERT INTO ' + tabela + ' VALUES(' + zastepniki + ')'
    kursor.executemany(zapytanie, dane)


def main():
    baza = 'studenci.db'
    pol = sqlite3.connect(baza)
    kursor = pol.cursor()
    
    utworz_tabele(kursor, 'studenci.sql')
    dodaj_dane(kursor, 'uczelnie')
    dodaj_dane(kursor, 'miasta')
    dodaj_dane(kursor, 'studenci')
    
    pol.commit()
    pol.close()
    
main()
