from random import randint

start = 1
stop = 10
n = int(input('Ile liczb wylosować? '))

liczby = []

while len(liczby) < n:
    liczba = randint(start, stop)
    wylosowana = False
    for j in range(len(liczby)):
        if liczba == liczby[j]:
            wylosowana = True
    if not wylosowana:
        liczby.append(liczba)

typy = []

while len(typy) < n:
    typ = int(input('Podaj typ: '))
    podany = False
    for j in range(len(typy)):
        if typ == typy[j]:
            podany = True
        else:
            print('Powtarzasz się!')
    if not podany:
        typy.append(typ)

trafione = []
for i in range(n):
    typ = typy[i]
    for j in range(n):
        if typ == liczby[j]:
            trafione.append(typ)

print(liczby)
print(typy)
print(trafione)
