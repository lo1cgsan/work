def any2dec(l, p):
    wynik = int(l[0])
    for i in range(1, len(l)):
        print(wynik)
        wynik = wynik * p + int(l[i])
    return wynik

pw = int(input('Podstawa wejściowa: '))
lw = input('Liczba wejściowa: ')
l10 = any2dec(lw, pw)
print(l10)
