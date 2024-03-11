def dec2any(l10, p):
    reszty = []
    while l10 > 0:
        l10, reszta = divmod(l10, p)
        if reszta > 9:
            reszta = chr(reszta + 55)
        reszty.append(reszta)
    reszty.reverse()
    return reszty

def any2dec(a, p):
    # a = "1010"
    # a = "abc"
    l10 = 0
    ile = len(a)
    for cyfra in a.upper():
        l10 += int(cyfra) * pow(p, ile - 1)
        ile -= 1
    return l10

a = input("Podaj liczbę: ")
p = int(input("Podaj podstawę: "))

l10 = any2dec(a, p)
print(l10)
print(*dec2any(l10, p))
