from random import randint

n = int(input('Ile liczb wylosować? '))
start = 1
stop = 10

liczby = []  # utworzenie pustej listy
while len(liczby) < n:
    liczba = randint(start, stop)
    wylosowana = False
    for j in range(len(liczby)):
        if liczby[j] == liczba:
            wylosowana = True
    if not wylosowana:
        liczby.append(liczba)

typy = []
while len(typy) < n:
    liczba = int(input('Podaj liczbę: '))
    wylosowana = False
    for j in range(len(typy)):
        if typy[j] == liczba:
            wylosowana = True
    if not wylosowana:
        typy.append(liczba)

trafione = []
for i in range(n):
    typ = typy[i]
    for j in range(n):
        if liczby[j] == typ:
            trafione.append(typ)

print(liczby)
print(typy)
print(trafione)
