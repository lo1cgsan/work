def silnia_rek(n):
    print('n =', n)
    if n == 0:
        return 1
    s = n * silnia_rek(n-1)
    print('s =', s)
    return s


def potega_rek(a, n):
    if n == 0:
        return 1
    toDo


def main():
    n = int(input('Podaj liczbę: '))
    print(silnia_rek(n))


main()
