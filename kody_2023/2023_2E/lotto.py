"""
Napisz program, który losuje 3 liczby całkowite
z zakresu <1;10> i zapisuje je w liście wylosowane.
"""
from random import randint

def czy_zapisana(lista, liczba):
    for element in lista:
        if element == liczba:
            return True # zwróć prawdę

    return False # zwróć fałsz

wylosowane = [] # utworzenie pustej listy

# for i in range(3):
while len(wylosowane) < 3:
    liczba = randint(1, 10)
    if not czy_zapisana(wylosowane, liczba):
        wylosowane.append(liczba)

print(wylosowane)
