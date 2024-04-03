from random import randint, seed


def czy_w_liscie(liczba, lista):
    for element in lista:
        if liczba == element:
            return True
    return False


liczby = [] # utwórz pustą listę

# for i in range(3):
while len(liczby) < 3:
    liczba = randint(1, 10)
    if not czy_w_liscie(liczba, liczby):
        liczby.append(liczba) # dopisz element do listy

print(liczby)
