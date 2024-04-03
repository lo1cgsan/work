from random import randint


def czy_zapisana(x, lista):
    for el in lista:
        if x == el:
            return True
    return False


liczby = []

while len(liczby) < 3:
    liczba = randint(1, 10)
    print(liczba)

    if not czy_zapisana(liczba, liczby):
        liczby.append(liczba)

print(liczby)

typy = []
for i in range(3):
    pobierz typ od użytkownika
