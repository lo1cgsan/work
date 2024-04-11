from random import randint

def czy_zapisana(x, lista):
    for el in lista:
        if x == el:
            return True
    return False


liczby = [] # utworzenia pustej listy

while len(liczby) < 3:
    liczba = randint(1, 10)
    if not czy_zapisana(liczba, liczby):
        liczby.append(liczba)

typy = []
while len(typy) < 3:
    typ = int(input('Podaj typ: '))
    if not czy_zapisana(typ, typy):
        typy.append(typ)

licznik = 0
for typ in typy:
    if czy_zapisana(typ, liczby):
        print(typ)
        licznik += 1

