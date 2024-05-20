def any2dec(l, p):
    wynik = 0
    for i in range(len(l)):
        cyfra = l[i]
        if 64 < ord(cyfra) < 91:
            cyfra = ord(cyfra) - 55
        wynik = wynik * p + int(cyfra)
    return wynik


def dec2any(l10, p):
    reszty = []
    while l10 > 0:
        reszty.append(l10 % p)
        l10 = l10 // p
    reszty.reverse()
    return reszty


pw = int(input('Podstawa wejściowa: '))
lw = input('Liczba wejściowa: ').upper()
l10 = any2dec(lw, pw)
print(l10)
pd = int(input('Podstawa docelowa: '))
ld = dec2any(l10, pd)
print(ld)
