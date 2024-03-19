def silnia_rek(n):
    print('n =', n)
    if n == 0:
        return 1
    s = n * silnia_rek(n-1)
    print(s)
    return s


def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(a, n-1) * a


def main():
    a = int(input('Podaj podstawę: '))
    n = int(input('Podaj liczbę: '))
    print(silnia_rek(n))
    print(potega_rek(a, n))


main()
