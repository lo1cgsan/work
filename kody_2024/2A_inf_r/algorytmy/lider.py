# znajdowanie elementu, który występują w zbiorze
# n-elementowym więcej niż n/2 razy

zbior = [1, 2, 1, 6, 8, 1, 1, 3, 3]

def czy_lider(el, ile_razy):
    if ile_razy > len(zbior) // 2:
        print('Lider:', el, ile_razy)
    else:
        print('Brak lidera!')

def znajdz_lidera():
    lider = zbior[0]
    n = 1

    for i in range(1, len(zbior)):
        if n > 0:
            if lider == zbior[i]:
                n += 1
            else:
                n -= 1
        else:
            lider = zbior[i]
            n = 1
    return n, lider

n, lider = znajdz_lidera()
print(f'n = {n}, lider = {lider}')

if n == 0:
    print('Brak lidera!')
else:
    ile_razy = 0
    for i in range(len(zbior)):
        if lider == zbior[i]:
            ile_razy += 1
    czy_lider(lider, ile_razy)

def policz_elementy_1():
    sprawdzone = []
    for liczba in zbior:
        if liczba not in sprawdzone:
            sprawdzone.append(liczba)
            print(liczba, zbior.count(liczba))

def policz_elementy_2():
    maks_el = 0
    nakczestszy = None
    for liczba in set(zbior):
        ile_razy = zbior.count(liczba)
        if zbior.count(liczba) > maks_el:
            najczestszy = liczba
            maks_el = ile_razy

    return najczestszy, maks_el

# czy_lider(*policz_elementy_2())
