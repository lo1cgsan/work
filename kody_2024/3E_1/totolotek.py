from random import randint

n = int(input('Ile liczb wylosować? '))
start = 1
stop = 10

wylosowane = []  # utworzenie pustej listy
while len(wylosowane) < n:
    liczba = randint(start, stop)
    dodana = False
    for j in range(len(wylosowane)):
        if liczba == wylosowane[j]:
            dodana = True
    if not dodana:
        wylosowane.append(liczba)

typy = []  # utworzenie pustej listy
while len(typy) < n:
    typ = int(input('Podaj typ: '))
    dodany = False
    for j in range(len(typy)):
        if typ == typy[j]:
            dodany = True
    if not dodany:
        typy.append(typ)

trafione = []
for i in range(n):
    typ = typy[i]
    for j in range(n):
        if typ == wylosowane[j]:
            trafione.append(typ)

print(wylosowane)
print(typy)
print(trafione)
