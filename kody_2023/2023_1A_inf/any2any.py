def any2dec(p, l):
    # l = '1234'
    wynik = int(l[0])
    for i in range(len(l)-1):
        wynik = wynik * p + int(l[i+1])
    return wynik


def main():
    pw = int(input('Podstawa: '))
    lw = input('Liczba: ')
    l10 = any2dec(pw, lw)
    print(l10)


main()
