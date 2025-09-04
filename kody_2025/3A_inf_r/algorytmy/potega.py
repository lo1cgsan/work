# 2^0 = 1
# 2^4 = 2 * 2 * 2 * 2

def potega_it(a, n):
    wynik = 1
    for i in range(n):
       wynik = wynik * a
    return wynik


def potega_re(a, n):
    print(a, n)
    if n == 0:
        return 1
    return potega_re(a, n-1) * a

def main():

    # pobierz podstawę a
    a = int(input('Podaj podstawę: '))
    # pobierz wykładnik n
    n = int(input('Podaj wykładnik: '))

    print(potega_it(a, n))
    print(potega_re(a, n))


main()
