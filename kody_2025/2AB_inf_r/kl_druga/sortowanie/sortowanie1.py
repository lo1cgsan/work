import random

def sort_babel(dane):
    licznik = 0
    n = len(dane)
    for i in range(n):
        for j in range(n-1-i):
            if dane[j] > dane[j+1]:
                licznik += 1
                dane[j], dane[j+1] = dane[j+1], dane[j]
        print(dane)

    print(f'Licznik: {licznik}')

def sort_wybor(dane):
    n = len(dane)
    licznik = 0
    for i in range(n):
        k = i
        for j in range(i+1, n):
            if dane[j] < dane[k]:
                k = j

        if i != k:
            dane[i], dane[k] = dane[k], dane[i]
            licznik += 1

        print(dane)
    print(f'Licznik: {licznik}')

def sort_wstaw(dane):
    n = len(dane)
    licznik = 0
    for i in range(1, n):
        el = dane[i]
        j = i - 1
        while j >= 0 and dane[j] > el:
            dane[j+1] = dane[j]
            licznik += 1
            j = j - 1

        if j+1 != i:
            dane[j+1] = el
            licznik += 1

    print(f'Licznik: {licznik}')

dane = random.sample(range(0, 101), 10)
dane = list(range(10))
# dane.reverse()
print(dane)
#sort_babel(dane)
#sort_wybor(dane)
sort_wstaw(dane)
print(dane)
