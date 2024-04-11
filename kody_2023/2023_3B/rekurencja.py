def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n-1)


def potega(a, n):
    if n == 0:
        return 1
    return potega(a, n-1) * a


def main():
    n = int(input('Podaj liczbę: '))
    print(silnia(n))


main()
