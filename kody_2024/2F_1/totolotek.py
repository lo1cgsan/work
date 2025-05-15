from random import randint

n = int(input('Ile liczb wylosować? '))

liczby = []
while len(liczby) < n:
    liczba = randint(1, 10)
    dodana = False
    for j in range(len(liczby)):
        if liczba == liczby[j]:
            dodana = True
    if not dodana:
        liczby.append(liczba)

print(liczby)
typy = []
for i in range(n):
    typ = int(input('Podaj typ: '))
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
