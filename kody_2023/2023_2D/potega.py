def potega(a, n):
    # obliczenia
    wynik = 1
    for i in range(n):
        wynik = wynik * a

    # dane wyjściowe
    return wynik

# 4! = 1 * 2 * 3 * 4
def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik = wynik * i

    return wynik


# dane wejściowe
# a = int(input("Podaj a: "))
n = int(input("Podaj n: "))
# print(potega(a, n))
# p1 = potega(a, n)
# print(p1 + p1)

print(silnia(n))
