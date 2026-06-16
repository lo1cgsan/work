import random

n = int(input('Ile liczb wylosować? '))

maks = int(input('Podaj maksymalną wartość: '))
liczby = []

def czy_w_liscie(lista, wartosc):
    for elem in lista:
        if elem == wartosc:
            return True
    return False


def czy_w_liscie2(lista, wartosc):
    for i in range(len(lista)):
        if lista[i] == wartosc:
            return True
    return False


# losowanie liczb
while len(liczby) < n:
    liczba = random.randint(0, maks)
    # if czy_w_liscie(liczby, liczba):
    if liczba in liczby:
        print('Powtórzona liczba!')
    else:
        liczby.append(liczba)

# pobieranie typów
typy = []
# for i in range(n):
while len(typy) < n:
    typ = int(input('Podaj typ: '))
    if 0 <= typ <= maks:
        typy.append(typ)
    else:
        print('Błędne dane!')

# sprawdzanie liczby trafień
trafione = []
for typ in typy:
    if czy_w_liscie2(liczby, typ):
    # if typ in liczby:
        trafione.append(typ)

print(liczby)
print(typy)
print(trafione)
