from math import sqrt

def jest_pierwsza(n):
    for liczba in range(2, int(sqrt(n)) + 1):
        if n % liczba == 0:
            return False
    return True

n = int(input("Podaj liczbę: "))
for i in range(2, n + 1):
    print(i, jest_pierwsza(i))
