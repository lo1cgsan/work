from math import sqrt

def czy_pierwsza(l):
    for i in range(2, round(sqrt(l)) + 1):
        if l % i == 0:
            return False
    return True

# liczba = int(input('Podaj liczbę: '))
# if czy_pierwsza(liczba):
#     print('pierwsza')
# else:
#     print('nie pierwsza')

a = 20
b = 300
pierwsze = []
for i in range(a, b+1):
    if czy_pierwsza(i):
        pierwsze.append(i)
print(pierwsze)