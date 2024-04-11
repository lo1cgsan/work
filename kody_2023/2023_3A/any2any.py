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


def dec2any(l, p):


def main():
    pw = int(input('Podaj podstawę: '))
    liczba = input('Podaj liczbę: ').upper()
    l10 = any2dec(liczba, pw)
    print(l10)


main()
