# totolotek.py
from random import randint

n = int(input('Ile liczb wylosować? '))
start = 1
stop = 10

liczby = []  # utworzenie pustej listy
while len(liczby) < n:
    liczba = randint(start, stop)
    wylosowana = False
    for j in range(len(liczby)):
        if liczba == liczby[j]:
            wylosowana = True
    if not wylosowana:
        liczby.append(liczba)

typy = []  # utworzenie pustej listy
while len(typy) < n:
    liczba = int(input('Podaj liczbę: '))
    if start <= liczba <= stop:
        typy.append(liczba)
    else:
        print('Typ poza zakresem...')

trafione = []
for i in range(n):
    typ = typy[i]
    for j in range(n):
        if liczby[j] == typ:
            trafione.append(typ)

print(liczby)
print(typy)
print(trafione)
