def czytaj_txt(nazwa_pliku):
    dane = []

    plik_txt = open(nazwa_pliku)
    for wiersz in plik_txt:
        dane.append(wiersz.strip())
    plik_txt.close()
    
    return dane
    
dane = czytaj_txt('dane00.txt')
liczba_znakow = 0
for wiersz in dane:
    liczba_znakow += len(wiersz)
print("Liczba wierszy:", len(dane))
print(liczba_znakow)
