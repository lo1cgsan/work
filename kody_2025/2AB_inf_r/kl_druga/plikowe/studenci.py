from typing import List

def czytaj_dane(plik_wej: str, lista: List):
    with open(plik_wej, "r") as plik:
        # tresc = plik.read()
        # print(tresc.count("a"))
        # linia = plik.readline()
        # while linia:
            # print(linia)
            # linia = plik.readline()
        # exit()
        for wiersz in plik:
            # wiersz = wiersz.replace("\n", "")
            wiersz = wiersz.strip()
            wiersz = wiersz.split(",")
            lista.append(wiersz)

def zapisz_dane(plik_wyj: str, dane: List):
    with open(plik_wyj, "w") as plik:
        for wiersz in dane:
            wiersz = ",".join(wiersz)
            plik.write(wiersz + "\n")

plik_danych = 'studenci.csv'
studenci = []
czytaj_dane(plik_danych, studenci)

dane = []
for lista in studenci:
    dane.append(lista[1:3])

zapisz_dane('studenci1.txt', dane)

imiona = []
czytaj_dane('studenci1.txt', imiona)
print(imiona)
