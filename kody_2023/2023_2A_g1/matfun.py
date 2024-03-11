# potęgowanie
def potega(a, n):
    wynik = 1

    for i in range(n):
        wynik = wynik * a

    return wynik


# silnia
# n! = 1 * 2 * ... * n
def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik = wynik * i
    return wynik

