"""
Napisz program, który wylosuje 3 liczby z zakresu <1;10>,
następnie pobierze 3 typy użytkownika, sprawdzi, wypisze
i policzy liczby, które zostały odgadnięte.
"""
from random import randint

def czy_zapisana(liczba, lista):
    for element in lista:
        if element == liczba:
            return True
    return False

wylosowane = []

# for i in range(3):
while len(wylosowane) < 3:
    n = randint(1, 10)
    if not czy_zapisana(n, wylosowane):
        wylosowane.append(n)

print(wylosowane)
