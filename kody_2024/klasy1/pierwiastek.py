# jak sprawdzać dane wejściowe
# dane wejściowe: liczba całkowita dodatnia
from math import sqrt

liczba = int(input('Podaj liczbę: '))

if liczba < 1:
    print('Błędne dane!')
else:
    print(sqrt(liczba))

