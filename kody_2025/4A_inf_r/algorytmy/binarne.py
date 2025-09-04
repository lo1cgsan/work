lista = sorted([4, 8, 1, 2, 2, 5, 0])
szukany = 4
print(f'Szukany: {szukany}')
print(f'Lista: {lista}')


def szukaj_liniowo(l, e):
    for i in range(0, len(l)):
        if l[i] == e:
            return i
    return -1


def szukaj_bin_it(l, e):
    lewy, prawy = 0, len(l) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        print(f'Środek: {srodek}')
        if l[srodek] == e:
            return srodek
        elif e < l[srodek]:
            prawy = srodek -1
        else:
            lewy = srodek + 1

    return -1  # elementu nie znaleziono

def szukaj_bin_rek(lewy, prawy, l, e):
    if lewy > prawy:
        return -1

    srodek = (lewy + prawy) // 2
    if l[srodek] == e:
        return srodek

    if e < l[srodek]:
        return szukaj_bin_rek(lewy, srodek-1, l, e)
    else:
        return szukaj_bin_rek(srodek+1, prawy, l, e)


print('Indeks:', szukaj_bin_it(lista, szukany))
print('Indeks:', szukaj_bin_rek(0, len(lista)-1, lista, szukany))