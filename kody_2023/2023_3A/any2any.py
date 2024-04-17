def any2dec(l, p):
    wynik = 0
    d = len(l)
    for i in range(d):
        cyfra = l[i]
        if 65 <= ord(cyfra) <= 70:
            cyfra = ord(cyfra) - 55 # zamiana liter na liczby
        wynik = wynik * p + int(cyfra)
        print(wynik)
    return wynik


def dec2any(l10, p):
    reszty = []
    while l10 > 0:
        r = l10 % p
        if r > 9:
            r = chr(r + 55)
        reszty.append(r)
        l10 = l10 // p
    print(reszty)


def main():
    pw = int(input('Podaj podstawę: '))
    liczba = input('Podaj liczbę: ').upper()
    l10 = any2dec(liczba, pw)
    print(l10)
    pd = int(input('Podaj podstawę docelową: '))
    dec2any(l10, pd)


main()
