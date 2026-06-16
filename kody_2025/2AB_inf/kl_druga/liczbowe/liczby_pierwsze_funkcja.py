from math import sqrt

def czy_pierwsza(n):
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True

n = int(input('Podaj liczbę: '))

if czy_pierwsza(n):
    print('Liczba pierwsza.')
else:
    print('Liczba nie pierwsza.')
