# n! = (n-1)! * n

def silnia_it(n):
    wynik = 1
    for i in range(1, n+1):
       wynik = wynik * i
    return wynik


def silnia_re(n):
    print(n)
    if n == 0:
        return 1
    return silnia_re(n-1) * n


def main():
    # pobierz liczbę naturalną n
    n = int(input('Podaj n: '))

    print(silnia_it(n))
    print(silnia_re(n))


main()
