def czytaj_dane(nazwa_pliku):
    dane = []  # pusta lista
    with open(nazwa_pliku) as plik:
        for wiersz in plik:
            for wyraz in wiersz.strip().split():
                dane.append(wyraz)
    return dane
    
anagramy = czytaj_dane("tkaniny.txt")
# print(anagramy)

liczba_wierszy = 0

for i in range(0, len(anagramy), 3):
    if len(anagramy[i]) != 4:
        continue
    if sorted(anagramy[i]) == sorted(anagramy[i+1]) == sorted(anagramy[i+2]):
        liczba_wierszy += 1
        print(anagramy[i], anagramy[i+1], anagramy[i+2])


print("Liczba wierszy z 4-znakowymi anagramami:", liczba_wierszy)
