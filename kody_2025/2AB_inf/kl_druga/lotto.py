import random

n = int(input('Ile liczb wylosować? '))
maks = int(input('Podaj maksymalną wartość: '))
liczby = []

def czy_w_liscie(lista, wartosc):
    for elem in lista:
        if elem == wartosc:
            return True
    return False

# for i in range(n):
while len(liczby) < n:
    liczba = random.randint(0, maks)
    # if czy_w_liscie(liczby, liczba):
    if liczba in liczby:
        print('Powtórzona liczba!')
    else:
        liczby.append(liczba)

print(liczby)

[4, 6, 10, 10, 5]
[3, 3, 4, 7, 9]
