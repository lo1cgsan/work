import csv

def czytaj_csv(plik, separator):
    dane = []
    with open(plik, newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
        for lista in tresc:
            dane.append(lista)
    return dane

