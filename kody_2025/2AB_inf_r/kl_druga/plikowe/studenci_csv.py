import csv
import os

def is_float(element: any) -> bool:
    if element is None:
        return False
    try:
        float(element)
        return True
    except:
        return False

def pobierz_dane(plik_wej, sep=','):
    dane = []
    if os.path.isfile(plik_wej):
        with open(plik_wej) as plik:
            for wiersz in csv.reader(plik, delimiter=sep):
                dane.append(wiersz)
    return dane

dane = pobierz_dane('studenci.csv')
# print(dane)

for lista in dane:
    # for pole in lista:
    for i in range(len(lista)):
        if lista[i].isnumeric():
            lista[i] = int(lista[i])

print(dane)
