from random import randint


def czy_w_liscie(liczba, lista):
    for element in lista:
        if liczba == element:
            return True
    return False


liczby = [] # utwórz pustą listę
while len(liczby) < 3:
    liczba = randint(1, 10)
    if not czy_w_liscie(liczba, liczby):
        liczby.append(liczba) # dopisz element do listy

typy = []
while len(typy) < 5:
    liczba = int(input('Podaj liczbę: '))
    if not czy_w_liscie(liczba, typy):
        typy.append(liczba) # dopisz element do listy

# przeglądanie listy za pomocą indeksów
licznik = 0
for i in range(5):
    if czy_w_liscie(typy[i], liczby):
        print(typy[i])
        licznik = licznik + 1
print('Odgadniętych:', licznik)
print(liczby)


# przeglądanie listy bezpośrednio
licznik = 0
for typ in typy:
    if czy_w_liscie(typ, liczby):
        print(typ)
        licznik = licznik + 1
print('Odgadniętych:', licznik)
print(liczby)
