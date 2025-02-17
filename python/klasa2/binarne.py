def szukaj_liniowo(l, e):
    for i in range(0, len(l)):
        if l[i] == e:
            return i
    return -1  # elementu nie znaleziono


def szukaj_bin_it(l, e):
    lewy, prawy = 0, len(l) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        print(f'Środek: {srodek}')
        if l[srodek] == e:
            return srodek
        elif e <= l[srodek]:
            prawy = srodek - 1
        else:
            lewy = srodek + 1

    return -1  # elementu nie znaleziono


def szukaj_bin_rek(lewy, prawy, lista, el):

    if lewy > prawy:
        return -1  # elementu nie znaleziono

    srodek = (lewy + prawy) // 2
    if el == lista[srodek]:
        return srodek  # element znaleziono

    if el < lista[srodek]:
        return szukaj_bin_rek(lewy, srodek - 1, lista, el)
    else:
        return szukaj_bin_rek(srodek + 1, prawy, lista, el)


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9, -4]
    el = 2
    print(szukaj_liniowo(lista, el))
    lista.sort()
    print(lista)
    print(szukaj_bin_it(lista, el))
    print(szukaj_bin_rek(0, len(lista) - 1, lista, el))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
