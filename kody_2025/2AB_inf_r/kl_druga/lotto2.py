from modul import pobierz_liczbe, pobierz_dane
from modul import losuj_liczby, pobierz_typy
from modul import sprawdz_trafione

n = pobierz_liczbe('Ile liczb wylosować? ')
while n == False or n < 1:
    n = pobierz_liczbe('Ile liczb wylosować? ')

maks = pobierz_dane('Podaj maksymalną wartość: ')
while maks == False or n > maks:
    maks = pobierz_dane('Podaj maksymalną wartość: ')

liczby = losuj_liczby(n, maks)
typy = pobierz_typy(n, maks)
trafione = sprawdz_trafione(typy, liczby)

# wyniki
print(liczby)
print(trafione)
print(f'Odgadłeś {len(trafione)} liczb.')
