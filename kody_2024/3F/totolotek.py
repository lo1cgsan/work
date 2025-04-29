from random import randint

n = int(input('Ile liczb wylosować? '))
start = 1
stop = 10

liczby = []
while len(liczby) < n:
    liczba = randint(start, stop)
    wylosowana = False
    for j in range(len(liczby)):
        if liczba == liczby[j]:
            wylosowana = True
    if not wylosowana:
        liczby.append(liczba)

print(liczby)

typy = []
while len(typy) < n:
    liczba = int(input('Podaj typ: '))
    podana = False
    for j in range(len(typy)):
        if liczba == typy[j]:
            podana = True
    if not podana:
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
