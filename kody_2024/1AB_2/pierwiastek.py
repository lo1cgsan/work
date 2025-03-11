# progam oblicza pierwiastek kwadratowy
# z całkowitej liczby dodatniej
from math import sqrt

a = int(input('Podaj liczbę: '))

if a < 1:
    print('Błędne dane!')
else:
    print('Pierwiastek:', sqrt(a))
