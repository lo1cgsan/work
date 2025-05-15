from random import randint

start = 1
stop = 10
n = int(input('Ile liczb wylosować? '))

liczby = []
for i in range(n):
    liczba = randint(start, stop)
    wyloswana = False
    for j in range(len(liczby)):
        if liczba == liczby[j]:
            wylosowana = True
    if not wylosowana:
        liczby.append(liczba)

typy = []
for i in range(n):
    typ = int(input('Podaj typ: '))
    typy.append(typ)

trafione = []
for i in range(n):
    typ = typy[i]
    for j in range(n):
        liczba = liczby[j]
        if typ == liczba:
            trafione.append(typ)

print(liczby)
print(typy)
print(trafione)
