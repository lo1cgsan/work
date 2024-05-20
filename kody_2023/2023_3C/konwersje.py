def any2dec(p, l):
    wynik = 0
    for i in range(len(l)):
        cyfra = l[i]
        if ord(cyfra) >= 65:  # cyfry mogą być literami!
            cyfra = ord(cyfra) - 55
        wynik = wynik * p + int(cyfra)
    return wynik


def dec2any(p, l):
    pass


def main():
    pw = int(input('Podaj podstawę: '))
    lw = input('Podaj liczbę: ').upper()
    l10 = any2dec(pw, lw)
    print(l10)

    pd = int(input('Podaj podstawę docelową: '))
    ld = dec2any(pd, l10)


main()
