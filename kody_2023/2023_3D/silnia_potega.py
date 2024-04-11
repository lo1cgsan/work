def silnia_rek(n):
    if n == 0:
        return 1
    return silnia_rek(n-1) * n


def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(a, n-1) * a


def nwd_rek(a, b):
    if b == 0:
        return a
    return nwd_rek(b, a % b)


def main():
    n = int(input('Podaj liczbę: '))
    print(silnia_rek(n))
    w = int(input('Podaj wykładnik: '))
    print(potega_rek(n, w))
    print(nwd_rek(12, 18))

main()
