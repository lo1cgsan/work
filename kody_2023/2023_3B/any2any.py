def any2dec(l, p):
    wynik = int(l[0])
    for i in range(1, len(p)):
        wynik = wynik * p + int(l[i])
    return wynik


def dec2any(l, p):
    wynik = 0
    return wynik


pw = int(input('Podstawa: '))
lw = input('Liczba: ')
l10 = any2dec(lw, pw)
print(l10)

pd = int(input('Podstawa docelowa: '))
print(dec2any(l10, pd))
