indeksy= 0, 1, 2, 3, 4, 5
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
        elif e <= l[srodek]:
            prawy = srodek -1
        else:
            lewy = srodek + 1

    return -1  # elementu nie znaleziono


print('Indeks:', szukaj_bin_it(lista, szukany))
